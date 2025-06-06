from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session 
from app.models.classes import Class, ClassStatus
from app.database import get_db_session
from app.auth.jwt_handler import get_current_user
from app.schemas.classes import CreateClassInput, CreateClassOutput, GetClassOutput, GetClassInput, GetClass
from app.utils.timezone_utils import convert_timezone
from app.Logger import logger

router = APIRouter(prefix = '/classes',tags = ["classes"])

@router.post("/create",response_model=CreateClassOutput)
def create_class(class_data:CreateClassInput,instructor = Depends(get_current_user) , db_session:Session = Depends(get_db_session)):
    """ 
    Function to create class
    """
    try:
        logger.info("Class Creation Started")
        class_to_db = Class(
            name = class_data.name,
            ist_start_time = class_data.ist_start_time,
            ist_end_time = class_data.ist_end_time,
            total_slots = class_data.total_slots,
            booked_slots = class_data.booked_slots,
            instructor_id = instructor.id,
            status = class_data.status

        )
        db_session.add(class_to_db)
        db_session.commit()
        db_session.refresh(class_to_db)

        logger.info("Class Creation Completed")

        return {"status":200, "message":"Class created Successfully"}
    
    except Exception as e:
        logger.error("Error while creating class: %s",str(e))
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/",response_model=GetClassOutput)
def get_all_classes(class_params:GetClassInput = Depends(),client = Depends(get_current_user),db_session:Session = Depends(get_db_session)):
    """ 
    Function to fetch all available classes
    """
    try:
        logger.info("Fetching Classes Initiated")
        class_response = []
        if not client:
            logger.error("Invalid Client")
            raise HTTPException(status_code = 400,detail = "Invalid Client")
        
        offset_value = (class_params.page_number - 1) * class_params.page_size
        sort_by = getattr(Class,class_params.sort_by)
        classes = db_session.query(Class).filter(Class.status == ClassStatus.AVAILABLE).order_by(
                sort_by.desc() if class_params.sort_order == "desc" else sort_by.asc() 
                ).offset(offset_value).limit(class_params.page_size).all()

        if not classes:
            logger.error("Class not found")
            raise HTTPException(status_code = 400,detail = "No classes found")
        
        for cls in classes:
            if class_params.timezone:
                cls.ist_start_time = convert_timezone(cls.ist_start_time,class_params.timezone)
                cls.ist_end_time = convert_timezone(cls.ist_end_time,class_params.timezone)
            class_response.append(GetClass(
                id = cls.id,
                name = cls.name,
                start_time = cls.ist_start_time,
                end_time = cls.ist_end_time,
                total_slots = cls.total_slots,
                booked_slots = cls.booked_slots,
                instructor_name = cls.instructor.name,
                status = cls.status
            ))

        logger.info("Fetching Classes Completed")
        return {
            "status": 200,
            "message": "classes retrived successfully",
            "classes": class_response
        }
    
    except Exception as e:
        logger.error("Error while fetching classes: %s",str(e))
        raise HTTPException(status_code=500, detail="Internal Server Error")
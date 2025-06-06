from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session 
from app.schemas.client import ClientSignup, Token, ClientLogin
from app.schemas.instructor import InstructorSignup
from app.database import get_db_session
from app.models.client import Client
from app.models.instructor import Instructor
from app.auth.password import hash_password, verify_password
from app.auth.jwt_handler import create_access_token
from app.Logger import logger

router = APIRouter(prefix = "/auth", tags=["auth"])

@router.post("/signup/client",response_model=Token)
def client_signup(client_data:ClientSignup, db_session:Session = Depends(get_db_session)):
    """  
    Function to Sign up client, store client in DB and return access token 
    """
    try:
        logger.info("client signup initiated")

        client_in_db = db_session.query(Client).filter(Client.email == client_data.email).first()
        if client_in_db: 
            logger.error("Client already exists")
            raise HTTPException(status_code=400,detail="Client already Exists Try Logging in !!")
        
        hashed_pwd = hash_password(client_data.password)
        client_to_db = Client(name = client_data.name, email = client_data.email, hashed_password= hashed_pwd)
        db_session.add(client_to_db)
        db_session.commit()
        db_session.refresh(client_to_db)
        access_token = create_access_token(data = {"sub":client_to_db.email,"role":"client"})

        logger.info("client signup completed")
        return {"access_token":access_token, "token_type":"Bearer"}
    
    except Exception as e:
        logger.error("Error during client signup: %s",str(e))
        raise HTTPException(status_code=500, detail="Internal Server Error") 
    

@router.post("/signup/instructor",response_model=Token)
def instructor_signup(instructor_data:InstructorSignup, db_session:Session = Depends(get_db_session)):
    """  
    Function to Sign up instructor, store instructor in DB and return access token 
    """
    try: 
        logger.info("instructor signup initiated")

        instructor_in_db = db_session.query(Instructor).filter(Instructor.email == instructor_data.email).first()
        if instructor_in_db: 
            logger.error("Instructor already exists")
            raise HTTPException(status_code = 400,detail = "Instructor already Exists Try Logging in !!")
        
        hashed_pwd = hash_password(instructor_data.password)
        instructor_to_db = Instructor(name = instructor_data.name, email = instructor_data.email, hashed_password= hashed_pwd)
        db_session.add(instructor_to_db)
        db_session.commit()
        db_session.refresh(instructor_to_db) 
        access_token = create_access_token(data = {"sub":instructor_to_db.email,"role":"instructor"})

        logger.info("instructor signup initiated")
        return {"access_token":access_token, "token_type":"Bearer"}

    except Exception as e:
        logger.error("Error instructor signup: %s",str(e))
        raise HTTPException(status_code=500, detail="Internal Server Error") 


@router.post("/login",response_model = Token)
def user_login(user_data: ClientLogin, db_session: Session = Depends(get_db_session)):
    """
    Function to Login client & Instructor and provide access token
    """
    try:
        logger.info("user login initiated")
        if user_data.role == "client":
            user_db = db_session.query(Client).filter(Client.email == user_data.email).first()
            if not user_db: 
                logger.error("Client not found")
                raise HTTPException(status_code = 400,detail = "Client not Found Try Signing Up !!")
            
        elif user_data.role == "instructor":
            user_db = db_session.query(Instructor).filter(Instructor.email == user_data.email).first()
            if not user_db: 
                logger.error("instructor not found")
                raise HTTPException(status_code = 400,detail = "Instructor not Found Try Signing Up !!")
        else: 
            logger.error("Invalid role provided")
            raise HTTPException(status_code = 400,detail = "Invalid Role provided")

        is_valid_password = verify_password(user_data.password, user_db.hashed_password)
        if not is_valid_password:
            logger.error("mismatch in password")
            raise HTTPException(status_code = 400,detail = "Wrong Password Try again!!")
        
        access_token = create_access_token(data = {"sub":user_db.email,"role":user_data.role})

        logger.info("user login completed")
        return {"access_token":access_token, "token_type":"Bearer"}
    
    except Exception as e:
        logger.error("Error while user login: %s",str(e))
        raise HTTPException(status_code=500, detail="Internal Server Error") 

    
from fastapi import APIRouter, Depends, HTTPException
from app.models.booking import Booking
from app.models.classes import Class, ClassStatus
from app.schemas.booking import BookingInput,BookingOut, GetBookingResponse, GetBookingInput, GetBooking
from app.database import get_db_session
from app.auth.jwt_handler import get_current_user
from sqlalchemy.orm import Session
from app.utils.timezone_utils import convert_timezone
from app.Logger import logger

router = APIRouter(tags=["book"])

@router.post('/book',response_model=BookingOut)
def book_class(booking_input:BookingInput,client = Depends(get_current_user), db_session:Session = Depends(get_db_session)):
    """ 
    Function to create booking
    """
    try:
        logger.info("Booking Initiated")
        class_availability = db_session.query(Class).filter(Class.id == booking_input.class_id).first()

        if not class_availability:
            logger.error("Class not found")
            raise HTTPException(status_code=400,detail="Class not found")

        if class_availability.status == ClassStatus.SOLD_OUT :
            logger.error("Class sold out")
            raise HTTPException(status_code=400,detail="Class Sold Out please book other class")
        
        if class_availability.booked_slots>=class_availability.total_slots:
            class_availability.status = ClassStatus.SOLD_OUT
            db_session.commit()
            logger.error("Class sold out")
            raise HTTPException(status_code=400,detail="Class Sold Out please book other class")
            
        
        already_booked = db_session.query(Booking).filter(
            Booking.class_id == class_availability.id,
            Booking.client_id == client.id
        ).first()

        if already_booked:
            logger.error("Already booked")
            raise HTTPException(status_code=400,detail="You have already Booked the Class")

        booking = Booking(
            class_id = booking_input.class_id,
            client_id = client.id
        )
        db_session.add(booking)
        db_session.commit()
        db_session.refresh(booking)
        
        class_availability.booked_slots += 1
        if class_availability.total_slots == class_availability.booked_slots:
            class_availability.status = ClassStatus.SOLD_OUT
        
        db_session.commit()

        logger.info("Booking Completed")

        return {
            "status":200,
            "message":"Class booked successfully",
            "booking_id":booking.id
        }   
     
    except Exception as e:
        logger.error("Error while booking: %s",str(e))
        raise HTTPException(status_code=500, detail="Internal Server Error") 

@router.get('/bookings',response_model=GetBookingResponse)
def get_bookings(booking_input:GetBookingInput = Depends(),client = Depends(get_current_user), db_session:Session = Depends(get_db_session)):
    """ 
    Function to fetch all bookings Client has booked
    """
    try:
        logger.info("Fetching Bookings Initiated")
        bookings = []
        order_by_value = getattr(Booking,booking_input.sort_by)
        offset_value = (booking_input.page_number - 1) * booking_input.page_size
        
        query_result = (db_session.query(Booking,Class)
            .join(Class, Booking.class_id == Class.id)
            .filter(Booking.client_id == client.id)
            .order_by(order_by_value.desc() if booking_input.sort_order == 'desc' else order_by_value.asc())
            .offset(offset_value).limit(booking_input.page_size) ).all()

        if not query_result:
            logger.error("No Bookings Found")
            raise HTTPException(status_code=400,detail="No Bookings found")
        
        for book,cls in query_result:
            if booking_input.timezone:
                cls.ist_start_time = convert_timezone(cls.ist_start_time,booking_input.timezone)
                cls.ist_end_time = convert_timezone(cls.ist_end_time,booking_input.timezone)

            bookings.append(GetBooking(
                id = book.id,
                booking_created_at = book.created_at,
                booking_status = book.status,
                class_id = cls.id,
                class_name = cls.name,
                class_start_time = cls.ist_start_time,
                class_end_time = cls.ist_end_time,
                instructor_name = cls.instructor.name,
                total_slots = cls.total_slots,
                available_slots = cls.booked_slots, 
                class_status = cls.status
            ))

        response = {
            "status":200,
            "message":"Bookings Fetched successfully",
            "bookings":bookings
        }
        logger.info("Fetching Bookings Completed")

        return response

    except Exception as e:
        logger.error("Error while fetching bookings: %s",str(e))
        raise HTTPException(status_code=500, detail="Internal Server Error")

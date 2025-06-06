from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class BookingInput(BaseModel):
    """ 
    Booking requires class_id to add booking against a class
    """
    class_id:str


class BookingOut(BaseModel):
    """ 
    Booking creation response format
    """
    status: int
    message:str
    booking_id:str


class GetBookingInput(BaseModel):
    """ 
    Get client boookings input params
    """
    timezone : Optional[str] = None
    page_number : Optional[int] = 1
    page_size : Optional[int] = 10
    sort_by:Optional[str] = 'created_at'
    sort_order:Optional[str] = 'desc'

class GetBooking(BaseModel):
    """ 
    GET Bookings output response structure
    """
    id: str 
    booking_created_at: datetime
    booking_status : str
    class_id: str 
    class_name: str 
    class_start_time:datetime 
    class_end_time:datetime 
    instructor_name:str
    total_slots:int
    available_slots:int 
    class_status: str


class GetBookingResponse(BaseModel):
    """ 
    GET Bookings output response structure
    """
    status:int 
    message: str 
    bookings:List[GetBooking]

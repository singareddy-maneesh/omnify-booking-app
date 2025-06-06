import enum
from uuid import uuid4
from datetime import datetime
from sqlalchemy import Column, String, DateTime, Integer, Enum, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class ClassStatus(str,enum.Enum):
    """ 
    Class statuses allowed
    """
    AVAILABLE = "Available"
    SOLD_OUT  = "Sold out"


class Class(Base):
    """ 
    Class table to store classes
    """
    __tablename__ = "classes"

    id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    name = Column(String)
    ist_start_time = Column(DateTime)
    ist_end_time = Column(DateTime)
    total_slots = Column(Integer)
    booked_slots = Column(Integer, default=0)
    instructor_id = Column(String, ForeignKey("instructors.id"))
    status = Column(Enum(ClassStatus), default = ClassStatus.AVAILABLE)
    created_at = Column(DateTime, default = datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    instructor = relationship("Instructor",back_populates = 'classes')
    bookings = relationship("Booking",back_populates = 'classes')
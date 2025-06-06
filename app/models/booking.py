import datetime
from uuid import uuid4
import enum
from sqlalchemy import Column, String, Enum, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.database import Base

class BookingStatus(str, enum.Enum):
    """ 
    Booking statuses allowed
    """
    BOOKED = "booked"
    CANCELLED = "cancelled"

class Booking(Base):
    """ 
    Booking table to store client bookings
    """
    __tablename__ = "bookings"

    id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    class_id = Column(String, ForeignKey("classes.id"))
    client_id = Column(String, ForeignKey("clients.id"))
    status = Column(Enum(BookingStatus), default=BookingStatus.BOOKED)
    created_at = Column(DateTime, default=datetime.datetime.now())
    updated_at = Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)

    clients = relationship("Client",back_populates="bookings")
    classes = relationship("Class",back_populates = 'bookings')

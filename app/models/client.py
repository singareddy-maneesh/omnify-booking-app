from uuid import uuid4
import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import relationship
from app.database import Base 


class Client(Base):
    """ 
    Client Table to store client details
    """
    __tablename__ = 'clients'

    id = Column(String, primary_key=True, default = lambda : str(uuid4()))
    name = Column(String)
    email = Column(String, unique=True, index = True)
    hashed_password = Column(String)    
    created_at = Column(DateTime, default = datetime.datetime.now())

    bookings = relationship("Booking",back_populates="clients")

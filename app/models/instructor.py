from uuid import uuid4
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from app.database import Base


class Instructor(Base):
    """ 
    Instructor Table to store instructor details
    """
    __tablename__ = "instructors"

    id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    name = Column(String)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    classes = relationship("Class",back_populates = 'instructor')

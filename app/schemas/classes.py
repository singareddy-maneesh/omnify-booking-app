from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel

class CreateClassInput(BaseModel):
    """ 
    Create class input payload
    """
    name :str
    ist_start_time : datetime
    ist_end_time : datetime
    total_slots : int
    booked_slots : int = 0
    status:str = "Available" 

class CreateClassOutput(BaseModel):
    """ 
    Create class output payload
    """
    status: int 
    message: str


class GetClassInput(BaseModel):
    """ 
    GET classes input params
    """
    timezone : Optional[str] = None
    page_number : Optional[int] = 1
    page_size : Optional[int] = 10
    sort_by:Optional[str] = 'created_at'
    sort_order:Optional[str] = 'desc'



class GetClass(BaseModel):
    """ 
    GET classes output structure
    """
    id: str 
    name: str 
    start_time : datetime
    end_time : datetime
    total_slots : int
    booked_slots : int
    instructor_name : str
    status:str

class GetClassOutput(BaseModel):
    """ 
    GET classes output response format
    """
    status : int 
    message : str 
    classes : List[GetClass]

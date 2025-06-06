from pydantic import BaseModel, EmailStr

class InstructorSignup(BaseModel):
    """ 
    Input params for instructor sign up
    """
    name: str 
    email: EmailStr
    password: str


from pydantic import BaseModel, EmailStr

class ClientSignup(BaseModel):
    """ 
    Input params for client sign up
    """
    name: str 
    email: EmailStr
    password: str

class Token(BaseModel):
    """ 
    Token payload structure
    """
    access_token: str 
    toke_type: str = "Bearer"

class ClientLogin(BaseModel):
    """ 
    Input params for client login
    """
    email: EmailStr
    password : str
    role : str = 'client'

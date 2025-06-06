    
from datetime import datetime,timedelta
from typing import Optional
from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException  
from sqlalchemy.orm import Session
from app.database import get_db_session
from app.models.client import Client
from app.models.instructor import Instructor

oauth2_scheme = OAuth2PasswordBearer(tokenUrl = '/auth/login')

SECRET_KEY = "SingaredddyManeeshOmnifyBookingAPP"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict, expiry_duration: Optional[timedelta] = None):
    """
    Function to create access token
    """
    data_copy = data.copy()
    expiry_time = datetime.now() + (expiry_duration or timedelta(minutes = ACCESS_TOKEN_EXPIRE_MINUTES))
    data_copy.update(exp = expiry_time)
    jwt_encoded = jwt.encode(data_copy,SECRET_KEY,algorithm=ALGORITHM)

    return jwt_encoded


def get_current_user(token:str = Depends(oauth2_scheme),db_session :Session = Depends(get_db_session) ):
    """ 
    Method to validate the user
    """
    user_exception = HTTPException(
        status_code=401,
        detail = "Token Validation Error",
        headers={"WWW-Authenticate":"Bearer"}
    )
    try: 
        print("11111111111111")
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        email_id = payload.get('sub')
        role_type = payload.get("role")
        if not email_id or not role_type : 
            raise user_exception
        
        user = None
        if role_type == "client":
            user = db_session.query(Client).filter(Client.email == email_id).first() 
        elif role_type == "instructor":
            user = db_session.query(Instructor).filter(Instructor.email == email_id).first() 

        if not user:
            raise user_exception
        print("2222222222222")
        return user
    except JWTError :
        raise user_exception 


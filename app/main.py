from fastapi import FastAPI
from app.database import Base, engine
from app.routers import auth, classes,booking

# Base.metadata.drop_all(bind = engine)
Base.metadata.create_all(bind = engine)

app = FastAPI(title="Omnify Booking App")

@app.get('/')
def welcome():
    """ 
    Root API
    """
    return {"message":"Welcome to Omnify Booking App. Please signup/login to book your class."}

app.include_router(auth.router)
app.include_router(classes.router)
app.include_router(booking.router)

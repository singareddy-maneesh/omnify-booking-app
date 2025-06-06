from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from fastapi import HTTPException

DB_URL = "sqlite:///./omnify_database.db"
engine = create_engine(DB_URL,connect_args={"check_same_thread":False})
session_local = sessionmaker(bind = engine, autocommit = False, autoflush= False)
Base = declarative_base()

def get_db_session():
    """ 
    Function to yield db sesison to interact with the DB
    """

    session = None
    try: 
        session = session_local()
        yield session

    except Exception as error:
        raise HTTPException(status_code=500, detail = str(error)) from error
    
    finally: 
        if session: 
            session.close()
    


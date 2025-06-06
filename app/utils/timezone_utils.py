from datetime import datetime
from fastapi import HTTPException
import pytz
from app.Logger import logger

IST = pytz.timezone("Asia/Kolkata")

def convert_timezone(ist_time:datetime, desired_timezone:str) -> datetime:
    """ 
    Convert ist datetime to required timezone
    """
    try:
        if ist_time.tzinfo is None:
            ist_time = IST.localize(ist_time)
        target_tz = pytz.timezone(desired_timezone)
        converted = ist_time.astimezone(target_tz)
        return converted.replace(tzinfo=None)

    except Exception as error: 
        logger.error("Error while converting timezone: %s",str(error))
        raise HTTPException(status_code=500, detail=f"{str(error)} Error occurred while converting timezone") from error

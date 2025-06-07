from datetime import datetime, timedelta
from app.database import session_local
from app.models.client import Client
from app.models.classes import Class
from app.models.instructor import Instructor
from app.models.booking import Booking, BookingStatus
from app.auth.password import hash_password

db_session = session_local()

# Client data

client = Client(
    name = "Test Client",
    email = "testclient@testmail.com",
    hashed_password = hash_password("test_pwd")
)

db_session.add(client)
db_session.commit()
db_session.refresh(client)

# Instructor data

instructor = Instructor(
    name = "Test Instructor",
    email = "testinstructor@fitmail.com",
    hashed_password = hash_password("test_pwd123")
)

db_session.add(instructor)
db_session.commit()
db_session.refresh(instructor)


# Class data

cls = Class(
    name =  "Yoga Class",
    ist_start_time = datetime.now(),
    ist_end_time = datetime.now() + timedelta(hours = 1),
    total_slots = 10,
    booked_slots = 0,
    status = "Available",
    instructor_id = instructor.id
)

db_session.add(cls)
db_session.commit()
db_session.refresh(cls)

# Booking Data

booking = Booking(
    class_id = cls.id,
    client_id = client.id,
    status = BookingStatus.BOOKED

)

db_session.add(booking)
db_session.commit()
db_session.refresh(booking)

print("Sample data Inserted")
print(booking.id,client.id,cls.id,instructor.id)


from datetime import datetime, timedelta
from app.models.client import Client
from app.models.classes import Class, ClassStatus
from app.models.booking import Booking
from app.models.instructor import Instructor
from app.auth.jwt_handler import create_access_token
from app.auth.password import hash_password


def create_test_user_and_token(db_session):
    """ 
    Test user and token creation for authentication
    """
    user = Client(
        name="Test User2",
        email="testuser2@gmail.com",
        hashed_password=hash_password("testpass")
    )
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)

    token = create_access_token({"sub":user.email,"role":"client"})
    return user, token

def create_test_instructor(db_session):
    """ 
    create a test instructor
    """
    instructor = Instructor(
        name="Test User2",
        email="testuser2@gmail.com",
        hashed_password=hash_password("testpass")
    )

    db_session.add(instructor)
    db_session.commit()
    db_session.refresh(instructor)

    token = create_access_token({"sub":instructor.email,"role":"instructor"})
    return instructor, token


def create_test_class(db_session):
    """ 
    create a test class to book
    """
    instructor,token = create_test_instructor(db_session)
    now = datetime.now()
    test_class = Class(
        name="Yoga Session",
        ist_start_time=now + timedelta(hours=1),
        ist_end_time=now + timedelta(hours=2),
        total_slots=1,
        booked_slots=0,
        status=ClassStatus.AVAILABLE,
        instructor_id=instructor.id
    )
    db_session.add(test_class)
    db_session.commit()
    db_session.refresh(test_class)
    return test_class

def test_successful_booking(test_client, db_session):
    user, token = create_test_user_and_token(db_session)
    test_class = create_test_class(db_session)
    payload = {
        "class_id": test_class.id
    }
    response = test_client.post(
        "/book",
        json=payload,
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200
    data = response.json()
    assert data["status"] == 200
    assert data["message"] == "Class booked successfully"
    assert "booking_id" in data

    booking = db_session.query(Booking).filter(Booking.class_id == test_class.id, Booking.client_id == user.id ).first()
    assert booking!=None


def test_get_bookings(test_client):
    token = create_access_token({"sub":"testuser2@gmail.com","role":"client"})
    response = test_client.get(
        "/bookings?page_number=1&page_size=10&timezone=America/New_York",
        headers = {"Authorization":f"Bearer {token}"})
    assert response.status_code == 200
    assert response.json()["message"] == "Bookings Fetched successfully"

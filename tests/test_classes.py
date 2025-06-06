from app.models.instructor import Instructor
from app.auth.password import hash_password
from app.auth.jwt_handler import create_access_token

def test_create_class(test_client, db_session):

    instructor = Instructor(
        name="test", email="test@fit.com", hashed_password=hash_password("pass")
    )
    db_session.add(instructor)
    db_session.commit()
    db_session.refresh(instructor)
    token = create_access_token({"sub":instructor.email,"role":"instructor"})

    response = test_client.post("/classes/create", json={
        "name": "Yoga",
        "ist_start_time": "2025-06-06T08:00:00",
        "ist_end_time": "2025-06-06T09:00:00",
        "total_slots": 10,
        "instructor_id": instructor.id},
        headers = {"Authorization":f"Bearer {token}"})

    assert response.status_code == 200
    assert response.json()["message"] == "Class created Successfully"

def test_get_classes(test_client):
    token = create_access_token({"sub":"test@fit.com","role":"instructor"})
    response = test_client.get("/classes?page_number=1&page_size=10&timezone=America/New_York",
                               headers = {"Authorization":f"Bearer {token}"})
    assert response.status_code == 200
    assert response.json()["message"] =="classes retrived successfully"


# Omnify Booking App

A backend service built using FastAPI that handles class bookings, client registration, and authentication.

## Features

- Client Signup/Login with JWT auth
- List all available classes with pagination, sort and timezone conversion
- Book classes and view availability
- View all upcoming and past bookings with pagination, sort and timezone conversion
- Instructor and class management

## Tech Stack

- FastAPI
- SQLAlchemy (ORM)
- SQLite
- JWT (Python-JOSE)
- Uvicorn (ASGI server)
- Pytest (for unit testing)
- passlib (for hashing password)

## Setup Instructions

1. **Clone the repository**

git clone https://github.com/singareddy-maneesh/omnify-booking-app
cd omnify-booking-app

2. **Create and Activate Virtual Environment**

    python -m venv venv
    venv\Scripts\activate

3. **Install Dependencies**

pip install -r requirements.txt

4. **Run the Applications**

uvicorn app.main:app --reload

5. **Access API Documentation**

Open in Browser
Swagger UI: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc


## Postman  API collection  

1. **ROOT API**: 

    Method : GET

    Url = http://127.0.0.1:8000/

    Response = {"message": "Welcome to Omnify Booking App. Please signup/login to book your class."}

    curl --location 'http://127.0.0.1:8000/'

2. **Client Signup API**: 

    Method : POST

    Url = http://127.0.0.1:8000/auth/signup/client

    Request Payload = {
        "name": "test213",
        "email": "test321@yopmail.com",
        "password": "12345"
    }

    Response = {
        "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0MzIxQHlvcG1haWwuY29tIiwicm9sZSI6ImNsaWVudCIsImV4cCI6MTc0OTMwNDI0N30.DuVFTycCrh3tHtuh6OWm9KKzlJgvgV1S8ous4FLUVLo",
        "toke_type": "Bearer"
    }

    curl --location 'http://127.0.0.1:8000/auth/signup/client' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "name": "test213",
        "email": "test321@yopmail.com",
        "password": "12345"
    }'


3. **Client login API**: 

    Method : POST

    Url = http://127.0.0.1:8000/auth/login

    Payload = {
        "email": "test321@yopmail.com",
        "password": "12345",
        "role": "client"
    }

    Response = {
        "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0MzIxQHlvcG1haWwuY29tIiwicm9sZSI6ImNsaWVudCIsImV4cCI6MTc0OTMwNDUxOH0.sfGYIC0AS3hRrraOovPeIUfkqz0q-FI54nVXz6yRRDM",
        "toke_type": "Bearer"
    }

    curl --location 'http://127.0.0.1:8000/auth/login' \
    --header 'Authorization: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJtYW5pc2hAZ21haWwuY29tIiwiZXhwIjoxNzQ5MTc5MDkwfQ.2GQml3Pm_75h1oCUifAvkyb3i-iBT0bqlGG2r9TXXoo' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "email": "test321@yopmail.com",
        "password": "12345",
        "role": "client"
    }'


4. # Instructor Signup API: 

    Method : POST

    Url = http://127.0.0.1:8000/auth/signup/instructor

    Payload = {
        "name": "test instructor",
        "email": "testinstructor@yopmail.com",
        "password": "12345"
    }

    Response = {
        "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0aW5zdHJ1Y3RvckB5b3BtYWlsLmNvbSIsInJvbGUiOiJpbnN0cnVjdG9yIiwiZXhwIjoxNzQ5MzA0NzM1fQ.sE9mcG8Tb46XOGNXLVnK_HuV4DbHi29nCKD_B7w35vA",
        "toke_type": "Bearer"
    }

    curl --location 'http://127.0.0.1:8000/auth/signup/instructor' \
    --header 'Authorization: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJtYW5pc2hAZ21haWwuY29tIiwiZXhwIjoxNzQ5MTc5MDkwfQ.2GQml3Pm_75h1oCUifAvkyb3i-iBT0bqlGG2r9TXXoo' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "name": "test instructor",
        "email": "testinstructor@yopmail.com",
        "password": "12345"
    }'


5. # Instructor login API: 

    Method : POST

    Url = http://127.0.0.1:8000/auth/login

    Payload = {
        "email": "testinstructor@yopmail.com",
        "password": "12345",
        "role": "instructor"
    }

    Response = {
        "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0aW5zdHJ1Y3RvckB5b3BtYWlsLmNvbSIsInJvbGUiOiJpbnN0cnVjdG9yIiwiZXhwIjoxNzQ5MzA0ODM1fQ.YsFyXquyOffkekYDVSD4eytir7WVFxpXZU2S4SxJMH0",
        "toke_type": "Bearer"
    }

    curl --location 'http://127.0.0.1:8000/auth/login' \
    --header 'Authorization: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJtYW5pc2hAZ21haWwuY29tIiwiZXhwIjoxNzQ5MTc5MDkwfQ.2GQml3Pm_75h1oCUifAvkyb3i-iBT0bqlGG2r9TXXoo' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "email": "testinstructor@yopmail.com",
        "password": "12345",
        "role": "instructor"
    }'



6. # Create class API: 

    Method : POST

    Url = http://127.0.0.1:8000/classes/create

    Payload = {
        "name": "Yoga",
        "ist_start_time": "2025-06-05T10:00:00",
        "ist_end_time": "2025-06-05T11:00:00",
        "total_slots": 2,
        "booked_slots": 0,
        "status": "Available"
    }

    Response = {
        "status": 200,
        "message": "Class created Successfully"
    }

    curl --location 'http://127.0.0.1:8000/classes/create' \
    --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0aW5zdHJ1Y3RvckB5b3BtYWlsLmNvbSIsInJvbGUiOiJpbnN0cnVjdG9yIiwiZXhwIjoxNzQ5MzA0ODM1fQ.YsFyXquyOffkekYDVSD4eytir7WVFxpXZU2S4SxJMH0' \
    --header 'Content-Type: application/json' \
    --data '{
    "name": "Yoga",
    "ist_start_time": "2025-06-05T10:00:00",
    "ist_end_time": "2025-06-05T11:00:00",
    "total_slots": 2,
    "booked_slots": 0,
    "status": "Available"
    }'



7. # Get classes API: 

    Method : GET

    Url = http://127.0.0.1:8000/classes/?page_number=1&page_size=10&timezone=America%2FNew_York

    Response = {
        "status": 200,
        "message": "classes retrived successfully",
        "classes": [
            {
                "id": "6dc1e528-6468-4fb7-807b-38f7b19540cf",
                "name": "Yoga",
                "start_time": "2025-06-05T00:30:00",
                "end_time": "2025-06-05T01:30:00",
                "total_slots": 2,
                "booked_slots": 0,
                "instructor_name": "test instructor",
                "status": "Available"
            },
            {
                "id": "7338d0c7-6ce5-452e-802e-7b3f1cec8611",
                "name": "Yoga Class",
                "start_time": "2025-06-07T03:36:40.592698",
                "end_time": "2025-06-07T04:36:40.592698",
                "total_slots": 10,
                "booked_slots": 0,
                "instructor_name": "Test Instructor",
                "status": "Available"
            }
        ]
    }

    curl --location 'http://127.0.0.1:8000/classes/?page_number=1&page_size=10&timezone=America%2FNew_York' \
    --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0aW5zdHJ1Y3RvckB5b3BtYWlsLmNvbSIsInJvbGUiOiJpbnN0cnVjdG9yIiwiZXhwIjoxNzQ5MzA0ODM1fQ.YsFyXquyOffkekYDVSD4eytir7WVFxpXZU2S4SxJMH0'

8. # POST book class API: 

    Method : POST

    Url = http://127.0.0.1:8000/book/

    Payload = {
        "class_id":"6dc1e528-6468-4fb7-807b-38f7b19540cf"
    }

    Response = {
        "status": 200,
        "message": "Class booked successfully",
        "booking_id": "13574915-c0b3-46aa-b076-44892310fe82"
    }


    curl --location 'http://127.0.0.1:8000/book/' \
    --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0MzIxQHlvcG1haWwuY29tIiwicm9sZSI6ImNsaWVudCIsImV4cCI6MTc0OTMxMDgyM30.QUxoRRanvBCs-cYP_NyCSS6IADEfv3VPThwbfR166Ro' \
    --header 'Content-Type: application/json' \
    --data '{
        "class_id":"6dc1e528-6468-4fb7-807b-38f7b19540cf"
    }'


9. # GET bookings API: 

    Method : GET

    Url = http://127.0.0.1:8000/bookings?page_number=1&page_size=10&timezone=America%2FNew_York

    Response = {
        "status": 200,
        "message": "Bookings Fetched successfully",
        "bookings": [
            {
                "id": "13574915-c0b3-46aa-b076-44892310fe82",
                "booking_created_at": "2025-06-07T13:11:16.066997",
                "booking_status": "booked",
                "class_id": "6dc1e528-6468-4fb7-807b-38f7b19540cf",
                "class_name": "Yoga",
                "class_start_time": "2025-06-05T00:30:00",
                "class_end_time": "2025-06-05T01:30:00",
                "instructor_name": "test instructor",
                "total_slots": 2,
                "available_slots": 1,
                "class_status": "Available"
            }
        ]
    }


    curl --location 'http://127.0.0.1:8000/bookings?page_number=1&page_size=10&timezone=America%2FNew_York' \
    --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0MzIxQHlvcG1haWwuY29tIiwicm9sZSI6ImNsaWVudCIsImV4cCI6MTc0OTMxMDgyM30.QUxoRRanvBCs-cYP_NyCSS6IADEfv3VPThwbfR166Ro'


## Author
Singareddy Maneesh
GitHub: @singareddy-maneesh
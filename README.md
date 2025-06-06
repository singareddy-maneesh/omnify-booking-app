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

```bash
git clone https://github.com/singareddy-maneesh/omnify-booking-app
cd omnify-booking-app

2. **Create and Activate Virtual Environment**

# Create virtual environment
python -m venv venv

# Activate
# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate

3. **Install Dependencies**

pip install -r requirements.txt

4. **Run the Applications**

uvicorn app.main:app --reload

5. **Access API Documentation**

Open in Browser
Swagger UI: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc



🧑‍💻 Author
Singareddy Maneesh
GitHub: @singareddy-maneesh



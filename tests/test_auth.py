def test_client_signup(test_client):
    """ 
    test client signup
    """
    response = test_client.post("/auth/signup/client",json = {
        "name": "test",
        "email": "test@gmail.com",
        "password": "12345"

    })

    assert response.status_code == 200

def test_instructor_signup(test_client):
    """ 
    test instructor signup
    """
    response = test_client.post("/auth/signup/instructor",json = {
        "name": "test",
        "email": "test@gmail.com",
        "password": "12345"

    })

    assert response.status_code == 200

def test_client_login(test_client):
    """ 
    test client login
    """
    response = test_client.post("/auth/login",json={
        "email": "test@gmail.com",
        "password": "12345",
        "role":"client"
    })

    assert response.status_code == 200
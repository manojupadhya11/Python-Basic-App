# test_app.py

import pytest
from app import create_app
from urllib.parse import quote

@pytest.fixture
def app():
    return create_app()

@pytest.fixture
def client(app):
    return app.test_client()

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200

    expected_text = 'HI MANOJ UPADHYA SAYS HE IS GOOD DEVOPS ENGINNER WHO LOVES CONTINOUS LEARNING Exploring the DevOps Engineer'
    print("Test Successful")
    print("Manoj Upadhya Github webhook")
#Comment

    print(response.data)
    assert expected_text.encode() == response.data

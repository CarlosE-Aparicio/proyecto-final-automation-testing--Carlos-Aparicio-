import pytest
import random
from pages.pet_api import PetApi

api = PetApi()

@pytest.fixture
def pet_data():
    return{
        "id": random.randint(100000, 999999),
        "name": "Beethoven",
        "status": "available"
    }

@pytest.fixture
def created_pet(pet_data):
    response = api.create_pet(
        pet_data["id"],
        pet_data["name"],
        pet_data["status"]
    )
    assert response.status_code == 200
    return pet_data

def pytest_html_report_title(report):
    report.title = "PETSTORE API - CRUD PETS"
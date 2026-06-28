from pages.pet_api import PetApi
from utils.logger import logger
import pytest_check as check

api = PetApi()


def test_create_pet(pet_data):
    

    response = api.create_pet(
        pet_data["id"],
        pet_data["name"],
        pet_data["status"]
    )
    
    logger.info(
     f"""
     ===== CREATE PET =====
     ID: {pet_data["id"]}
     Name: {pet_data["name"]}
     Status: {pet_data["status"]}
     Response: {response.json()}
     ======================
     """
)

    check.equal(
        response.status_code,
        200,
        "NO SE AGREGO LA MASCOTA"
    )
    


def test_get_pet(created_pet):
    
    pet_id = created_pet["id"]
    response = api.get_pet(pet_id)

    logger.info(f"ID fixture creada: {created_pet['id']}")
    logger.info(f"ID response GET: {response.json()['id']}")

    logger.info(
    f"""
    ===== GET PET =====
    ID consultado: {pet_id}
    Response: {response.json()}
    ===================
    """
)
    
    check.equal(
        response.status_code,
        200,
        "STATUS INCORRECTO"
    )
    check.equal(
        response.json()["name"],
        created_pet["name"],
        "Nombre INCORRECTO"
    )
    check.equal(
        response.json()["id"],
        created_pet["id"],
        "ID INCORRECTO"
    )

def test_get_pet_not_found():

    pet_id = 999999999999

    response = api.get_pet(pet_id)

    logger.info(
        f"""
        === GET PET NOT FOUND ===
        Response: {response.json()}
        =========================
        """
    )

    check.equal(response.status_code, 404)

    check.equal(
        response.json()["message"],
        "Pet not found"
    )

def test_update_pet(created_pet):

    pet_id = created_pet["id"]

    response = api.update_pet(
        pet_id,
        "Beethoven Actualizado",
        "sold"
    )

    logger.info(
        f"""
        === UPDATE PET ===
        ID: {pet_id}
        Response: {response.json()}
        ====================
        """
    )
    
    check.equal(response.status_code, 200)

    check.equal(
        response.json()["id"],
        pet_id
    )

    check.equal(
        response.json()["name"],
        "Beethoven Actualizado"
    )

    check.equal(
        response.json()["status"],
        "sold"
    )
    response_get = api.get_pet(pet_id)

    check.equal(
    response_get.status_code,
    200,
    "STATUS GET POSTERIOR AL UPDATE INCORRECTO"
    )
    check.equal(
    response_get.json()["name"],
    "Beethoven Actualizado"
    )
    check.equal(
    response_get.json()["status"],
    "sold"
    )
    

def test_delete_pet(created_pet):
    pet_id = created_pet["id"]

    response = api.delete_pet(pet_id)

    logger.info(
        f"""
        === DELETE PET ===
        ID ELIMINADO: {pet_id}
        Response: {response.text}
        ==================
        """
    )

    check.equal(
        response.status_code,
        200,\
        "STATUS DELETE INCORRECTO"
    )

    response_get = api.get_pet(pet_id)

    logger.info(
         f"""
        === VALIDACION DELETE ===
        ID CONSULTADO: {pet_id}
        Response GET: {response_get.json()}
        =========================
        """
    )

    check.equal(
        response_get.status_code,
        404,
        "LA MASCOTA NO FUE ELIMINADA"
    )
    check.equal(
        response_get.json()["code"],
        1,
        "CODIGO DE ERROR INCORRECTO"
    )
    check.equal(
        response_get.json()["type"],
        "error",
        "TIPO DE ERROR INCORRECTO"
    )
    check.equal(
        response_get.json()["message"],
        "Pet not found",
        "MENSAJE DE ERROR INCORRECTO"
    )


import requests

class PetApi:
    URL_BASE = "https://petstore.swagger.io/v2"
    
    def create_pet(self, pet_id, name, status):

        data= {
            "id": pet_id,
            "name": name,
            "status": status
            }
        return requests.post(
           f"{self.URL_BASE}/pet",
           json=data
        )
    
    def get_pet(self,pet_id):
        return requests.get(
            f"{self.URL_BASE}/pet/{pet_id}"
        )
    
    def update_pet(self, pet_id, name, status):

        data= {
            "id": pet_id,
            "name": name,
            "status": status
        }

        return requests.put(
            f"{self.URL_BASE}/pet",
            json=data
        )
    
    def delete_pet(self, pet_id):
        return requests.delete(
            f"{self.URL_BASE}/pet/{pet_id}"
        )
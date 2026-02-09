import requests

data_post = {
    "id": 333,
    "category": {
        "id": 0,
        "name": "string"
    },
    "name": "doggie",
    "photoUrls": [
        "string"
    ],
    "tags": [
        {
            "id": 0,
            "name": "Bim1"
        }
    ],
    "status": "available"
}

BASE_URL = "https://petstore.swagger.io/v2/pet"

headers_post = {"accept": "application/json", "Content-Type": "application/json"}
response_post = requests.post(BASE_URL, headers=headers_post, json=data_post)
print(response_post.status_code)

headers_get = {"accept": "application/json"}
response_get = requests.get(f"{BASE_URL}/333", headers=headers_get)
print(response_get.status_code)

data_put = {
    "id": 333,
    "category": {
        "id": 0,
        "name": "string"
    },
    "name": "doggie",
    "photoUrls": [
        "string"
    ],
    "tags": [
        {
            "id": 0,
            "name": "Bim2"
        }
    ],
    "status": "available"
}

headers_put = {"accept": "application/json", "Content-Type": "application/json"}
response_put = requests.put(f"{BASE_URL}", headers=headers_put, json=data_put)
print(response_put.status_code)

headers_delete = {"accept": "application/json"}
response_delete = requests.delete(f"{BASE_URL}/333", headers=headers_delete)
print(response_delete.status_code)

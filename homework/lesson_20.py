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
            "name": "Bim"
        }
    ],
    "status": "available"
}

headers_post = {"accept": "application/json", "Content-Type": "application/json"}
response_post = requests.post("https://petstore.swagger.io/v2/pet", headers=headers_post, json=data_post)
print(response_post.status_code)

headers_get = {"accept": "application/json"}
response_get = requests.get("https://petstore.swagger.io/v2/pet/333", headers=headers_get)
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
response_put = requests.put("https://petstore.swagger.io/v2/pet", headers=headers_put, json=data_put)
print(response_put.status_code)

headers_delete = {"accept": "application/json"}
response_delete = requests.delete("https://petstore.swagger.io/v2/pet/333", headers=headers_delete)
print(response_delete.status_code)

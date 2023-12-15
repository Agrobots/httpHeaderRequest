import requests
from datetime import date
import re


USERNAME = "igor5653"
TOKEN = "asdasd234sdfsdEWRWsdfwer"
GRAPH_ID = "mygraph001"

str_to_remove = "-"

today = re.sub(str_to_remove, "", str(date.today()))

print(today)

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)



graph_config = {
    "id": GRAPH_ID,
    "name": "MyHabbits",
    "unit": "Exercises",
    "type": "int",
    "color": "ajisai",
}

# нужен токен в заголовке у нас же POST - key+description
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

headers = {
    "X-USER-TOKEN": TOKEN,
}

pixel_data = {
    "date": today,
    "quantity": "5"
}


response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

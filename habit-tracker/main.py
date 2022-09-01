import requests

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "yitav"
TOKEN = "s78f8y238d"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": 'yes',

}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print((response.text))

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Gaming",
    "unit": "Hours",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

pixel_data = {
    "date": "20220901",
    "quantity": "1.2"
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)
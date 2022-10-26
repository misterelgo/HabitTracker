import requests

pixela_endpoint = "https://pixe.la/v1/users"

# 1- Create your user account
USERNAME = "elgo"
TOKEN = "osghfugofnbf8HJ7gfg"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# 2- Create a graph definition
graph_endpoints = f"{pixela_endpoint}/{USERNAME}/graphs"
headers = {
    "X-USER-TOKEN": TOKEN
}
graph_configs = {
    "id": "graph1",
    "name": "Reading Graph",
    "unit": "km",
    "type": "float",
    "color": "shibafu"
}

response = requests.post(url=graph_endpoints, json=graph_configs, headers=headers)
print(response.text)
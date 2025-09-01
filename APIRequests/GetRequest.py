import json
import random
import string

import requests

# base_url
baseurl = "https://jsonplaceholder.typicode.com"


# Get request
def get_request():
    url = baseurl + "/todos/1"
    headers = {"Accept": "application/json", "Content-Type": "application/json"}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print(json_str)
    return response.json()


# Post request
def post_request():
    url = baseurl + "/posts"
    data = {"userId": 1, "title": "POST | PUT | DELETE", "completed": False}
    response = requests.post(url, json=data)
    assert response.status_code == 201
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print(json_str)
    return response.json()


get_request()
post_request()

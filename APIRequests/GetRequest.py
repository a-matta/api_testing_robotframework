import json
import random
import string

import requests

# base_url
baseurl = "https://jsonplaceholder.typicode.com"


# get request
def get_request():
    url = baseurl + "/todos/1"
    headers = {"Accept": "application/json", "Content-Type": "application/json"}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    print(response.json())
    return response.json()


get_request()

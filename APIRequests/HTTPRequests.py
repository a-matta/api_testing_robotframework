import json
import random
import string

import requests

# base_url
baseurl = "https://jsonplaceholder.typicode.com"


# Get request
def get_request():
    url = baseurl + "/todos/1"
    print("GET request")
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
    print("POST request")
    data = {"userId": 1, "title": "Do greatest at in learning steepest", "completed": False}
    response = requests.post(url, json=data)
    assert response.status_code == 201
    f"Unexpected Status Code:{response.status_code}"
    json_data = response.json()
    print(response.status_code)
    assert json_data["title"] == "Do greatest at in learning steepest"
    assert json_data["userId"] == 1
    assert json_data["completed"] == False
    assert "id" in json_data
    print(json_data)
    json_str = json.dumps(json_data, indent=4)
    return json_str


# PUT Request
def put_request(user_id: int = 1):
    url = f"{baseurl}/posts/{user_id}"
    print("PUT request")

    data = {
        "id": user_id,
        "userId": user_id,
        "title": "Updated title with PUT",
        "body": "This is the updated content of the post.",
    }

    response = requests.put(url, json=data)
    print(f"Response status: {response.status_code}")

    json_data = response.json()
    if json_data.get("title") != "Updated title with PUT":
        raise ValueError(f'Unexpected title: {json_data.get("title")}')

    # Pretty-print JSON
    json_str = json.dumps(json_data, indent=4)
    return json_str


# PATCH Request
def patch_request():
    url = f"{baseurl}/posts/1"
    print("PATCH request")
    data = {"title": "Updated title with PATCH"}
    response = requests.patch(url, json=data)
    assert response.status_code in (200, 201)
    json_data = response.json()
    assert json_data["title"] == "Updated title with PATCH"

    # Pretty-print JSON
    json_str = json.dumps(json_data, indent=4)
    print(json_str)


# DELETE Request
def delete_request(user_id: int):
    url = f"{baseurl}/posts/{user_id}"
    print("DELETE request")
    response = requests.delete(url)
    if response.status_code != 200:
        raise ValueError(f"Unexpected status: {response.status_code}")
    return response


get_request()
post_request()
put_request(1)
patch_request()
delete_request(1)

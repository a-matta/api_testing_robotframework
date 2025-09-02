import json
import random
import string

import requests
from requests.auth import HTTPBasicAuth

response = requests.get("http://api.github.com/user", auth=HTTPBasicAuth("username", "password"))
print(response.status_code)
print(response.json)

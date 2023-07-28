from tinydb import TinyDB
import json
from api import base_url
import requests
db = TinyDB('data.json',indent=4)
for i in range(10):
    response= requests.get(base_url)
    r=response.json()
    result=r["results"][-1]
    user={"first_name":result["name"]["first"],
        "last_name": result["name"]["last"],
        "age": result["registered"]["age"],
        "phone": result["phone"],
        "country": result["location"]["country"],
        "email": result["email"]
        }
    db.insert(user)
    print(i)
db.truncate()

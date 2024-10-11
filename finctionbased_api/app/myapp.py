import requests
import json

URL = "http://127.0.0.1:8000/student/"

def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}

    # Send GET request with query parameters using `params`
    r = requests.get(url=URL, params=data)

    # Try to decode JSON response
    try:
        data = r.json()
        print(data)
    except requests.exceptions.JSONDecodeError:
        print("The response content is not valid JSON")
    
#get_data()

def post_data():
    data = {
        
        'name': 'Omkar',  # 'sonam' should be a string
        'roll': 501,
        'city': 'pune'
    }

    # Use the json parameter to send JSON data in the request
    r = requests.post(url=URL, json=data)

    # Try to decode the JSON response
    try:
        response_data = r.json()  # Using a different variable name to avoid confusion
        print(response_data)
    except requests.exceptions.JSONDecodeError:
        print("The response content is not valid JSON")

#post_data()

def update_data():
    data = {
        'id':1,
        'name': 'Rajani',  
        'roll': 102,
        'city': 'Punawale'
    }

   
    r = requests.put(url=URL, json=data)

   
    try:
        response_data = r.json()  # Using a different variable name to avoid confusion
        print(response_data)
    except requests.exceptions.JSONDecodeError:
        print("The response content is not valid JSON")

#update_data()

def delete_data():
    data = {
        'id':1,
        
    }

    # Use the json parameter to send JSON data in the request
    r = requests.delete(url=URL, json=data)

    # Try to decode the JSON response
    try:
        response_data = r.json()  # Using a different variable name to avoid confusion
        print(response_data)
    except requests.exceptions.JSONDecodeError:
        print("The response content is not valid JSON")

delete_data()

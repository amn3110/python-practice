# # # import requests

# # response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

# # print(response.status_code)
# # print(response.text)

# # data = response.json()

# print(data["id"])
# print(data["userId"])
# #

# import requests
# try:
#    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

# if response.status_code == 200:
#     print("UP")
# else:
#     print("not up")

import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

print(response.status_code)
print(response.text)

data = response.json()

print(data["title"])
print(data["userId"])

##===================================

#####practise exception handil############

import requests

try:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/1",
        timeout=10
    )

    response.raise_for_status()
    data = response.json()
    print(data["title"])
except requests.exceptions.Timeout:
    print("API request timeout")
except requests.exceptions.HTTPError as error:
    print("HTTP error:", error)
except requests.exceptions.RequestException as error:
    print("api request failed:", error)



##++++++++++++++++++++++

import requests

try:
    reponse = requests.get(
        "https://jsonplaceholder.typicode.com/posts/1",
        timeout=10)
    #data = reponse.json()
    if reponse.status_code == 200:
        print(f"API is UP: {reponse.status_code}")
    else:
        print("api is Down")
except requests.exceptions.RequestException:
    print("API connection failed")

###############################################
+++++++++ headers ############

import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

params = {
    "userId" : 1
}

response = requests.get(url, params=params)
print(response.url)
print(response.status_code)

##===POST ===========

import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

data = {
    "title" : "High CPU Alert",
    "body" : "app1 cpu is 95%",
    "userId" : 1
}

response = requests.post(url, json=data)

print(response.status_code)



#===============================

import requests


def get_server_info(userId):
    url = "https://jsonplaceholder.typicode.com/posts/1"

    params = {
        "userId" : userId
    }

    headers = {
        "Accept" : "application/json"
    }

    try:
        response = requests.get(url, params=params, headers=headers,timeout=10)
        response.raise_for_status
        print(response.status_code)
    except requests.exceptions.RequestException as error:
        print("api connction failed")
        
get_server_info(1)
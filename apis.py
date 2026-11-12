# # # import requests

# # # response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

# # # print(response.status_code)
# # # print(response.text)

# # # data = response.json()

# # print(data["id"])
# # print(data["userId"])
# # #

# import requests
# try:
# response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

# if response.status_code == 200:
#     print("UP")
# else:
#     print("not up")

##load() json file - python object
##dump( )python object json file
##loads() json sting python object

##dumps() python object json sring 
# # import json

# # data = '{"name":"app1", "status": "UP", "CPU":45}'

# # server = json.loads(data)

# # print(server["name"])


# import json

# with open("servers.json", "r") as file:
#     servers = json.load(file)
# for server in servers:
#     print(server['name'], server['status'])


#  import json

# alerts = [
#     {"name": "app1", "issue": "DOWN"},
#     {"name": "app2", "issue": "UP"}
#     ]

# with open(alerts.json, "w") as file:
#     json.dump(alerts, file, indent=4)
# import json

# # Your list of alerts
# alerts = [{"id": 1, "message": "Low disk space"}]

# # Correct way to write a list to a JSON file
# with open("alerts.json", "w") as file:
#   json.dump(alerts, file, indent=4)


import json

alerts = [
    {"name": "app1", "issue": "Down"},
    {"name": "app2", "issue":"UP"}
]

with open("alerts.json", "w") as file:
    json.dump(alerts, file, indent=4)
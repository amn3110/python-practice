##Task 1

server = {"name":"app1",
          "status": "UP",
          "CPU": 90,
          "memory": 70
          }
##print(server)

###Task 2
# print(f"Server name: {server['name']}")
# print(f"status: {server['status']}")
# print(f"CPU: {server['CPU']}%")

###Task 3

# server["CPU"] = 90
# server["status"] = "DOWN"
# print(server)

### Task 4

# server["env"] ="prod"
# print(server)

##task 5

# if server["CPU"]>80:
#     print(f"high cpu on {server['name']}")
# else:
#     print("normal")

servers= [
    {"name" : "app1", "status" : "up", "cpu" : 45},
    {"name" : "app2", "status" : "down", "cpu" : 90},
    {"name" : "app3", "status" : "up", "cpu" : 85}
    ]

# for server in servers:
#     if server["cpu"]>80:
#         print(f"{server['name']}")

###task 6

for server in servers:
    if server["status"] == "down":
        print(f"{server['name']}")

         

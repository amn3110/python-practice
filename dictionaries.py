server= {"name" : "app1",
         "status" : "up",
         "cpu" : 75
         }

# print(server["name"])
# print(server["cpu"])
# print(server["status"])


# ###Update value
# server["cpu"] = 80

# print(server["cpu"])

# ##Remove value

# del server["cpu"]
# print(server)

# ###pop

# server.pop("status")
# print(server)


###print key
# for key in server:
#     print(key)

###Print values 

# for value in server.values():
#     print(value)

# for key, value in server.items():
#     print(f"{key} : {value}")

# if server["cpu"]>80:
#     print("high cpu")
# else:
#     print("Normal")

######List of dictionary 

servers= [
    {"name" : "app1", "status" : "up", "cpu" : 75},
    {"name" : "app2", "status" : "down", "cpu" : 90},
    {"name" : "app3", "status" : "up", "cpu" : 80}
    ]

for server in servers:
    if server["cpu"]>80:
        print(f"High cpu server is {server['name']}")
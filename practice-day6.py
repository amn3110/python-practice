# ###Practise Dictionary+List SRE automation##########

# server = {"name":"app1",
#           "status": "Up",
#           "cpu": 67}
# #Print dictionary
# print(server)
# ##Add
# server["memory"] = 89
# print(server)
# ##Remove value 

# del server["cpu"]
# print(server)

# ##update 
# server["cpu"] = 56
# print(server)


servers = [{"name":"app1", "cpu":78, "status":"Down"},
          {"name":"app2", "cpu":67, "status":"Down"},
          {"name":"app3", "cpu": 90, "status":"UP"}
          ]
# for server in servers:
#     if server["cpu"] > 70:
#         print(f"Server {server['name']} cpu is High server['cpu']}")
# for server in servers:
#     print(server["name"])

###print each servers name and status

# for server in servers:
#     print(f"{server['name']} is {server['status']}")
###printt server name whos cpu is >80

# for server in servers:
#     if server["cpu"]>80:
#         print(f"{server['name']}")


## down server 

# for server in servers:
#     if server["status"] == "Down":
#         print(f"{server['name']}")

##count failed servers 

# failed_servers = 0

# for server in servers:
#     if server["status"] == "UP":
#         failed_servers = failed_servers + 1
# print(f"failed servers {failed_servers}")

### create emply list ad=nd add servers which failed

failed_servers = []
for server in servers:
    if server["status"] == "Down":
        failed_servers.append(server["name"])
print(failed_servers)

    
    

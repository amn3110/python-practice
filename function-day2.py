##function list 

def check_status(servers):
    failed = []
    for server in servers:
        if server["status"] == "DOWN":
            failed.append(server["name"])
    return failed







servers = [{"name":"app1", "status":"UP"},
           {"name":"app2", "status":"DOWN"},
           {"name":"app3", "status":"UP"}
        ]
result = check_status(servers)
print(result)
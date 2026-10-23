servers = [
    {"name" : "app1", "cpu": 45},
    {"name" : "app2", "cpu": 56},
    {"name" : "app3", "cpu": 89}
]

with open("alert.txt", "w") as file:
    for server in servers:
        if server["cpu"]>50:
            message = f"ALERT: server {server['name']} has high cpu {server['cpu']}"
            file.write(message)
print("moniroring alert saved")

# server = ["app1", "app2", "app3", "app4"]
# print(server[2])
# print(server[0])

###negative indexing

# server = ["app1", "app2", "app3", "app4"]
# print(server[-1])
# print(server)
# server[1] ="app2-new"
# print(server)

#######Append item

# servers = ["app1", "app2", "app3"]
# servers.append("app4")
# print(servers)

# failed_servers =[]
# failed_servers.append("app1")
# print(failed_servers)

#######insert 

# servers = ["app1", "app2", "app3"]
# servers.insert(2, "app4")
# print(servers[2])

########extend 

# servers = ["app1", "app2"]
# servers.extend(["app3", "app4"])
# print(servers)

###Remove 

# servers = ["app1", "app2", "app3"]
# servers.remove("app3")
# print(servers)

##pop

# servers.pop()
# print(servers)
# servers.clear()
# print(servers)

##Len

servers = ["app1", "app2", "app3"]
# print(len(servers))

#####Use in 
print("app2" in servers)
if "app2" in servers:
    print("server exist")

##Slicing 

print(servers[1:2])

for server in servers:
    print(f"checking {server}")
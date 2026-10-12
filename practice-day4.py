#Task 1

# servers = ["app1", "app2", "app3", "app4", "app5"]
# print(servers[0])
# print(servers[2])
# print(servers[4])

##Task 2

# servers = ["app1", "app2", "app3"]

# servers[1] = "database01"
# print(servers)

###Task3

# servers = ["app1", "app2"]
# servers.append("app3")
# servers.append("app4")
# servers.append("app5")
# print(servers)

##Task4
# servers = ["app1", "app2", "app3", "app4"]
# servers.remove("app3")
# print(servers)

#Task5

# new_cpu= []
# cpu_values = [45,91,67,88,72,95]
# for cpu in cpu_values:
#     if cpu>80:
#         new_cpu.append(cpu)
# print(new_cpu)

###Task 6
# failed_servers = []
# servers = ["app1", "app2", "app3", "app4"]
# status = ["UP", "DOWN", "UP", "DOWN"]
# for i in range(len(servers)):
#     if status[i] == "DOWN":
#         failed_servers.append(servers[i])
# print(failed_servers)

##Tak 7
final_list = []
servers = ["app1", "app2", "app3", "app4", "app5"]
cpu = [45, 92, 67, 88, 95]

for i in range(len(servers)):
    if cpu[i]>80:
        final_list.append(servers[i])
print(final_list)


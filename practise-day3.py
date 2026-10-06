##Task1
# servers = ["app1", "app2","app3","app4","app5"]
# for server in servers:
#     print(server)

##Task 2

# servers = ["app1","app2","app3","app4"]
# stauses = ["UP","DOWN","UP","DOWN"]
# for i in range(len(servers)):
#     print(f"{servers[i]} is {stauses[i]}")

#Task 3

# cpu_values = [45,87,91,55,88,72]
# for cpu in cpu_values:
#     if cpu > 80:
#         print(f"High CPU {cpu}%")
#     else:
#         print(f"Normal CPU {cpu}%")

###task 4
# count = 0
# cpu_values = [45,87,91,55,88,72]
# for cpu in cpu_values:
#     if cpu > 80:
#         #print(f"High CPU {cpu}%")
#         count =count +1
# print(f"High CPU servers {count}")

#Task 5

# 

## Task 6
count = 1
while count<=3:
    print(f"Checking application ...Attempt {count}")
    count = count +1
print("Application is DOwN")

    
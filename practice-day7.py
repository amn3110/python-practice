##Task 1###

# def show_message():
#     print("Pythonn automation started")
# show_message()

##Task2##

# def check_cpu(cpu):
#     if cpu > 80:
#         print("High Cpu")
#     else:
#         print("Normal")
# check_cpu(70)
# check_cpu(90)

##Task 3

# def check_status(server, status):
#     print(f"{server} is {status}")
# check_status("app1", "UP")
# check_status("app2", "down")

##Task 4

def is_high_cpu(cpu):
    if cpu > 80:
        return True
    else:
        return False
result = is_high_cpu(90)
print(result)


## Task5 
def check_server(server, cpu):
    for i in range(len(server)):
        if cpu[i]>80:
            print(f"ALERT: {server[i]} cpu is high- {cpu[i]}%")

    
server_list = ["app1", "app2", "app3"]
cpu_list = [70, 80, 90]
check_server(server_list, cpu_list)
#if -else
# status_code = 503
# if status_code == 200:
#     print("server is healthy")
# elif status_code > 500:
#     print(f"status recived: {status_code}")
# else:
#     print("not found")

#`logical operations - and, or,not
# cpu = 80
# memory =90

# if cpu > 75 and memory > 80:
#     print("server is under heavy load")
# else:
#     print("server is healthy")

#not

status_up = False 
if not status_up:
    print("server down")
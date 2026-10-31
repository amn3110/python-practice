# #########import

# import platform
# print(platform.system())
# print(platform.release())

# import datetime

# print(datetime.datetime.now())

from server_utils import check_cup, check_status

print(check_cup(95))
print(check_cup(70))

print(check_status("DOWN"))
print(check_status("UP"))
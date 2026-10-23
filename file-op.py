##read() and "r" read mode

# with open("server.txt", "r") as file:
#     data = file.read()
# print(data)

##readline()

# with open("server.txt", "r") as file:
#     data = file.readline()
# print(data)

##readlines()

# with open("server.txt", "r") as file:
#     lines = file.readlines()

# for line in lines:
#     print(line.strip())

#"w" write mode and write()

# with open("server2.txt", "w") as file:
#     file.write("app4 CPU 45%\n")
#     file.write("app5 CPU 67%\n")

### "a" Append mode 

with open("server2.txt", "a") as file:
    file.write("Practice")
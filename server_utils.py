def check_cup(cpu, treshold=80):
    if cpu >treshold:
        return "High CPU"
    else:
        return "Normal CPU"

def check_status(status):
    if status == "DOWN":
        return "server is down"
    else:
        return "server is up"
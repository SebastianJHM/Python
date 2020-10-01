import re
import operator
import csv

def isERROR(line):
    result = re.search(r"ticky: ERROR ([\w ]*) ", line)
    return(result)

def isINFO(line):
    result = re.search(r"ticky: INFO ([\w ]*) ", line)
    return(result)
    
def getUSER(line):
    result = re.search(r"\((\w.+)\)", line)
    return result

error = {}


filepath = 'syslog.log'
file  = open(filepath,'r')
events = file.read().splitlines()
for line in events:
    if isERROR(line) is not None:
        x = isERROR(line)
        x = x.groups()[0]
        if not x in error:
            error[x] = 1
        else:
            error[x] += 1

error_list = sorted(error.items(), key = operator.itemgetter(1), reverse=True)
error_list.insert(0, ("Error", "Count"))
print(error_list)

error_output_file = open("error_message.csv", "w")
writer = csv.writer(error_output_file)
writer.writerows(error_list)



user = {}
for line in events:
    u = getUSER(line)
    u = u.groups()[0]
    if not u in user:
        user[u] = [0, 0]
        if isERROR(line) is not None:
            user[u][1] += 1
        else:
            user[u][0] += 1
    else:
        if isERROR(line) is not None:
            user[u][1] += 1
        else:
            user[u][0] += 1

ul = sorted(user.items(), key = operator.itemgetter(0))
user_list = [("Username", "INFO", "ERROR")]
for x in ul:
    user_list.append((x[0], x[1][0], x[1][1]))
print(user_list)

user_output_file = open("user_statistics.csv", "w")
writer = csv.writer(user_output_file)
writer.writerows(user_list)
        

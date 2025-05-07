import os
import time
# 
import csv
import datetime
# 
# #1) salvestada tulemused failisse ping_long.csv
# # Time,status
# # 05.04.20.25,OK
# # 05.04.20.25,Fail
# 
# hosts= ["8.8.8.8","1.1.1.1", "192.168.1.1" ]
# 
# with open("ping_log.csv","w",newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow(["Time","Status"])
# 
# while True:
#     print("kättesadavuse kontroll")
#     now = datetime.datetime.now()
#     result = ""
#     for elem in hosts:
#         response = os.system(f"ping -n 1 {elem} > null")
#         
#         if response == 0:
#             resul = "OK"
#             print(elem, "kätesadavalt")
#         else:
#             result = "Fail"
#             print(elem, "ei ole kättesadavalt")
#         print("-"*30)
#         time.sleep(5)
#         
#         with open("ping_log.csv", "a",newline="") as file:
#             writer = csv.writer(file)
#             writer.writerow(["",result])





            
# võimalus vadata kõil  protsesid arvutis
# salvestada need failise tasklist ["Time", "Process name", "Memory usage"]
import os

with open("taskid.csv", "w",newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Time","Process name", "Proccesid"])


    
    



output = os.popen("tasklist").read()
test = output.splitlines()
for i in range(7,len(test)):
    print(test[i])
    now = datetime.datetime.now()
    proccesName = test[i].split()
    name = proccesName[0]
    memory = proccesName[-2]
    print("time: ", now,"name: ", name, "memory: ", memory)
    
    with open("taskid.csv", "a",newline="") as file:
        writer = csv.writer(file)
        writer.writerow([now, proccesName, "ProccesId"])
    





import csv
file_name = "/Users/suwaidi/Desktop/G44P1/air_quality.csv"
file = open(file_name, "r")
data_reader = csv.reader(file)
UHF_to_measurements ={}
date_to_measurements = {}
x = 0
for i in data_reader:
    if len(i[0]) > 3:
        continue
    if x == 0:
        i[0] = "101"
        x+=1
    if i[0] not in UHF_to_measurements.keys():
        UHF_to_measurements[i[0]] = [(i[1:])]
        
    else:
        UHF_to_measurements[i[0]].append((i[1:]))
        
    if i[2] not in date_to_measurements.keys():
        date_to_measurements[i[2]] = [(i[1:])]
    else:
        date_to_measurements[i[2]].append((i[1:]))



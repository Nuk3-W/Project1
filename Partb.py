import csv
file_name = "/Users/suwaidi/Desktop/G44P1/uhf.csv"
file = open(file_name, "r")
data_reader = csv.reader(file)
zipcode_to_UHF = {}
Borough_to_UHF = {}
for i in data_reader:
    UHF = i[2]
    if len(UHF) > 3:
        continue
    for j in i[3:]:
        if j in zipcode_to_UHF.keys():
            zipcode_to_UHF[j].append(UHF)
        else:
            zipcode_to_UHF[j] = [UHF]
    
    if i[0] in Borough_to_UHF.keys():
        Borough_to_UHF[i[0]].append(UHF)
    else:
        Borough_to_UHF[i[0]] = [UHF]

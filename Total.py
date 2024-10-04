# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 15:14:34 2024

@author: colin
"""
import csv
file_name = "uhf.csv"
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

file.close()

file = open("air_quality.csv", 'r')
data_reader = csv.reader(file)
UHF_to_measurements ={}
date_to_measurements = {}
x = 0
for i in data_reader:
    if len(i[0]) > 3:
        continue

        
    if i[0] not in UHF_to_measurements.keys():
        UHF_to_measurements[i[0]] = [(i[1:])]
        
    else:
        UHF_to_measurements[i[0]].append((i[1:]))
        
    if i[2] not in date_to_measurements.keys():
        date_to_measurements[i[2]] = [(i[0:])]
    else:
        date_to_measurements[i[2]].append((i[0:]))
        
file.close()
        
search = input("Search by zip code, UHF id, borough, or date: ")
user_input = input("input " + search.lower() + " of thing: ")

if (search.lower() == "zip code"):
    for i in UHF_to_measurements[zipcode_to_UHF[user_input][0]]:
        print(i[1], "UHF", zipcode_to_UHF[user_input][0], i[0], i[2], "mcg/m^3")
elif (search.lower() == "date"):
    for i in date_to_measurements[user_input]:
        print(user_input, "UHF",i[0], i[1], i[3], "mcg/m^3")
elif (search.lower() == "uhf id"):
    for i in UHF_to_measurements[user_input]:
        print(i[1], "UHF", user_input, i[0], i[2], "mcg/m^3")
else:
    for i in UHF_to_measurements[Borough_to_UHF[user_input][0]]:
        print(i[1], "UHF", Borough_to_UHF[user_input][0], i[0], i[2], "mcg/m^3")
    

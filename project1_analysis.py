"""
a) What was the highest and lowest pollution measurement ever recorded in zip code 10027?
b) Which UHF id had the worst pollution in 2019.
c) What was the average air pollution in Manhattan in 2008 and in 2019.
d) Come up with at least two other questions to ask about the dataset and 
write code to answer them.
"""

import project1

Borough_to_UHF, zipcode_to_UHF = project1.uhf_file_load()
UHF_to_measurements, date_to_measurements = project1.air_quality_load()


high = -1
low = -1
for i in UHF_to_measurements[zipcode_to_UHF["10027"][0]]:
    pollution = float(i[-1])
    if high == -1:
        high = pollution
        low = pollution
    if high < pollution:
        high = pollution
    elif low > pollution:
        low = pollution

print("The highest pollution in zip code 10027 is", high)
print("The lowest pollution in zip code 10027 is", low)

high = -1
data = []
for i in date_to_measurements['6/1/19']:
    pollution = float(i[-1])
    if high == -1:
        high = pollution
    if high < pollution:
        high = pollution
        data = i
for i in date_to_measurements['12/1/19']:
    pollution = float(i[-1])
    if high < pollution:
        high = pollution
        data = i
        
print("The UHF id that had the worst pollution in 2019 is", data[0])

#c) What was the average air pollution in Manhattan in 2008 and in 2019.

sum_of_pollution = 0
iterables = 0
for i in Borough_to_UHF["Manhattan"]:
    for j in UHF_to_measurements[i]:
        if len(j) == 4:
            x = j[2]
        else:
            x = j[1]
        if (int(x[-2:]) >= 8) and (int(x[-2:]) <= 19):
            sum_of_pollution += float(j[-1])
            iterables += 1
            
#print(sum_of_pollution, iterables)

print("The aveage between 2008 and 2019 in Manhattan is", sum_of_pollution/iterables)

#What borough had the lowest average pollution between 2008 and 2019

borough_average = []
for i in Borough_to_UHF.keys():
    sum_of_pollution = 0
    iterables = 0
    for j in Borough_to_UHF[i]:
        for k in UHF_to_measurements[j]:
            if len(k) == 4:
                x = k[2]
            else:
                x = k[1]
            if (int(x[-2:]) >= 8) and (int(x[-2:]) <= 19):
                sum_of_pollution += float(k[-1])
                iterables += 1
    borough_average.append((i,sum_of_pollution/iterables))
                
    
borough_average.sort(key=lambda i: i[1])
print("The borough with the lowest pollution across the dataset is", borough_average[0][0], "with an average of", borough_average[0][1])


#What UHF ID has the lowest average pollution
UHF_average_pollution = []
for i in UHF_to_measurements.keys():
    sum_of_pollution = 0
    iterables = 0    
    for j in UHF_to_measurements[i]:
        sum_of_pollution += float(k[-1])
        iterables += 1
    UHF_average_pollution.append((i,sum_of_pollution/iterables))
            
    
UHF_average_pollution.sort(key=lambda i: i[1])
print("The UHF id with the lowest pollution across the dataset is", UHF_average_pollution[0][0], "with an average of", UHF_average_pollution[0][1])

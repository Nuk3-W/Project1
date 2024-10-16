import csv
def uhf_file_load():
    file = open("uhf.csv", "r")
    data_reader = csv.reader(file)
    zipcode_to_UHF = {}
    Borough_to_UHF = {}
    for i in data_reader:
        UHF = i[2]
        for j in i[3:]:
            if j.strip() in zipcode_to_UHF.keys():
                zipcode_to_UHF[j.strip()].append(UHF)
            else:
                zipcode_to_UHF[j.strip()] = [UHF]
        
        if i[0] in Borough_to_UHF.keys():
            Borough_to_UHF[i[0]].append(UHF)
        else:
            Borough_to_UHF[i[0]] = [UHF]
    
    file.close()
    return Borough_to_UHF, zipcode_to_UHF

def air_quality_load():
    file = open("air_quality.csv", 'r')
    data_reader = csv.reader(file)
    UHF_to_measurements ={}
    date_to_measurements = {}
    x = 0
    for i in data_reader:
        if x == 1:
            x+=1
            continue #This is to ensure that the "weird" 101 UHF is not included
        
        if i[0] not in UHF_to_measurements.keys():
            UHF_to_measurements[i[0]] = [(i[1:])]           
        else:
            if UHF_to_measurements[i[0]][-1][1] != i[2]:
                UHF_to_measurements[i[0]].append((i[1:]))

    
    
        if i[2] not in date_to_measurements.keys():
            date_to_measurements[i[2]] = [(i[:])]
        else:
            if i not in date_to_measurements[i[2]]:
                date_to_measurements[i[2]].append((i[:]))
            # else:
            #     print(i)
            
    file.close()
    return UHF_to_measurements, date_to_measurements
        
Borough_to_UHF, zipcode_to_UHF = uhf_file_load()
UHF_to_measurements, date_to_measurements = air_quality_load()

if __name__ == "__main__": 
    search = input("Search by zip code, UHF id, borough, or date: ")
    user_input = input("input "+ search+ " you want to look more into: ")
    
    if (search.lower() == "zip code"):
        if len(zipcode_to_UHF[user_input]) == 2:
            for i, j in zip(UHF_to_measurements[zipcode_to_UHF[user_input][0]], UHF_to_measurements[zipcode_to_UHF[user_input][1]]):
                print(i[1], "UHF", zipcode_to_UHF[user_input][0], i[0], i[2], "mcg/m^3")
                print(j[1], "UHF", zipcode_to_UHF[user_input][1], j[0], j[2], "mcg/m^3 \n")
        else:
            for i in UHF_to_measurements[zipcode_to_UHF[user_input][0]]:
                print(i[1], "UHF", zipcode_to_UHF[user_input][0], i[0], i[2], "mcg/m^3 \n")
        
    elif (search.lower() == "date"):
        for i in date_to_measurements[user_input]:
            print(user_input, "UHF",i[0], i[1], i[3], "mcg/m^3 \n")
            
    elif (search.lower() == "uhf id"):
        for i in UHF_to_measurements[user_input]:
            print(i[1], "UHF", user_input, i[0], i[2], "mcg/m^3 \n")
            
    elif (search.lower() == 'borough'):
        for j in Borough_to_UHF[user_input]:
            for i in UHF_to_measurements[j]:
                print(i[1], "UHF", j, i[0], i[2], "mcg/m^3 \n")
    else:
        print("Your input is not valid")
        

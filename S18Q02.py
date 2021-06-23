"""S18Q02
The lap speeds recorded for 
Michael Schumacher, 
Montoya Juan-Pablo and 
Barrichello Rubens in a F1 race are

( 258.626, 255.931, 258.998, 255.195 ), 
(258.680, 257.925, 259.828, 257.422) and 
(258.405, 256.700, 260.395) respectively

- Find the fastest lap for each driver
- Find the average speed for each driver
- Which driver has recorded the fastest lap ?
- Which driver has the fastest lap average ?

- Print the data in the following formats


INPUT FILE NAME: RACE.TXT

"""
# Helper functions


def get_filename_as_agrv_if_no_ask(prompt):
    """ get filename as argument from user or if not given, take filename interactively.
         Return file handle
    """
    Found = False
    ln = len(sys.argv)
    while not Found:
        if ln < 2:
            file = input( prompt)
        else:
            file = sys.argv[1]
        try:
            RFH = open(file)
            Found = True
        except FileNotFoundError:
            print("%%Error! File not found!")
            ln = 1
#            break
    return  RFH

def get_shell_env_var_data(RFH):
    line = "xx"
    var_dict = dict()
    print("FILE CONTENTS:-\n")
    while line != "":
        line = RFH.readline()
        line = line.strip()
        if line == "": 
            break
        
        print(line)
        data = line.split(sep=",")
        var_dict[data[0]] = data[1]
    print("\n")
    return var_dict
def get_data_list(RFH):
    """ reading data from RACE data file line after line, processing it and build 1 list and a dictionary.
        One list is for holding  Keys(Names). Dictionary will have all values against each key
    """
    line = "xx"
    race_data = dict()  # To hold all race related data in dictionary
#    key_list = list() # List to hold Keys
    contents = []
    print("FILE CONTENTS:-")
    while line != "":   #For Each Line read, till end of file
        line = RFH.readline() 
        line = line.strip()  # Remove leading and trailing white spaces
        print(line)
        if line == "":  # If EOF, break from loop
            break
        contents = line.split(",")
        print("Contents:",contents)
#        key_list.append(contents[0])
        data_len = len(contents)
        n = len(contents)
        for i in range(1,n):
            contents[i] = float(contents[i])
        race_data[contents[0]] = contents[1:data_len]
    return race_data
def make_list_ascending(list1,list2,list3):
    i = 0
    j = 0
    n = len(list1)
    while i < n:
        j = 0
        while j < n-i-1:
            if list1[j] > list1[j+1]:
                list1[j],list1[j+1] = list1[j+1],list1[j]
                list2[j],list2[j+1] = list2[j+1],list2[j]
                list3[j],list3[j+1] = list3[j+1],list3[j]
                j += 1
            else:
                j += 1
        i += 1
    return list1,list2,list3

import sys
# Main starts from here
def main():
    keys = list()
    RFH = get_filename_as_agrv_if_no_ask("Enter Contact List Data File Name : ")
    race_data = get_data_list(RFH)
#    print(race_data)
    keys = list(race_data.keys())
    values = list()
    average = list()
    laps = list()
    best_timing = list()
#    print("KEYS:",keys)
    i = 0
    for key in keys:
        values = list(race_data.get(key))
#        print("for Key:",key," ","VALUES:",values)
        min = 10**20
        sum = 0
        for value in values:
            sum += value
            if value < min:
                min = value
        average.append(sum/len(values))
        best_timing.append(min)

    best_timing,keys,average = make_list_ascending(best_timing,keys,average)
    print("\nRank","Driver"," "*11,"Fastest Lap",3*" ","Av.speed")
    for i in range(0,len(keys)):
        print( i+1,"  ",keys[i],best_timing[i]," "*7,average[i])
    print("\n RACE     ",end = "")
    for key in keys:
        print(str(key[:key.find(" ")]),"      ",end = "")
    # find max rows
    laps = list()
    rows = 0
    print("")
    for key in keys:
#        laps.append(len(race_data.get(key)))
#        print("Key",key,"# races",len(race_data.get(key)))
        
        if len(race_data.get(key)) > rows:
            rows = len(race_data.get(key))
        
    for i in range(0,rows):
        print("  ",i,"   ",end="")
        for j in range(0,len(keys)):
            try:
                print("  ",race_data[keys[j]][i],"    ",end = "")
                continue
            except IndexError:
                print("              ",end="")
        
        print("\n")
    
        
        
 

main()

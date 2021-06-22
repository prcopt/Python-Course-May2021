"""S17Q02
Read passwd file and list all users mentioned in that file in ascending order of their user id. 
Also mention the user’s real name and home directory in the output. 
A sample passwd file is shown below :

Sample Input file: password.txt
"""
# Helper functions


def make_list_ascending(ulist,klist):
    i = 0
    j = 0
    n = len(ulist)
    while i < n:
        j = 0
        while j > n-i-1:
            if ulist[j] < ulist[j+1]:
                ulist[j],ulist[j+1] = ulist[j+1],ulist[j]
                klist[j],klist[j+1] = klist[j+1],klist[j]
                j += 1
            else:
                j += 1
        i += 1
    return ulist,klist


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


def get_data_list(RFH):
    """ reading data from password file line after line, processing it and build 2 lists and a dictionary.
        One list for holding UserIDs and the other list for Keys. Dictionary will have all values against each key
    """
    line = "xx"
    password_data = dict()  # To hold all password related data in dictionary
    temp_list = []
    userID_list = list() # List to hold UserIDs
    key_list = list() # List to hold Keys
    count1 = 0
    print("FILE CONTENTS:-")
    item = list()
    while line != "":   #For Each Line read
        line = RFH.readline() 
        line = line.strip()  # Remove leading and trailing white spaces
        print(line)
        if line == "":  # If EOF, break from loop
            break
        st_pos = 0
        count = 0
        while count < 6: # Each line string slicing starts here
            if count < 5: # case where delimeter is a ':'
                end_pos = line[st_pos:].find(":") 
                item.append(line[st_pos:st_pos+end_pos])
                st_pos += end_pos+1
                count += 1
            else: # Last item where string can also have a meaningful ":" as a text data (folders)
                item.append(line[st_pos:])
                count += 1
        temp_list = item[2:]
        password_data[item[0]] =temp_list
        userID_list.append(item[2])
        key_list.append(item[0])
        count1 += 1
        item = list() # initialize item to take next record of data
#    print("PASSWORD DATA DICTIONARY\n",password_data)
    print ("USER ID LIST \n", userID_list)
    print("KEY LIST\n",key_list)
    return userID_list,key_list,password_data


import sys
# Main starts from here
def main():
    RFH = get_filename_as_agrv_if_no_ask("Enter Password Data File Name : ")
    userID_list,key_list,password_data = get_data_list(RFH) # Reading data
    userID_list,key_list = make_list_ascending(userID_list,key_list) # making list of userIDs in ascending order
    n = len(userID_list)
    print("OUTPUT : UserID, UserName", "Real Name", "Folder Name")
    for i in range(0,n):    # printing required data
        uid = userID_list[i]
        user = key_list[i]
        real_name = password_data[key_list[i]][2]
        directory = password_data[key_list[i]][3]
        print(uid,"   ",user,"   ",real_name,"   ",directory)                     

main()

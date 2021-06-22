"""S17Q03 - Phonebook Search Program
Write a Python program that takes a file name as its argument. 
This file contains names of people and their corresponding contact numbers.

- Prompt the user to enter a few characters to search for.
- Print all the names that contain this sequence of characters 
in the ascending order of their names

Input File: contact_list.txt

"""
# Helper functions


def make_list_ascending(nlist):
    i = 0
    j = 0
    n = len(nlist)
    while i < n:
        j = 0
        while j < n-i-1:
            if nlist[j][0] > nlist[j+1][0]:
                nlist[j][0],nlist[j+1][0] = nlist[j+1][0],nlist[j][0]
                nlist[j][1],nlist[j+1][1] = nlist[j+1][1],nlist[j][1]
                j += 1
            else:
                j += 1
        i += 1
    return nlist
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

def get_contact_list(RFH):
    line = "xx"
    contact_list = list()
    print("FILE CONTENTS:-")
    while line != "":
        line = RFH.readline()
        line = line.strip()
        if line == "": 
            break

        data = line.split(sep=":")
        print(line)
        data[1] = int(data[1])
        contact_list.append(data)
    item_count = len(contact_list)
    return contact_list


import sys
# Main starts from here
def main():
    
    RFH = get_filename_as_agrv_if_no_ask("Enter Contact List Data File Name : ")
    contact_list = get_contact_list(RFH)
    ascending_list = make_list_ascending(contact_list)
    ln = len(ascending_list)
    inchars = input("Key-in Search String>")
    for i in range(0,ln):
        if contact_list[i][0].find(inchars) >= 0:
            print(contact_list[i][0],"  ",contact_list[i][1])
        

            
##    items = len(descending_list)
##    print("\nCONTACT LIST IN ASCENDING ORDER OF AGE:-")
##    tabular_formatted_printing(ascending_list)
    


main()

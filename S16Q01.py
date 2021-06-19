"""S16Q01
Write a Python program that takes a file name as its argument. 
This file contains names of people and their corresponding contact numbers. 

Read the file, and print the list in the ascending order of their names. 
A sample file [ CONTACT_LIST.TXT ] is shown below :
Sample Datafile: Contact_list.txt

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
        if line == "":
            break
        print(line,end="")
        data = line.split(sep=":")
        data[1] = int(data[1])
        contact_list.append(data)
    item_count = len(contact_list)
    return contact_list

def tabular_formatted_printing(data_list):
    """ prints a list consisting of each element is a list of 2 itmes as (str,int) in a neat format
    [example list = [ ("abc",1),("efghij",20),......etc ]
    """
    n = len(data_list)
    max = 0
    for i in range(0,n):
        if int(len(data_list[i][0])) > max:
            max = len(data_list[i][0])
    for i in range(0,n):
        if int(len(data_list[i][0])) < max:
            space = max - len(data_list[i][0])
        else:
            space = 0
        print(data_list[i][0]+space*' '+' :  '+str(data_list[i][1]))
    return
    
        
        
        
    
import sys
# Main starts from here
def main():
    
    RFH = get_filename_as_agrv_if_no_ask("Enter Contact List Data File Name : ")
    contact_list = get_contact_list(RFH) 
    ascending_list = make_list_ascending(contact_list)
    items = len(ascending_list)
    print("CONTACT LIST IN ASCENDING ORDER:-")
##    for i in range(0,items):
##        print(ascending_list[i][0],":",ascending_list[i][1])
    tabular_formatted_printing(ascending_list)


main()

"""S16Q02
Write a Python program that prompts the user for a file. 
This file contains names of people and their ages. 

Read the file, and print the list with the oldest person’s name listed first. 
A sample file [ AGES.TXT ] is shown above :

Test Data File: ages.txt


"""
# Helper functions


def make_list_descending(nlist):
    i = 0
    j = 0
    n = len(nlist)
    while i < n:
        j = 0
        while j < n-i-1:
            if nlist[j][1] < nlist[j+1][1]:
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

        data = line.split(sep="-")
        print(line)
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
    descending_list = make_list_descending(contact_list)
    items = len(descending_list)
    print("\nCONTACT LIST IN DESCENDING ORDER OF AGE:-")
    tabular_formatted_printing(descending_list)
    


main()

 

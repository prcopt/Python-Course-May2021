"""S18Q01
Shell Environment variables are shown below.

- Use “keys()” and “items()” methods to print the
names of all the environment variables

- Which environment variables has the longest name ?

- Print the names of all the environment variables in a sorted order

- Print the names and values of environment variables in the following format :

- NAME = value1
- MORE_NAME = longer_value2
- ANOTHER_NAME = val
- HOME = some_value_3

INPUT FILE NAME: SHELL_VARIABLES.TXT

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
        data = line.split(sep="=")
        var_dict[data[0]] = data[1]
    print("\n")
    return var_dict


import sys
# Main starts from here
def main():
    
    RFH = get_filename_as_agrv_if_no_ask("Enter Contact List Data File Name : ")
    var_dict = get_shell_env_var_data(RFH)
    var_keys = list(var_dict.keys())
    var_values = list(var_dict.items())
    n = len(var_keys)
    print("RESULTS:\n")
    longest=0
    #Finding longest name
    for i in range(0,n):
        if len(str(var_keys[i])) > longest:
            longest =len(str(var_keys[i]))
            index = i
    print("Longest Key:", var_keys[index])
    #printing environement in sorted order
    vkey = var_keys.copy()
    vkey.sort()
    print("\nEnvironment Variables in Sorted Order:-\n")
    for i in range(0,n):
        print(vkey[i])
    print(" \nNames & Values of environment variables:-\n")
    for i in range(0,n):
        print(var_keys[i],"=",var_values[i][1])

main()


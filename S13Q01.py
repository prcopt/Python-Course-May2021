"""S13Q01
Ask the user to enter a 3 digit number, till he enters 0. 
Discard all numbers that are not 3 digit numbers. 
From all the 3 digit numbers entered by the user, 
find and print the prime numbers in descending order.
"""


def get_number():
    """ This function prompts the user for a number
        It returns an integer [ and not a string ]
    """
    ns= input("Enter a number: ")
    return ns

def get_no_of_digits(n):
    digits = len(n)
    return digits

def Number_entry_and_give_list(prompt,exit_no,ndigit=0):
    """ Keyboard entry of numbers. Exit when exit_no is typed
        return list of numbers
        inputs: prompt is the prompt text to display: exit_no
        is the number when typed, will exit reading loop.
        ndigit is set to prescribed no of digits required in input; else set to 0(no limit) by default
    """
    n = 1
    nlist = list()
    while n != 0:
        n = int(input(prompt))
        if n != 0:
            if ndigit != 0:
                if get_no_of_digits(str(n)) == ndigit:
                    nlist.append(n)
                else:
                    print("Entry Error! No of digits should be :",ndigit)
    return nlist

def is_prime_number(no):
    """ check is parameter is a prime number.
         if yes, return True Else False
    """
    Prime = False
    if no <= 1:
        return Prime
    for i in range(2,no-1):
        if  no%i != 0:
            continue
        else:
            print(no," is Not a Prime Number")
            return Prime
            
    Prime = True
    print(no," is a prime number")

    return Prime
                    
def make_list_ascending(nlist):
    i = 0
    j = 0
    n = len(nlist)
    while i < n:
        j = 0
        while j < n-i-1:
            if nlist[j] > nlist[j+1]:
                nlist[j],nlist[j+1] = nlist[j+1],nlist[j]
                j += 1
            else:
                j += 1
        i += 1
    return nlist


def make_list_descending(nlist):
    i = 0
    j = 0
    n = len(nlist)
    while i < n:
        j = 0
        while j < n-i-1:
            if nlist[j] < nlist[j+1]:
                nlist[j],nlist[j+1] = nlist[j+1],nlist[j]
                j += 1
            else:
                j += 1
        i += 1
    return nlist               
                
""" input is a list of numbers; Output is the list of same numbers in ascending order
"""


import sys

# Main starts here
if __name__ == "__main__":
    prompt = """Enter a Number :\n[ '0' to exit ] >>"""
    plist = list()
    nlist = Number_entry_and_give_list( prompt,0,3) # type '0' to terminate entry, allow only 3 digit numbers
#    print("Entered list of 3 digit nos:",nlist)
    nlist = make_list_descending(nlist)
#    print(" List in descending order:", nlist)
    for i in range(0,len(nlist)):
        if is_prime_number(nlist[i]):
            plist.append(nlist[i])
    print(" List of Prime Numbers:",plist)
    


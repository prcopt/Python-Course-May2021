""" S13Q02
Create a text file “num.txt” that contains one number per line. 
These numbers can be 1, 2, 3 or 4 digit numbers.

- Write a program to read the numbers from this file
- Discard all numbers that are not 3 digit numbers.
- From all the 3 digit numbers in the file,
find and print the prime numbers in descending order.



"""
def get_no_of_digits(n):
    digits = len(n)
    return digits


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
                
def get_filename_as_agrv_and_get_contents_of_file(prompt):
    """ get filename as argument from user or if not given, take filename interactively.
       - get contents in the file.
       - close file and return text contents. 
    """
    if len(sys.argv)< 2:
        file = input( prompt)
    else:
        file = sys.argv[1]
    RFH = open(file)
    contents = RFH.read()
    RFH.close()
    return  contents,file



import sys

# Main starts here
if __name__ == "__main__":

    """  check if file is existing: if not ask again """
    File = False
    while not File:
        prompt = "Enter filename containing list of numbers:"
        try:
            contents,file = get_filename_as_agrv_and_get_contents_of_file(prompt)
            File = True
            break
        except FileNotFoundError:
            print("File Not Found")
        except:
            print("Unknown Error")
        
    cleaned_contents = contents.replace("\n"," ")
    striped_contents = cleaned_contents.strip()
    items = []
    items = striped_contents.split(' ')
    print("total raw numbers from file",len(items))
    print(items)
    nlist = []
    for i in range(0,len(items)):
        ndigit = get_no_of_digits(items[i])
        if ( ndigit == 3):
            nlist.append(int(items[i]))
    print("3 digit numbers :",len(nlist))
    print(nlist)
    nlist = make_list_descending(nlist)
    print (" List in descending order",nlist)
    plist = list()
    for i in range(0,len(nlist)):
        if is_prime_number(nlist[i]):
            plist.append(nlist[i])
    print(" List of Prime Numbers:",plist)

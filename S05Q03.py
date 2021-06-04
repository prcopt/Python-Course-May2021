""" S05Q03
Take a number as input from the user. 
Print all the squares of numbers from 1 to any large number. 
The numbers printed should be less than 
the number given as input by the user

"""

def get_number():
    """ 
        This function should fetch a number from user
        Input : None
        Return : Entered integer
    """
    number = input("Enter the Number:")
    number = int(number) 
    return number


def print_square(num,limit):
    """ 
        This function prints squares of a numbers from 1
        as long as square is less than number given.
        Input : an integer
        Return : None
    """
    i = num
    while i**2 < limit:
        print(i**2)
        i += 1
   

def main():
    '''
        Main program
    '''
    inp = get_number()
    for i in range(1,inp):
        print_square(i,inp)

# Main starts from here
main()

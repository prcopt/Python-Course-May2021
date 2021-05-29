""" S01AQ03
This program is to print the multiplication table 
of any number desired by the user

"""

def get_number():
    """ 
        This function should fetch a number from user
        Input : None
        Return : an integer
    """
    number = input("Enter the Number to print table:")
    number = int(number) 
    return number


def print_mtable(num):
    """ 
        This function prints the multiplication table of num
        Input : an integer
        Output : Display multiplication table of input integer
        Return : None
    """

    for i in range(1,11):
        print(i,"x",num,"=",i*num)  
    return

def main():
    '''
        Main program
    '''
    inp = get_number()
    print_mtable(inp)

# Main starts from here
main()

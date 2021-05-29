""" S03Q01
Take 2 numbers from the user. 
Print which number is a 2 digit number, 
and which number is a 3 digit number. 
If it is neither, then print the number as it is

"""

# Implement the helper functions here
def check_if_2digit(number):
    twodigit = False
    if number > 9 and number <100 :
        twodigit = True
        return twodigit

def check_if_3digit(number):
    threedigit = False
    if number > 99 and number < 1000 :
        threedigit = True
        return threedigit
    
        
    

def perform_check(number):
    """ This function uses helper functions
        check_if_2digit
        check_if_3digit
        to perform the required operations
    """

    if check_if_2digit(number):
        print( "Entered Number:",number,"is a 2 digit Number")
    else:
        if check_if_3digit(number):
            print("Entered Number:",number,"is a 3 digit Number")
        else:
            print("Entered Number is:",number)
                  
    
        

def get_number():
    """ This function prompts the user for a number
        It returns an integer [ and not a string ]
    """
    n= int(input("Enter Number: "))
    return n
    
# Main starts from here
num1 = get_number()
num2 = get_number()
perform_check(num1)
perform_check(num2)

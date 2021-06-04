""" S08Q01
Ask the user to enter a number. 
Find the number of digits in that number

"""

# Implement the helper functions here

def get_number():
    """ This function prompts the user for a number
        It returns an integer [ and not a string ]
    """
    ns= input("Enter a number: ")
    return ns

def get_no_of_digits(n):
    digits = len(n)
    return digits
    

    
# Main starts from here
number_s = get_number()
print("No of digits in number:",number_s,"is ",len(number_s))

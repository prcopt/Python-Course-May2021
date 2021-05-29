""" S03Q02
- Ask the user to enter a number.
- If the number is a single digit number,
add 7 to it, and print the number in its unit’s place
- If the number is a two digit number,
raise the number to the power of 5, 
and print the number in its unit’s place
- If the number is a three digit number, 
ask the user to enter another number. 
Add the 2 numbers and print the number in its unit’s place
"""

# Implement the helper functions here
def do_1digit_oper(number):
    if number >= 0 and number <10 :
        number += 7
        if number < 10:
            print("digit at unit's place:",number)
        else:
            print("digit at unit's place:",number%10)
    return
    
def do_2digit_oper(number):
    if number > 9 and number <100 :
        number **= 5
        s = str(number)
        i = len(s)
        print("digit at unit's place:",s[i-1]) 
    return
    
def do_3digit_oper(number1):
    if number1 > 99 and number1 <1000 :
        number2 = int(input("Enter another number please:"))
        number1 += number2             
        s = str(number1)
        i = len(s)
        print("digit at unit's place:",s[i-1]) 
    return        
    
       

def get_number():
    """ This function prompts the user for a number
        It returns an integer [ and not a string ]
    """
    n= int(input("Enter Number: "))
    return n
    
# Main starts from here

num1 = get_number()
do_1digit_oper(num1)
do_2digit_oper(num1)
do_3digit_oper(num1)

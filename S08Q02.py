"""S08Q02
Ask the user to enter a number.
- If the number is a single digit number, add 7 to it, 
and print the number in its unit’s place
- If the number is a two digit number, raise the number to the power of 5, 
and print the last 2 digits
- If the number is a three digit number, ask user to enter another number. 
Add the 2 numbers and print the last 3 digits


"""

# Implement the helper functions here

def get_number_string():
    """ This function prompts the user for a number
        It returns an integer [ and not a string ]
    """
    ns= input("Enter a number: ")
    return ns

def get_no_of_digits(n):
    digits = len(n)
    return digits
    

    
# Main starts from here

number_s = get_number_string()
ln = len(number_s)
num = int(number_s)
if ln == 1:
    print("insert logic for single digit case")
    num += 7
    number_s = str(num)
    print("digit at unit's place is :",number_s[-1])
elif ln == 2:
    print("insert logic for 2 digit case")
    num **= 5
    number_s = str(num)
    print("Last two digits of ",number_s,"is:",number_s[-2:])
elif ln ==3:
    print("insert logic for 3 digit case")
    num2 = int(get_number_string())
    num +=num2
    number_s = str(num)
    print("Last 3 digits of sum is:",number_s[-3:])
else:
    print(" No is not a case for logic. don't do anything:")

            

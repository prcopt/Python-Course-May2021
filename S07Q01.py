""" S07Q01
Get the user’s first name and last name. 
Assume the user provides “Dharmender” and “Singh” as inputs, 
then print the user’s name in the following order and format

- Name : dharmender, Surname : singh 
- DHARMENDER SINGH
--------------------- ---------
- Singh, Dharmender

"""

# Implement the helper functions here

def get_name():
    """ This function prompts the user for First and Last names
    """
    first_N = input("Enter First Name: ")
    last_N  = input("Enter Last Name:")
    return first_N,last_N

    
# Main starts from here
first_name,last_name = get_name()
print("Name : "+ first_name.lower() + ", Surname : " + last_name.lower())
print( first_name.capitalize() + " " + last_name.capitalize())
print("-"*20+" "+"-"*10)
print( first_name.capitalize() + " " + last_name.capitalize())





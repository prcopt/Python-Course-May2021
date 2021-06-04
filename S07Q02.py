""" S07Q02
Get the user’s first name and last name. 
Assume the user provides “Dharmender” and “Singh” as inputs, 
Find his best possible initials by eliminating the last character 
from each of the name as shown in this sample output

- Step 1 : Dharmender Singh
- Step 2 : Dharmende Sing
- Step 3 : Dharmend Sin
- Step 4 : Dharmen Si
- Step 5 : Dharme S

Expected output :
Best possible initials of "Dharmender Singh" is :
Dharme S

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
lenL = len(last_name)
lenF = len(first_name)
i = 0
while i < lenL :
    fn = first_name[0:lenF-i]
    ln = last_name[0:lenL-i]
    print('- Step',i+1,':',fn,ln)
    i += 1
print('Best possibile initials of "'+first_name+' '+last_name+'" is :')
print(fn,ln)


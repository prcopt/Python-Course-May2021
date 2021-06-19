""" S14Q03
Ask the user to enter any 10 numbers as input. 
Randomly pick any 5 numbers from this list 
but print them in the same order as given by the user


"""

# Implement the helper functions here

def get_numbers(m):
    """ This function prompts the user for a number
        It returns an integer [ and not a string ]
    """
    i = 1
    number_list = list()
    while i <= m:
        prompt = "Enter Number #"+str(i)+">"
        try:
            n = int(input(prompt))
            number_list.append(n)
        except ValueError:
            print("%% Input error!!")
            continue
        except:
            print ("%% Unknown error!!")
        i += 1
    print("Keyed-in numbers: ",number_list)
    return number_list

import random    
# Main starts from here

random_list = list() # To hold random set of numbers
user_list = get_numbers(10) # user input of numbers
random_list = random.sample(user_list,5)
print(random_list)
for i in user_list:
    try:
        ind = random_list.index(i)
    except ValueError:
        continue
    print("Number:",i)
    

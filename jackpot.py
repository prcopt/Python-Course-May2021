"""S0BQ03 - PART II NAME: jackpot.py
Write a Python program “sumops.py” that contains a function called “dsum”. 
This function takes a number as argument. 
It returns the sum of its digits. 
Write a test program that will test this function.

- Write another Python program “jackpot.py”. 
It should ask the user to enter a 5 digit number,
but only if the user has not provided it as an argument to jackpot.py
- This program should use the dsum function by importing it 
from sumops.py to calculate the sum of all the digits of 
the 5 digit number provided by the user.
- Now, generate a random number from 1 to 50.
- If the sum of the digits matches this random number, 
the user wins the jackpot.
- If not, then print the random number.

This program makes use of sumops.py
"""

# Implement the helper functions here

import sumops
import random
import sys
print(sys.argv, len(sys.argv))

if len(sys.argv) == 1 : # if the user has not given the number
    arg_data = input("Enter a 5 digit number:")
else: # if user has given the number
    arg_data = sys.argv[1]
sum = sumops.dsum(arg_data)    
found = False
counter = 1
while not found:
    rand_no = random.randint(1,50)
    print("USER #",counter,"Random no generated: ",rand_no)
    if rand_no == sum:
        print("User#",counter," WON JACKPOT!! 5Digit No: ",arg_data,"Sum of Digits:",sum)
        found = True
    else:
        print ("Random Number generated: ",rand_no)
    counter += 1
    

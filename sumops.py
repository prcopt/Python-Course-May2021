"""S0BQ03 - PART 1 NAME: sumops.py
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

"""

# Implement the helper functions here



def dsum(n):
    digits = len(n)
    sum = 0
    str_n = str(n)
    for i in range(0,digits):
        sum += int(str_n[i])
    return sum
    

    
# Testing program  starts from here
if __name__ == "__main__":
    sum = 1
    while sum != 0:
        n = input("Enter Number:")
        sum = dsum(n)
        print("Sum of Digits:",sum)

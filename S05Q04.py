""" S05Q04
Check if a given number is a fibonacci number. 
If not, then print the closest fibonacci number to the given number
"""

def get_number():
    """ 
        This function should fetch a number from user
        Input : None
        Return : Entered integer
    """
    number = input("Enter the Number:")
    number = int(number) 
    return number


def find_fibonacci(num1):
    """ 
        This function find if the number is fibonacci and return it. if not fibonacci return nearest fibonacci number
    """
    fib_seq = [0,1]
    i = 2
    while fib_seq[i-2]+fib_seq[i-1] <= num1:
        next_fib = fib_seq[i-1]+fib_seq[i-2]
        fib_seq.append(next_fib)
        if next_fib == num1:
            print("Fibonacci list",fib_seq)
            return next_fib
        i += 1
    high_fib = fib_seq[i-2]+fib_seq[i-1]
    print("higher fib, lower fib, num1",high_fib,next_fib,num1)
    if high_fib-num1 < num1-next_fib:
        next_fib = high_fib
        fib_seq.append(high_fib)
    
    print("Fibonacci list",fib_seq)
    return next_fib
     
   

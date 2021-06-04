"""S05Q02
- Ask the user to enter a number till he enters 0. 
Print the maximum and minimum values among all entered numbers. 
Print the number of single, two and three digit numbers entered.

"""
# Helper functions
def digit_count(number_list):
# Counts the number of 1,2,3 digit nos through counters
    one_digit_count   = 0
    two_digit_count   = 0
    three_digit_count = 0
    for number in number_list:
        if number <= 9 :
            one_digit_count += 1
        elif number <= 99:
            two_digit_count += 1
        elif number <= 999:
            three_digit_count += 1
        else:
            continue
    return one_digit_count,two_digit_count,three_digit_count
            


def get_numbers():
#Getting a set of numbers from user as input and make a list of numbers
    n = 1
    nlist = []
    while n != 0:  
        n = int(input("Key-in any positive Number\n[Enter 0 to terminate entry\nEnter: "))
        if n != 0:
            nlist.append(n)
    return nlist

def min_max(nos):
#Finding min & max numbers in the list
    min= 10**20
    max = 0
    for i in nos:
        if i > max:
            max = i
        if i <= min:
            min = i
    return min,max
  
# Main starts from here
def main():
    list_of_numbers = get_numbers()
    print("Entered List:" ,list_of_numbers)
##    nos = len(list_of_numbers)
##    print("length of list:",nos)
    min,max = min_max(list_of_numbers)
    print("Min:",min,"Max:",max)
    one_dig,two_dig,three_dig = digit_count(list_of_numbers)
    print("One Digit number count :",one_dig,"\nTwo Digit number count :",two_dig,"\nThree Digit number count :",three_dig)

main()

 
    
    

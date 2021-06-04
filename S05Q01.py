""" S05Q01
Print the multiplication table of a given number using “for” and “while” loops.

"""
def mult_table_for(integer):
    print("Multiplication Table of",integer,"using for loop:")
    for i in range(1,11):
        print(i,"x",integer,"=",i*integer)

def mult_table_while(integer):
    print("Multiplication Table of",integer,"using while loop:")
    i = 1
    while i <= 10:
        print(i,"x",integer,"=",i*integer)
        i += 1

    

def main():
    num = int(input("Enter a number:"))
    mult_table_for(num)
    mult_table_while(num)

main()

"""S08Q03
Ask the user to enter a number.
- If the user enters a number as 5, then
generate the following string :
- 00001111222233334444

- If the user enters the number as 3, then
generate the following string :
- 001122


"""
# Helper functions
#Getting a  number  from user as input
def get_number():
    n = int(input("Key-in a sentence: "))
    return n
  
# Main starts from here
def main():
    no = get_number()
    sno = str(no)
    string_list = []
    final_string = ""
    for i in range(0,no):
        sno = str(i)
        string_list.append(sno*(no-1))
    s = len(string_list)
    final_string = ''.join(string_list)
    print("final_string",final_string,">>")

main()

 

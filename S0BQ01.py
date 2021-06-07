""" S0BQ01
Write a Python function, that asks the user if he wants to continue. 
It should print “continue” and return True, if the user types in a yes,
irrespective of the case in which “yes” is typed. 

Import this function in any of your earlier exercises and 
run that exercise in a loop as long as the user enters “No”

"""

def get_YesNo():
    ans = "NO"
    wish = False
    while ans != "YES":
        YesNo =  input("Do you want to Continue?")
        ans =YesNo.upper()
        if ans == "YES":
            print("Continue")
            wish = True
        else:
            break
    return wish

# test main starts here
if __name__ == "__main__":
    wish = True
    while wish:
        wish = get_YesNo()
        print("Wish = ",wish)

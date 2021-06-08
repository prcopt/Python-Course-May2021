""" S0BQ02
Create a log table of base 10 for all numbers from 1 to 10. 
Then create a log table to base 10 for all numbers from 1 to 100 
that are multiples of 10. 
Make sure the log values are printed unto 4 decimal places. 

Display the log tables as shown below. 
What similarities and differences do you see in the 2 tables ?

"""
import math
def create_logtable(nos):
    logs = []
    print(nos)
    for i in nos:
        n = math.log(i,10)
        logs.append(n)
    return logs
       

# main starts here
if __name__ == "__main__":
    nos =[]
    nos_10 = []
    for i in range(1,11):
        nos.append(i)
    logs = create_logtable(nos)
    for i in range(1,101):
        if i%10 == 0:
            nos_10.append(i)
    log10s = create_logtable(nos_10)
    if len(nos) > len(nos_10):
        type1 = True
    elif len(nos) < len(nos_10):
        type2 = True
    else:
        type  = True

    if type:
        n = len(nos)
        for i in range(0,n):
            print(nos[i],"---",round(logs[i],4),"    ",nos_10[i],"---",round(log10s[i],4))
    else:
        print(" For this problem, the length of Table should have been same!")
#   add logic here in case the table sizes are different, based to type1 & type2 above.
        
            
        

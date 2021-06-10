""" S0CQ02
Read the contents of a file and randomly print any one line from that file.
The user passes the name of the file as a command line argument. 
Re-use the functions from fileops.py for this program

"""

from fileops import *
import random

# Main starts here
# Get filename from command line
file = sys.argv[1]
FH, lines = get_lines(file) 
FH.close()

no_of_lines = len(lines)
print(lines)
i = random.randint(0,no_of_lines-1)
print("Random Line:",lines[i])

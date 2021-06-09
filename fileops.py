""" S0CQ01 - Nameed fileops.py
Two Python scripts “fileops.py” and “shuffle_lines.py” are present at

1> https://github.com/asarfraaz/PyPractice/blob/master/Mod5_Files/fileops.py
2> https://github.com/asarfraaz/PyPractice/blob/master/Mod5_Files/shuffle_lines.py

Implement the missing parts
"""
import random
# part 1>

def get_lines(filename):
    
    """ Reads the contents of filename
        and returns the - File handle
        - List of all lines of the file
    """
    RH = open(filename,'r')
    contents = RH.read()
    lines = contents.split("\n")
 #   RH.close()
    print(lines)
    return RH,lines  


def write_lines(filename, lines):
    """ Writes the lines into the a file whose
        filename is given as argument
    """
    WH = open(filename,'w')
    for line in lines:
        print(line)
        WH.write(line+"\n")
    WH.close()
        
    ## Your implementation goes here ###

import sys 

# Main starts here
if __name__ == "__main__":
# Get filename from command line
    file = sys.argv[1]
    FH, lines = get_lines(file) 
    FH.close()
    print(lines)



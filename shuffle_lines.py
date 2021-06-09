""" S0CQ01
Two Python scripts “fileops.py” and “shuffle_lines.py” are present at

1> https://github.com/asarfraaz/PyPractice/blob/master/Mod5_Files/fileops.py
2> https://github.com/asarfraaz/PyPractice/blob/master/Mod5_Files/shuffle_lines.py

Implement the missing parts
"""
# PART - 2> shuffle_lines.py
""" Takes a filename as argument 
    Creates a new file with the name
    "shuffle" appended to the original filename.
    The lines in the input are shuffled 
    and written into the new file
"""

from fileops import *
import random
def shuffler(lines):
    """ Shuffle a list of strings
    Input : list of strings
    Return : a new list with original strings shuffled
    """
    print("List of strings:",lines)
    random.shuffle(lines)
    print("Shuffled list of strings",lines)
    return lines
# Main starts here
# Get filename from command line
file = sys.argv[1]
FH, lines = get_lines(file) 
FH.close()

shuffled_lines = shuffler(lines)

new_name = file + "shuffle" 
write_lines(new_name, shuffled_lines)

"""S0CQ03
insert_in_file.py is a Python script that is used to insert a given line
at any place in an existing file.

The file can be found at : https://github.com/asarfraaz/PyPractice/blob/master/Mod5_Files/insert_in_file.py

Implement the missing parts


"""

#!/usr/bin/python

"""
    This program insert's some text in any given line of a file.
    Input : 
            Filename is taken as argument to the program
            The user is prompted for the line where the text 
             is to be inserted
    Output :
            The same file is updated with some new text
"""

import sys

def insert_text(WFH, all_lines, new_text, line_num):
    """
         Insert the text at a given line of a file
        Input :
                WFH : The file handle for the file opened in write mode
                all_lines : List of all lines in existing file
                new_text : A string of new text to be inserted in the file
                line_num : The line number where the file should be inserted
        Output :
                None
    """
    all_lines.insert(line_number-1,new_text)
    for i in range(0,len(all_lines)):
        if i < len(all_lines)-1:
            WFH.write(all_lines[i]+"\n")
        else:
            WFH.write(all_lines[i])
    return 

def get_linenumber(num):
    """
        Prompt the user for the line number where he wants to insert the text
        Input :
                The max number of lines in the existing file
        Output :
                A number that is less than the max number of lines in file
    """
    ans = num + 10 # Initialise ans to a number larger than number of lines
    while ans >= num:
        prompt = "Please enter the line number where you want to insert the text[max: " + str(num) + " ]"
        ans = raw_input (prompt)
        ans = int(ans)

    return ans
def raw_input(prompt):
    ans = input(prompt)
    return ans

def print_file(FH):
    """
        Print the contents of the file on the output screen
        Input : 
                file handle
        Return : 
                The number of lines in the file
                The list of all the lines in the existing file
    """
    all_text = FH.read()
    all_lines = all_text.split('\n')
    for line in all_lines:
        print (line)
    return len(all_lines), all_lines

# Main : This is where the program starts
# First check if the mandatory argument is given to the program
if len(sys.argv) < 2:
    print ("No filename provided as argument to program")
    print ("Usage :", sys.argv[0], "<filename>")
    quit()

fname = sys.argv[1]
text = "This line is added by my program"

FH = open(fname)

print ("Printing the contents of file", fname)
(num_of_lines, lines) = print_file(FH)
FH.close()

line_number = get_linenumber(num_of_lines)
WFH = open(fname, 'w') ## ALERT !!! This will over write the existing file
insert_text(WFH, lines, text, line_number)
WFH.close()
print(" File has been inserted with the new text '"+text+"' as line:",line_number)


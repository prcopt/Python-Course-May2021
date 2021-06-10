""" S10Q01
Get the name of the text file from the user. 
Check if all the sentences in that text file begin with a capital letter.

"""

def get_contents(filename):
    
    """ Reads the contents of filename
        and returns the - File handle
        - List of all lines of the file
    """
    RH = open(filename,'r')
    contents = RH.read()
    lines = contents.split(".")
    return RH,lines

import sys

# Main starts here
if __name__ == "__main__":
# Get filename from command line
    file = sys.argv[1]
    FH, sentences = get_contents(file) 
    FH.close()
    caps = True
    non_caps_count = 0
    for i in range(0,len(sentences)-1):
        print(sentences[i]+'\n')
        sentences[i] = sentences[i].strip()
        c = sentences[i]
        if c[0] < "A" or c[0] > "Z":
            caps = False
            non_caps_count += 1
    print ("All sentences do not start with CAPs (",non_caps_count,")") 
    print(sentences)
        

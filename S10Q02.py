""" S10Q02
Write a Python script that takes a file name as its argument. 
In that file, find the line that has the maximum number of 
occurrences of the letter ‘e’
"""

def get_filename_as_agrv_and_get_contents_of_file():
    """ get filename as argument from user or if not given, take filename interactively.
       - get contents in the file.
       - close file and return text contents. 
    """
    if len(sys.argv)< 2:
        file = input( "Enter Data Filename wwith text contents:")
    else:
        file = sys.argv[1]
    RFH = open(file)
    contents = RFH.read()
    RFH.close()
    return  contents


def get_segement_list(contents,delim):
    """ get segments from the content received in parameter based on delimeter.
       - return a list of segments along with the count of segments
       (Segments are lines(\n) or sentencese (".") or words (" ")
    """
    segments = contents.split(delim)
    segment_count = len(segments)
    return segments,segment_count

def get_char_count(string,char):
    count = string.count(char)
    return count


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
    contents = get_filename_as_agrv_and_get_contents_of_file()
    lines, line_count = get_segement_list(contents,"\n")
    e_max_line = ""
    e_max_count = 0
    for aline in lines:
        e_count = get_char_count(aline,"e")
        if e_count > e_max_count:
            e_max_line = aline
            e_max_count = e_count
    print("The line: '"+e_max_line,"' has ",e_max_count," of 'e' characters")
    
        

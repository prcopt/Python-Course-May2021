""" S10Q03
Write a Python script that takes a file name as its argument. 
Write the contents of this file to another file such that, 
each sentence is stored on a new line.

"""

def get_filename_as_agrv_and_get_contents_of_file():
    """ get filename as argument from user or if not given, take filename interactively.
       - get contents in the file.
       - close file and return text contents. 
    """
    if len(sys.argv)< 2:
        file = input( "Enter Data Filename with text contents:")
    else:
        file = sys.argv[1]
    RFH = open(file)
    contents = RFH.read()
    RFH.close()
    return  contents,file


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
    contents,file = get_filename_as_agrv_and_get_contents_of_file()
    print("INPUT file Contents:-")
    print(contents)
    strped_contents = contents.strip() # remove leading and training whitespaces
    fin_contents = strped_contents.replace("\n","") # remove any blank lines
    sentce, sentce_count = get_segement_list(fin_contents,".")
    n = file.find(".")
    fname = file[0:n]
    l=len(file)
    ext=file[n:]
    nfname=fname+'new'+ext
    WFH = open(nfname,'w')
    print("OUTPUT file contents:-")
    for s in range(0,sentce_count-1):
        WFH.write(sentce[s]+'.\n')
        print(sentce[s]+'.\n')
    WFH.close()
     

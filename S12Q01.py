"""S12Q01
Write a search and replace program in Python. 
This should prompt the user for which word to search,
and what new word it should be replaced with. 

The file to be modified should be taken as argument to this program


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

import sys

# Main starts here
if __name__ == "__main__":
    contents,file = get_filename_as_agrv_and_get_contents_of_file()
    print("INPUT file Contents:-")
    print(contents)
    # Relpace txt
    search_word = input(" Input the text to search for:")
    new_word = input("Input the new word to replace with:")
    new_contents = contents.replace(search_word,new_word)
    # new file name creation
    n = file.find(".")
    l = len(file)
    ext = file[n:]
    wf_name = file[:n]+"-new"+ext
    print ("\nWriting as below in new file:-")
    print(new_contents)
    wfh = open(wf_name,'w')
    wfh.write(new_contents)
    print("File : ",wf_name,"created/updated!")
    wfh.close()

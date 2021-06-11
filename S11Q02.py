"""S11Q02
Write a Python program that takes a file as the first argument 
and a search word as the second argument. 

This script should print only those lines that have the search word
"""

def get_filename_as_agrv_and_get_all_lines_of_file():
    """ get filename as argument from user or if not given, take filename interactively.
       - get contents in the file.
       - close file and return text contents. 
    """
    contents = []
    if len(sys.argv)< 2:
        file = input( "Enter Data Filename with text contents:")
    else:
        file = sys.argv[1]
    
    RFH = open(file)
    while True:
        line = RFH.readline()
        if line == "":
            break
        else:
            contents.append(line)
    RFH.close()
    print("no of lines:",len(contents))
    return  contents,file



import sys

# Main starts here
if __name__ == "__main__":
    contents,file = get_filename_as_agrv_and_get_all_lines_of_file()
    print("INPUT file Contents:-")
    for i in range(0,len(contents)):
        print(contents[i],end="")
    if len(sys.argv)< 3:
        search_str = input("Enter Search String:")
    else:
        search_str = sys.argv[2]
    print("\nSearch String supplied:",search_str)
    for i in range(0,len(contents)):
        if contents[i].find(search_str) >= 0 :
            print(contents[i])
               

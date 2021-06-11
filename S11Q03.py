"""S11Q03
Write a Python script that takes a file name as its first argument. 
Create a copy of the contents of this file satisfying the following conditions :

- If the file name is “file.txt”,
then the name of the new file should be “file-new.txt”
- Every even line of the first file, should be
repeated in the new file.
- The first line of the first line, should be
repeated after the last line of the first file.
- A sample input and output file is shown below

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
    return  contents,file



import sys

# Main starts here
if __name__ == "__main__":
    contents,file = get_filename_as_agrv_and_get_all_lines_of_file()
    print("INPUT file Contents:-")
    for i in range(0,len(contents)):
        print(contents[i],end="")
    print()
    # new file name creation
    n = file.find(".")
    l = len(file)
    ext = file[n:]
    wf_name = file[:n]+"-new"+ext
    print ("\nWriting as below in new file:-")
    wfh = open(wf_name,'w')
    for i in range(0,len(contents)):
        s = contents[i]
        ln = len(contents[i])
        print(s[:ln-1])
        wfh.write(s[:ln-1]+"\n")
        if (i+1)%2 == 0:
            print(s[:ln-1])
            wfh.write(s[:ln-1]+"\n")
    print(contents[0])
    wfh.write(contents[0])
    print("File : ",wf_name,"created/updated!")
    wfh.close()
            

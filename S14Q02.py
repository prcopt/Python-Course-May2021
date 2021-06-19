"""S14Q02
Create a text file called “students.txt”. 
Each line should be of the form
“student_name : student_marks”

- Write a Python program to read the contents from this file.
- Print the names and marks of all students 
who have scored more than 90% marks, 
in ascending order of their marks.

"""
# Helper functions

def get_student_data():
#Getting a set of numbers from user as input and make a list of numbers
    strg = "start"
    nlist = []
    while strg != "":  
        strg = input("Key-in student name and total SSLC Exam marks:\n[Enter <Return> to terminate entry\nEnter >> ")
        if strg != "":
            data = strg.split()
            data[1] = int(data[1])
            nlist.append(data)
    return nlist

def make_list_ascending(nlist):
    i = 0
    j = 0
    n = len(nlist)
    while i < n:
        j = 0
        while j < n-i-1:
            if nlist[j][1] > nlist[j+1][1]:
                nlist[j][1],nlist[j+1][1] = nlist[j+1][1],nlist[j][1]
                nlist[j][0],nlist[j+1][0] = nlist[j+1][0],nlist[j][0]
                j += 1
            else:
                j += 1
        i += 1
    return nlist
def get_filename_as_agrv_and_get_contents_of_file(prompt):
    """ get filename as argument from user or if not given, take filename interactively.
       - get contents in the file.
       - close file and return text contents. 
    """
    if len(sys.argv)< 2:
        file = input( prompt)
    else:
        file = sys.argv[1]
    RFH = open(file)
    contents = RFH.read()
    RFH.close()
    c1 = contents.replace(":"," ")
    return  c1
import sys
# Main starts from here
def main():
    tot_marks = 1000
    percent_cutoff = 90/100
    contents = get_filename_as_agrv_and_get_contents_of_file("Enter Student marks Data File Name")
    split_list = contents.split()
    print(split_list)
    student_data = []
    for i in range(0,len(split_list),2):
        record = [split_list[i],int(split_list[i+1])]
        student_data.append(record)
    score_list = make_list_ascending(student_data)
    print(" Students who scored more than 90%")
    j = 1
    for i in range(0,len(score_list)):
        percent_scored = score_list[i][1]/tot_marks
        if percent_scored > percent_cutoff:
            print(j,".", score_list[i][0]," -- ",score_list[i][1])
            j += 1
    
    


main()

 

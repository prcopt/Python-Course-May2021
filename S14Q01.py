"""S14Q01
Ask user to enter the student’s name followed by his total marks in the SSLC exam. 
An empty line indicates the end of input. 
Print the names and marks of all students 
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
    print(nlist)
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

# Main starts from here
def main():
    tot_marks = 1000
    percent_cutoff = 90/100
    student_data = get_student_data()
    print("Entered List:" ,student_data)
    score_list = make_list_ascending(student_data)
    print(" Students who scored more than 90%")
    j = 1
    for i in range(0,len(score_list)):
        percent_scored = score_list[i][1]/tot_marks
        if percent_scored > percent_cutoff:
            print(j,".", score_list[i][0]," -- ",score_list[i][1])
            j += 1
    
    


main()

 

 
    

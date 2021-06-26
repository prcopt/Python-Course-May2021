"""S19Q02 - Bonus Question
Solve this question, only if you are feeling challenged enough to attempt it.

The data for 4 students of Sunflower School class X is shown below :

- Write a program that ranks the students
based on the total of their marks in all
the subjects for each unit test.

- Then, rank the students based on their
total marks for all the tests using the below formula
- Total marks = 25% Unit test + 75% Final

- Among unit tests, which student has
scored the highest marks for each subject ? 
- Also mention the highest score for each subject

- Which is the subject where each student has scored his/her highest marks ?


- There was a printing mistake in Maths paper of the final exam. 
All the students who attempted that question are given 3 bonus marks. 
Sneha and Ashish have attempted that question. 
What are the new ranks now ?

DATA FILES: ashish.txt, sneha.txt., vishal.txt,pinto.txt

also used another file 'filenames.dat' that contain all above file names.
"""
# Helper functions



def get_filename_as_agrv_if_no_ask(prompt):
    """ get filename as argument from user or if not given, take filename interactively.
         Return file handle
    """
    Found = False
    ln = len(sys.argv)
    while not Found:
        if ln < 2:
            file = input( prompt)
        else:
            file = sys.argv[1]
        try:
            RFH = open(file)
            Found = True
        except FileNotFoundError:
            print("%%Error! File not found!")
            ln = 1
#            break
    return  RFH

def get_nomination_list(RFH):
    line = "xx"
    nomination_list = list()
#    print("FILE CONTENTS:-")
    while line != "":
        line = RFH.readline()
        line = line.strip()
        if line == "":
            break
#        print(line)
        data = line.split(sep=" - ")
        nomination_list.append(data)
    return nomination_list

def tabular_formatted_printing(data_list):
    """ prints a list consisting of each element is a list of 2 itmes as (str,int) in a neat format
    [example list = [ ("abc",1),("efghij",20),......etc ]
    """
    n = len(data_list)
    max = 0
    for i in range(0,n):
        if int(len(data_list[i][0])) > max:
            max = len(data_list[i][0])
    for i in range(0,n):
        if int(len(data_list[i][0])) < max:
            space = max - len(data_list[i][0])
        else:
            space = 0
        print(data_list[i][0]+space*' '+' :  '+str(data_list[i][1]))
    return
def read_file_names():
    RFH = open("filenames.dat","r")
    line = "xx"
    file_list = list()
    while line != "":
        line = RFH.readline()
        line = line.rstrip()
        if line != "":
            file_list.append(line)
    RFH.close()
    return file_list
def get_student_data(fname):
    RFH = open(fname,"r")
    rec = 'xx'
    student_data = dict()
    while rec != "":
        string = RFH.readline()
        if string == "":
            break;
        if string != "":
            subject = string[:string.find(':')].strip()
#            print(subject)
            string = string.strip()
            marks = string[string.find(':')+1:].split(',')
            for i in range(0,len(marks)):
                marks[i] = int(marks[i])
#            print(marks)
            student_data[subject] = marks
#    print(student_data)
                
    return student_data                            
def print_ranks(title,name,score):
    i = 0
    j = 0
    n = len(score)
    while i < n:
        j = 0
        while j < n-i-1:
            if score[j] < score[j+1]:
                score[j],score[j+1] = score[j+1] ,score[j]
                name[j], name[j+1] = name[j+1],name[j]
                j += 1
            else:
                j += 1
        i += 1
    print(title)
    for i in range(0,len(name)):
        print(str(i+1)+'.',name[i],'-',score[i])
    return 
import sys
# Main starts from here
def main():
    student_file = read_file_names()
    student_names = list()
    student_marks_records = dict()
    for i in range(0,len(student_file)):
        name = student_file[i][:student_file[i].rfind(".")]
        student_names.append(name)
        student_data = get_student_data(student_file[i])
        student_marks_records[name]=student_data
 # all data captured in dictionary above
    unit_test_total = list()
    final_test_total = list()
    total_marks = list()
    max_marks = list()
    for each in student_names:
        
         st_marks_data = student_marks_records[each]
         subj = st_marks_data.keys()
         sum_of_unit_test = 0
         sum_of_final_test = 0

         for s in subj:
             marks = st_marks_data[s]
             max= 0
             for i in range(0,len(marks)-1):
                 sum_of_unit_test += marks[i]
                 if marks[i] > max:
                     max = marks[i]
             max_marks.append([each,s,max])
             sum_of_final_test += marks[len(marks)-1]

          
         unit_test_total.append(sum_of_unit_test)
         final_test_total.append(sum_of_final_test)
         total_marks.append(.25*sum_of_unit_test+0.75*sum_of_final_test)

    title = "Rank Based on Unit test Scores"
    copy_of_list = student_names.copy()
    copy_of_unit_test_total = unit_test_total.copy()
    print_ranks(title,copy_of_list,copy_of_unit_test_total)
    title = "Rank Based on Total Marks"
    copy_of_list = student_names.copy()
    copy_of_total_marks = total_marks.copy()
    print_ranks(title,copy_of_list,copy_of_total_marks)

    print("\nunit Tests: Subject-wise max score & student\n")    
    for s in subj:
        max_score_marks = 0
        max_score_student =""
        max_score_subj = s
        for i in range(0,len(max_marks)):
            if max_marks[i][1] == s:
                if max_marks[i][2] > max_score_marks:
                    max_score_marks = max_marks[i][2]
                    max_score_student = max_marks[i][0]
        print(max_score_subj,"- Highest marks",max_score_marks,"scored by ",max_score_student)       
# finding max marks & subject of each student            
    print("\nSubject where each student scored his/her highest Marks\n")

    for each in student_names:
        max_score_marks = 0
        max_score_subj = ""
        max_score_student = each
        for i in range(0,len(max_marks)):
            if max_marks[i][0] == each:
                if max_marks[i][2] > max_score_marks:
                    max_score_marks = max_marks[i][2]
                    max_score_subj=max_marks[i][1]

        sub_list = []
        for j in range(0,len(max_marks)):
            if max_marks[j][0] == each :
                if max_score_marks == max_marks[j][2]:
                    sub_list.append(max_marks[j][1])
        print( "Student: ",each,":")
        for k in range(0,len(sub_list)):
            print( '    * scored',max_score_marks,'in',sub_list[k])
    for i in range(0,len(student_names)):
        if student_names[i] == "sneha" or student_names[i] == "ashish":
                final_test_total[i] += 3
                

    total_marks_new = list()
    for i in range(0,len(student_names)):
        total_marks_new.append((.25*unit_test_total[i])+(0.75*final_test_total[i]))
    title = "Rank based on Total Marks (revised with Grace marks)"
    copy_of_list = student_names.copy()
    copy_of_total_marks = total_marks_new.copy()
    print_ranks(title,copy_of_list,copy_of_total_marks)
         
main()

 
    


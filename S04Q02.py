""" S04Q02
 Computation of Student Grade
 input:  1) marks for english    - an integer <=  80
         2) marks for Science    - an integer <=  90
         3) marks for Mathematics- an integer <= 100
 Output: Grade of student - First Class, Second Class, Average or Failed
"""

def get_marks(subject):
    print("Enter Marks for:",subject,":")
    marks = int(input())
    return marks

def get_percentage(eng,sci,maths):
    return (eng+sci+maths)/270 # Total marks= 80+90+100 = 270
                
def get_grade(percent):
    if percent >= 0.9:
        return "First Class"
    else:
        if percent >= 0.75:
            return "Second Class"
        else:
            if percent <= .35:
                return"Failed"
            else:
                return "Average"
    

# Main starts from here
e_marks = get_marks("English")
s_marks = get_marks("Science")
m_marks = get_marks("Mathematics")
percentage = get_percentage(e_marks,s_marks,m_marks)
print("Grade for Student is:",get_grade(percentage))
      


""" S12Q02
Write a program that generates a HTML file. 
Prompt the user for webpage title and webpage body contents. 
The webpage body should contain 
one main header, 
one sub header, and 
at least 2 paragraphs.
"""

def get_filename_as_agrv():
    """ get filename as argument from user or if not given, take filename interactively.      
    """
    if len(sys.argv)< 2:
        file = input( "Enter HTML filename to create:")
    else:
        file = sys.argv[1]
    return file

def insert_title(wfh,title):
    wfh.write("\t<head>\n\t\t<title>\n\t\t\t"+title + "\n\t\t</title>\n\t</head>\n")
#    print("\t<head>\n\t\t<title>\n\t\t\t"+title + "\n\t\t</title>\n\t</head>\n")

def insert_header(wfh,header_contents,In_Body):
    if not In_Body:
        wfh.write("\t<body>\n")
#        print("\t<body>\n")
        In_Body = True
    wfh.write("\t\t<h1>"+header_contents+"</h1>\n")
#    print("\t\t<h1>"+header_contents+"</h1>\n")
    return In_Body

def insert_para(wfh,para_contents):
    wfh.write("\t\t<p>"+para_contents+"\n\t\t</p>\n")
#    print("\t\t<p>"+para_contents+"\n\t\t</p>\n")
              

import sys

# Main starts here
if __name__ == "__main__":
    file = get_filename_as_agrv()+'.html'
    WFH = open(file,'w')
    WFH.write("<html>\n")
#    print("<html>\n")
    title = input("Please provide the Webpage Title:")
    insert_title(WFH,title)
    menu_prompt= "Please select:\n1. To add main header\n2. To add sub header\n3. To add paragraph\n4. To Quit\n  ENTER:"
    In_Body = False
    while True:
        n = int(input(menu_prompt))
        if n < 1 or n > 4:
                print("Entry error! Type a number between 1 to 4")
        elif n == 4:
                break
        else:
            if n == 1:
                header_contents = input("Please provide contents for  header:")    
                In_Body = insert_header(WFH,header_contents,In_Body)
            elif n == 2:
                header_contents = input ("please provide cotnents for Sub-Header:")
                In_Body = insert_header(WFH,header_contents,In_Body)
            elif n == 3:
                para = input("Please provide contents for para:")
                insert_para(WFH,para)
    if In_Body:
        WFH.write("\t</body>\n")
#        print("\t</body>\n")
    WFH.write("</html>")
#    print("</html>")
    WFH.close()
     

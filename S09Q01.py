"""S09Q01
Write a program that generates a HTML webpage. 
Prompt the user for webpage title and webpage body contents. 
The webpage body should contain 
- one main header, 
- one sub header, and 
- at least 2 paragraphs.

"""
# Helper functions
#Getting a  sentence  from user as input
def get_sentence(prompt):
    s = input(prompt)
    return s

def insert_tag(txt,tabs):
    print(" "*tabs+"<"+txt+">")
    return
    
def insert_main_header(title):
    insert_tag("html",0)
    insert_tag("head",1)
    insert_tag("title",2)
    print(" "*3,title)
    insert_tag("/title",2)
    insert_tag("/head",1)
    return
def insert_sub_header(title):
    print(' '*2+"<h1>" + title + "</h1>")

def insert_para(text):
    print(' '*2+"<p>"+text+"\n</p>")
 
# Main starts from here
def main():
    Title = get_sentence("Enter Webpage Title: ")
    insert_tag("body",1)
    page_banner = get_sentence("Enter Webpage Banner: ")
    para1 = get_sentence("Enter Content para#1:")
    para2 = get_sentence("Enter Content para#2:")
    insert_main_header(Title)
    insert_sub_header(page_banner)
    insert_para(para1)
    insert_para(para2)
    insert_tag("/body",1)
    insert_tag("/html",0)
               
   
main()


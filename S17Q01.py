"""S17Q01
Write a Python program that takes a file name as its argument. 
This program should count the occurrences of all the words in a file.

- It should then print the top 10 most repeated words 
in the descending order of their count.
- Print a separate list of all the words that
are not repeated in that file.

Data File Name: wordcount.txt
"""
# Helper functions



def get_filename_as_agrv_if_no_ask(prompt,rw):
    """ get filename as argument from user or if not given, take filename interactively.
         Return file handle; 2nd argument 'rw' is either 'r' or 'w' depending on whether to open for read or write.
    """
    Found = False
    ln = len(sys.argv)
    while not Found:
        if ln < 2:
            file = input( prompt)
        else:
            file = sys.argv[1]
        try:
            RFH = open(file,rw)
            Found = True
        except FileNotFoundError:
            print("%%Error! File not found!")
            ln = 1
#            break
    return  RFH

def get_contents(RH):
    
    """ Reads the contents of filename
        and returns the - File handle
        - List of all lines of the file
    """
    contents = RH.read()
    contents1 = contents.replace("."," ")
    stripped = contents1.strip()
    
    words = stripped.split()
    RH.close()
    return words
def make_list_descending(nlist):
    i = 0
    j = 0
    n = len(nlist)
    while i < n:
        j = 0
        while j < n-i-1:
            if nlist[j][1] < nlist[j+1][1]:
                nlist[j][0],nlist[j+1][0] = nlist[j+1][0],nlist[j][0]
                nlist[j][1],nlist[j+1][1] = nlist[j+1][1],nlist[j][1]
                j += 1
            else:
                j += 1
        i += 1
    return nlist

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

import sys
# Main starts from here
def main():
    
    RFH = get_filename_as_agrv_if_no_ask("Enter word  Data File Name : ","r")
    words = get_contents(RFH)
    print(words)
    unique = []
    count = []
    unique_words = list()
    unique.append(words[0])
    count.append(0)
    print("words list length:",len(words))
    for  i in range(0,len(words)):
        if words[i] in unique:
            j = unique.index(words[i])
            count[j] += 1
        else:
            unique.append(words[i])
            count.append(1)
    for i in range(0,len(unique)):
        unique_words.append([unique[i],count[i]])
    unique_words = make_list_descending(unique_words)
    tabular_formatted_printing(unique_words)

        
        

main()

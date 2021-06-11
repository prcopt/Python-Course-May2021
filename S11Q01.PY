""" S11Q01
From a file that contains a list of numbers.
Find the maximum number in that list. 
Also find the sum of all the numbers in that list.


"""

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
    return  contents,file

def get_max_number(numbers):
    """ Finds out the largest of the number from a list
        Input parameter: List containing numebrs
        function return the maximum of numbers
    """
    max = int(numbers[0])
    for i in range(0,len(numbers)):
        if numbers[i] > max:
            max = numbers[i]
    return max

def sum_of_numberlist(list):
    """ Finds out the sum of all numbers in a list
        Input parameter: List containing numebrs
        function return the maximum of numbers
    """
    sum = 0
    for i in list:
        sum += i
    return sum   

import sys

# Main starts here
if __name__ == "__main__":
    prompt = "Enter filename containing list of numbers:"
    contents,file = get_filename_as_agrv_and_get_contents_of_file(prompt)
    cleaned_contents = contents.replace("\n"," ")
    striped_contents = cleaned_contents.strip()
#    print("INPUT file Contents:-",contents,"Size:",len(contents))
#    print("cleaned contents:-",cleaned_contents,"Size:",len(cleaned_contents))
#    print("Stripped contents:-",striped_contents,"Size:",len(striped_contents))

    items = []
    items = striped_contents.split(' ')
    nlist = []
    for i in range(0,len(items)):
        nlist.append(int(items[i]))
#    print(items)
#    print("count of items:",len(items))
    print(nlist)
    max = get_max_number(nlist)
    sum = sum_of_numberlist(nlist)
    print("Max : ",max,"Sum of List: ",sum)
    

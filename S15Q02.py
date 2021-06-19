"""S15Q02
Write a function that accepts 2 lists as arguments. 
Both these 2 lists must be already sorted in the ascending order
This function should combine the lists into a sorted order and return the resulting list. 
This function should not use any built-in sort function or method.

- Write a test function that will test that the sorted list is correct. 

After successfully testing your program, 
pass the following 2 lists as arguments to your function 
and print the sorted result.

- left = [4, 17, 21, 47, 69, 75, 91, 97]
- right = [3, 10, 11, 14, 18, 21, 44, 55, 76,97]



"""
# Helper functions

def make_list_ascending(nlist):
    i = 0
    j = 0
    n = len(nlist)
    while i < n:
        j = 0
        while j < n-i-1:
            if nlist[j] > nlist[j+1]:
                nlist[j],nlist[j+1] = nlist[j+1],nlist[j]
                j += 1
            else:
                j += 1
        i += 1
    return nlist

def test(left,right,full_list,sorted_list):
    """ This function is to test the sorting function that use custom sorting algorithm """   
    length_of_list = len(sorted_list)
    if length_of_list == len(left)+len(right):
        print("Length of new list (",length_of_list,") found to be sum of two individual lists (",len(left),"&",len(right),")")
    temp_list = left+right

    temp_list.sort()
    print("Library SORTED List:",temp_list)
    if sorted_list == temp_list:
        print( "sorting done correctly")
    else:
        print(" Sorting algorithm had error",sorted_list,"\n",temp_list)
        
# Main starts from here
def main():
    left = [4, 17, 21, 47, 69, 75, 91, 97]
    right = [3, 10, 11, 14, 18, 21, 44, 55, 76,97]
    print("Left  list:",left)
    print("Right list:",right)
    full_list = left+right
    print("Concatenated List:",full_list)
    sorted_list = make_list_ascending(full_list)
    print("Custom Sorted list:",sorted_list)
    test(left,right,full_list,sorted_list)
    
main()

 

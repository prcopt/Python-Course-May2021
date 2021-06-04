"""S06Q01
- Write a program that takes multiple sentences as input from the user. 
The last input is indicated by an empty line.
- Find the number of words entered
- Find the number of words that contain the vowel ‘a’


"""
# Helper functions

def get_sentences():
#Getting a set of sentences  from user as input and make a list of sentences
    s = "a"
    slist = []
    first_entry = False
    print()
    while s != "":
        if not first_entry:
            s = input("Key-in a sentence.\n[Just Enter to terminate entry\nNow start Entry: ")
            first_entry = True
        else:
            s = input("Enter Next Sentence:")
        if s != "":
            slist.append(s)
    return slist

  
# Main starts from here
def main():
    list_of_sentences =[]
    list_of_sentences = get_sentences()
# for each sentence, find number of words and count words with character 'a'
    a_count = 0
    word_count = 0
    temp_string =[]
    for i in list_of_sentences:
        temp_string = i.split()
        w = len(temp_string)
        word_count += w
        for j in temp_string:
            c = j.count("a")
            if c >0:
                a_count += 1
  # Printing Results        
    print(list_of_sentences)
    print("a char count:",a_count,"word count: ",word_count)
    
   

main()

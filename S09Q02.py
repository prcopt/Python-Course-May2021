"""S09Q02
Write a search and replace program in Python. 
This should first take the original text as input by prompting the user for it. 
It should then, prompt the user for which word to search, 
and what new word it should be replaced with.
"""
# Helper functions
#Getting a  sentence  from user as input
def get_sentence(prompt):
    s = input(prompt)
    return s
def get_word(prompt):
    """ This function prompts the user for a word
        It returns a word
    """
    ns= input(prompt)
    return ns 
# Main starts from here
def main():
    sentence = get_sentence("Key-in a sentence: ")
    setence_list = []
    sentence_list = sentence.split()
    print(sentence_list)
    ori_word = get_word("Enter word to replace:")
    new_word = get_word("Enter new word to replace with:")
    ind = sentence_list.index(ori_word)
    print("index:",ind)
    sentence_list[ind] = new_word
    print(sentence_list)
    sentence = ' '.join(sentence_list)
    print(sentence)
    
          
main()

 

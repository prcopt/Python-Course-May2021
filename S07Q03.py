"""S07Q03
Prompt the user to enter a long sentence
- What is the last character in the sentence ?
- What are the last 5 characters in the sentence ?
- Print the characters that are present in 2nd and 5th position of the sentence
- Print the character at the center of the string, along with the 2 adjoining characters. 
Ex : If the string entered is "Web Browser”
the character at its centre is "r" and so print "Bro"

"""
# Helper functions
#Getting a  sentence  from user as input
def get_sentence():
    s = input("Key-in a sentence: ")
    return s
  
# Main starts from here
def main():
    sentence = get_sentence()
    print("Last Character is:"+"'"+sentence[-1]+"'")
    print("Last 5 Characters:"+"'"+sentence[-5:]+"'")
    print("2nd position Character: "+"'"+sentence[1]+"'")
    print("5th position Character: "+"'"+sentence[4]+"'")
    length = len(sentence)
    mid = int(length/2)
    if length%2 > 0:
        mid += 1
    start = mid - 2
    end = mid + 1
    print("3 Char in mid:"+"'"+sentence[start:end]+"'")
          
main()

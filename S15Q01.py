""" S15Q01
You invited 10 friends to your house to play a game. 
Each one is asked to pick a card that contains a number between 99 and 999. 
The one with the maximum number wins the game. 
Simulate this game using Python
- Which cards did each one pick ? 
- Who won the game ?
"""
import random

def get_card(pack):
    card = random.sample(pack,1)
    no_picked = card[0]
    if no_picked in pack:
        pack.remove(no_picked)
    return no_picked,pack

# Main starts from here
friends = ["Ahir","Balsu","Choudhary","Dilip","Elsa","Firoz","Ganesh","Hiremath","Ishaan","Jay"]
pack = []
max = 0
number = 0
for i in range(99,999):
    pack.append(i)
    
for each in friends:
    number,pack = get_card(pack)
#   print(each," picked ",number) # enable if you want to know who picked which card
    if number > max:
        max = number
        winner = each
    print(each," picked card #",number)
print ( "Winner is :",winner,"Card Picked: ",max)       

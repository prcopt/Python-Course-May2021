""" S0AQ03
You invite home 10 of your closest friends and play a simple game of luck.
Each of your friend picks up a card from a stack of cards numbered from 300 to 325. 
The person with the highest number wins

Simulate this simple game using Python
[ Hint : Make sure that no 2 friends get the same numbered card ]


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
for i in range(300,326):
    pack.append(i)
    
for each in friends:
    number,pack = get_card(pack)
#   print(each," picked ",number) # enable if you want to know who picked which card
    if number > max:
        max = number
        winner = each
print ( "Winner is :",winner,"Card Picked: ",max)       
    

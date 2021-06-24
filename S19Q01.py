"""S19Q01
Write a Python program that takes a file name as its argument. 
This file [ nominations.txt ] contains the nominations for a sports event.

- What are the games that have nominations ?
- Print the list of players playing each game 
in the ascending order of their names.
- Print the list of players who are playing more than one game.
- Print the list of players who are playing only one game.
INPUT FILE: NOMINATIONS.TXT
"""
# Helper functions



def get_filename_as_agrv_if_no_ask(prompt):
    """ get filename as argument from user or if not given, take filename interactively.
         Return file handle
    """
    Found = False
    ln = len(sys.argv)
    while not Found:
        if ln < 2:
            file = input( prompt)
        else:
            file = sys.argv[1]
        try:
            RFH = open(file)
            Found = True
        except FileNotFoundError:
            print("%%Error! File not found!")
            ln = 1
#            break
    return  RFH

def get_nomination_list(RFH):
    line = "xx"
    nomination_list = list()
#    print("FILE CONTENTS:-")
    while line != "":
        line = RFH.readline()
        line = line.strip()
        if line == "":
            break
#        print(line)
        data = line.split(sep=" - ")
        nomination_list.append(data)
    return nomination_list

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
    
    RFH = get_filename_as_agrv_if_no_ask("Enter Nomination List Data File Name : ")
    nomination_list = get_nomination_list(RFH)

    players=list()
    games = list()
    for i in range(0,len(nomination_list)):
        players.append(nomination_list[i][0])
        games.append(nomination_list[i][1])
    unique_player = list()
    unique_player.append(players[0])
    for plyr in players:
        if plyr not in unique_player:
            unique_player.append(plyr)
### Make unique games list unique_games
    unique_games = list()
    unique_games.append(games[0])
    for gms in games:
        if gms not in unique_games:
            unique_games.append(gms)
    games_played = list()        
    for i in range(0,len(unique_player)):
        game_set = list()
        for j in range(0,len(games)):
            if unique_player[i] == players[j]:
                game_set.append(games[j])
        games_played.append(game_set)

## Make unique player list player
    player_names = list()
    for i in range(0,len(unique_games)):
        player_set = list()
        for j in range(0,len(players)):
            if unique_games[i] == games[j]:
                player_set.append(players[j])
        player_names.append(player_set)        

    print("Games That have nominations:-")
    for i in range(0,len(unique_games)):
        print(i+1,'.',unique_games[i])

    print("List of players playing Each Game")
    for i in range(0,len(unique_games)):
        print(i+1,'.',unique_games[i],':')
        plyr_list = list()
        for j in range(0,len(player_names[i])):
            plyr_list.append(player_names[i][j])
        plyr_list.sort()
        for j in range(0,len(plyr_list)):
            print("    ",j+1,'.',plyr_list[j])
    print("Players playing more than one game:")
    c = 0
    for i in  range(0,len(unique_player)):
        game_count = len(games_played[i])
        if game_count > 1 :
            print(c+1,'.',unique_player[i],'(',game_count,')')
            c += 1
    c = 0
    print("Players playing only one game:")
    for i in  range(0,len(unique_player)):
        game_count = len(games_played[i])
        if game_count == 1 :
            print(c+1,'.',unique_player[i])
            c += 1
#    tabular_formatted_printing(nomination_list)


main()

 
    
    

"""S06Q02 : T20 Cricket Match
- Collect the runs scored for each ball faced by the batsman. 
A dot ball is represented by a dot in input. 
An empty line represents a wicket. 

- Find the total runs scored by the batsman
- Find the strike rate of the batsman [ runs scored/balls faced ]
- Find the number of balls wasted by the batsman
- How many boundaries and sixes did he score ?



"""
# Helper functions

def Bowl(over_no,ball_no):
    out = False
    runs = 0
    inp_validity = False
    while not inp_validity:
        action = input("Runs Scored:")
        if action == "":
            out = True
            inp_validity = True
        elif action == ".":
            runs = 0
            inp_validity = True
        else:
            runs = int(action)
            if runs >= 0 and runs <= 6:
                inp_validity = True
            else:
                print("Data Entry Error! Enter again:")
    return runs,out
    

def play_an_over(over_no,bat1,bat2,tot_runs,sixer,boundaries,wastage,balls_faced,next_player):
#Execution of an over
    no_of_balls = 6
    ball_no = 1
    striker = bat1
    non_striker = bat2
    out = False
    while ball_no <= 6:
        runs,out = Bowl(over_no,ball_no)
        print("Over No:",over_no,"Ball No: ",ball_no, "Striker Player:",striker, "Non-Striker:",non_striker) 
        balls_faced[striker-1] += 1
        tot_runs[striker-1] += runs
        if runs == 6:
            sixer[striker-1] += 1
            print( " Player:",striker,"Hit a Sixer!!!")
        elif runs == 4:
            print( " Player:",striker,"Hit a Boundery!!") 
            boundaries[striker-1] += 1
        elif runs == 0:
            if out:
                print(" Player:",striker," is OUT !!!")
                wastage[striker-1] += 1
                if next_player > 11:
                    print(" GAME IS OVER")
                    return striker,non_striker,tot_runs,sixer,boundaries,wastage,balls_faced,next_player
                else:
                    striker = next_player
                    print("NEXT PLAYER: ",next_player) 
                    next_player +=1
            else:
                print("Did'nt score run")
                wastage[striker-1] += 1
        elif runs%2 != 0:
            striker, non_striker = non_striker,striker
        ball_no += 1
        if ball_no > 6:
            return striker,non_striker,tot_runs,sixer,boundaries,wastage,balls_faced,next_player            
 
  
# Main starts from here    
def main():
    total_overs = 5
    tot_runs = [0,0,0,0,0,0,0,0,0,0,0]
    sixer =[0,0,0,0,0,0,0,0,0,0,0]
    boundaries = [0,0,0,0,0,0,0,0,0,0,0]
    wastage = [0,0,0,0,0,0,0,0,0,0,0]
    balls_faced = [0,0,0,0,0,0,0,0,0,0,0]
    batsmen = [1,2,3,4,5,6,7,8,9,10,11]
    strike_rate = [0,0,0,0,0,0,0,0,0,0,0]
    bat1 = 1
    bat2 = 2
    next_player = 3
    over_no = 1
    
    while over_no <= total_overs:
        striker,non_striker,tot_runs,sixer,boundaries,wastage,balls_faced,next_player = play_an_over(over_no,bat1,bat2,tot_runs,sixer,boundaries,wastage,balls_faced,next_player)
        if over_no +1 <= total_overs:
            over_no += 1
            bat1 = striker
            bat2 = non_striker
        else:
            break
    print("MATCH OVER")
    total_runs = 0
    for i in tot_runs:
        total_runs += i
    print (" Total Runs Scored :", total_runs,"\n Runs Break-up:")
    print( "PLAYER PERFORMANCES:")
    i = 0
    for i in batsmen:
        if balls_faced[i-1] !=0:
            strike_rate[i-1] = tot_runs[i-1]/balls_faced[i-1]
    print("Batsman" ," Runs ","Balls faced", "Strike Rate ","balls wasted","Sixes","Boundaries")
    i = 0
    while i < next_player-1:
        print(batsmen[i],tot_runs[i],balls_faced[i],strike_rate[i],wastage[i],sixer[i],boundaries[i])
        i += 1
        
main()

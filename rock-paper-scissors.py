def line(): print("+-----------------------------+")

def scoreboard(p1_score : int, pc_score : int) -> None :
    line()
    print("|          SCORE              |")
    line()
    print("|   PLAYER    |    COMPUTER   |")
    line()
    print(f"|      {p1_score}      |       {pc_score}       |")
    line()

import random
choices=['rock','paper','scissors']
wins={'rock':'scissors','paper':'rock','scissors':'paper'}
p1_score,pc_score=0,0
while True:
    print("----------ROCK, PAPER AND SCISSORS----------")
    p1=None
    while p1 not in choices:
        p1=str(input("Enter your move (rock/paper/scissors) : ")).lower()
    pc=choices[random.randint(0,2)]
    print(f"PLAYER : {p1}\t\tCOMPUTER : {pc}")
    #print("TIE")if p1==pc else print("YOU WIN!") if wins[p1]==pc else print("YOU LOSE")
    if (p1==pc):
        print("TIE")
    elif (wins[p1]==pc):
        print("YOU WIN!")
        p1_score+=1
    else:
        print("COMPUTER WINS!")
        pc_score+=1
    scoreboard(p1_score,pc_score)
    ch=int(input("Enter 1 to continue : "))
    if ch!=1:
        break



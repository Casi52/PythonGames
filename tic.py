import random as r
import time as t
from collections import Counter

row1 = [" "," "," "]
row2 = [" "," "," "]
row3 = [" "," "," "]
rows = (row1,row2,row3)

def prnt(r1,r2,r3):
    print("+", "-", "+", "-", "+", "-", "+")
    print("|", r1[0],"|", r1[1],"|", r1[2],"|")
    print("+", "-", "+", "-", "+", "-", "+")
    print("|", r2[0],"|", r2[1],"|", r2[2],"|")
    print("+", "-", "+", "-", "+", "-", "+")
    print("|", r3[0],"|", r3[1],"|", r3[2],"|")
    print("+", "-", "+", "-", "+", "-", "+")

def pplace(sym):
    notPlaced = True
    while notPlaced:
        try:
            px = int(input("x: ")) - 1
            py = int(input("y: ")) - 1
            if rows[py][px] == " ":
                rows[py][px] = sym
                notPlaced = False
            else:
                print("Invalid placement.")
        except:
            print("Invalid placement.")

xplacements = [
    (0,1),
    (0,2),
    (0,3),
    (1,0),
    (1,1),
    (1,2),
    (2,0),
    (2,1),
    (2,2),
]

oplacements = [
    (0,1),
    (0,2),
    (0,3),
    (1,0),
    (1,1),
    (1,2),
    (2,0),
    (2,1),
    (2,2),
]

def oplace(place, placed, sym):

    notPlaced = True
    tries = 0
    while notPlaced and tries <= 9:
        try:
            p = r.sample(place, 1)

            if rows[p[0][0]][p[0][1]] == " ":
                rows[p[0][0]][p[0][1]] = sym
                notPlaced = False
                placed.append(p[0])
            else:
                pass
        except:
            pass
        tries += 1

def wincalc():
    wins = (
    (rows[0][0],rows[0][1],rows[0][2]),
    (rows[1][0],rows[1][1],rows[1][2]),
    (rows[2][0],rows[2][1],rows[2][2]),
    (rows[0][0],rows[1][0],rows[2][0]),
    (rows[0][1],rows[1][1],rows[2][1]),
    (rows[0][2],rows[1][2],rows[2][2]),
    (rows[0][0],rows[1][1],rows[2][2]),
    (rows[0][2],rows[1][1],rows[0][2]),
    )
    for i in range(8):
        if wins[i][0] != " " and wins[i][0] == wins[i][1] == wins[i][2]:
            print(wins[i][0], "wins!")
            if wins[i][0] == "X":
                return 1
            if wins[i][0] == "O":
                return 2
        else:
            pass
    return 0

def game(turns):
    while wincalc() and turns <= 9:
        prnt(row1,row2,row3)
        pplace("X")
        oplace("O")

def sgame(speed):

    global xtp,otp

    xtp = list()
    otp = list()
    turns = 0
    while wincalc() == 0 and turns <= 9:
        print(turns)
        oplace(xplacements, xtp, "X")
        prnt(row1,row2,row3)
        t.sleep(speed/10)
        oplace(oplacements, otp, "O")
        prnt(row1,row2,row3)
        t.sleep(speed/10)
        turns += 1

yes = ("Y", "y", "Yes", "yes")

def reset():
    global row1,row2,row3,rows

    row1 = [" "," "," "]
    row2 = [" "," "," "]
    row3 = [" "," "," "]
    rows = (row1,row2,row3)



sim = input("Simulate? ")
if sim in yes:
    cont = True
    while cont:
        x = float(input("Speed (3 = slow, 1 = fast): "))
        y = int(input("Sim amount: "))
        xwins = 0
        owins = 0
        for i in range(y):
            sgame(x)
            if wincalc() == 1:
                xwins += 1
                for i in range(len(xtp)):
                    xplacements.append(xtp[i])
            if wincalc() == 2:
                owins += 1
                for i in range(len(otp)):
                    oplacements.append(otp[i])
            reset()
            t.sleep(x)
        print("X wins: ", xwins)
        print("O wins: ", owins)
        data1 = Counter(xplacements)
        print("\n\nX top three spots: \n\n{}\n\n{}\n\n{}" .format(data1.most_common(3)[0],data1.most_common(3)[1],data1.most_common(3)[2]))
        data2 = Counter(oplacements)
        print("\n\nO top three spots: \n\n{}\n\n{}\n\n{}" .format(data2.most_common(3)[0],data2.most_common(3)[1],data2.most_common(3)[2]))
        

play = True
while play:

    turns = 0

    game(turns)
    if input("Play again? ") in yes:
        play = True
    else:
        play = False
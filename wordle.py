import random as r
from termcolor import colored

w = open("./wrds", "r", encoding="utf-8")
words = list()

for i in w:
  words.append(i[:5])

w.close()

def prnt(squares):
  print("+", "-", "+", "-", "+", "-", "+", "-", "+", "-", "+")
  print("|", squares[0], "|", squares[1], "|", squares[2], "|", squares[3], "|", squares[4], "|")
  print("+", "-", "+", "-", "+", "-", "+", "-", "+", "-", "+")

yes = ("Y", "y", "Yes", "yes")

def RWord():
  return r.sample(words, 1)[0]

while input("Play? ") in yes:
  tries = 0
  wrd = RWord().lower()
  a,b,c,d,e = " ", " ", " ", " ", " "
  spaces = [a,b,c,d,e]
  prnt(spaces)
  print()
  win = False
  while not win:
    try:
      inp = input("Word: ")
      tries += 1
      for i in range(len(inp)):
        if inp[i] in wrd:
          if inp[i] == wrd[i]:
            spaces[i] = colored(inp[i], "green")
          else:
            spaces[i] = colored(inp[i], "yellow")
        else:
          spaces[i] = colored(inp[i], "grey")
      prnt(spaces)
    except:
      print("invalid input, try again.")
    if inp == wrd:
      print("You Win! Tries:", tries)
      win = True
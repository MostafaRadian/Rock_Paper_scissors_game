import random as rand


def PrintInput(inp):
    if inp == "rock":
        print(rock)
    elif inp == "paper":
        print(paper)
    else:
        print(scissors)


def Winner(com, ply):
    if ply == com:
        print("Draw!")
    elif ply == "rock" and com == "scissors":
        print("You Win!")
    elif ply == "paper" and com == "rock":
        print("You Win!")
    elif ply == "scissors" and com == "paper":
        print("You Win!")
    else:
        print("You Lose :(")


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game = ["rock", "paper", "scissors"]
randNum = rand.randint(0, 2)
playerInput = int(input("Please enter 0, 1 or 2 for rock, paper, scissors respectively\n"))

if playerInput in [0, 1, 2]:

    print("Player: \n")
    player = game[playerInput]
    PrintInput(player)

    print("Computer: \n")
    computer = game[randNum]
    PrintInput(computer)
    Winner(computer, player)
else:
    print("Wrong Input")

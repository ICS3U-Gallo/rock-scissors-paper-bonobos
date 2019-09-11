from random import randint

t = ["Rock", "Paper", "Scissors"]

loopcontrol = False

while loopcontrol == False:
    computer = t[randint(0,2)]
    player = input("Choose: Rock, Paper, or Scissors?") 
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("Uh oh! I don't recognize that. Check your spelling!")
        continue
    
    exitloop = False

    while exitloop == False:
        player = input("Do you want to play again? Yes or No?")
        if player == "Yes":
            exitloop = True
        elif player == "No":
            print("Thank you for playing.")
            loopcontrol = True
            exitloop = True
        else:
            print("Uh oh! I don't recognize that. Check your spelling!")
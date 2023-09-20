from getpass import getpass as input

print("!!! Rock, Paper, Scissors Game!!!.")
print()
print("Enter R for Rock, P for paper, or S for Scissors")
print()
input1 = input("Player 1 : ").upper()
input2 = input("Player 2 : ").upper()
print()

#Player 1 - Rock
if input1 == "R":
    if input2 == "R":
        print("Rock and Rock. Nobody won. Play again.")
    elif input2 == "P":
        print("Paper of Player 2 covers Rock of Player 1, Player 2 won!")
    elif input2 == "S":
        print("Rock of Player 1 smashes Scissors of Player 2, Player 1 won!")
    else:
        print("Wrong input, Player 2, try again!")
#Player 1 - Paper
elif input1 == "P":
    if input2 == "P":
        print("Paper and Paper.Nobody won. Play again.")
    elif input2 == "R":
        print("Paper of Player 1 covers Rock of Player 2, Player 1 won!")
    elif input2 == "S":
        print("Scissors of Player 2 cut Paper of Player 1, Player 2 won!")
    else:
        print("Wrong input, Player 2, try again!")
#Player 1 = Scissors
elif input1 == "S":
    if input2 == "S":
        print("Scissors and Scissors.Nobody won. Play again.")
    elif input2 == "R":
        print("Rock of Player 2 smashes Scissors of Player 1, Player 2 won!")
    elif input2 == "P":
        print("Scissors of player 1 cut Paper of Player 2, Player 1 won!")
    else:
        print("Wrong input, Player 2, try again!")

else: 
    #Player 1 and Player 2 - bad input
    if input2 != "R" and input2 != "S" and input2 != "P":
        print("Wrong input, Player 2 and Player 1, try again!")
    #Player 1 - bad input
    else:
        print("Wrong input, Player 1, try again!")

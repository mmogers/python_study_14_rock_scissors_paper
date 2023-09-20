from getpass import getpass as input

print("\033[1;92m!!! Rock, Paper, Scissors Game!!!.\033[0;0m")
round = 0
count1 = 0
count2 = 0
while True:
  if count1 == 3 or count2 == 3:
    break
  round += 1
  print()
  print("\033[1;95mRound ", round, "\033[0;0m")
  print("Enter R for Rock, P for paper, or S for Scissors")
  print()
  input1 = input("Player 1 : ").upper()
  input2 = input("Player 2 : ").upper()
  print()
  
  #Player 1 - Rock
  if input1 == "R":
      if input2 == "R":
          print("Rock and Rock. Nobody won. Play again.")
          continue
      elif input2 == "P":
          print("Paper of Player 2 covers Rock of Player 1, \n\033[95mPlayer 2 \033[0mwins the round!")
          count2 += 1
          continue
      elif input2 == "S":
          print("Rock of Player 1 smashes Scissors of Player 2, \n\033[95mPlayer 1 \033[0mwins the round!")
          count1 += 1
          continue
      else:
          print("Wrong input, Player 2 :( ")
          exit()
  #Player 1 - Paper
  elif input1 == "P":
      if input2 == "P":
          print("Paper and Paper.Nobody won. Play again.")
          continue
      elif input2 == "R":
          print("Paper of Player 1 covers Rock of Player 2, \n\033[95mPlayer 1 \033[0m wins the round!")
          count1 += 1
          continue
      elif input2 == "S":
          print("Scissors of Player 2 cut Paper of Player 1, \n\033[95mPlayer 2 \033[0m wins the round!")
          count2 += 1
          continue
      else:
          print("Wrong input, Player 2 :(")
          exit()
  #Player 1 = Scissors
  elif input1 == "S":
      if input2 == "S":
          print("Scissors and Scissors.Nobody won. Play again.")
          continue
      elif input2 == "R":
          print("Rock of Player 2 smashes Scissors of Player 1, \n\033[95mPlayer 2 \033[0m wins the round!")
          count2 += 1
          continue
      elif input2 == "P":
          print("Scissors of player 1 cut Paper of Player 2, \n\033[95mPlayer 1 \033[0m wins the round!")
          count1 += 1
          continue
      else:
          print("Wrong input, Player 2 :(")
          exit()
  else: 
      #Player 1 and Player 2 - bad input
      if input2 != "R" and input2 != "S" and input2 != "P":
          print("Wrong input, Player 2 and Player 1 :(")
          exit()
      #Player 1 - bad input
      else:
          print("Wrong input, Player 1 :(")
          exit()     
print()
print("\U0001F49A \U0001F49A \U0001F49A")
if count1 == 3:
  print("\033[1;92mPlayer 1 won!\033[0;0m")
else:
  print("\033[1;92mPlayer 2 won!!!\033[0;0m")
  
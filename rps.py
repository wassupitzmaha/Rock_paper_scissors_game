
print ("WELCOME TO THE GAME!\n When asked for your choice, please select either 'r', 's', 'p'")

# Take inputs
playerOneInput = input("player one select: r, p or s")
playerTwoInput = input("player two select: r, p or s")
print("player one input: " + playerOneInput + "\n" 
      + "player two input: " + playerTwoInput)

# compare our inputs to see results. Either player1 wins or player2 wins

# SCISSORS
if playerOneInput == "s":
    if playerTwoInput == "s":
        print("IT IS A TIE!! TRY AGAIN")
    if playerTwoInput == "r":
        print("PLAYER TWO WON")
    if playerTwoInput == "p":
        print("PLAYER ONE WON")

#  ROCK
if playerOneInput == "r":
    if playerTwoInput == "r":
        print("IT IS A TIE!! TRY AGAINN")
    if playerTwoInput == "s":
        print("SUCKS TO SUCK PLAYER 2!!")
    if playerTwoInput == "p":
        print("SUCKS TO SUCK PLAYER 1")

# PAPER
if playerOneInput == "p":
    if playerTwoInput == "p":
        print("IT'S A TIE!! TRY AGAIN")
    if playerTwoInput == "s":
        print("SUCKS TO SUCK PLAYER 1")
    if playerTwoInput == "r":
        print("SUCKS TO SUCK PLAYER 2")

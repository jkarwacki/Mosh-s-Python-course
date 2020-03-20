secretNumber = 9
noOfGuesses = 0
maxGuesses = 3

while noOfGuesses < maxGuesses:
    guess = int(input('Guess: '))
    noOfGuesses += 1
    if guess == secretNumber:
        print("You won!")
        break
else:                                     # else statement to the while loop; if the condition is not longer fulfilled
    print("Sorry, you failed")            # and no break was made, this code is run


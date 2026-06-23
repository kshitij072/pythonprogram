#Make a simple game involving a computer and a user. The computer first guesses a number between 1 and 9 inclusive, then ask the user to enter a number between 1 and
 
#9 inclusive. If the user guess is correct then display “You got it right”, if the guess is
#close (+1, -1) “Almost got it “, Otherwise “You got it wrong”.


import random

computer = random.randint(1, 9)

user = int(input("Enter a number between 1 and 9: "))

if user == computer:
    print("You got it right")
elif user == computer + 1 or user == computer - 1:
    print("Almost got it")
else:
    print("You got it wrong")

print("Computer's number was:", computer)
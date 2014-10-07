# Guess My Number
#
# The player picks a random number between 1 and 100
# The computer tries to guess it and the player lets
# the computer know if the guess is too high, too low
# or right on the money

import random  

print("Welcome to 'Guess Your Number'!")
print("I want you to think of a number between 1 and 100.")
print("I'll try to guess it in as few attempts as possible.")

# set the initial values
the_number = int(input('What is your number? '))
guess = random.randint(1, 100)
print(guess)
tries = 1
heighest = 100
lowest = 0


# guessing loop
while guess != the_number:
    higher_or_lower = input('Am I too high or too low? ')
    if higher_or_lower == 'Too High':
        heighest = guess - 1
        
    if higher_or_lower == 'Too low':
        lowest = guess + 1
    guess = random.randint(lowest, heighest)
    print(guess)
    tries += 1
        





print("I guessed it!  The number was", the_number)
print("And it only took me", tries, "tries!\n")
  
input("\n\nPress the enter key to exit.")

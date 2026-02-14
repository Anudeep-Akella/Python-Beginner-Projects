"""
Bagels, a deductive logic game.
By Al Sweigart al@inventwithpython.com
"""
import random as ra

print("""Bagels, a deductive logic game.
By Al Sweigart al@inventwithpython.com
I am thinking of a 3-digit number. Try to guess what it is.
Here are some clues:
When I say:    That means:
  Pico         One digit is correct but in the wrong position.
  Fermi        One digit is correct and in the right position.
  Bagels       No digit is correct.""")


thought = str(ra.randint(100,999))

print("I have thought up a number\n.You have 10 guesses to get it.")

guess = 1

while guess <= 10:
    clues = []
    print("Guess #",guess)
    num = str(input("> "))
    guess += 1
    for i in range(len(num)):
        if num[i] == thought[i]:
            clues.append("Fermi")
        elif num[i] in thought:
            clues.append("pico")
    if len(clues)==0:
        print("Bagels")
        continue
    else:
       print(' '.join(clues))

    if num == thought:
        print("You got it!")
        break

    if guess == 10:
        print("You ran out of guesses")
        print(f"The number is {thought}")
        break
        

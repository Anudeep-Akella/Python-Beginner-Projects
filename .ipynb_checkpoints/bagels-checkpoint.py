'''
    Bagels a deductive logic game where you must guess the number based on clues.
    This is a python project present in AI Segwart BIG book of Python Projects.
    This is first project.
'''
import random as ra

NUM_DIGITS = int(input("Enter the number of digits number game you want to play: "))
MAX_GUESS = int(input("Enter the number of guesses you think you can win this game: "))

def main():
   print(f'''Bagels, a deductive logic game.
     By Al Sweigart al@inventwithpython.com

        I am thinking of a {NUM_DIGITS}-digit number with no repeated digits.
        Try to guess what it is. Here are some clues:
        When I say:    That means:
        Pico         One digit is correct but in the wrong position.
        Fermi        One digit is correct and in the right position.
        Bagels       No digit is correct.
.
         For example, if the secret number was 248 and your guess was 843, the
        clues would be Fermi Pico.''')
    while True:
        thought = secretNumber()
        print("I have thought a number")
        print(f"You have {MAX_GUESS}guesses to try")
        numGuess = 1
        while numGuess <=MAX_GUESS:
            guess = ''
            while(len(guess
            




def secretNumber():
    """A function to get the secret number that is randomly selected selected by the program.
        It returns the number."""
    num = list('0123456789')
    ra.shuffle(num)

    secretnum = ''
    for i in range(NUM_DIGITS):
        secretnum += num[i]

    return secretnum

def clues(guess,thought):
    if guess == thought:
        return "Congratulations! You got it!"

    clues = []
    for i in range(len(guess)):
        if guess[i] == thought[i]:
            clues.append('Fermi')
        elif guess[i] in thought[i]:
            clues.append('Pico')

    if not clues:
        return 'Bages!'

    else:

        return ''join(clues)
            
main()

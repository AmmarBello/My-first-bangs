# This is a guess the number game.
import random

def game():
    guessesTaken = 0
    print('Hello! What is your name?')
    myName = raw_input()

    number = random.randint(1, 20)
    print('welcome, ' + myName + ', I am thinking of a number between 1 and 20.')

    while guessesTaken < 6:
       try:
          print('Guess a number between 1 and 20: ') # There are four spaces in front of print.
          guess = raw_input()
          guess = int(guess)
       except ValueError:
          print("{} isn't a number!".format(guess))
       else:     
          if guess == number:
                break
          elif guess < number:
                print("My number is higher than {}".format(guess))
          else:
                print("My number is lower than {}".format(guess)) 

       guessesTaken = guessesTaken + 1

    if guess == number:
       guessesTaken = str(guessesTaken)
       print('Good job, ' + myName + ' You got it! My number was %d') %(number)

    if guess != number:
       number = str(number)
       print(' You didn\'t get it! The number I was thinking of was ' + number)
    play_again = raw_input("Do you want to play again? Y/n ")
    if play_again.lower() != 'n':
        game()
    else:
        print("Bye!")

game()

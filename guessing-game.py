#!/usr/bin/env python

print("""
========================================================================
 Guessing Game
---------------

I've got a secret number in my head, can you guess what it is? 

Here are the rules:
 - The number is between 0 and 100.
 - You have 10 guesses.
 - I'll tell you if it's higher or lower than your guess.

Let's begin!

========================================================================
""")

secretNumber = 5
guess = input('> ')
guessCount = 1


def printWinningStatment(count):
  text = """
You won!

It took you %s tries to guess the correct number.

Well Done!
""" % (count)
  return text

while guess != secretNumber:
  guessCount += 1
  print('Nope.. Try again.')
  guess = input('> ')
else:
  print(printWinningStatment(guessCount))

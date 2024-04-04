#!/usr/bin/env python

import random

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

guess = int(input('> '))
guess_count = 1
start_range = 0
end_range = 100
secret_number = random.randint(start_range, end_range)


def printWinningStatment(count):
  text = """
You won!

It took you %s tries to guess the correct number.

Well Done!
""" % (count)
  return text

while guess != secret_number:
  if guess_count == 10:
    print('Game Over. You did not guess the correct number in 10 turns or less.')
    break

  guess_count += 1
  print('\nNope... Try again.')

  if guess > secret_number:
    print('Lower...\n')
  else:
    print('Higher...\n')

  guess = int(input('> '))

else:
  print(printWinningStatment(guess_count))

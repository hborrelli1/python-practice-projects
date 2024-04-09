#!/usr/bin/env python3

import random

def main():  
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

  guess: int = get_integer_input('> ')
  guess_count: int = 1
  start_range: int = 0
  end_range: int = 100
  secret_number: int = random.randint(start_range, end_range)
  
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
    
    guess: int = get_integer_input('> ')

  else:
    print(print_winning_statment(guess_count))

def get_integer_input(prompt: str) -> int:
  """Get integer input from user."""
  while True:
    try:
      value = int(input(prompt))
      return value
    except ValueError:
      print('Invalid Input. Please enter an integer.')

def print_winning_statment(count: int) -> str:
  text = """
You won!

It took you %s tries to guess the correct number.

Well Done!
""" % (count)
  return text

if __name__ == '__main__':
  main()
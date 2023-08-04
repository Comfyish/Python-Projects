'''roll dice and ask user to guess number that is rolled, if correct the user wins otherwise the computer wins'''

from random import randint
from time import sleep

def get_user_guess():
  '''ask for the users guess and return the input value as an int'''
  guess = int(input('What is your guess?'))
  return guess

def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides * 2
  print ('the maximum value you can roll for is %d' % (max_val))
  guess = get_user_guess()
  if guess > max_val:
    print ('guess is greater than the maximum possible value')
  else:
    print ('Rolling...')
    sleep(2)
    print ('Dice 1 rolled for %d' % (first_roll))
    sleep(1)
    print ('Dice 2 rolled for %d' % (second_roll))
    sleep (1)
    total_roll = first_roll + second_roll
    print ('You rolled a total of %d' %(total_roll))
    print ('Result...')
    sleep(1)
    if guess == total_roll:
      print ('CONGRATS YOU WON RAHHHHH')
    else: 
      print ('Today you took an L.')

roll_dice(4)

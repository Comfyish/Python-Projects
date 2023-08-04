# coding=utf-8
'''This Program will play a game of Rock Paper Scissors by asking the player for an input and rolling randomly for its response'''

import random

options = ['ROCK', 'PAPER', 'SCISSORS']
message = {'tie':'Yawn it\'s a tie!', 'won':'Yay you won!','lost':'Aww you lost!'}

def decide_winner(user_choice, computer_choice):
  user_choice = user_choice.upper()
  print ('You chose %s' % user_choice)
  print ('RPS-Bot chose %s' % computer_choice)
  if user_choice == computer_choice:
    print (message['tie'])
  elif user_choice == 'ROCK' and computer_choice == 'SCISSORS':
    print (message['won'])
  elif user_choice == 'PAPER' and computer_choice == 'ROCK':
    print (message['won'])
  elif user_choice == 'SCISSORS' and computer_choice == 'PAPER':
    print (message['won'])
  else:
    print (message['lost'])

Intro = '''
┼┼┼┼┼┼┼┼┼┼┼┼▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼█▒▒░░░░░░░░░▒▒█┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼█░░█░░░░░█░░█┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼─▄▄──█░░░▀█▀░░░█──▄▄─┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼█░░█─▀▄░░░░░░░▄▀─█░░█┼┼┼┼┼┼┼┼
┼┼┼┼┼┼██░██░████░██░░░██░░░█████┼┼┼┼┼┼
┼┼┼┼┼┼██▄██░██▄▄░██░░░██░░░██░██┼┼┼┼┼┼
┼┼┼┼┼┼██▀██░██▀▀░██░░░██░░░██░██┼┼┼┼┼┼
┼┼┼┼┼┼██░██░████░████░████░█████┼┼┼┼┼┼'''
print(Intro)

Game_name = '''

██╗░░░░░███████╗████████╗░██████╗  ██████╗░██╗░░░░░░█████╗░██╗░░░██╗
██║░░░░░██╔════╝╚══██╔══╝██╔════╝  ██╔══██╗██║░░░░░██╔══██╗╚██╗░██╔╝
██║░░░░░█████╗░░░░░██║░░░╚█████╗░  ██████╔╝██║░░░░░███████║░╚████╔╝░
██║░░░░░██╔══╝░░░░░██║░░░░╚═══██╗  ██╔═══╝░██║░░░░░██╔══██║░░╚██╔╝░░
███████╗███████╗░░░██║░░░██████╔╝  ██║░░░░░███████╗██║░░██║░░░██║░░░
╚══════╝╚══════╝░░░╚═╝░░░╚═════╝░  ╚═╝░░░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░

░█▀▀█ █▀▀█ █▀▀ █─█ 　 ░█▀▀█ █▀▀█ █▀▀█ █▀▀ █▀▀█ 　 ░█▀▀▀█ █▀▀ ─▀─ █▀▀ █▀▀ █▀▀█ █▀▀█ █▀▀ █ 
░█▄▄▀ █──█ █── █▀▄ 　 ░█▄▄█ █▄▄█ █──█ █▀▀ █▄▄▀ 　 ─▀▀▀▄▄ █── ▀█▀ ▀▀█ ▀▀█ █──█ █▄▄▀ ▀▀█ ▀ 
░█─░█ ▀▀▀▀ ▀▀▀ ▀─▀ 　 ░█─── ▀──▀ █▀▀▀ ▀▀▀ ▀─▀▀ 　 ░█▄▄▄█ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀▀ ▀─▀▀ ▀▀▀ ▄
'''
print(Game_name)

def play_RPS():
  user_choice = input("Enter your hand choice (rock, paper, or scissors): ")
  computer_choice = options[random.randint(0,2)]
  decide_winner(user_choice, computer_choice)

play_RPS()
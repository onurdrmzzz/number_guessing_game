from art import logo
import random
from os import system

EASY_LEVEL_LIVES = 10
HARD_LEVEL_LIVES = 5

def check_answer(guess, number, lives):
  if guess > number:
    print("Too high.")
    return lives - 1
  elif guess < number:
    print("Too low.")
    return lives -1
  else:
    print(f"You got it! The answer was {number}")

def set_difficulty():
  """sets the difficulty of game by given answer.
  if the answer is 'easy' you will have 10 lives
  if the answer is 'hard' you will have 5 lives"""
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
  if difficulty == 'easy':
    return EASY_LEVEL_LIVES
  else:
    return HARD_LEVEL_LIVES


def play_game():
  lives = 0
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  number = random.randint(1,100)

  lives = set_difficulty()
  guess = 0
  while guess != number:
    print(f"You have {lives} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    lives = check_answer(guess, number, lives)
    if lives == 0:
      print(f"The correct answer was {number}")
      print("You've run out of guesses, you lose.")
      return
    elif guess != number:
      print("Guess again")
play_game()
while input("Type 'y' for play again, 'n' for quit: ") == 'y':
  system("clear")
  play_game()
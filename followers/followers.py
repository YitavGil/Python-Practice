from game_data import data
import random
from art import logo, vs
from replit import clear

print(logo)

def format_data(account):
  account_name = account["name"]
  account_desc = account['description']
  account_country = account["country"]
  return f"{account_name}, a {account_desc}, from {account_country}"

def check_answer(guess, first_account_followers, second_account_followers):
  if first_account_followers > second_account_followers:
    return guess == 'a'
  else:
    return guess == 'b'
    
score = 0
continue_game = True
second_account = random.choice(data)

while continue_game:
  first_account = second_account
  second_account = random.choice(data)
  
  if first_account == second_account:
    second_account = random.choice(data)
  
  print(f"Compare A: {format_data(first_account)}.")
  print(vs)
  print(f"Against B: {format_data(second_account)}.")
  
  guess = input('Who has more folloers? A or B: \n').lower()
  
  first_account_followers = first_account['follower_count']
  second_account_followers = second_account['follower_count']
  
  is_correct = check_answer(guess, first_account_followers,   second_account_followers)

  clear()
  print(logo)
  
  if is_correct:
    score += 1
    print(f"You're Correct! Your Score is {score}")
  else:
    continue_game = False
    print("Wrong Answer! Final Score is {score}")
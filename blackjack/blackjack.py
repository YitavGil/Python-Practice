import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_card():
  random_card = random.choice(cards)
  return random_card

user_cards = [deal_card(), deal_card()]
computer_cards = [deal_card(), deal_card()]
def init_play():
  def score(arr):
      sum=0
      n = len(arr)
      for i in range(n):
          sum = sum + arr[i]
      return sum
    
  user_score = score(user_cards)
  computer_score = score(computer_cards)

  

  def check_blackjack():
    if user_score == 21 and computer_score == 21:
      print("It's a draw!")
      return
    elif computer_score > 21 and  user_score <= 21:
      print("You Win!")
      return
    elif computer_score == 21 or user_score < computer_score:
      print("Computer wins!")
      return
    elif user_score == 21 or user_score > computer_score:
      print("You Win!")
      return
    elif user_score > 21:
      print("Computer wins!")
      return
   
    
   
    
      
  print(f"Your cards: {user_cards}. Yore score {user_score}")
  print(f"Computer first card is {computer_cards[0]}")

  in_game = True

  while in_game:
    hit = input("Do you wish to add another card? Choose 'y' for yes or 'n' to stay \n")
  
    if hit == 'y':
      user_cards.append(deal_card())
      user_score = score(user_cards)
      if computer_score < 16:
        computer_cards.append(deal_card())
        computer_score = score(computer_cards)
      print(f"Your cards: {user_cards}. Total score {user_score}")
    if hit == 'n':
       if computer_score < 16:
        computer_cards.append(deal_card())
        computer_score = score(computer_cards)
        check_blackjack()
        in_game = False 
       
      
  print(f"Your cards: {user_cards}. Total score {user_score}")
  print(f"Computer cards: {computer_cards}. Total score {computer_score}")

 

init_play()
  
gender = input("Are you a boy or are you a girl?\n")
lower_gender = gender.lower();
if lower_gender == "boy":
  print("You are not allow to lie in this game. Better luck next time!")

elif lower_gender == "girl": 
  place = input("Where should we look for captain? In the forest or at Guli's house?").lower()
if place == "forest":
  shit = input("You went to the forest and saw dogshit on the ground. Pick up the dogshit? Y or N").lower()
  shit = shit
  if shit == "Y":
    print("You can tell by sniffing the poop that it does not belong to Captain. Also it was poisonous. You died")
  else:
    print("You got lost in the woods and got eaten by a demagorgen. Game Over")
  if place == "guli": 
    print("You found Captain! You Win!")
else:
  print("So how are you existing? You Died.")



print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")


names = name1 + name2;
lowercase_names = names.lower();

t = lowercase_names.count("t");
r = lowercase_names.count("r");
u = lowercase_names.count("u");
e = lowercase_names.count("e");

true = t + r + u + e;

l = lowercase_names.count("l");
o = lowercase_names.count("o");
v = lowercase_names.count("v");
e = lowercase_names.count("e");

love = l + o + v + e;

true_love = str(true) + str(love);
final_score = int(true_love);

if final_score < 10 or final_score > 90:
    print(f"Your score is {final_score}, you go together like coke and mentos.")
elif final_score >= 40 and final_score <= 50:
    print(f"Your score is {final_score}, you are alright together.") 
else: 
    print(f"Your score is {final_score}.")
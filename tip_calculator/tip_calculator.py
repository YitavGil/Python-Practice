print("Welcome to the tip calculator!")

bill = int(input("What was the total bill?\n"))

tip = float(input("What precentage of tip would you liek to give?\n"))

number_of_persons = int(input('How many of you?\n'))

tip_prec = tip / 100

total_tip = tip_prec * bill

total_bill =  bill + total_tip

bill_per_person = total_bill / number_of_persons

final_price = round(bill_per_person, 2)


print(f"Each person should pay: {final_price}$")
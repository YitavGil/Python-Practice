#Add
def add(n1, n2):
  return n1 + n2
#Substract
def substract(n1, n2):
  return n1 - n2
#Multiply
def multiply(n1, n2):
  return n1 * n2
#Divide
def divide(n1, n2):
  return n1 / n2


operations = {
  "+": add,
  "-": substract,
  "*": multiply,
  "/": divide
}

num1 = int(input("What is the first number? "))
num2 = int(input("What is the second number? "))

for symbol in operations:
  print(symbol)

operation_symbol = input("Choose a symbol from the list \n")

calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} is equal to {answer}")
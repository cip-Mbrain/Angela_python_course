# Simple Cli Calculator

print("Welcome to simple cli calculator")

is_running = True

while is_running:
  print("starting calculator process")
  # processing calculations....
  user_operation = input("what operation would you like to perform?print['+','-','*','/','%'] ")

  # Get user numbers
  try: # Try to get user input if the're valid integers/floats, count
    num1 = float(int("Enter First Name: "))
    num2 = float(int("Enter Second Number: "))

  except: # we get an error when running it
    print("Failed, invalid numbers....")
  
  if user_operation == "+":
    # perform addition 
    print(f"the sum is: {num1 + num2}")
    # pass

  elif user_operation == "-":
    # perform subtraction 
    pass
  elif user_operation == "*":
    # perform multiplication
    pass
  elif user_operation == "/":
    # perform Division 
    pass
  elif user_operation == "%":
    # perform modulus
    pass
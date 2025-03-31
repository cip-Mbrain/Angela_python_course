# A python Program that perform: Arithmetic operations & accept user input.

print("select an operation to perform: ")
print("For Addition press 1 ")
print("For subtraction press 2 ")
print("For Multiplication press 3 ")
print("For Division Press 4 ")
print("For Modulus operation press 5")


operation = input()

if operation == "1":
  num1 = input("Enter First Number: ")
  num2 = input("Enter Second Number: ")
  print("The sum is: " + str(int(num1) + int(num2)))

elif operation == "2":
  num1 = input("Enter First Number: ")
  num2 = input("Enter Second Number: ")
  print("The difference is: " + str(int(num1) - int(num2)))

elif operation == "3":
  num1 = input("Enter First Number: ")
  num2 = input("Enter second Number: ")
  print("The product is: " + str(int(num1) * int(num2)))

elif operation == "4":
  num1 = input("Enter First Number: ")
  num2 = input ("Enter Second Number: ")
  print("The remainder is: " + str(int(num1) / int(num2)))

elif operation == "5":
  num1 = input("Enter First Number: ")
  num2 = input("Enter Second Number: ")
  print("The Modulus is: " + str(int(num1) % int(num2)))

else:
  print("Invalid Entry")
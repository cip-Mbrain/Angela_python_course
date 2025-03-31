""" operation = input()

if operation == "1":
  num1 = input("Enter First Number: ")
  num2 = input("Enter Second Number: ")
  print("The sum is: " + str(int(num1) + int(num2)))
else:
    print("invalid operation")
"""


# print(3 * 3 + 3 / 3 - 3)

height = int(input("Enter height in meters: "))
weight = int(input("Enter weight in kilograms: ")) 

BMI = weight / (height ** height)

print("Your body Mass Index is: ", BMI)
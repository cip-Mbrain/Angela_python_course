"""
if condition:
  do this
else:
  do this
"""

# temperature = int(input("Enter current temperature:\n"))

# if temperature > 20:
#   print("Do not wear a Coat!")
# else:
#   print("Wear a Coat!")


print("welcome to Mortgage Calculator")

Salary = int(input("what is your Salary in $ ? "))

if Salary >= 2000:
  print("Your are eligible for Mortgage!")
  credit_score = int(input("what is your credit score? "))
  if credit_score > 800:
    print("Interest rate is 4%")
  else:
    print("Interest rate is 6%")
else:
  print("sorry, you are not eligible for mortgage!")


"""
Write a program that takes an integer number from console and checks whether if a number is an odd or even.
"""
# any_num = int(input("Enter any number! "))

# if any_num % 2 ==0:
#   print("Even")
# else:
#   print("Odd")

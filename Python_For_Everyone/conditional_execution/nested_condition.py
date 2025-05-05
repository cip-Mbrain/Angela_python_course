"""
if condition:
  if  another condition:
    do this
  else:
    do this
else:
  do this
"""

x = 2
y = 3
if x == y:
  print('x and y are equal')
else:
  print('x and y are not equal')

  # Mortgage Cal
  """
  print("welcome to Mortgage Calculator!")
  salary =  int(input("what is your salary?\n"))

  if salary >= 2000:
    print("you are eligible for mortgage!")
    credit_score = int(input('enter your credit score!'))
    if credit_score >= 800:
      print('interest rate is 4%')
    else:
      print('interest rate is 6%')
  else:
    print("sorry, you are not eligible!")
  """


# Chained conditional
"""
if condition1:
  do A
elif condition2:
  do B
else:
  do this
"""

print("welcome to Mortgage Calculator!")
salary =  int(input("what is your salary?\n"))
rate = 0

if salary >= 2000:
    print("you are eligible for mortgage!")
    credit_score = int(input('enter your credit score!'))
    if credit_score >= 800:
      rate = 4
      print('interest rate is 4%')
    elif credit_score >750:
      rate = 6
      print('interest rate is 6%')
    else:
      rate = 8
      print('interest rate is 8%')
    disability = input('Do you have any disability? Y or N ')
    if disability == 'Y':
       rate -= 2
    print(f'Final Interest Rate: {rate}')
else:
    print("sorry, you are not eligible!")

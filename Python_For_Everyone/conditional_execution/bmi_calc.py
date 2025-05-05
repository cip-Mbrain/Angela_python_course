print("welcome to Body Mass Index (BMI) Calculator!")


height = float(input("Enter your height in m! "))
weight = int(input("Enter your weight in kg! "))

BMI = round(weight/height**2,2)

if BMI > 30:
  print(f'Your Body Mass Index is {BMI}, you are Obese!')
elif BMI > 25:
  print(f'Your Body Mass Index is {BMI}, you are Overweight!')
elif BMI >= 18.5:
  print(f'Your Body Mass Index is {BMI}, you are Normal!')
else:
  print(f'Your Body Mass Index is {BMI}, you are underweight!')
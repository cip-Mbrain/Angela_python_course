# try:
#   print(x)
# except:
#   print("print and exceptional error")

# print(3 * 3 + 3 / 3 -3)

# ######## BMI Calculator ############
# height = float(input("Enter height in meters: "))
# weight = int(input("Enter weight in kilograms: ")) 

# BMI = weight / (height ** 2)
# BMI = round(BMI, 1)

# print("Your body Mass Index is: ", BMI)

#create a program using maths and f-strings that tells us how many weeks we have left, if we live until 90 years old.

# life in a week calculator

# current_age = input('Enter your current age: ')
# years = 90 - int(current_age)
# week_left = years * 52

# print(f"you have {week_left} weeks left")


### Total bill calculator 
# welcome to a tip calculator

total_bill = input("What is the total bill?:\n ")
tip_num = input("how much tip would you like to give? 10, 12 or 15?\n")
bill_split = input("how many people to split the bills:\n")

if tip_num == 10:
  total_tip = (int(total_bill) * int(tip_num)) / int(bill_split)
  my_total_tip = float(total_tip)
print(f"Each people should pay: {my_total_tip}")
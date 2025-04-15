"""
write a program to prompt user for hours and rate per hour to compute gross pay. You need to take into account that the result has exactly two digits after the decimal place.
"""

hours = input("Enter Hours: ")
rate = input("Enter Rate: ")

gross_pay = int(hours) * float(rate)
print(f"gross pay is: {round(gross_pay, 2)}")
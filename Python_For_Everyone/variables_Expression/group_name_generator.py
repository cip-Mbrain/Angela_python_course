"""
- create a greeting for your program.
- Ask the user for their favorite color.
- Ask the user for their favorite animal.
- combine the name of their favorite animal and show their group name.
"""

print("Helooo! What's good!😊")
fav_color = input("do you mind telling me your favorite color?\n")
fav_animal = input("do you also mind telling me your favorite animal too!\n")
group_name = (f"{fav_color}{fav_animal}")

print(f"your group name is: {group_name}")
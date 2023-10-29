'''
CHALLENGE: ADD MORE QUESTIONS
# ./images_breadboard/01_breadboard.png

1. Can you change the program to ask more than one question, 
storing the answers in multiple variables? 
2. Can you make a program which uses conditionals and comparison operators 
to print whether a number typed in by the user is higher or lower than 5?
'''

# 1
user_name = input("What is your name? ")
user_lastname = input("What is your last name? ")
if user_name == "Clark" and user_lastname == "Kent":
    print("You are Superman!")
else:
    print("You are not Superman!")

# 2
number = int(input("Give me a number: "))
if number > 5:
    print("Your number is greater than 5")
elif number < 5:
    print("Your number is less than 5")
else:
    print("Your number is equal to 5")

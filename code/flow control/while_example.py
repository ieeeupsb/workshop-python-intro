#!/usr/bin/env python3

number = 123
choice = "yes"

guess = int(input("Your guess? "))

# Parantheses are optional
# The tested condition works the same as in the If structure
while (number != guess) and (choice == "yes"):
    choice = input("You didn't get it right, would you like to try again? (yes/no) ")
    guess = int(input("Your guess? "))

if choice == "yes":
    print("You got it right!!")

else:
    print("Better luck next time.")


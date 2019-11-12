#!/usr/bin/env python3

number = 123

guess = int(input("Your guess (tries left = 3)? "))
if number == guess:
    print("You got it right with 1 try!!")

else:
    guess = int(input("Your guess (tries left = 2)? "))
    if number == guess:
        print("You got it right with 2 tries!!")

    else:
        guess = int(input("Your guess (tries left = 1)? "))
        if number == guess:
            print("You got it right with 3 tries!!")

        else:
            print("You didn't manage to guess the number")


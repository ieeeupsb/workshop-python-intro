#!/usr/bin/env python3

number = 123

for i in range(3):
    print(3 - i, "guess(es) left")
    guess = int(input("Your guess? "))

    if number == guess:
        print("You got it right!!")
        # We use the break keyword to end a loop early
        break

    else:
        print("Better luck next time.")
        # We use the continue keyword to go straight to the next loop iteration
        # (We just wanted to show it in this case)
        continue

if number != guess:
    print("You didn't manage to guess the number.")


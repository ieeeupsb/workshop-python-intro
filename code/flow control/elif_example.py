#!/usr/bin/env python3

day = int(input("Weekday? (1-7) "))

if (day == 1):  # Parentheses are optional
    print("Sunday")

elif day == 2:
    print("Monday")

elif day == 3:
    print("Tuesday")

elif day == 4:
    print("Wednesday")

elif day == 5:
    print("Thursday")

elif day == 6:
    print("Friday")

elif day == 7:
    print("Saturday")

else:
    print("Number out of the expected range (1-7)")


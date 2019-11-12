#!/usr/bin/env python3

# Examples a dictionary declaration that associates names with age
# Equivalent to ages = dict([[Carlos, 12], [Vilas, 19], [Tiago, 5]])
# Or, since the keys are all simple strings, ages = dict(Carlos=12, Vilas=19, Tiago=5)
ages = {"Carlos": 12, "Vilas": 19, "Tiago": 5}
print("Our dict:", ages)

# Print a single element
print("Tiago's age:", ages["Tiago"])

# We can add any key:value pair to dictionary at any time
ages[432.5] = "oops"
print("Our dict:", ages)

# The list() funtion will return a list of the keys in the dictionary in insertion order
print("Our list:", list(ages))

# A dictionary is also an iterable (will be discussed in the iterable chapter)
print("Carlos" in ages)

# The next commented line results in an order because we can't access non-existant keys
# print(ages["123"])

# If we store a key that's already in use, the previous value of that key is dropped
ages["Carlos"] = 11
print("Our dict:", ages)

# We can use the del keyword with dictionaries
del ages["Vilas"]
print("Our dict:", ages)

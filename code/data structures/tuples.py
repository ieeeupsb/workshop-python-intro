#!/usr/bin/env python3

# The paratheses are not mandatory in most declaratios but we recommend their use either way
atuple = (1, 2, 'hey', 4.2, 0)

# Print the whole tuple
print("Our tuple:", atuple)

# Elements are indexed
print("1st element of out tuple", atuple[0])

# Nested tuples
btuple = ("a", atuple, 96, atuple)
print("Our nested tuple:", btuple)

# Since tuples are immutable, this next commented line results in an error
# atuple[1] = 3

# But they can contain mutable objects
alist = [1, 2, 3]
ctuple = (alist, 4, 5)
print("Our ctuple:", ctuple)

ctuple[0][0] = 3
print("Our ctuple:", ctuple)


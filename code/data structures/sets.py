#!/usr/bin/env python3

# Declare a set
aset = {"yum", "sweet", "potato", "yum"}
# Equivalent to aset = set(['yum', 'sweet', 'potato'])
print("Our set:", aset)

# Check membership
# This in keyword will be discussed in detail in the chapter about iterables
# For now, we just need to know that it checks if "yum" is equal to at least 1 of the elements of aset
print("yum" in aset)
print("Iargo" in aset)

# Crating sets from an iterable (string)
x = set("comparable")
y = set("complementary")

# Unique letters
print("Unique letters in x:", x)
print("Unique letters in y:", y)

# Difference
print("Letters in x but nor in y:", x - y)

# Union (Or)
print("Letters in x, y or both:", x | y)

# Intersection (And)
print("Letter in both x and y:", x & y)

# Symmetric difference (Xor)
print("Letters in x or y but not in both:", x ^ y)


#!/usr/bin/env python3

alist = [1, 2, 3, 4, 5, 6, 7, 8]
print("Our list:", alist)

# Remove 1 element
del alist[1]
print("Our list:", alist)

# Remove a slice
del alist[0:3]
print("Our list:", alist)

# Remove all elements (same as alist.clear())
del alist[:]
print("Our list:", alist)


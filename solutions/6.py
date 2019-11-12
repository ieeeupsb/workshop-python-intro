# a)
num = int(input())

alist = []
for i in range(num):
    read = input().split()
    #  Appends to the list a tuple with the word and the float: (Joao, 21.3)
    alist.append( (read[0], float(read[1])) )

print("a)", alist[-1])

# b)
def sorting_key(t):  # Receives an element and return something for the function to return
    return t[1]

# Save the list sorted using our sorting_key() and in reverse order (descending)
sorted_list = sorted(alist, key=sorting_key, reverse=True)

print("b)", sorted_list[-1])

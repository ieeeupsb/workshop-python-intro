names = input().split()

name = ""
if len(names) == 1:  # If there is only one word, our solution is done
    name = names[0]
else:  # There were two or more words
    name = names[0]

    #  For every word in names, from index 1 to the penultimate one
    for i in range(1, len(names) - 1):  # If len(names) is 2, this loop won't run
        if names[i].capitalize() == names[i]:  # If the word is capitalized, to ignore "da", "de", etc
            name += " " + names[i][0] + "."  # Add the first letter (already capitalized)

    name += " " + names[-1] # Add the last name

print(name)

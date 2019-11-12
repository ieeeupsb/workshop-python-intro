# create a set from a given string's characters
# (after converting them to lower-case if necessary)
given_word = set(input().lower())

# for each word in the given sentence
for word in input().split():
  if given_word == set(word.lower()):
    print(word)

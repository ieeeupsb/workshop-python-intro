template: slide_section
name: comprehensions_and_generators
# Comprehensions and Generators

---

template: slide_normal
## List Comprehensions

List comprehensions can be used to create a list from another iterator. You can apply **functions** or even **lambda functions** inside them to filter what you want.

For example, to create a new list with all positive numbers from a previous list:
```py
list1 = [12, 5, -4, 6, -18, 0, 4, 2]
list2 = [n for n in list1 if n > 0]
print(list2)

# [12, 5, 6, 4, 2]
```

---

## List Comprehensions

If you wanted to know the length of every word in a sentence:
```py
sentence = "List comprehensions rule"
n_words = [len(word) for word in sentence.split()]
print(n_words)

# [4, 14, 4]
```

Iterating through other structures is also viable, for example, extrating from a dictionary only the values whose key are an even number:
```py
adict = {1: "a", 2: "b", 3: "c", 4: "d"}
alist = [adict[key] for key in adict if key % 2 == 0]
print(alist)

# ['b', 'd']
```

---

## Generators

Generators are the next step once you've learned list comprehensions, as the following code has the exact same meaning:

```py
[item for item in iterable]
list(item for item in iterable) # Notice the cast to list
```

### Why Generators?

Just like *iterators*, generators are also ***lazy***, as they will *generate* the next element when asked to, instead of storing them all in memory.  
Their major advantage in comparison to iterators, is that the code required to create a generator is **significantly** more reduced and readable.

To create a generator, you can simply create a function, but instead of using a ***return*** statement, you call the ***yield*** statement.  

---

```py
def list_range(start, end, step=1):
    i, result = start, []
    while (i < end):
        result += i
        i += step
    return result

def generator_range(start, end, step=1):
    i = start
    while (i < end):
        yield i
        i += step

print(list_range(0, 10, 2))
print(generator_range(0, 10, 2))
print(list(generator_range(0, 10, 2)))

# [0, 2, 4, 6, 8]
# <generator object false_range at 0x012F0CF0>
# [0, 2, 4, 6, 8]
```

???

For an example of this behaviour, we implemented a minimalist version of the `range()` object.
Although the code is very similar, the performance impact is very different.  
As you can see, calling our ***yield*** function returned us a ***generator object***, but casting it to list returned the same as our function using ***return***
Now let's compare a call of these two approaches with a really large argument, as such, `range(0, 1000000)`.  
The function returning a list would have to allocate in memory a list with a whopping million elements... this is not prefereable.  
The generator function (*yield*) only returns one number at a time, therefore not filling system's memory with a million long list.

---

### Inline Generators

As you saw from the example comparing a list comprehensions to a generator, it can be written in a ***compact*** and ***lambda like*** format.

Just like in that example, where we used an iterable, **generators can use other generators** in their definition, which still maintains the generator lazy, keeping their advantages.

```py
square_generator = (n**2 for n in range(1, 10000000000))

from itertools import takewhile
list_squares = takewhile(lambda square : square <= 25, square_generator)

print(list(list_squares))

# [1, 4, 9, 16, 25]
```

***Note:*** Inline generators should always be inside parenthesis.

???

Actual infinite generator (in the representable integer range)

```py
def infinite_generator():
    a = 0
    while (True):
        yield a
        a += 1
```

---

### Conditions in Generators

Conditions can be incorporated in one of two ways:
- In the end, to indicate which elements to select:  
Selecting all positive elements
```py
[n for n in alist if n > 0]  
```
- In the beginning, to indicate how to return the selected element:  
Halving all even numbers and squaring all odd numbers
```py
[n / 2 if n % 2 == 0 else n**2 for n in alist]
```

---

### Conditions in Generators

For example, this next snippet combines both to halve even positive numbers and square positive odd numbers:

```py
alist = [-1, 2, -7, 3, 7, -9, -200, 20]
print(list( [n / 2 if n % 2 == 0 else n**2 for n in alist] ))

# [6, 9, 49, 10]
```

You can also chain multiple if else statements in the beginning, to create more complex generators:

```py
alist = [-4, -2, 0, 2, 4]
[1 if n < 0 else 2 if n < 4 else 3 for n in alist]

# [1, 1, 2, 2, 3]
```

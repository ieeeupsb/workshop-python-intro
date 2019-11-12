template: slide_section
name: iteration
# Iteration

---

template: slide_normal
## 'Iteration'?

When you previously used a `for` cycle, you would write `for i in range(5)` to ***iterate*** the numbers 0 through 4. This is because the `in` keyword allows you to cycle through all elements of a data structure. For example, if you cast the previous range object, you would obtain the following list:

```python
print(list(range(0, 5)))
# [0, 1, 2, 3, 4]
```

### Definition:

- **Iterable**: An object you can loop over.

- **Iterator**: An object that represents a **data stream** that handles **iterating** over an iterable.

---

## The 'in' keyword

This allows you to iterate through any object that is classified as an `Iterable`, such as **lists**, **tuples**, **dictionaries**, **sets**, **strings** and **file objects** if used, for example, in a for loop. You can even iterate through an Iterable object of another iterator:

```python
alist = ["One", "Two"]
for item in alist:
    for letter in item:
        print(letter, end=' ')
    print()
 
# O n e
# T w o
```

As such, you can see that Python's `for` loop behaves more like a `for each` rather than a traditional for loop. 

---

## The 'in' keyword

You can check for the **existance** of an element in a data structure:

```python
# Checking for elements in a dictionary
adict = {"Tiago": 19, "Costa": 18, "Lucas": 21}
print("Is Lucas in adict:", "Lucas" in adict) # True
print("Is Fábio in adict:", "Fábio" in adict) # False
print("Is there anyone 21 years old:", 21 in adict.values()) # True
print("Is there anyone 39 years old:", 39 in adict.values()) # False
```

This method of iteration even works with other modules data structures, such as pandas' Dataframes or numpy's Arrays.

---

## Iterators are lazy

A great advantage of iterators is they only do their job when it's actually needed. This is, if you would need to access only 3 out of 500 elementes of, for example, a list, python's iterable would only load the first 3 instead of loading all 500 elements automatically.

 This means that you could, theoretically, deal with *infinitely* large data structures because the iterable would only care about an element at a time, saving both **memory** and **CPU time**.

---

## Iterators are everywhere!

There are a lot of handy functions in Python whose implementaion relies heavily on iteration, from which some of the more noticeable are:

- `reversed()`:  
Iterates through an iterable from the end to the beginning

```python
alist = [1, 2, 3]
for item in reversed(alist):
    print(item)

# 3
# 2
# 1
```

---

## Iterators are Everywhere!

- `enumerate()`:  
Enumerates all elements of an iterable as such:  
(0, *first item*); (1, *second item*); (2, *third item*)

```python
alist = ["A", "B", "C"]
for item in enumerate(alist):
    print(item)

# (0, "A")
# (1, "B")
# (2, "C")
```

---

## Iterators are Everywhere!

- `zip()`:  
Allows you to "compress" two iterables into a tuple structure, until the end of the shortest iterable.

```python
list1 = ["Hello", "there", "General", "Kenobi"]
list2 = [1, 2]
zipped_tuple = zip(list1, list2)
for item in zipped_tuple:
    print(item)

# ('Hello', 1)
# ('there', 2)
```

---

## Standard Itertools Module

This [module](https://docs.python.org/3/library/itertools.html) brings a wide array of tools to work with iteration, we advise you to give it a read in your spare time.  
Some noteworthy methods:

- `itertools.takewhile(predicate, iterable)`:  
Takes elements from an iterable (or generator) while `predicate` is true.  
Argument `predicate` can be a simple comparison or a lambda function, for example.

- `itertools.chain(*iterables)`  
Takes various iterable objects and returns an iterator that ties all objects together (given two lists, it would return an iterator that once list1 is over, iteratres through list2).

---

## Under the Hood

This topic may be confusing for begginners of the language, but can provide an invaluable look into how Python magically handles iteration and for loops for you.

Every `Iterable` object can be called using the built-in function `iter()` to return an `iterator object`, which representes a **stream of data**.

```python
alist = [1, 2, 3, 4]
adict = {1: "a", 2: "b", 3: "c", 4: "d"}
astring = "Hello World!"

print(iter(alist))    # <list_iterator object at 0x02C02270>
print(iter(adict))    # <dict_keyiterator object at 0x02C2B8D0>
print(iter(astring))  # <str_iterator object at 0x02C02970>
```
***Note:*** 0x02C02270 represents the memory address where the list_iterator object was stored during our test run.

---

## Under the Hood

You can advance through the data stream of an iterator by calling the built-in function `next()`, which returns **successive items** from the **data stream**.

When all the data is read from the stream, the iterator is gone. If you were to call the function `next()` again, python would raise a `StopIteration` exception (exceptions are not covered in this workshop).

---

## Under the Hood

Here's how Python ***iterates through any iterable*** under the hood (as such it cannot use a for loop, because this is its own implementaion):

```python
def iterate(any_iterable, function_call):
    iterator = iter(any_iterable)
    continue_iterating = True
    while continue_iterating:
        try:
            item = next(iterator)
        except StopIteration:
            continue_iterating = False
        else:
            function_call(item)

alist = ["a", "b", "c", "d"]
iterate(alist, print)
```

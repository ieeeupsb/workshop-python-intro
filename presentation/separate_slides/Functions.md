template: slide_section
name: functions
# Functions

---

template: slide_normal
## Functions - Introduction 
Functions are essential in keeping code efficient and readable.
To define a function we declare:

+ The **Header** - Keyword ***def*** followed by the
name of the function and the ***parameters*** that it may
receive inside parenthesis.

+ The **Body** - The code of the function that produces intended result.
When the result is achieved the keyword **return**(*value*)
exits the function with a given value so that may be used on the function call.

+ Note: If the function reaches its end without reaching a return it will return ***None***.

---

## Functinos - Introduction

Big projects often have innumerous functions and it is often very difficult
to keep track of every single one of them.
In order to prevent confusion and make the code more readable functions
often have a ***docstring***: a string at the start of the ***function body***
, surrounded by """, that describes what is the ***input*** of the function, what it does
and its ***output***.

```python
def my_function(my_parameters):
    """docstring here"""
    # Function defined here
    return result
```

---

## Functions - Introduction

When a function is defined we can **call** it.
Its return value can then be used in expressions or attributions.

````python
var=my_function(my_parameters)
if(my_function(my_parameters))
````

### Example ###

(Adapted from Big C++)

Suppose that we are given a plethora of interest rates (in percentage) and we
want to compute the value of a savings account based on those interests.
The result must be the final balance of the account after 10 years, the initial balance
is $1000.

The balance can be calculated using this formula:

** b=1000 * (1+ (p/100)^10) **

---

## Functions - Example

So, firstly we need to define the ***header*** of the function.
The only parameter that we are going to use is the interest rate.

```python
def final_balance(interest_rate):
```

Secondly we need to compute the final balance into a variable.

```python
result = 1000 * (1 + p / 100) ** (10)
```

---

## Functions - Example

Lastly, having achieved our goal, we return the result and finish writing the function.

```python
def final_balance(interest_rate):
    result = 1000 * (1 + p / 100) ** (10)
    return result
```

We can then use the function to produce and compare different results using distinct
interest rates.

```python
print("${:.2f}".format(final_balance(5))) # 1628.89 $
print("${:.2f}".format(final_balance(10))) # 2593.74 $
print("${:.2f}".format(final_balance(25))) # 9313.23 $
```

---

## Functions - Example

But let's suppose that you wanted to change the initial deposit of the account
to 1500 and wanted to see the value of the deposit after 20 years.
The solution is to add the starting balance and the number of years as a new parameters
to the function definition.

```python
def final_balance(interest_rate, years=10, initial_value=1000):
    result = initial_value * (1 + p / 100) ** years
    return result
```

Notice how the parameters are assigned to a value in the function header.
This means that if the function is called without specifing the value of
years or initial_value they will have a value equal to their  ***default values***.

```python
print("{:.2f}".format(final_balance(5))) # 1628.89
print("{:.2f}".format(final_balance(5, 20, 1500))) # 3979.95
```

???
Falar como alguns metodos da string já têm default vals (como o [:])

---

## Functions - Important Tips

Some very important notes to keep in mind:

+ When you keep repeating the same code over and over again it is
    usually a sign that you could turn that code into a function.
  Doing this will drastically improve the readability of your code.

+ Try to name your functions in a way that is self describing. This also
    improves code readability.

 ```python
    interest_rate=5                         # What is more readable?
    print(final_balance(interest_rate))
    print(calc(interest_rate))
    print(1000*(1+interest_rate/100)**(10))
 ```

---

## Functions - Scope ##

Variables can be in one of three places in which Python will look for,
these places are called *scopes* (or *namespaces*):

1. **Local scope** - Variables that are defined inside of functions.
1. **Global scope** - Variables that are defined at the global level. (can be accessed everywhere)
1. **Built-in scope** - Variables that are predefined in Python.

Whenever Python looks for a variable, it will always look for it in the
previous order. To use a global variable inside a function call, use the global keyword.

**Note:** After you invoke a function and its execution ends, all the local variables
created by it are deleted by the garbage collector.

---

### Examples

```python
x=5
y=2
def func():
    x=7
    print("x:", x) # prints 7
    global y
    print("y:", y) # prints 2
    y = 4
    print("y:", y) # prints 4

func()
print("x:", x) # prints 5
print("y:", y) # prints 4
```

Although we may use global variables in this workshop, you should avoid using them
whenever possible, as they diminish readability and lead to increased memory
usage.

---

## Lambda Functions ##

Lambda functions are anonymous expressions used to create small functions on-the-fly.
Invoke them by using the keyword lambda, followed by its argument,
a colon and the function definition.

```python
print((lambda p: 1000 * (1 + p / 100) ** (10)) (5)) #  1628.89
```

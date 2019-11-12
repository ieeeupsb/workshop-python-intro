template: slide_section
name: flow_control
# Flow Control

---

template: slide_normal
## Flow Control Tools
  
Up until now, all the code we've written was executed in **top-down order**. Sometimes it's necessary to change the way a program flows, for example, making a program that can decide weather or not to run a piece of code.

In Python, we have 3 flow control structures:  
1. [If statement](#if)  
1. [For loop](#for)  
1. [While loop](#while)  

---
name: if
## If

- **If** statements are **Python's** decision making structure.
- The decisions are made by checking the **truth value** of a condition.
- The blocks of code that are inside an **If** structure are only run if the condition is **True**.

Usually **If** structures are followed by an optional **Else** clause. The code inside the **Else** clause is only run if the condition in its corresponding **If** structure was **False**.

```python
a = 1
b = 2
if a == b:
    print("Equal")
elif a > b:
    print("a > b")
else: print("a < b")

```
---

#### If Cheat Table

| Operator | Meaning |
|:-:|:-|
| == | equality test |
| != | inequality test |
| > | greater than |
| < | less than |
| >= | greater than or equal to |
| <= | less than or equal to |
| and | logical and |
| or | logical or |
| not | logical not |
| True | logical true |
| False | logical false |


---

name: for
## For

The **For** loop is one of the two loops available in **Python**. We use this loop when we want to repeat a code block a known, finite, number of times.  
The **For** loop makes heavy use of the **range** object.

- A **range** is defined as follows: `range(start, [end, [step]])`.
- The interval is closed on the left side and open on the right side [start, end).
- The **step** parameter is optional and by default is 1.
- We can also create **range** objects with only 1 parameter: `range(3)`. These are the same as: `range(0, 3)`.

---

## For

The **For** loop can be followed by an **Else** clause. The block of code inside the **Else** clause is executed once after the **For** loop is over, unless we reach a **break** keyword inside the **For** loop.

Another structure of a **For** loop will be presented in [Iteration](#iteration).

### Example

```python
for i in range(3):
    print(i)
```

---

name: while
## While

**While** is the second and last available loop in **Python**. We use this loop when we want to repeat a code for an unknown amount of times (while a condition is **True**).

### Example
```python
a, b = 0, 5
while(a < b):
    print(a)
    a += 1
```
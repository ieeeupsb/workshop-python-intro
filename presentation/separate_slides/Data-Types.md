template: slide_section
name: data_types
# Data Types

---

template: slide_normal
## Variables and Data Types - Concept

***Variables*** and ***data types*** are the building blocks of all programs.

In order to better manipulate them, two concepts must be taken into consideration:

+ **State**: The current *status* of a data type.
    True or False; 1, 2, 1000; 1.4, 1.2, etc ...
+ **Mutation**: The process of altering the *state* of a data type.

Then, we can define:

+ **Data type**: A way in which data can be arranged.
    When creating a new data type a "copy" of it is created
    (an ***object***) in memory.
     Some are ***mutable*** (are sucseptible to change) where as others are ***immutable***.
     Ex: boolean, integer, string, etc ...

---

## Numbers

In general there are two types of representing numbers: ***integers*** and ***floats***.
You can create these variables easily in the interpreter:

```python
a=3   # integer
b=4.0 # float
```

|*Operation* | *Symbol* |
|:-|:-:|
|Addition            |          + |
|Subtraction         |          - |
|Multiplication      |          * |
|Division            |          / |
|Integer Division    |          // |
|Remainder           |          % |
|Power               |          ** |

???

Mostrar q 2e5 funciona
Mostrar q += e amigos existem

---

## Numbers

Some notes to take into account:

+ When dividing two numbers the result is a *float*.
+ When using operators between *integers* the result is an *integer*
    (except for division).
+ When using operators between *floats* the result is a *float*.
+ When using operators between *floats* and integers the result is a *float*.

  ```python
  print(3.0 * 2) # 6.0
  print(1 / 1) # 1.0
  ```

+ Python takes operation priority into account
   (parenthesis are the highest priority, then \*\*, etc...)

---

## Booleans

The ***boolean*** type is used to store values for ***True*** or ***False***.
Some variables can be converted to boolean by using:

```python
bool("") # False
bool("qwerty") # True
```

In general, an object that is considered to be empty (Ex: "", [  ], 0)
returns false, while an object that contains anything returns true (Ex: 5, 0.1).

True          | False
--------------|----------------
True          | False
"0"           | ""
[1, 2, "asd"] | [  ]
{4}           | {}
4             | 0
0.01          | 0.0

---

## Strings

The ***string*** data type stores text or a sequence of characters. We can define
them by surrounding text by ', " or """.

```python
a="this is a string"
```

To define a quote inside a string, so as to not confuse the python interpreter,
a escape sequence \" can be used.

```python
print("\"This is a quote\"")
```

---

## Escape Sequences

| **Output** | **Escape Sequence** |
| :- | :-: |
| Backslash | \\\\ |
| Newline / Paragraph | \\n |
| Double quote | \\" |
| Single quote | \\' |
| Unicode character | \\Uxxxx |
| Octal character | \\o87 |
| Hexadecimal character | \\xFA |

---

## String Indexing

By convention, the indexing of the characters in a string starts at 0.  

<p align="center">
    <img src="assets/slicing.png" alt="List Indexing (Bird, Steven, Edward Loper and Ewan Klein (2009), Natural Language Processing with Python. O’Reilly Media Inc.)" width="auto" height="200px"/>
</p>

---

## String Indexing

You can use indexing to:

+ Access the nth character of a string using __**str[n]**__.
+ Retrieve the last character of a string by __**str[-1]**__.
+ Access the nth last character with __**str[-n]**__.
+ Inverse the string with __**str[::-1]**__.

```python
a="IEEE"
print(a[0])   # "I"
print(a[-2]   # "E")
print(a[::-1] # EEEI)
```

---

## String Slicing

Indexing also allows string slicing. Slicing returns a substring of the string that we are slicing.

To specify the starting and ending indexes of the substring we use the following syntax: ***str[start:end]***.

```python
my_str="A beautiful morning"
my_substr=my_str[2:11]
print(my_substr) # beautiful
print("A beautiful morning"[12:]) # morning
print("A beautiful morning"[:12]) # A beautiful
```

+ If we ommit the starting index, the substring will be made from the beggining of the original string.
+ If we ommit the ending index, the substring will be made to the end of the original string.
???

Explain a inclusidade: 1o int é inclusivo, 2o é exclusivo.
O que acham que my_str[:] vai dar retreive

---

## String Methods

One particularity of strings is that they are ***immutable***,
and as such, cannot be changed. 

```python
a="str"
a[0]="t" # ILLEGAL! - str object does not support assignment
```

As a consequence, when trying to change the content of a
string we are forced to create a new one.

Therefore, all methods of the str class will always return a new string
and will **never** modify an existing one.

---

## String Methods

To call a string method we use the syntax: **string_variable**.***method***(*args*).

Some methods may require a number of arguments (which may be mandatory, depending on the method).

We won't cover all string methods due to time constraints, but keep in mind that the command
***help(__method__)*** or the [***official documentation***](https://docs.python.org/3/index.html)
both have extensive information on how to use all methods of the library.

The following list contains the most common string methods.

+ ***str.capitalize()*** - Makes first character upper case and the rest lower.

    ```python
    "ferNANdo caRVALho".capitalize() # Fernando carvalho
    ```

???

Vamos dar so um cheirinho de todos os metodos.
Explicar [:] de como era um arg optional.

---

## String Methods

+ ***str.count(sub[, start[, end]])*** - Return the number of non-overlapping
  occurrences of substring sub in the range [start, end].
  Optional arguments start and end are interpreted as in slice notation.

  ```python
  "ananas".count("an") # 2
  "ananas".count("an", 2) # 1
  ```

+ ***str.join(iter)*** - Concatenates str between every member of iter.

    ```python
    ", ".join("123") # "1, 2, 3"
    "_".join(["1", "2", "3"]) # 1_2_3
    ```

???

The last example is a list, which we will discuss later.

---

## String Methods

+ ***str.find(sub[, start[, end]])*** - Return the lowest index in the string where
    substring sub is found within the slice s[start:end]. Optional arguments start
    and end are interpreted as in slice notation. Return -1 if sub is not found.

    ```python
    "Dory_Nemo".find("Nemo") # 5
    ```

    **Note:** Don't use when trying to check if sub is a substring. Use the in operator
    (much more efficient)

    ```python
    "Nemo" in "Dory_Nemo" # True
    ```

+ ***str.lower()*** - Return a copy of the string with all the cased characters
    converted to lowercase.

    ```python
    "FeRNaNDo".lower() # "fernando"
    ```

---

## String Methods

+ ***str.replace(old, new[, count])*** - Return a copy of the string with all
    occurrences of substring old replaced by new. If the optional argument
    count is given, only the first count occurrences are replaced.

    ```python
    "I3E".replace("3", "EE") # IEEE
    "IEEE".replace("E", "_", 2) # I__E
    ```

+ ***str.split()*** - Return a **list** of the words in the string, using sep
    as the delimiter string. If maxsplit is given, at most maxsplit splits are done

    ```python
    "1, 2, 3".split(", ") # ["1", "2", "3"]
    "1,2,3".split(',', maxsplit=1) # ["1", "2,3"]
    ```

---

## Format Method

The ***format*** formats strings that are identified with the {} (braces) placeholder.
All placeholders will be replaced by the arguments given in the .format call.

The type of formatting can be specified in the arguments of the method.

```python
name="Fernando"
print("My name is {}".format(name)) # "My name is Fernando"
```

It is possible to specify the order in which the strings are substitute
by inserting an integer into the braces.

```python
print("1st:{3};2nd:{0};3rd:{1};4th:{2}".format("Second", "Third", "Forth", "First"))
# 1st:First;2nd:Second;3rd:Third;4th:Forth
```

---

## Format Method

There is a whole portefolio of different options that can be used with format.

```python
print("{:>30}".format("IEEE")) # Right with 30 width
#                IEEE

print("{:b}\n{:x}\n{:X}\n".format(8, 13, 13)) # Binary or Hexa notation
# 1000
# d
# D
print("{:.3e}\n{:.2g}\n{:%}".format(3.14, 1.26, 0.666)) # Exponent
# 3.140e00
# 1.3
# 66.600000%
```

Make sure to check the wiki for a brief summary or the official docs for a more extensive explanation.

???
Time constrains, xau nao vamos falar mt
Dizer o que o width representa quando usamos o format (linha onde o fim de todas as strings vai estar)

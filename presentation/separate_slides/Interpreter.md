template: slide_section
name: interpreter

# Interpreter

---

template: slide_normal
## REPL
The **REPL** (Read Evaluate Print Loop) runs on a command line and can be called through `python`.  
*Warning:* As python is a language where tabs have meaning, extra spaces or tabs before the input will result in an error.
```py
Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> print("Hello World")
Hello World
```

To exit the REPL type **quit()**. Certain OS specific keybinds also work, in windows Ctrl+Z and in Unix Ctrl+D. 

???

REPL: It loops while awaiting for an input, interpreting it and printing its result.  
Multilne: New line and keep writing (symbol changes from `>>>` to `...`).  
Comments:'#'.  
Brincar com o REPL.  

---

## Useful REPL Functions:

## dir

This funcion returns the attributes of an object.  
For example, to know all the attributes of a string:

```py
>>> dir("anyString")  # or dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
```

This function can help you get all the attributes when your IDE doesn't show it or when you don't have access to the internet.

---

## help

Documentation built-in python itself!
Calling `help()` without arguments will bring up an interactive menu (*tip:* experiment calling it from the REPL) 

Calling `help()` with an argument will give that argument's documentation:  
- With a **variable** in the argument it will assume its datatype as the argument; 
- With `int`, `str` or `float`, it will yield information about the data types;  
- With a **class**, **function** or **method**, it will yield even more information (*see next slide*).  

**Note**: In windows, sometimes too much information will show up, if you want to stop the help function in the REPL simply type Ctrl+C to stop it.  
---

## Calling help() with a method

```py
>>> help(str.split)
Help on method_descriptor:

split(self, /, sep=None, maxsplit=-1)
    Return a list of the words in the string, using sep as the delimiter string.

    sep
      The delimiter according which to split the string.
      None (the default value) means split according to any whitespace,
      and discard empty strings from the result.
    maxsplit
      Maximum number of splits to do.
      -1 (the default value) means no limit.
```


template: slide_section
name: variables
# Variables

---

template: slide_normal
## Variables as Objects

In Python all variables point to objects with 3 parts: id, value and type. 
 
As variables are light, reusing them doesn't really improve memory usage. We recommend you keep your variable types consistent to avoid confusing code.

<p align="center">
    <img src="assets/variables-objects.png" alt="Relationship between variables and objects" width="auto" height="250px">
</p>

---

## Garbage Collection

The explanation for the reassigned objects being deleted is that every object has a reference count, the number of times it is referenced. This number is always positive and once it reaches zero, the garbage collector is called to free the memory used by that object, efectively making it disappear. If you ever wish to know this reference count use the following code:

```py
>>> import sys
>>> name = "IEEE"
>>> sys.getrefcount(name)
2
```

Please note that, as the documentation says, the reference count returned is generally one higher than you might expect, because it includes the (temporary) reference as an argument to getrefcount().

???
IMUTÁVEL:
Ao alterar um objeto, ele ficará a apontar para um novo objeto ou para outro já existente
MUTÁVEL:
Altera o objeto em si
---

## Variable Naming

Python enforces that a ***variable should never have the name of a keyword or start with numbers***, doing so will result in a syntax error:
```py
>>> if = "if"
  File "<stdin>", line 1
    if = "if"
       ^
SyntaxError: invalid syntax
```

**Note**: For a list of all keywords that will produce a syntax error:
```py
>>> import keyword
>>> print(keyword.kwlist)
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```

---

## Variable Naming

Other naming conventions are not mandatory, but are considered good practice:
- Separate words in variable names either with underscores (big_variable) or with capital letters (bigVariable). Use only one of these throughout your code.
- Don't override built-ins.

Although built-in words could be used for a variable, doing this will not allow you to access them again and is considered a bad practice. The only way to use that built-in word again is through the `__builtins__` module.  
Many can be used by accident, such as **dict**, **id**, **list**, **min**, **max** or **str**.

**Note**: For a list of all built-ins that you should avoid:
```py
>>> dir(__builtins__)
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', '_', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
```
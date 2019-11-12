template: slide_section
name: modules
# Modules

---

template: slide_normal
### Using Modules

To use modules in your scripts, simply use the `import` keyword.
You can use it to import an entire module, or some specific method, data type or constant from it. You can also rename their *namespace* during the import.   
Here's a couple of examples:

```py
import numpy
array1 = numpy.array([1, 2])

import numpy as np
array2 = np.array([3, 4])

from numpy import array
array3 = array([5, 6])

from numpy import array as np_array
array3 = np_array([7, 8])
```
---

### Standard Library Modules

For all standard library modules, check [the standard library](https://docs.python.org/3/library/).  
Here's some of the modules you'll see yourself using somewhat frequently:
- **[Math](https://docs.python.org/3/library/math.html)**:  
Math functions such as sin(), cos(), log(), and constants such as e and π.
- **[Random](https://docs.python.org/3/library/random.html)**:  
Pseudo-Random number generator, can generate numbers based on some statistical distributions.
- **[Time](https://docs.python.org/3/library/time.html)**:  
Provides a Time datatype to you, amazing module since times are painful to program.
- **[DateTime](https://docs.python.org/3/library/datetime.html)**:    
Provides a DateTime datatype to you, amazing module since dates and times are painful to program.
- **[Os](https://docs.python.org/3/library/os.html)**:  
Handles operating system related operation.

---

### External Modules

For all available modules, check [Python Package Index](https://pypi.org/). To install these, you will probably have to use a `pip install` command on the terminal, or some similar method (Anaconda brings lots of external modules already).  
Here's a highlight of some great modules:
- **[NumPy](https://numpy.org/) & [ScyPy](https://www.scipy.org/)**:  
Uses code written in C to boost computing speed and introduce computation with matrices and other mathematical data structures.
- **[MatPlotLib](https://matplotlib.org/)**:  
Plot graphs, bar graphs, histograms and more.
- **[Seaborn](https://seaborn.pydata.org/index.html)**:  
Statistical data visualization.
- **[Pandas](https://pandas.pydata.org/)**:  
Process large data from files and apply statistics related methods.
- **[SciKit-Learn](https://scikit-learn.org/stable/index.html)**:  
Regressions, machine learning and more.
- **[TensorFlow](https://www.tensorflow.org/)**:  
Machine learning, neural networks and deep learning.

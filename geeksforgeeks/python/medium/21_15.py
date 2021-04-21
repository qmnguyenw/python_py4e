Python | __import__() function



While writing a code, there might be a need for some specific modules. So we
import those modules by using a single line code in Python.

But what if the name of the module needed is known to us only during runtime?
How can we import that module? One can use the Python’s inbuilt
**__import__()** function. It helps to import modules in runtime also.

>  **Syntax:** __import__(name, globals, locals, fromlist, level)
>
>  **Parameters:**  
>  **name** : Name of the module to be imported  
>  **globals** and **locals** : Interpret names  
>  **formlist** : Objects or submodules to be imported (as a list)  
>  **level** : Specifies whether to use absolute or relative imports. Default
> is -1(absolute and relative).

 **Example #1** :

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# importing numpy module

# it is equivalent to "import numpy"

np = __import__('numpy', globals(), locals(), [], 0)

 

# array from numpy

a = np.array([1, 2, 3])

 

# prints the type

print(type(a))  
  
---  
  
 __

 __

 **Output** :

    
    
    <class 'numpy.ndarray'>

  
**Example #2** :  
Both the following statements has same meaning and does the same work.

 __

 __  
 __

 __

 __  
 __  
 __

# from numpy import complex as comp, array as arr

np = __import__('numpy', globals(), locals(),
['complex', 'array'], 0)

 

comp = np.complex

arr = np.array  
  
---  
  
 __

 __

  
**Application** :  
 **__import__()** is not really necessary in everyday Python programming.
Its direct use is rare. But sometimes, when there is a need of importing
modules during the runtime, this function comes quite handy.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


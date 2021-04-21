Numpy string operations | splitlines() function



In this **numpy.core.defchararray.splitlines()** function, each element in
arr, return a list of the lines in the element, breaking at line boundaries.

>  **Syntax :** numpy.core.defchararray.splitlines(arr, keepends = None)
>
>  **Parameters :**
>
>  **arr :** [array-like of str] Given array-like of string.
>
>  **keepends :** [bool, optional] Line breaks are not included in the
> resulting list unless keepends is given and true.
>
>  
>
>
>  
>
>
>  **Return :** [ndarray] Return the Array of list objects.

 **Code #1 :**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program explaining

# numpy.char.splitlines() function 

 

# importing numpy as geek 

import numpy as geek 

 

gfg = geek.char.splitlines('GeeksforGeeks \n A computer science portal
\n for geeks')

 

print (gfg)  
  
---  
  
 __

 __

 **Output :**

> [‘GeeksforGeeks ‘, ‘ A computer science portal ‘, ‘ for geeks’]

 **Code #2 :**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program explaining

# numpy.char.splitlines() function 

 

# importing numpy as geek 

import numpy as geek 

 

gfg = geek.char.splitlines('This is \r a Python-Numpy \r article \r for
geeks')

 

print (gfg)  
  
---  
  
 __

 __

 **Output :**

> [‘This is ‘, ‘ a Python-Numpy ‘, ‘ article ‘, ‘ for geeks’]

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save


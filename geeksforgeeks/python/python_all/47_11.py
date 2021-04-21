Numpy string operations | replace() function



In the **numpy.core.defchararray.replace()** function, each element in arr,
return a copy of the string with all occurrences of substring old replaced by
new.

>  **Syntax :** numpy.core.defchararray.replace(arr, old, new, count = None)
>
>  **Parameters :**
>
> **arr :** [array-like of str] Given array-like of string.
>
> **old :** [str or unicode] Old substring you want to replace.
>
>  
>
>
>  
>
>
>  **new :** [str or unicode] New substring which would replace the old
> substring.
>
> **count :** [int, optional] If the optional argument count is given, only
> the first count occurrences are replaced.
>
>  **Return :** [ndarray] Return the output array of str .

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

# numpy.char.replace() function 

 

# importing numpy as geek 

import numpy as geek 

 

gfg = geek.char.replace('GFG | a computer science portal for geeks',
'GFG', 'GeeksforGeeks')

 

print (gfg)  
  
---  
  
 __

 __

 **Output :**

> GeeksforGeeks | a computer science portal for geeks

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

# numpy.char.replace() function 

 

# importing numpy as geek 

import numpy as geek 

 

gfg = geek.char.replace('This is a python article', 'python',
'Numpy-Python', count = 1)

 

print (gfg)  
  
---  
  
 __

 __

 **Output :**

> This is a Numpy-Python article

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save


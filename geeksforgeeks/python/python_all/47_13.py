Numpy string operations | rindex() function



 **numpy.core.defchararray.rindex()** function, raises ValueError when the
substring sub is not found. Calls str.rindex element-wise.

>  **Syntax :** numpy.core.defchararray.rindex(arr, sub, start = 0, end =
> None)
>
>  **Parameters :**
>
>  **arr :** [array-like of str or unicode] Array-like of str .
>
>  **sub :** [str or unicode] Input string or unicode.
>
>  
>
>
>  
>
>
>  **start, end :** [int, optional] Optional arguments start and end are
> interpreted as in slice notation.
>
>  **Return :** Return the output array of ints.

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

# numpy.char.rindex() function 

 

# importing numpy as geek 

import numpy as geek 

 

arr = "GeeksforGeeks - A computer science portal for geeks"

sub = 'science'

 

gfg = geek.char.rindex(arr, sub)

 

print (gfg)  
  
---  
  
 __

 __

 **Output :**

> 27

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

# numpy.char.rindex() function 

 

# importing numpy as geek 

import numpy as geek 

 

arr = "GeeksforGeeks - A computer science portal for geeks"

sub = 'geeks'

 

gfg = geek.char.rindex(arr, sub, start = 0, end = None)

 

print (gfg)  
  
---  
  
 __

 __

 **Output :**

> 46

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save


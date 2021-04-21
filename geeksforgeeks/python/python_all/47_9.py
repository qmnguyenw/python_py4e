Numpy string operations | partition() function



In the **numpy.core.defchararray.partition()** function, each element in arr,
split the element as the first occurrence of sep, and return 3 strings
containing the part before the separator, the separator itself, and the part
after the separator. If the separator is not found, return 3 strings
containing the string itself, followed by two empty strings.

>  **Syntax :** numpy.core.defchararray.partition(arr, sep)
>
>  **Parameters :**
>
>  **arr :** [array_like, {str, unicode}] Given Input array.
>
>  **sep :** [str or unicode] Separator to split each string element in arr.
>
>  
>
>
>  
>
>
>  **Return :** [ndarray] Return the output array of str or unicode, depending
> on input type.

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

# numpy.char.partition() function 

 

# importing numpy as geek 

import numpy as geek 

 

arr = "GeeksforGeeks - A computer science portal for geeks"

sep ='None'

 

gfg = geek.char.partition(arr, sep)

 

print (gfg)  
  
---  
  
 __

 __

 **Output :**

> [‘GeeksforGeeks – A computer science portal for geeks’ ” ”]

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

# numpy.char.partition() function 

 

# importing numpy as geek 

import numpy as geek 

 

arr = "GeeksforGeeks - A computer science portal for geeks"

sep = 'portal'

 

gfg = geek.char.partition(arr, sep)

 

print (gfg)  
  
---  
  
 __

 __

 **Output :**

> [‘GeeksforGeeks – A computer science ‘ ‘portal’ ‘ for geeks’]

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save


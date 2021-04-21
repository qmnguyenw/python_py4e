How to calculate dot product of two vectors in Python?



In mathematics, the **dot product** or also known as the **scalar product** is
an algebraic operation that takes two equal-length sequences of numbers and
returns a single number. Let us given two vectors **A** and **B,** and we have
to find the dot product of two vectors.

Given that,

![A = a_1i + a_2j + a_3k ](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-ce3d5303e73d4ba86f21a8d59ae44ada_l3.png)

and,

![B = b_1i + b_2j + b_3k ](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-286d6d9c33a95b637e071ca694d095f7_l3.png)

  

  

>  **Where,**
>
>  **i:** the unit vector along the x directions
>
>  **j:** the unit vector along the y directions
>
>  **k:** the unit vector along the z directions

Then the dot product is calculated as:

![DotProduct = a_1 * b_1 + a_2 * b_2 + a_3 * b_3
](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-a0770cb572b1412f40d6f1aec32258df_l3.png)

 **Example:**

Given two vectors A and B as,

  

  

![A = 3i + 5j + 4k \\\\ B = 2i + 7j + 5k \\\\ DotProduct = 3 * 2 + 5 * 7 + 4 *
5 = 6 + 35 + 20 = 61](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-a98a9faf3d30c6ccf595025c7835288f_l3.png)

## Dot Product of Two Vectors in Python

Python provides a very efficient method to calculate the dot product of two
vectors. By using **numpy.dot()** method which is available in the NumPy
module one can do so.

>  **Syntax:**
>
> numpy.dot(vector_a, vector_b, out = None)
>
>  **Parameters:**
>
>  **vector_a:** [array_like] if a is complex its complex conjugate is used
> for the calculation of the dot product.
>
>  **vector_b:** [array_like] if b is complex its complex conjugate is used
> for the calculation of the dot product.
>
>  **out:** [array, optional] output argument must be C-contiguous, and its
> dtype must be the dtype that would be returned for dot(a,b).
>
> **Return:**
>
> Dot Product of vectors a and b. if vector_a and vector_b are 1D, then scalar
> is returned

 **Example 1:**

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python Program illustrating

# dot product of two vectors

 

# Importing numpy module

import numpy as np

 

# Taking two scalar values

a = 5

b = 7

 

# Calculating dot product using dot()

print(np.dot(a, b))  
  
---  
  
 __

 __

 **Output:**

    
    
    35
    

**Example 2:**

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python Program illustrating

# dot product of two vectors

 

# Importing numpy module

import numpy as np

 

# Taking two 1D array

a = 3 + 1j

b = 7 + 6j

 

# Calculating dot product using dot()

print(np.dot(a, b))  
  
---  
  
 __

 __

 **Output:**

    
    
    (15+25j)
    

**Example 3:**

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python Program illustrating

# dot product of two vectors

 

# Importing numpy module

import numpy as np

 

# Taking two 2D array

# For 2-D arrays it is the matrix product

a = [[2, 1], [0, 3]]

b = [[1, 1], [3, 2]]

 

# Calculating dot product using dot()

print(np.dot(a, b))  
  
---  
  
 __

 __

 **Output:**

    
    
    [[5 4]
     [9 6]]
    

**Example 4:**

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python Program illustrating

# dot product of two vectors

 

# Importing numpy module

import numpy as np

 

# Taking two 2D array

# For 2-D arrays it is the matrix product

a = [[2, 1], [0, 3]]

b = [[1, 1], [3, 2]]

 

# Calculating dot product using dot()

# Note that here I have taken dot(b, a)

# Instead of dot(a, b) and we are going to

# get a different ouput for the same vector value

print(np.dot(b, a))  
  
---  
  
 __

 __

 **Output:**

    
    
    [[2 4]
     [6 9]]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


Types of padding in convolution layer



Let’s discuss padding and its types in convolution layers. In convolution
layer we have kernels and to make the final filter more informative we use
padding in image matrix or any kind of input array. We have three types of
padding that are as follows.

  1.  **Padding Full :**

Let’s assume a kernel as a sliding window. We have to come with the solution
of padding zeros on the input array. This is a very famous implementation and
will be easier to show how it works with a simple example, consider x as a
filter and h as an input array.

x[i] = [6, 2]  
h[i] = [1, 2, 5, 4]

Using the zero padding, we can calculate the convolution.

You have to invert the filter x, otherwise the operation would be cross-
correlation. First step, (now with zero padding):  
![](https://media.geeksforgeeks.org/wp-
content/uploads/Screenshot-2019-01-08-17.02.11.png)

  

  

= 2 * 0 + 6 * 1 = 6

Second step:  
![](https://media.geeksforgeeks.org/wp-
content/uploads/Screenshot-2019-01-08-17.06.03.png)

= 2 * 1 + 6 * 2 = 14

Third step:

![](https://media.geeksforgeeks.org/wp-
content/uploads/Screenshot-2019-01-08-17.08.42.png)

= 2 * 2 + 6 * 5 = 34

Fourth step:

![](https://media.geeksforgeeks.org/wp-
content/uploads/Screenshot-2019-01-08-17.11.11.png)

  

  

= 2 * 5 + 6 * 4 = 34

Fifth step:

= 2 * 4 + 6 * 0 = 8

The result of the convolution for this case, listing all the steps above,
would be: Y = [6 14 34 34 8]

 __

 __  
 __

 __

 __  
 __  
 __

# importing numpy

import numpy as np

 

x = [6, 2]

h = [1, 2, 5, 4]

 

y = np.convolve(x, h, "full")

print(y)   
  
---  
  
__

__

**Output:**

    
    
    [ 6 14 34 34  8]
    

  2. **Padding same :**

In this type of padding, we only append zero to the left of the array and to
the top of the 2D input matrix.

 __

 __  
 __

 __

 __  
 __  
 __

# importing numpy

import numpy as np

 

x = [6, 2]

h = [1, 2, 5, 4]

 

y = np.convolve(x, h, "same")

print(y)  
  
---  
  
 __

 __

 **Output:**

    
    
    [ 6 14 34 34]
    

  3. **Padding valid :**

In this type of padding, we got the reduced output matrix as the size of the
output array is reduced. We only applied the kernel when we had a compatible
position on the h array, in some cases you want a dimensionality reduction.

 __

 __  
 __

 __

 __  
 __  
 __

# importing numpy

import numpy as np

 

x = [6, 2]

h = [1, 2, 5, 4]

 

y = np.convolve(x, h, "valid")

print(y)  
  
---  
  
 __

 __

 **Output:**

    
    
    [14 34 34]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


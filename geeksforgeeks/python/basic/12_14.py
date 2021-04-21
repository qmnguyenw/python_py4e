Python | Numpy matrix.trace()



With the help of **Numpy matrix.trace()** method, we can find the sum of all
the elements of diagonal of a matrix by using the matrix.trace() method.

>  **Syntax :** matrix.trace()  
>  **Return :** **Return sum of a diagonal elements of a matrix**

 **Example #1 :**  
In this example we can see that by using **matrix.trace()** method can help
us to find the sum of all the elements of a diagonal of given matrix.

 __

 __  
 __

 __

 __  
 __  
 __

# import the important module in python

import numpy as np

 

# make matrix with numpy

gfg = np.matrix('[4, 1; 12, 3]')

 

# applying matrix.trace() method

geek = gfg.trace()

 

print(geek)  
  
---  
  
 __

 __

 **Output:**

    
    
    [[7]]
    

**Example #2 :**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# import the important module in python

import numpy as np

 

# make matrix with numpy

gfg = np.matrix('[4, 1, 9; 12, 3, 1; 4, 5, 6]')

 

# applying matrix.trace() method

geek = gfg.trace()

 

print(geek)  
  
---  
  
 __

 __

 **Output:**

    
    
    [[13]]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


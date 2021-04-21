numpy.random.uniform() in Python



With the help of **numpy.random.uniform()** method, we can get the random
samples from uniform distribution and returns the random samples as numpy
array by using this method.

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200805141844/Screenshot20200805141548.png)

Uniform distribution

>  **Syntax :** numpy.random.uniform(low=0.0, high=1.0, size=None)
>
>  **Return :** Return the random samples as numpy array.

 **Example #1 :**

In this example we can see that by using **numpy.random.uniform()** method, we
are able to get the random samples from uniform distribution and return the
random samples.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import numpy

import numpy as np

import matplotlib.pyplot as plt

 

# Using uniform() method

gfg = np.random.uniform(-5, 5, 5000)

 

plt.hist(gfg, bins = 50, density = True)

plt.show()  
  
---  
  
 __

 __

 **Output :**

> ![](https://media.geeksforgeeks.org/wp-
> content/uploads/20200805142417/Screenshot20200805142252-660x500.png)

 **Example #2 :**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import numpy

import numpy as np

import matplotlib.pyplot as plt

 

# Using uniform() method

gfg = np.random.uniform(2.1, 5.5, 10000)

 

plt.hist(gfg, bins = 100, density = True)

plt.show()  
  
---  
  
 __

 __

 **Output :**

> ![](https://media.geeksforgeeks.org/wp-
> content/uploads/20200805142731/Screenshot20200805142602-660x496.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


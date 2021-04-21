Creating a Pandas Series from Dictionary



A **Series** is a one-dimensional labeled array capable of holding any data
type (integers, strings, floating point numbers, Python objects, etc.). It has
to be remembered that unlike Python lists, a Series will always contain data
of the same type.

Let’s see how to create a Pandas Series from Dictionary.

### Using Series() method without index parameter.

In this case, dictionary keys are taken in a sorted order to construct index.

 **Code #1 :** Dictionary keys are given in sorted order.

 __

 __  
 __

 __

 __  
 __  
 __

# import the pandas lib as pd

import pandas as pd

 

# create a dictionary

dictionary = {'A' : 10, 'B' : 20, 'C' : 30}

 

# create a series

series = pd.Series(dictionary)

 

print(series)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    A    10
    B    20
    C    30
    dtype: int64
    


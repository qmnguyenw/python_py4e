Python | Convert Numpy Arrays to Tuples



Given a numpy array, write a programm to convert numpy array into tuples.

 **Examples –**

    
    
    **Input:** ([[1, 0, 0, 1, 0], [1, 2, 0, 0, 1]])
    **Output:** ((1, 0, 0, 1, 0), (1, 2, 0, 0, 1))
    
    **Input:** ([['manjeet', 'akshat'], ['nikhil', 'akash']])
    **Output:** (('manjeet', 'akshat'), ('nikhil', 'akash'))
    

Given below are various methods to convert numpy array into tuples.

 **Method #1: Using tuple and map**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# deletion of columns from numpy array

 

import numpy as np

 

# initialising numpy array

ini_array = np.array([['manjeet', 'akshat'], ['nikhil',
'akash']])

 

 

# convert numpy arrays into tuples

result = tuple(map(tuple, ini_array))

 

# print result

print ("Resultant Array :"+str(result))  
  
---  
  
 __

 __

 **Output:**

    
    
    Result:(('manjeet', 'akshat'), ('nikhil', 'akash'))
    

**Method #2: Using Naive Approach**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# deletion of columns from numpy array

 

import numpy as np

 

# initialising numpy array

ini_array = np.array([['manjeet', 'akshat'], ['nikhil',
'akash']])

 

 

# convert numpy arrays into tuples

result = tuple([tuple(row) for row in ini_array])

 

# print result

print ("Result:"+str(result))  
  
---  
  
 __

 __

 **Output:**

    
    
    Result:(('manjeet', 'akshat'), ('nikhil', 'akash'))
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


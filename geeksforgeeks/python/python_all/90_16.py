Python – Numpy Array Column Deletion



Given a numpy array, write a programme to delete columns from numpy array.

 **Examples –**

    
    
    **Input:** [['akshat', 'nikhil'], ['manjeeet', 'akash']]
    **Output:** [['akshat']['manjeeet']]
    
    **Input:** [[1, 0, 0, 1, 0], [0, 1, 2, 1, 1]]
    **Output:** [[1 0 1 0][0 2 1 1]]
    

Given below are various methods to delete columns from numpy array.

 **Method #1: Using np.delete()**

  

  

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

ini_array = np.array([[1, 0, 0, 1, 0],

 [0, 1, 2, 1, 1]])

 

 

# deleting second column from array

result = np.delete(ini_array, 1, 1)

 

# print result

print ("Resultant Array :"+str(result))  
  
---  
  
 __

 __

 **Output:**

    
    
    Resultant Array :[[1 0 1 0]
     [0 2 1 1]]
    

**Method #2: Using compress() and logical_not()**

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

ini_array = np.array([[1, 0, 0, 1, 0], [1, 2,
0, 0, 1]])

z = [False, True, False, False, False]

 

 

# deleting second column from array

result = ini_array.compress(np.logical_not(z), axis = 1)

 

# print result

print ("Resultant Array :"+str(result))  
  
---  
  
 __

 __

 **Output:**

    
    
    Resultant Array :[[1 0 1 0]
     [1 0 0 1]]
    

**Method #3: Using logical_not()**

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

ini_array = np.array([[1, 0, 0, 1, 0], [1, 2,
0, 0, 1]])

z = [False, True, False, False, False]

 

 

# deleting second column from array

result = ini_array[:, np.logical_not(z)]

 

# print result

print ("Resultant Array :"+str(result))  
  
---  
  
 __

 __

 **Output:**

    
    
    Resultant Array :[[1 0 1 0]
     [1 0 0 1]]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


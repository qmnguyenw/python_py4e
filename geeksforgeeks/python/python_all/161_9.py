Python | Ways to convert array of strings to array of floats



Sometimes in a competitive coding environment, we get input in some other
datatypes and we need to convert them in other forms this problem is same as
that we have an input in the form of string and we need to convert it into
floats.  
Let’s discuss a few ways to convert an array of strings to array of floats.

 **Method #1 : Using astype**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate converting

# array of strings to array of floats

# using astype

 

import numpy as np

 

# initialising array

ini_array = np.array(["1.1", "1.5", "2.7", "8.9"])

 

# printing initial array

print ("initial array", str(ini_array))

 

# conerting to array of floats

# using np.astype

res = ini_array.astype(np.float)

 

# printing final result

print ("final array", str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    initial array ['1.1' '1.5' '2.7' '8.9']
    final array [ 1.1  1.5  2.7  8.9]
    

  
**Method #2: Usingnp.fromstring**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate converting

# array of strings to array of floats

# using fromstring

 

import numpy as np

 

# initialising array

ini_array = np.array(["1.1", "1.5", "2.7", "8.9"])

 

# printing initial array

print ("initial array", str(ini_array))

 

# conerting to array of floats

# using np.fromstring

ini_array = ', '.join(ini_array)

ini_array = np.fromstring(ini_array, dtype = np.float, 

 sep =', ' )

 

# printing final result

print ("final array", str(ini_array))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    initial array ['1.1' '1.5' '2.7' '8.9']
    final array [ 1.1  1.5  2.7  8.9]
    


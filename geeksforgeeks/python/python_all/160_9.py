Python | Ways to flatten a 2D list



Given a 2D list, write a Python program to convert the given list into a
flattened list.

 **Method #1: Using chain.iterable()**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# converting 2d list into 1d list

# using chain.from_iterables

 

# import chain

from itertools import chain

 

ini_list = [[1, 2, 3],

 [3, 6, 7],

 [7, 5, 4]]

 

# printing initial list

print ("initial list ", str(ini_list))

 

# converting 2d list into 1d

# using chain.from_iterables

flatten_list = list(chain.from_iterable(ini_list))

 

# printing flatten_list

print ("final_result", str(flatten_list))  
  
---  
  
 __

 __

 **Output:**

    
    
    initial list  [[1, 2, 3], [3, 6, 7], [7, 5, 4]]
    final_result [1, 2, 3, 3, 6, 7, 7, 5, 4]
    

  
**Method #2: Using list comprehension**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# converting 2d list into 1d list

# using list comprehension

 

# import chain

from itertools import chain

 

ini_list = [[1, 2, 3],

 [3, 6, 7],

 [7, 5, 4]]

 

# printing initial list

print ("initial list ", str(ini_list))

 

# converting 2d list into 1d

# using list comprehension

flatten_list = [j for sub in ini_list for j in sub]

 

# printing flatten_list

print ("final_result", str(flatten_list))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    initial list  [[1, 2, 3], [3, 6, 7], [7, 5, 4]]
    final_result [1, 2, 3, 3, 6, 7, 7, 5, 4]
    


Python | Zipping two unequal length list in dictionary



Given two lists of possibly unequal lengths, the task is to zip two lists in
dictionary such that the list with shorter length will repeat itself.

Since the dictionary in Python is an unordered collection of key:value pairs,
the result will be printed on unordered fashion.

 **Method #1: Usingitertools()**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# return the sum of values of a dictionary

# with same keys in the list of dictionary

 

from itertools import cycle

 

# Initialising list of dictionary

ini_lis1 = ['a', 'b', 'c', 'd', 'e']

ini_lis2 = [1, 2, 3]

 

# zipping in cyclic if shorter length

result = dict(zip(ini_lis1, cycle(ini_lis2)))

 

# printing resultant dictionary

print("resultant dictionary : ", str(result))  
  
---  
  
 __

 __

 **Output:**

    
    
    resultant dictionary :  {'b': 2, 'd': 1, 'c': 3, 'e': 2, 'a': 1}
    

  
**Method #2: Using dict comprehension**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# return the sum of values of dictionary

# with same keys in list of dictionary

 

from itertools import cycle

 

# Initialising list of dictionary

ini_lis1 = ['a', 'b', 'c', 'd', 'e']

ini_lis2 = [1, 2, 3]

 

# zipping in cyclic if shorter length

result = {v: ini_lis2[i % len(ini_lis2)] 

 for i, v in enumerate(ini_lis1)}

 

print("resultant dictionary : ", str(result))  
  
---  
  
 __

 __

 **Output:**

    
    
    resultant dictionary :  {'d': 1, 'c': 3, 'e': 2, 'b': 2, 'a': 1}
    

  
**Method #3: Using deque()**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# return the sum of values of dictionary

# with same keys in list of dictionary

 

from collections import deque

 

# Initialising list of dictionary

ini_lis1 = ['a', 'b', 'c', 'd', 'e']

ini_lis2 = deque([1, 2, 3])

 

# zipping in cyclic if shorter length

result = {}

for letter in ini_lis1:

 number = ini_lis2.popleft()

 result[letter] = number

 ini_lis2.append(number)

 

print("resultant dictionary : ", str(result))  
  
---  
  
 __

 __

 **Output:**

    
    
    resultant dictionary :  {'c': 3, 'd': 1, 'b': 2, 'e': 2, 'a': 1}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


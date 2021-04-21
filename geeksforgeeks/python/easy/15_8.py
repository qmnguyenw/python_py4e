Python program to get all subsets of given size of a set



Given a set, write a Python program to generate all possible subset of size
_n_ of given set within a list.

 **Examples:**

    
    
    **Input :** {1, 2, 3}, n = 2
    **Output :** [{1, 2}, {1, 3}, {2, 3}]
    
    **Input :** {1, 2, 3, 4}, n = 3
    **Output :** [{1, 2, 3}, {1, 2, 4}, {1, 3, 4}, {2, 3, 4}]
    

We have already discussed the same problem using Naive approach in this
article. This article focuses on the Pythonic approaches to Print all subsets
of given size of a set.

Python has **itertools.combinations(iterable, n)** which Return _n_ length
subsequences of elements from the input iterable. This can be used to Print
all subsets of given size of a set. Now, we have various alternatives to use
this function.

 **Code #1 :**  
Simply pass the set as iterable and the size as arguments in the
itertools.combinations() to directly fetch the combination list.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python Program to Print

# all subsets of given size of a set

 

import itertools

 

def findsubsets(s, n):

 return list(itertools.combinations(s, n))

 

# Driver Code

s = {1, 2, 3}

n = 2

 

print(findsubsets(s, n))  
  
---  
  
 __

 __

 **Output:**

    
    
    [(1, 2), (1, 3), (2, 3)]
    

  
**Code #2 :**  
We can also use an alternative to above discussed method which is _mapping_
set to itertools.combinations() function.

 __

 __  
 __

 __

 __  
 __  
 __

# Python Program to Print

# all subsets of given size of a set

 

import itertools

from itertools import combinations, chain

 

def findsubsets(s, n):

 return list(map(set, itertools.combinations(s, n)))

 

# Driver Code

s = {1, 2, 3}

n = 2

 

print(findsubsets(s, n))  
  
---  
  
 __

 __

 **Output:**

    
    
    [{1, 2}, {1, 3}, {2, 3}]
    

  
**Code #3 :**  
Another method is to use for loop in itertools.combinations() function and
append the combination sets to the list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python Program to Print

# all subsets of given size of a set

 

import itertools

# def findsubsets(s, n):

def findsubsets(s, n):

 return [set(i) for i in itertools.combinations(s, n)]

 

# Driver Code

s = {1, 2, 3, 4}

n = 3

 

print(findsubsets(s, n))  
  
---  
  
 __

 __

 **Output:**

    
    
    [{1, 2, 3}, {1, 2, 4}, {1, 3, 4}, {2, 3, 4}]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


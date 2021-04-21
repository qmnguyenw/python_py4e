Python | Intersection of multiple lists



Given two list of lists, write a Python program to find the intersection
between the given two lists.

 **Examples:**

    
    
    **Input :** lst1 = [['a', 'c'], ['d', 'e']]
            lst2 = [['a', 'c'], ['e', 'f'], ['d', 'e']]
    **Output :** [['a', 'c'], ['d', 'e']]
    
    **Input :** lst1 = [[1, 5, 7], [2, 3], [6, 9], [4, 8]]
            lst2 = [[9, 3], [2, 3], [6, 9]]
    **Output :** [[2, 3], [6, 9]]
    

  
**Approach #1 :** Naive(List comprehension)

The brute-force or naive approach to find the intersection of list of lists is
to use List comprehension or simply a _for_ loop.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to find

# Intersection of list of lists

 

def intersection(lst1, lst2):

 

 return [item for item in lst1 if item in lst2]

 

# Driver code

lst1 = [['a', 'c'], ['d', 'e']]

lst2 = [['a', 'c'], ['e', 'f'], ['d', 'e']]

print(intersection(lst1, lst2))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    [['a', 'c'], ['d', 'e']]
    


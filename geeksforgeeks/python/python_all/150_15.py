Python | Find all distinct pairs with difference equal to k



Given a list of integers and a positive integer _k_ , write a Python program
to count all distinct pairs with difference equal to k.

 **Examples:**

    
    
    **Input :** [1, 5, 3, 4, 2], k = 3
    **Output :** [(5, 2), (4, 1)]
    
    **Input :** [8, 12, 16, 4, 0, 20], k = 4
    **Output :** [(8, 4), (12, 8), (16, 12), (4, 0), (20, 16)]
    

  
**Approach #1 :** Python list comprehension

We will use list comprehension using two loops using ‘e1’ and ‘e2’ that will
traverse given list. We check if _e1-e2 == k_ or not and return the (e1, e2)
tuple respectively. Finally, a list with required tuples will be returned.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to Find all distinct

# pairs with difference equal to k

 

def findPairs(lst, k):

 

 return [(e1, e2) for e1 in lst 

 for e2 in lst if (e1-e2 == k)]

 

# Driver code

lst = [1, 5, 3, 4, 2]

k = 3

print(findPairs(lst, k))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    [(5, 2), (4, 1)]
    


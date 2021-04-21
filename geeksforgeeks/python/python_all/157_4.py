Python | Count occurrence of all elements of list in a tuple



Given a tuple and a list as input, write a Python program to count the
occurrences of all items of the list in the tuple.

 **Examples:**

    
    
    **Input :** tuple = ('a', 'a', 'c', 'b', 'd')
            list = ['a', 'b']
    **Output :** 3 
    
    **Input :** tuple = (1, 2, 3, 1, 4, 6, 7, 1, 4)
            list = [1, 4, 7]
    **Output :** 6
    

  
**Approach #1 :** Naive Approach

The first approach is the naive approach. Use a for loop and traverse through
the given list and count the occurrence of each item of tuple in a list.
Finally, return the count.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 Program to count occurrence

# of all elements of list in a tuple

from collections import Counter

 

def countOccurrence(tup, lst):

 count = 0

 for item in tup:

 if item in lst:

 count+= 1

 

 return count 

 

# Driver Code

tup = ('a', 'a', 'c', 'b', 'd')

lst = ['a', 'b']

print(countOccurrence(tup, lst))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    3
    


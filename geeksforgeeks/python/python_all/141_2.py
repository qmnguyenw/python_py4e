Python | Remove duplicate tuples from list of tuples



Given a list of tuples, Write a Python program to remove all the duplicated
tuples from the given list.

 **Examples:**

    
    
    **Input :** [(1, 2), (5, 7), (3, 6), (1, 2)]
    **Output :** [(1, 2), (5, 7), (3, 6)]
    
    **Input :** [('a', 'z'), ('a', 'x'), ('z', 'x'), ('a', 'x'), ('z', 'x')]
    **Output :** [('a', 'z'), ('a', 'x'), ('z', 'x')]
    

**Method #1 :** List comprehension

This is a naive approach to use list comprehension. Here, we use two _for_
loops and _set_ data structure to cancel out all the duplicates.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to remove duplicate

# tuples from list of tuples

 

def removeDuplicates(lst):

 

 return [t for t in (set(tuple(i) for i in
lst))]

 

# Driver code

lst = [(1, 2), (5, 7), (3, 6), (1, 2)]

print(removeDuplicates(lst))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    [(1, 2), (5, 7), (3, 6)]
    


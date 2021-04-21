Python | Reverse each tuple in a list of tuples



Given a list of tuples, write a Python program to reverse each tuple in the
given list of tuples.

 **Examples:**

    
    
    **Input :** [(1, 2), (3, 4, 5), (6, 7, 8, 9)]
    **Output :** [(2, 1), (5, 4, 3), (9, 8, 7, 6)]
    
    **Input :** [('a', 'b'), ('x', 'y'), ('m', 'n')]
    **Output :** [('b', 'a'), ('y', 'x'), ('n', 'm')]
    

  
**Method #1 :** Negative-step slicing

We can use standard negative-step slicing tup[::-1] to get the reverse of a
tuple, and a list comprehension to get that for each tuple.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to Reverse

# each tuple in a list of tuples

 

def reverseTuple(lstOfTuple):

 

 return [tup[::-1] for tup in lstOfTuple]

 

# Driver code

lstOfTuple = [(1, 2), (3, 4, 5), (6, 7,
8, 9)]

print(reverseTuple(lstOfTuple))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    [(2, 1), (5, 4, 3), (9, 8, 7, 6)]
    


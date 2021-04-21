Python | Get first element of each sublist



Given a list of lists, write a Python program to extract first element of each
sublist in the given list of lists.

 **Examples:**

    
    
    **Input :** [[1, 2], [3, 4, 5], [6, 7, 8, 9]]
    **Output :** [1, 3, 6]
    
    **Input :** [['x', 'y', 'z'], ['m'], ['a', 'b'], ['u', 'v']]
    **Output :** ['x', 'm', 'a', 'u']
    

  
**Approach #1 :** List comprehension

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to extract first and last

# element of each sublist in a list of lists

 

def Extract(lst):

 return [item[0] for item in lst]

 

# Driver code

lst = [[1, 2], [3, 4, 5], [6, 7, 8,
9]]

print(Extract(lst))  
  
---  
  
 __

 __

 **Output:**

    
    
    [1, 3, 6]
    

  
**Approach #2 :** Using _zip_ and unpacking(*) operator

  

  

This method uses _zip_ with * or unpacking operator which passes all the items
inside the ‘lst’ as arguments to zip function. Thus, all the first element
will become the first tuple of the zipped list. Returning the 0th element will
thus, solve the purpose.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to extract first and last

# element of each sublist in a list of lists

 

def Extract(lst):

 return list(list(zip(*lst))[0])

 

# Driver code

lst = [[1, 2], [3, 4, 5], [6, 7, 8,
9]]

print(Extract(lst))  
  
---  
  
 __

 __

 **Output:**

    
    
    [1, 3, 6]
    

Another method of using _zip_ is given below:-

 __

 __  
 __

 __

 __  
 __  
 __

def Extract(lst):

 return list(next(zip(*lst)))  
  
---  
  
 __

 __

  
**Approach #3 :** Using itemgetter()

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to extract first and last

# element of each sublist in a list of lists

from operator import itemgetter

 

def Extract(lst):

 return list( map(itemgetter(0), lst ))

 

# Driver code

lst = [[1, 2], [3, 4, 5], [6, 7, 8,
9]]

print(Extract(lst))  
  
---  
  
 __

 __

 **Output:**

    
    
    [1, 3, 6]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


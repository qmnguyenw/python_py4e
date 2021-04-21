Python | Get last element of each sublist



Given a list of lists, write a Python program to extract the last element of
each sublist in the given list of lists.

 **Examples:**

    
    
    **Input :** [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
    **Output :** [3, 5, 9]
    
    **Input :** [['x', 'y', 'z'], ['m'], ['a', 'b'], ['u', 'v']]
    **Output :** ['z', 'm', 'b', 'v']
    

  
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

 return [item[-1] for item in lst]

 

# Driver code

lst = [[1, 2, 3], [4, 5], [6, 7, 8,
9]]

print(Extract(lst))  
  
---  
  
 __

 __

 **Output:**

    
    
    [3, 5, 9]
    

  
**Approach #2 :** Using _zip_ and unpacking(*) operator

  

  

This method uses _zip_ with * or unpacking operator which passes all the items
inside the ‘lst’ as arguments to zip function. There is a little trick with
extracting last item of list, Instead of using direct zip, use the reversed
list iterators.

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

 return list(zip(*[reversed(el) for el in
lst]))[0]

 

# Driver code

lst = [[1, 2, 3], [4, 5], [6, 7, 8,
9]]

print(Extract(lst))  
  
---  
  
 __

 __

 **Output:**

    
    
    (3, 5, 9)
    

Another way of using zip is to use it with Python map, passing reversed
as function.

 __

 __  
 __

 __

 __  
 __  
 __

def Extract(lst):

 return list(list(zip(*map(reversed, lst)))[0])  
  
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

 return list( map(itemgetter(-1), lst ))

 

# Driver code

lst = [[1, 2, 3], [4, 5], [6, 7, 8,
9]]

print(Extract(lst))  
  
---  
  
 __

 __

 **Output:**

    
    
    [3, 5, 9]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


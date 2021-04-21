Python | Group list elements based on frequency



Given a list of elements, write a Python program to group list elements and
their respective frequency within a tuple.

 **Examples:**

    
    
    **Input :** [1, 3, 4, 4, 1, 5, 3, 1]
    **Output :** [(1, 3), (3, 2), (4, 2), (5, 1)]
    
    **Input :** ['x', 'a', 'x', 'y', 'a', 'x']
    **Output :** [('x', 3), ('a', 2), ('y', 1)]
    

**Method #1 :** List comprehension

We can use list comprehension to form tuples of each element and the count of
its occurrence and store it in ‘res’, but that will contain the duplicate
first element. Thus, to remove the duplicate first element, we use
OrderedDict(res).items().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to Grouping list

# elements based on frequency

from collections import OrderedDict 

 

def group_list(lst):

 

 res = [(el, lst.count(el)) for el in lst]

 return list(OrderedDict(res).items())

 

# Driver code

lst = [1, 3, 4, 4, 1, 5, 3, 1]

print(group_list(lst))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    [(1, 3), (3, 2), (4, 2), (5, 1)]
    


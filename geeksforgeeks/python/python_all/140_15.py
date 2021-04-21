Python | Merging nested lists



Given two nested lists, ‘lst1’ and ‘lst2’, write a Python program to create a
new nested list ‘lst3’ out of the two given nested lists, so that the new
nested list consist common intersections of both lists as well as the non-
intersecting elements.

 **Examples:**

    
    
    **Input :** lst1 = [[5, 9], [8, 2, 6], [3, 4]]
            lst2 = [[9, 5, 8], [2, 6], [3, 4, 1]]
    **Output :** [[9, 5], [8], [2, 6], [3, 4], [1]]
    
    **Input :** lst1 = [['a', 'b', 'c'], ['x']]
            lst2 = [['b', 'c', 'y'], ['x', 'y']]
    **Output :** [['b', 'c'], ['x'], ['y'], ['a']]
    

  
**Approach #1 :** By set intersection using _functools.reduce()_

This method uses the set intersection to compute each intersection, then add
any item which is left over (that is, items appearing on only one of the two
lists). We will first use functools.reduce() to yield unique elements of
‘lst1’ and ‘lst2’ and save them to ‘temp1’ and ‘temp2’ respectively. After
this, find the set intersection of both the list in ‘lst3’. At last, find the
symmetric difference of ‘lst1’ and ‘lst2’, which yields the items which appear
in only one of the 2 sets and append it to ‘lst3’.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to find Greatest common

# intersection of two nested lists

import itertools

import functools

 

def GCI(lst1, lst2):

 

 temp1 = functools.reduce(lambda a, b:
set(a).union(set(b)), lst1)

 temp2 = functools.reduce(lambda a, b:
set(a).union(set(b)), lst2)

 

 lst3 = [list(set(a).intersection(set(b))) 

 for a, b in itertools.product(lst1, lst2) 

 if len(set(a).intersection(set(b))) != 0]

 

 lst3.extend([x] for x in temp1.symmetric_difference(temp2))

 

 return lst3

 

# Driver code

lst1 = [[5, 9], [8, 2, 6], [3, 4]]

lst2 = [[9, 5, 8], [2, 6], [3, 4, 1]]

print(GCI(lst1, lst2))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    [[9, 5], [8], [2, 6], [3, 4], [1]]
    


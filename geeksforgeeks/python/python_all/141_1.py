Python | Increase list size by padding each element by N



Given a list and an integer N, write a Python program to increase the size of
the list by padding each element by N.

 **Examples:**

    
    
    **Input :** lst = [1, 2, 3]
            N = 3
    **Output :** [1, 1, 1, 2, 2, 2, 3, 3, 3]
    
    **Input :** lst = ['cats', 'dogs']
            N = 2
    **Output :** ['cats', 'cats', 'dogs', 'dogs']
    

**Approach #1 :** List comprehension

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to increase list size

# by padding each element by N

 

def increaseSize(lst, N):

 

 return [el for el in lst for _ in range(N)]

 

# Driver code

lst = [1, 2, 3]

N = 3

print(increaseSize(lst, N))  
  
---  
  
 __

 __

 **Output:**

    
    
    [1, 1, 1, 2, 2, 2, 3, 3, 3]
    

  
**Approach #2 :** Using functools.reduce() method

  

  

The _reduce_ function apply a particular function passed in its argument to
all of the list elements. Therefore, in this approach we apply a function on
each element where it’s occurrence gets multiplied by N.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to increase list size

# by padding each element by N

from functools import reduce

 

def increaseSize(lst, N):

 

 return reduce(lambda x, y: x + y, [[el]*N for el in
lst])

 

# Driver code

lst = [1, 2, 3]

N = 3

print(increaseSize(lst, N))  
  
---  
  
 __

 __

 **Output:**

    
    
    [1, 1, 1, 2, 2, 2, 3, 3, 3]
    

  
**Approach #3 :** Using _itertools.chain()_

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to increase list size

# by padding each element by N

from itertools import chain

 

def increaseSize(lst, N):

 

 return list(chain(*([el]*N for el in lst)))

 

# Driver code

lst = [1, 2, 3]

N = 3

print(increaseSize(lst, N))  
  
---  
  
 __

 __

 **Output:**

    
    
    [1, 1, 1, 2, 2, 2, 3, 3, 3]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


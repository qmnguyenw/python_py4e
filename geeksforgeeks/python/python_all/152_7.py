Python | Unpacking tuple of lists



Given a tuple of lists, write a Python program to unpack the elements of the
lists that are packed inside the given tuple.

 **Examples:**

    
    
    **Input :** (['a', 'apple'], ['b', 'ball'])
    **Output :** ['a', 'apple', 'b', 'ball']
    
    **Input :** ([1, 'sam', 75], [2, 'bob', 39], [3, 'Kate', 87])
    **Output :** [1, 'sam', 75, 2, 'bob', 39, 3, 'Kate', 87]
    

  
**Approach #1 :** Using reduce()

reduce() is a classic list operation used to apply a particular function
passed in its argument to all of the list elements. In this case we used add
function of _operator_ module which simply adds the given list arguments to an
empty list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to unpack

# tuple of lists

from functools import reduce

import operator

 

def unpackTuple(tup):

 

 return (reduce(operator.add, tup))

 

# Driver code

tup = (['a', 'apple'], ['b', 'ball'])

print(unpackTuple(tup))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    ['a', 'apple', 'b', 'ball']
    


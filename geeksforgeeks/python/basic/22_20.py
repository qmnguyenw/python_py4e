Python groupby method to remove all consecutive duplicates



Given a string S, remove all the consecutive duplicates.

Examples:

    
    
    Input  : aaaaabbbbbb
    Output : ab
    
    Input : geeksforgeeks
    Output : geksforgeks
    
    Input : aabccba
    Output : abcba
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

We have existing solution for this problem please refer Remove all consecutive
duplicates from the string link. We can solve this problem in python quickly
using itertools.groupby() method.

### How itertools.groupby(iterable,key[optional]) works in Python ?

 **Group by** method takes two input one is **iterable
(list,tuple,dictionary)** and second is key function which calculates keys for
each element present in iterable. It returns key and iterable of grouped
items. If key function not specified or is None, key defaults to an identity
function and returns the element unchanged. For example,

  

  

 __

 __  
 __

 __

 __  
 __  
 __

numbers= [1, 1, 1, 3, 3, 2, 2, 2, 1,
1]

import itertools

for (key,group) in itertools.groupby(numbers):

 print (key,list(group))  
  
---  
  
 __

 __

Output:

    
    
    (1, [1, 1, 1])
    (3, [3, 3])
    (2, [2, 2])
    (1, [1, 1])
    

__

__  
__

__

__  
__  
__

# function to remove all consecutive duplicates

# from the string in Python

 

from itertools import groupby

def removeAllConsecutive(input):

 

 # group all consecutive characters based on their 

 # order in string and we are only concerned

 # about first character of each consecutive substring

 # in given string, so key value will work for us

 # and we will join these keys without space to 

 # generate resultant string

 result = []

 for (key,group) in groupby(input):

 result.append(key)

 

 print (''.join(result))

 

# Driver program

if __name__ == "__main__":

 input = 'aaaaabbbbbb'

 removeAllConsecutive(input)  
  
---  
  
 __

 __

 ** _References :_**  
https://docs.python.org/3/library/itertools.html

Output:

    
    
    ab
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


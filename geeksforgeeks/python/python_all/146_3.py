Python | Check if given string can be formed by concatenating string elements
of list



Given a string ‘str’ and a list of string elements, write a Python program to
check whether given string can be formed by concatenating the string elements
of list or not.

 **Examples:**

    
    
    **Input :** str = 'python'
            lst = ['co', 'de', 'py', 'ks', 'on']
    **Output :** False
    
    **Input :** str = 'geeks'
            lst = ['for', 'ge', 'abc', 'ks', 'e', 'xyz']
    **Output :** True
    

  
**Approach #1 :** Using itertools.permuations

We can use all the permutations of the given list and then perform _join_
operation on them. If any join result is equal to the given string, return
true, otherwise false.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to Check if given string can

# be formed by concatenating string elements 

# of list

from itertools import permutations

 

def checkList(str, lst):

 for i in range(2, len(lst)+1):

 for perm in permutations(lst, i):

 if ''.join(perm)== str:

 return True

 

 return False

 

# Driver code

str = 'geeks'

lst = ['for', 'ge', 'abc', 'ks', 'e', 'xyz']

print(checkList(str, lst))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    True
    


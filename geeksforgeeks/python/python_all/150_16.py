Python | Remove elements of list that are repeated less than k times



Given a list of integers (elements may be repeated), write a Python program to
remove the elements that are repeated less than k times.

 **Examples:**

    
    
    **Input :** lst = ['a', 'a', 'a', 'b', 'b', 'c'], k = 2
    **Output :** ['a', 'a', 'a', 'b', 'b']
    
    **Input :** lst = [1, 1, 1, 1, 2, 2, 3, 3, 3, 4, 4], k = 3
    **Output :** [1, 1, 1, 1, 3, 3, 3]
    

**Approach #1 :** Pythonic naive

Counter() from collections module construct a dictionary mapping values to
counts and save them in ‘counted’. Then we make use of ‘temp_lst’ to store the
elements that need to be removed. Finally, we traverse through the given list
and append all elements that are not in ‘temp_lst’ to ‘res_lst’ containing the
required output.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to Remove elements of

# list that repeated less than k times

from collections import Counter

 

def removeElements(lst, k):

 counted = Counter(lst)

 

 temp_lst = []

 for el in counted:

 if counted[el] < k:

 temp_lst.append(el)

 

 res_lst = []

 for el in lst:

 if el not in temp_lst:

 res_lst.append(el)

 

 return(res_lst)

 

# Driver code

lst = ['a', 'a', 'a', 'b', 'b', 'c']

k = 2

print(removeElements(lst, k))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    ['a', 'a', 'a', 'b', 'b']
    


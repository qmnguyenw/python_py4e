Python | Remove sublists that are present in another sublist



Given a list of lists, write a Python program to remove sublists from the
given list of lists that are present in another sublist.

 **Examples:**

    
    
    **Input :** [['a', 'b', 'c'], ['a', 'c'], ['a', 'b', 'c'], ['d']]
    **Output :** [['a', 'b', 'c'], ['d']]
    
    **Input :** [[1], [1, 2], [1, 2, 3], [0], [0, 1]]
    **Output :** [[1, 2, 3], [0, 1]]
    

  
**Approach #1 :** Using _Python Set_ (If order of list doesn’t matter)

This approach makes use of Python _sets_. Create two empty lists ‘curr_res’ to
store current sublist and ‘result’ to store the finalized sublists. Convert
the sub-lists in the given list of lists to sets and sort them by length in
reverse order, so that you can iterate through them and add each set to the
_curr_res_ only if it is not a subset of any of the existing sets in the
_curr_res_.  
The only drawback of this approach is that it may produce the result in an
unordered way(Since sets are unordered).

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to remove sublists from

# list of lists that are in another sublist

 

def removeSublist(lst):

 curr_res = []

 result = []

 for ele in sorted(map(set, lst), key = len, reverse
= True):

 if not any(ele <= req for req in curr_res):

 curr_res.append(ele)

 result.append(list(ele))

 

 return result

 

# Driver code

lst = [['a', 'b', 'c'], ['a', 'b'], ['a',
'b', 'c'], ['d']]

print(removeSublist(lst))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    [['c', 'b', 'a'], ['d']]
    


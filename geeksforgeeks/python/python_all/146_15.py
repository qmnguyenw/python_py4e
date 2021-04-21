Python | Remove repeated sublists from given list



Given a list of lists, write a Python program to remove all the repeated
sublists (also with different order) from given list.

 **Examples:**

    
    
    **Input :** [[1], [1, 2], [3, 4, 5], [2, 1]]
    **Output :** [[1], [1, 2], [3, 4, 5]]
    
    **Input :** [['a'], ['x', 'y', 'z'],  ['m', 'n'], ['a'], ['m', 'n']]
    **Output :** [['a'], ['x', 'y', 'z'], ['m', 'n']]
    

  
**Approach #1 :** _Set_ comprehension + Unpacking

Our first approach is to use _set_ comprehension with _sorted_ tuple. In every
iteration in the list, we convert the current sublist to a sorted tuple, and
return a set of all these tuples, which in turn eliminates all repeated
occurrences of the sublists and thus, remove all repeated rearranged sublists.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to Remove repeated

# unordered sublists from list

 

def Remove(lst):

 return ([list(i) for i in {*[tuple(sorted(i))
for i in lst]}]) 

 

# Driver code

lst = [[1], [1, 2], [3, 4, 5], [2, 1]]

print(Remove(lst))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    [[1, 2], [3, 4, 5], [1]]
    


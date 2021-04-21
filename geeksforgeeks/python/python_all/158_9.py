Python | Update a list of tuples using another list



Given two list of tuples, write a Python program to update ‘list1’ according
to the ‘list2’ and return an updated list.

 **Examples:**

    
    
    **Input :** list1 = [('x', 0), ('y', 5)]
            list2 = [('x', 100), ('y', 200)]
    **Output :** [('x', 100), ('y', 200)]
    
    **Input :** list1 = [('a', 0), ('b', 0), ('c', 0)]
            list2 = [('a', 1), ('b', 2)]
    **Output :** [('a', 1), ('b', 2), ('c', 0)]
    

  
**Approach #1** Pythonic Naive  
This is a Pythonic naive approach. We simply convert the list of tuples into a
dictionary and just update it with _list2_ and convert the dictionary back to
list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to Update a list

# of tuples according to another list

 

def merge(list1, list2): 

 dic = dict(list1)

 dic.update(dict(list2))

 return list(dic.items())

 

# Driver Code

list1 = [('a', 0), ('b', 0), ('c', 0)]

list2 = [('a', 5), ('c', 3)]

print(merge(list1, list2))  
  
---  
  
 __

 __

 **Output:**

    
    
    [('a', 5), ('b', 0), ('c', 3)]
    

  
**Approach #2** Using _defaultdict_  
Python collections module provides _defaultdict()_ method which is used in
this approach. First we initialize ‘dic’ with defaultdict method passing list
as factory. Use a loop to append the left element of each tuple as key and
right element of each tuple as value for both the lists. Now simply use the
sorted function and produce the list in such a way that the for each unique
key it keeps the maximum value of right element of tuple.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to Update a list

# of tuples according to another list

 

from collections import defaultdict

 

def merge(list1, list2): 

 dic = defaultdict(list)

 for i, j in list1 + list2:

 dic[i].append(j)

 

 return sorted([(i, max(j)) for i, j in dic.items()],

 key = lambda x:x[0])

 

# Driver Code

list1 = [('a', 0), ('b', 0), ('c', 0)]

list2 = [('a', 5), ('c', 3)]

print(merge(list1, list2))  
  
---  
  
 __

 __

 **Output:**

    
    
    [('a', 5), ('b', 0), ('c', 3)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


Python | Record Similar tuple occurrences



Sometimes, while working with data, we can have a problem in which we need to
check the occurrences of records which occur similar times. This has
application in web development domain. Let’s discuss certain ways in which
this task can be performed.

 **Method #1 : Usingmap() + Counter() \+ sorted**

The combination of above functionalities can be used to perform this task. In
this, we before feeding data to Counter(), for counting occurrences, sort
the data to make all unordered tuple ordered to count similar ones as one.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Record Similar tuple occurrences

# Using Counter() + map() + sorted

from collections import Counter

 

# initialize list 

test_list = [(3, 1), (1, 3), (2, 5), (5,
2), (6, 3)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Record Similar tuple occurrences

# Using Counter() + map() + sorted

res = dict(Counter(tuple(ele) for ele in map(sorted,
test_list)))

 

# printing result

print("The frequency of like tuples : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [(3, 1), (1, 3), (2, 5), (5, 2), (6, 3)]
    The frequency of like tuples : {(2, 5): 2, (1, 3): 2, (3, 6): 1}
    

  

  

**Method #2 : Usingfrozenset() + Counter()**

The combination of above functions can be used to perform this particular
task. In this, the task performed by sorted and map() is performed by the
frozenset() which orders the tuples internally.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Record Similar tuple occurrences

# Using frozenset() + Counter()

from collections import Counter

 

# initialize list 

test_list = [(3, 1), (1, 3), (2, 5), (5,
2), (6, 3)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Record Similar tuple occurrences

# Using frozenset() + Counter()

res = dict(Counter(tuple(frozenset(ele)) for ele in
test_list))

 

# printing result

print("The frequency of like tuples : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [(3, 1), (1, 3), (2, 5), (5, 2), (6, 3)]
    The frequency of like tuples : {(2, 5): 2, (1, 3): 2, (3, 6): 1}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


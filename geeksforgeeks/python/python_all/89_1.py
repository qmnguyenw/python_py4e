Python – Count similar pair in Dual List



Sometimes, while working with data, we can have a problem in which we receive
the dual elements pair and we intend to find pairs of similar elements and
it’s frequency. This kind of data is usually useful in data domains. Let’s
discuss certain ways in which this task can be performed.

 **Method #1 : UsingCounter() + map() + sorted() + items()**  
The combination of above functions can be used to achieve this particular
task. In this, we first find frequency using Counter and then link it in a
tuple using map(). The sorted() peforms task of sorting before using above
method.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Count Similar pair in dual list

# using Counter() + map() + sorted() + items()

from collections import Counter

 

# initializing list 

test_list = [[1, 2], [2, 1], [3, 4], [4,
3], [5, 4]]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# Count Similar pair in dual list

# using Counter() + map() + sorted() + items()

temp = [sorted(ele) for ele in test_list]

res = [(i, j, k) for (i, j), k in Counter(map(tuple,
temp)).items()]

 

# printing result 

print ("The dual list similarity counts : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [[1, 2], [2, 1], [3, 4], [4, 3], [5, 4]]
    The dual list similarity counts : [(1, 2, 2), (4, 5, 1), (3, 4, 2)]
    

**Method #2 : Usingsum() + list comprehension + groupby() + sorted()**  
In this method, the task of counting is performed using sum() and task of
getting group is performed using groupby().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Count Similar pair in dual list

# using sum() + list comprehension + groupby() + sorted()

from itertools import groupby

 

# initializing list 

test_list = [[1, 2], [2, 1], [3, 4], [4,
3], [5, 4]]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# Count Similar pair in dual list

# using sum() + list comprehension + groupby() + sorted()

res = [(*temp, sum(1 for idx in elements))

 for temp, elements in groupby(test_list, key = lambda j :
sorted(j))]

 

# printing result 

print ("The dual list similarity counts : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [[1, 2], [2, 1], [3, 4], [4, 3], [5, 4]]
    The dual list similarity counts : [(1, 2, 2), (4, 5, 1), (3, 4, 2)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


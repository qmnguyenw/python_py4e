Python | Group tuple into list based on value



Sometimes, while working with Python tuples, we can have a problem in which we
need to group tuple elements to nested list on basis of values alloted to it.
This can be useful in many grouping applications. Let’s discuss certain ways
in which this task can be performed.

 **Method #1 : Usingitemgetter() \+ list comprehension + groupby()**

The combination of above functions can be used to perform this task. In this,
we access the value using itemgetter() and logic for grouping is performed
using groupby() and list comprehension.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Group tuple into list based on value

# using itemgetter() + list comprehension + groupby()

from operator import itemgetter

from itertools import groupby

 

# initialize list 

test_list = [(1, 4), (2, 4), (6, 7), (5,
1), (6, 1), (8, 1)]

 

# printing original list 

print("The original list : " + str(test_list))

 

# Group tuple into list based on value

# using itemgetter() + list comprehension + groupby()

res = [[i for i, j in temp]\

 for key, temp in groupby(test_list, key = itemgetter(1))]

 

# printing result

print("The list after grouping by value : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [(1, 4), (2, 4), (6, 7), (5, 1), (6, 1), (8, 1)]
    The list after grouping by value : [[1, 2], [6], [5, 6, 8]]
    

  

  

**Method #2 : Usingmap() + itemgetter() + groupby() \+ list comprehension**

This method is similar to the above method, the only difference is that we
chose map for formation of keys as nested list for formation of new resultant
lists.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Group tuple into list based on value

# using map() + itemgetter() + groupby() + list comprehension

from operator import itemgetter

from itertools import groupby

 

# initialize list 

test_list = [(1, 4), (2, 4), (6, 7), (5,
1), (6, 1), (8, 1)]

 

# printing original list 

print("The original list : " + str(test_list))

 

# Group tuple into list based on value

# using map() + itemgetter() + groupby() + list comprehension

res = [list(map(itemgetter(0), temp)) 

 for (key, temp) in groupby(test_list, itemgetter(1))]

 

# printing result

print("The list after grouping by value : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [(1, 4), (2, 4), (6, 7), (5, 1), (6, 1), (8, 1)]
    The list after grouping by value : [[1, 2], [6], [5, 6, 8]]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


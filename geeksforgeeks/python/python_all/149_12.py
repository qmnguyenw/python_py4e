Python | Grouped summation of tuple list



Many times, we are given a list of tuples and we need to group its keys and
perform certain operation while grouping. The most common operation being
addition. Let’s discuss certain ways in which this task can be performed.
Apart from addition other operations can also be performed by doing small
changes.

 **Method : UsingCounter() \+ "+" operator**

This task can be performed using the Counter function as it internally groups
and addition operator can be used to specify the functionality on the grouped
result.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# group summation of tuple list 

# using Counter() + "+" operator

from collections import Counter

 

# initializing list of tuples

test_list1 = [('key1', 4), ('key3', 6), ('key2',
8)]

test_list2 = [('key2', 1), ('key1', 4), ('key3',
2)]

 

# printing original lists

print("The original list 1 : " + str(test_list1))

print("The original list 2 : " + str(test_list2))

 

# using Counter() + "+" operator

# group summation of tuple list 

cumul_1 = Counter(dict(test_list1))

cumul_2 = Counter(dict(test_list2))

cumul_3 = cumul_1 + cumul_2 

res = list(cumul_3.items())

 

# print result

print("The grouped summation tuple list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 : [('key1', 4), ('key3', 6), ('key2', 8)]
    The original list 2 : [('key2', 1), ('key1', 4), ('key3', 2)]
    The grouped summation tuple list is : [('key2', 9), ('key1', 8), ('key3', 8)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


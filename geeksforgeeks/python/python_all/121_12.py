Python | Tuples with maximum key of similar values



Sometimes, while working with Python, we can have a problem in which we need
to get all the records. This data can have similar values and we need to find
maximum key’ed value pair. This kind of problem can occur while working with
data. Let’s discuss certain ways in which this task can be done.

 **Method #1 : Using max() + groupby() + itemgetter() \+ list
comprehension**  
The combination of above functions can be used to perform this particular
task. In this, we first group the like valued elements using groupby() and
itemgetter(), and then extract the maximum of those using max() and
cummulate the result in list using list comprehension.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Tuples with maximum key of similar values

# using max() + groupby() + itemgetter() + list comprehension

from operator import itemgetter

from itertools import groupby

 

# initialize list

test_list = [(4, 3), (2, 3), (3, 10), (5,
10), (5, 6)]

 

# printing original list

print("The original list : " + str(test_list))

 

# Tuples with maximum key of similar values

# using max() + groupby() + itemgetter() + list comprehension

res = [max(values) for key, values in groupby(test_list, key
= itemgetter(1))]

 

# printing result

print("The records retaining maximum keys of similar values : " +
str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [(4, 3), (2, 3), (3, 10), (5, 10), (5, 6)]
    The records retaining maximum keys of similar values : [(4, 3), (5, 10), (5, 6)]
    

**Method #2 : Using setdefault() + items() \+ loop + list comprehension**  
The combination of above functions can also achieve this task. In this, we
convert the list tuple key-value pairs into a dictionary and assign a default
value using setdefault(). The final result is computed using list
comprehension.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Tuples with maximum key of similar values

# using setdefault() + items() + loop + list comprehension

 

# initialize list

test_list = [(4, 3), (2, 3), (3, 10), (5,
10), (5, 6)]

 

# printing original list

print("The original list : " + str(test_list))

 

# Tuples with maximum key of similar values

# using setdefault() + items() + loop + list comprehension

temp = {}

for val, key in test_list:

 if val > temp.setdefault(key, val):

 temp[key] = val

res = [(val, key) for key, val in temp.items()]

 

# printing result

print("The records retaining maximum keys of similar values : " +
str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [(4, 3), (2, 3), (3, 10), (5, 10), (5, 6)]
    The records retaining maximum keys of similar values : [(4, 3), (5, 10), (5, 6)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


Python | Replace duplicates in tuple



Sometimes, while working with Python tuples, we can have a problem in which we
need to remove tuples elements that occur more than one times and replace
duplicas with some custom value. Let’s discuss certain ways in which this task
can be performed.

 **Method #1 : Usingset() \+ list comprehension**  
The combination of above functionalities can be used to perform this
particular task. In this, we just initialize a set container and then replace
the reoccurring elements with a value after checking its existance it’s
existance in tuple.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Replace duplicates in tuple

# using set() + list comprehension

 

# initialize tuple

test_tup = (1, 1, 4, 4, 4, 5, 5, 6,
7, 7)

 

# printing original tuple

print("The original tuple is : " + str(test_tup))

 

# Replace duplicates in tuple

# using set() + list comprehension

temp = set()

res = tuple(ele if ele not in temp and not
temp.add(ele) 

 else 'gfg' for ele in test_tup)

 

# printing result

print("Tuple after replacing values : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple is : (1, 1, 4, 4, 4, 5, 5, 6, 7, 7)
    Tuple after replacing values : (1, 'gfg', 4, 'gfg', 'gfg', 5, 'gfg', 6, 7, 'gfg')
    

**Method #2 : Usinggroupby() \+ loop**  
The combination of above functionalities can be solved using this problem. In
this, we just group the consecutive elements and then replace each element
except for 1st with default value. Works only in case of consecutive
duplicates.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Replace duplicates in tuple

# using groupby() + loop

from itertools import groupby

 

# initialize tuple

test_tup = (1, 1, 4, 4, 4, 5, 5, 6,
7, 7)

 

# printing original tuple

print("The original tuple is : " + str(test_tup))

 

# Replace duplicates in tuple

# using groupby() + loop

res = tuple()

for key, ele in groupby(test_tup):

 res = res + ((key, ) + ('gfg', ) *
(len(list(ele))-1))

 

# printing result

print("Tuple after replacing values : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple is : (1, 1, 4, 4, 4, 5, 5, 6, 7, 7)
    Tuple after replacing values : (1, 'gfg', 4, 'gfg', 'gfg', 5, 'gfg', 6, 7, 'gfg')
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


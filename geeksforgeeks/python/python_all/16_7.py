Python Program To Get Minimum Elements For String Construction



Given a String, the task is to write a Python program to count the minimum
elements required to form a string from list elements.

>  **Input** : test_list = [“geek”, “ring”, “sfor”, “ok”, “woke”], tar_str =
> “working”  
> **Output** : 2  
> **Explanation** : working can be formed using woke and ring.
>
>  **Input** : test_list = [“geek”, “ring”, “sfor”, “ok”, “woke”], tar_str =
> “workinggeek”  
> **Output** : 3  
> **Explanation** : workinggeek can be formed using woke, geek and ring.  
>

**Method :** Using issubset() \+ set() \+ combinations()

In this, we iterate for a list of strings and form all size combinations, each
combination is converted to set and checked to be forming target string using
issubset(), if found, the loop is exited and the count is recorded.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Minimum elements for String construction

# Using issubset() + set() + combinations()

from itertools import combinations

 

# initializing list

test_list = ["geek", "ring", "sfor", "ok", "woke"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing target string 

tar_str = "working"

 

res = -1

set_str = set(tar_str)

done = False

for val in range(0, len(test_list) + 1):

 

 # creating combinations

 for sub in combinations(test_list, val):

 

 # contructing sets of each combinations 

 temp_set = set(ele for subl in sub for ele in subl)

 

 # checking if target string has created set as subset

 if set_str.issubset(temp_set):

 res = val

 done = True

 break

 if done:

 break

 

# printing result 

print("The Minimum count elements for string : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : ['geek', 'ring', 'sfor', 'ok', 'woke']
    The Minimum count elements for string : 2

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


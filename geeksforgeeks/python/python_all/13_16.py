Python – All replacement combination from other list



Given a list, the task is to write a Python program to perform all possible
replacements from other lists to the current list.

>  **Input** : test_list = [4, 1, 5], repl_list = [8, 10]  
> **Output** : [(4, 1, 5), (4, 1, 8), (4, 1, 10), (4, 5, 8), (4, 5, 10), (4,
> 8, 10), (1, 5, 8), (1, 5, 10), (1, 8, 10), (5, 8, 10)]  
> **Explanation** : All elements are replaced by 0 or more elements from 2nd
> list  
>
>
> **Input** : test_list = [4, 1], repl_list = [8, 10]  
> **Output** : [(4, 1), (4, 8), (4, 10), (1, 8), (1, 10), (8, 10)]  
> **Explanation** : All elements are replaced by 0 or more elements from 2nd
> list

**Method #1 : Using** **combinations()** **+** **len()**

In this, we perform the task of constructing combinations of the merged lists
using _combinations()_ and _len()_ is used to restrict the size of output to
the length of the initial list.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# All replacement combination from other list

# Using combinations() + len()

from itertools import combinations

 

# initializing list

test_list = [4, 1, 5]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing replacement list

repl_list = [8, 10]

 

# using combinations() to get all combinations replacements

res = list(combinations(test_list + repl_list,
len(test_list)))

 

# printing result

print("All combinations replacements from other list : " +
str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [4, 1, 5]  
> All combinations replacements from other list : [(4, 1, 5), (4, 1, 8), (4,
> 1, 10), (4, 5, 8), (4, 5, 10), (4, 8, 10), (1, 5, 8), (1, 5, 10), (1, 8,
> 10), (5, 8, 10)]

 **Method #2 : Using** **combinations()** **+** **extend()**

In this, we perform the task of concatenating the list using extend(), rest
all the functionalities is similar to the above method.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# All replacement combination from other list

# Using combinations() + extend()

from itertools import combinations

 

# initializing list

test_list = [4, 1, 5]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing replacement list 

repl_list = [8, 10]

 

# using combinations() to get all combinations replacements

# extend() for concatenation

n = len(test_list)

test_list.extend(repl_list)

res = list(combinations(test_list, n))

 

# printing result 

print("All combinations replacements from other list : " +
str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [4, 1, 5]  
> All combinations replacements from other list : [(4, 1, 5), (4, 1, 8), (4,
> 1, 10), (4, 5, 8), (4, 5, 10), (4, 8, 10), (1, 5, 8), (1, 5, 10), (1, 8,
> 10), (5, 8, 10)]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


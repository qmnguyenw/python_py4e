Python – Smallest integer possible from combination of list elements



Given a list of integers, the task is to get smallest integer possible from
the combination of list elements. This is one of the problems that is
essential in a competitive point of view and this article discusses various
shorthands to solve this problem in Python. Let’s discuss certain ways in
which this problem can be solved.

 **Method #1 : Usingsorted() \+ lambda**  
The combination of the above function can be used to perform this task. The
sorted function performs the sort of list indices converted into string and
lambda functions handle the conversion and iteration operation.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# Smallest number from list

# using sorted() + lambda

import functools

 

# initializing list 

test_list = [23, 65, 98, 3, 4]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# lambda for custom operation

custom = lambda i, j: -1 if str(j) + str(i) >
str(i) + str(j) else 1

 

# using sorted() + custom function

# Smallest number from list 

res = sorted(test_list, key = functools.cmp_to_key(custom))

 

 

# printing result 

print ("The smallest possible number : " + "".join(map(str,
res)))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [23, 65, 98, 3, 4]
    The smallest possible number : 23346598
    

**Method #2 : Usingitertools.permutation() + join() + min()**

  

  

The itertools.permutation can be used to get possible permutation and min
function chooses the minimum of it after being converted to integer as a
result of joined output as given by join function.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Smallest number from list

# using itertools.permutation() + join() + min()

from itertools import permutations

 

# initializing list 

test_list = [23, 65, 98, 3, 4]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# using itertools.permutation() + join() + min()

# Smallest number from list

res = int(min((''.join(i) for i in permutations(str(i)


 for i in test_list)), key = int))

 

# printing result 

print ("The smallest possible number : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [23, 65, 98, 3, 4]
    The smallest possible number : 23346598
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


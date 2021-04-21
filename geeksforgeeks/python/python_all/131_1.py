Python | Incremental slice partition in list



Sometimes, while working with lists, we can come across a problem in which we
need to slice a list incrementally, i.e, with each slice, number of elements
increase by 1. This has application in competitive programming. Let’s discuss
certain ways in which this task can be performed.

 **Method #1 : Using loops**  
This is the brute force method by which this task can be performed. We just
manually count and increase the counter with each iteration for slicing and
dictionary key creation.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Incremental slice partition in list

# Using loop

 

# initializing list

test_list = [1, 2, 3, 4, 5, 6, 7, 8,
9, 10]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Incremental slice partition in list

# Using loop

res = {}

N = 1

strt = 0

while strt < len(test_list):

 res[N] = test_list[strt : strt + N]

 strt += N

 N += 1

 

# printing result 

print("The partitioned dictionary from list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list is : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
> The partitioned dictionary from list is : {1: [1], 2: [2, 3], 3: [4, 5, 6],
> 4: [7, 8, 9, 10]}

  

  

**Method #2 : Usingenumerate() + slice() + next() + iter() + count()**  
The combination of above functions can be used to perform this task. In this,
next() is used to iterate the list converted to iterator by iter(). The
slice() performs list slicing. The count() helps in managing the counter and
enumerate keeps track of element and indices in list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Incremental slice partition in list

# Using enumerate() + slice() + next() + iter() + count()

from itertools import islice, count

 

# initializing list

test_list = [1, 2, 3, 4, 5, 6, 7, 8,
9, 10]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Incremental slice partition in list

# Using enumerate() + slice() + next() + iter() + count()

res = {key : val for key, val in enumerate(iter(lambda
i = iter(test_list),

 c = count(1): list(islice(i, next(c))), []), 1)}

 

# printing result 

print("The partitioned dictionary from list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list is : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
> The partitioned dictionary from list is : {1: [1], 2: [2, 3], 3: [4, 5, 6],
> 4: [7, 8, 9, 10]}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


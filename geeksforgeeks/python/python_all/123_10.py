Python | Convert list elements to bi-tuples



Sometimes, while working with Python lists, we can have a subproblem in which
we need to tie a particular element with each of the list element. This task
can have it’s utility in web development domain while working with queries and
filters. Let’s discuss a ways to solve this problem.

 **Method : Usingzip() + repeat()**

This problem can be solved using zip() which can be used to attach to each
list element with a decided number using repeat().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert list elements to bi-tuples

# using zip() + repeat()

from itertools import repeat

 

# initialize list

test_list = [5, 6, 7, 8, 4, 3]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initialize attach element

ele = 'gfg'

 

# Convert list elements to bi-tuples

# using zip() + repeat()

res = list(zip(test_list, repeat(ele)))

 

# printing result

print("Tuple list after attaching element : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list is : [5, 6, 7, 8, 4, 3]  
> Tuple list after attaching element : [(5, ‘gfg’), (6, ‘gfg’), (7, ‘gfg’),
> (8, ‘gfg’), (4, ‘gfg’), (3, ‘gfg’)]
>
>  
>
>
>  
>

**Method #2 : Usingmap() \+ lambda**  
This is yet another way in which this task can be performed. In this, we just
extend the logic of adding element to list element to all elements using
map(), by feeding it with lambda function to perform computation tasks.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert list elements to bi-tuples

# using map() + lambda

from itertools import repeat

 

# initialize list

test_list = [5, 6, 7, 8, 4, 3]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initialize attach element

ele = 'gfg'

 

# Convert list elements to bi-tuples

# using map() + lambda

res = list(map(lambda key : (key, ele), test_list))

 

# printing result

print("Tuple list after attaching element : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list is : [5, 6, 7, 8, 4, 3]  
> Tuple list after attaching element : [(5, ‘gfg’), (6, ‘gfg’), (7, ‘gfg’),
> (8, ‘gfg’), (4, ‘gfg’), (3, ‘gfg’)]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


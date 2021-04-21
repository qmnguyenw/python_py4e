Python | Altering duplicate values from given list



Many times we deal with the lists having identical numbers as a sequence and
we wish to just keep the 1st occurrence of element and substituting all the
occurrences with the different number. Let’s discuss certain ways in which
this can be done.

 **Method #1 : Using list comprehension +enumerate()**

This task can be achieved using the list comprehension for traversal and
checking for element occurrence and index checking can be done using enumerate
function.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Altering duplicated

# using list comprehension + enumerate()

 

# initializing list

test_list = [2, 2, 3, 3, 3, 3, 4, 4,
5, 5, 5]

 

# printing original list

print("The original list : " + str(test_list))

 

# using list comprehension + enumerate()

# Altering duplicated

res = [False if (ele in test_list[ :idx]) else ele 

 for idx, ele in enumerate(test_list)]

 

# print result

print("The altered duplicate list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list : [2, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5]  
> The altered duplicate list is : [2, False, 3, False, False, False, 4, False,
> 5, False, False]
>
>  
>
>
>  
>

**Method #2 : Usingitertools.groupby() \+ list comprehension**

This particular task can also be performed using a combination of above
function, using groupby function to get the groups of different elements and
list comprehension to alter duplicates.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Altering duplicated

# using itertools.groupby() + list comprehension

from itertools import groupby

 

# initializing list

test_list = [2, 2, 3, 3, 3, 3, 4, 4,
5, 5, 5]

 

# printing original list

print("The original list : " + str(test_list))

 

# using itertools.groupby() + list comprehension

# Altering duplicated

res = [val for key, grp in groupby(test_list) 

 for val in [key] + [False] *
(len(list(grp))-1)]

 

# print result

print("The altered duplicate list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list : [2, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5]  
> The altered duplicate list is : [2, False, 3, False, False, False, 4, False,
> 5, False, False]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


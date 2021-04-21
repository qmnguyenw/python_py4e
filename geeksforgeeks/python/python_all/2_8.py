Python – Group contiguous strings in List



Given a mixed list, the task is to write a python program to group all the
contiguous strings.

    
    
    **Input :** test_list = [5, 6, 'g', 'f', 'g', 6, 5, 'i', 's', 8, 'be', 'st', 9]
    **Output :** [5, 6, ['g', 'f', 'g'], 6, 5, ['i', 's'], 8, ['be', 'st'], 9]
    **Explanation :** Strings are grouped to form result.
    
    **Input :** test_list = [5, 6, 6, 5, 'i', 's', 8, 'be', 'st', 9]
    **Output :** [5, 6, 6, 5, ['i', 's'], 8, ['be', 'st'], 9]
    **Explanation :** Strings are grouped to form result.

 **Method : Using** **isinstance()** **+** **generator** **+** **groupby()**

In this, we perform the task of identifying strings using _isinstance()_ and
_str, groupby()_ is used to group all the strings found by key using
_isinstance()_. The generator way of building a list helps to convert the
intermediate results to a list.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Group contiguous strings in List

# Using isinstance() + generator + groupby()

from itertools import groupby

 

# checking string instance

def str_check(ele):

 return isinstance(ele, str)

 

 

def group_strs(test_list):

 

 # grouping list by cont. strings

 for key, grp in groupby(test_list, key=str_check):

 if key:

 yield list(grp)

 else:

 yield from grp

 

 

# initializing list

test_list = [5, 6, 'g', 'f', 'g', 6, 5,

 'i', 's', 8, 'be', 'st', 9]

 

# printing original list

print("The original list is : " + str(test_list))

 

# calling recursion fnc.

res = [*group_strs(test_list)]

 

# printing result

print("List after grouping : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [5, 6, ‘g’, ‘f’, ‘g’, 6, 5, ‘i’, ‘s’, 8, ‘be’, ‘st’,
> 9]
>
>  
>
>
>  
>
>
> List after grouping : [5, 6, [‘g’, ‘f’, ‘g’], 6, 5, [‘i’, ‘s’], 8, [‘be’,
> ‘st’], 9]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


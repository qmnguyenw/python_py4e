Python – Find union of multiple sets



Given multiple sets list, the task is to write a Python program to find union
of each set.

 **Examples:**

>  **Input :** test_list = [{4, 3, 5, 2}, {8, 4, 7, 2}, {1, 2, 3, 4}, {9, 5,
> 3, 7}]
>
>  **Output :** {1, 2, 3, 4, 5, 7, 8, 9}
>
>  **Explanation :** All elements from all sets included. Duplicates removed.
>
>  
>
>
>  
>
>
>  **Input :** test_list = [{4, 3, 5, 2}, {8, 4, 7, 2}, {1, 2, 3, 4}]
>
>  **Output :** {1, 2, 3, 4, 5, 7, 8}
>
>  **Explanation :** All elements from all sets included. Duplicates removed.

 **Method #1 : Using** **union()** **\+ * operator**

In this, we perform task of getting union using union(), and * operator is
used to perform task of packing all the sets together.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Union multiple sets

# Using union() + * operator

 

# initializing list

test_list = [{4, 3, 5, 2}, {8, 4, 7, 2},
{1, 2, 3, 4}, {9, 5, 3, 7}]

 

# printing original list

print("The original list is : " + str(test_list))

 

# * operator packs sets for union

res = set().union(*test_list)

 

# printing result

print("Multiple set union : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [{2, 3, 4, 5}, {8, 2, 4, 7}, {1, 2, 3, 4}, {9, 3, 5,
> 7}]
>
> Multiple set union : {1, 2, 3, 4, 5, 7, 8, 9}
>
>  
>
>
>  
>

 **Method #2 : Using** **chain.from_iterable()** **\+ * operator**

In this, we perform task of union, which in turn is flattening using
from_iterable().

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Union multiple sets

# Using chain.from_iterable() + * operator

from itertools import chain

 

# initializing list

test_list = [{4, 3, 5, 2}, {8, 4, 7, 2},
{1, 2, 3, 4}, {9, 5, 3, 7}]

 

# printing original list

print("The original list is : " + str(test_list))

 

# * operator packs sets for union

res = set(chain(*test_list))

 

# printing result

print("Multiple set union : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [{2, 3, 4, 5}, {8, 2, 4, 7}, {1, 2, 3, 4}, {9, 3, 5,
> 7}]
>
> Multiple set union : {1, 2, 3, 4, 5, 7, 8, 9}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


Python – Remove Columns of Duplicate Elements



Given a Matrix, write a Python program to remove whole column if duplicate
occurs in any row.

 **Examples:**

>  **Input** : test_list = [[4, 3, 5, 2, 3], [6, 4, 2, 1, 1], [4, 3, 9, 3, 9],
> [5, 4, 3, 2, 1]]  
> **Output** : [[4, 3, 5], [6, 4, 2], [4, 3, 9], [5, 4, 3]]  
> **Explanation** : 1 has duplicate as next element hence 5th column is
> removed. 3 occurs as 2nd and 4th index, hence 4th index is removed.
>
>  **Input** : test_list = [[6, 4, 2, 1, 1], [4, 3, 9, 3, 9], [5, 4, 3, 2, 1]]  
> **Output** : [[6, 4, 2], [4, 3, 9], [5, 4, 3]]  
> **Explanation** : 1 has duplicate as next element hence 5th column is
> removed. 3 occurs as 2nd and 4th index, hence 4th index is removed.  
>

**Approach: Using** **list comprehension** **+** **set()** **+**
**chain.from_iterable()** **+** **generator** **\+ loop**

  

  

In this, indices which are duplicate elements are extracted as first step
using generator function and set(). In the second step, all the required
columns are excluded while reconstruction of Matrix.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove Columns of Duplicate Elements

# Using list comprehension + set() + 

# chain.from_iterable() + generator + loop

from itertools import chain

 

 

def dup_idx(sub):

 

 memo = set()

 for idx, ele in enumerate(sub):

 

 # adding element if not there

 if ele not in memo:

 memo.add(ele)

 else:

 

 # return index is Duplicate

 yield idx

 

 

# initializing list

test_list = [[4, 3, 5, 2, 3], [6, 4, 2,
1, 1],

 [4, 3, 9, 3, 9], [5, 4, 3, 2, 1]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K

K = 3

 

# passing each row to generator function

# flattening indices at end

temp_idxs = set(chain.from_iterable(dup_idx(sub) for sub in
test_list))

 

# extracting columns with only non-duplicate indices values

res = [[ele for idx, ele in enumerate(

 sub) if idx not in temp_idxs] for sub in test_list]

 

# printing result

print("The filtered Matrix : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[4, 3, 5, 2, 3], [6, 4, 2, 1, 1], [4, 3, 9, 3, 9],
> [5, 4, 3, 2, 1]]  
> The filtered Matrix : [[4, 3, 5], [6, 4, 2], [4, 3, 9], [5, 4, 3]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


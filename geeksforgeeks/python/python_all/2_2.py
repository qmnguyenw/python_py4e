Python Program to Extract Elements from list in set



Given a list, the task is to write a Python Program to extract all the
elements with its occurrence matching in set.

>  **Input :** test_list = [5, 6, 2, 3, 2, 6, 5, 8, 9], search_set = {6, 2, 8}
>
>  **Output :** [6, 2, 2, 6, 8]
>
>  **Explanation :** 2, 6 occur twice and in order with respect to other
> elements is output.
>
>  **Input :** test_list = [5, 6, 2, 3, 2, 6, 5, 8, 9], search_set = {8, 3, 5}
>
>  
>
>
>  
>
>
>  **Output :** [5, 3, 5, 8]
>
>  **Explanation :** 5 occurs twice and in order with respect to other
> elements is output.

 **Method #1 : Using loop**

In this, each list element is iterated and checked for its presence in set
using in operator and appended to result if found.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Elements from list in set

# Using loop

 

# initializing list

test_list = [5, 6, 2, 3, 2, 6, 5, 8,
9]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing search set

search_set = {6, 2, 8}

 

res = []

for ele in test_list:

 

 # check if element is present in set

 if ele in search_set:

 res.append(ele)

 

# printing result

print("Set present list elements : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [5, 6, 2, 3, 2, 6, 5, 8, 9]
    Set present list elements : [6, 2, 2, 6, 8]

 **Method #2 : Using** **repeat()** **\+ from_iterable() +** **count()**

In this, we test for each set element in list and repeat using repeat() by the
count required to be computed using count(). The order is not maintained in
this result.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Elements from list in set

# Using repeat() + from_iterable() + count()

from itertools import chain, repeat

 

# initializing list

test_list = [5, 6, 2, 3, 2, 6, 5, 8,
9]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing search set

search_set = {6, 2, 8}

 

# repeat repeats all the occurrences of elements

res = list(chain.from_iterable((repeat(ele, test_list.count(ele)) 

 for ele in search_set)))

 

# printing result

print("Set present list elements : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [5, 6, 2, 3, 2, 6, 5, 8, 9]
    Set present list elements : [6, 2, 2, 6, 8]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


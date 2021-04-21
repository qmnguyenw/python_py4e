Python Program to assign each list element value equal to its magnitude order



Given a list, the task is to write a Python program to assign each element
value equal to its magnitude order.

>  **Input :** test_list = [8, 3, 5, 8, 1, 5, 4]
>
>  **Output :** [4, 1, 3, 4, 0, 3, 2]
>
>  **Explanation :** 8 is 5th maximum hence 4 [starting from 0th index] is
> assigned to it.
>
> **Input :** test_list = [3, 2, 0]
>
>  
>
>
>  
>
>
>  **Output :** [2, 1, 0]
>
>  **Explanation :** 3 is 3rd maximum as 2 is assigned.

**Method 1 : Using** **set()** **+** **zip()** **+** **dict()** **+** **list
comprehension**

In this, we perform task of mapping sorted index of set converted list to
values using zip(), and then convert to dictionary of value mapped to values.
Then list comprehension is used to ordering in list.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Relative Size Ordering 

# Using set() + zip() + sorted() + dict() + list comprehension

 

# initializing list

test_list = [8, 3, 5, 8, 1, 5, 4]

 

# printing original list

print("The original list is : " + str(test_list))

 

# assigning order to each value

ord_dict = dict(zip(list(set(test_list)),

 range(len(set(test_list)))))

 

# mapping element with ordered value

res = [ord_dict[ele] for ele in test_list]

 

# printing result

print("Relative size ordered list : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [8, 3, 5, 8, 1, 5, 4]
    Relative size ordered list : [4, 1, 3, 4, 0, 3, 2]

 **Method 2 : Using** **sorted()** **+** **set()** **+** **index()** **+**
**list comprehension**

In this, we perform task of conversion to set and then sort, index mapping to
order is done using index() and list comprehension.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Relative Size Ordering 

# Using sorted() + set() + index() + list comprehension

 

# initializing list

test_list = [8, 3, 5, 8, 1, 5, 4]

 

# printing original list

print("The original list is : " + str(test_list))

 

# getting order

ord_dict = list(set(test_list))

 

# mapping index

res = [ord_dict.index(ele) for ele in test_list]

 

# printing result

print("Relative size ordered list : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [8, 3, 5, 8, 1, 5, 4]
    Relative size ordered list : [4, 1, 3, 4, 0, 3, 2]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


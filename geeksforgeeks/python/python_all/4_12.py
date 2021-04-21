Python – First occurrence of one list in another



Given two lists, the task is to write a Python program to extract the first
element that occurs in list 1 from list 2.

 **Examples:**

>  **Input :** test_list1 = [1, 6, 3, 7, 8, 9, 2], test_list2 = [4, 10, 8, 2,
> 0, 11]
>
>  **Output :** 8
>
>  **Explanation :** 8 is first element from list 2, that occurs in list 1, in
> 5th index.
>
>  
>
>
>  
>
>
>  **Input :** test_list1 = [1, 6, 3, 7, 8, 9, 2], test_list2 = [4, 10, 18,
> 12, 0, 11]
>
>  **Output :** None
>
>  **Explanation :** No element of list 2 found in list 1.

 **Approach : Using** **set()** **\+ next()**

In this, initially, the check container is converted to set, and each element
is checked using next() and generator expression. The next() function returns
the first element matching, else if no match element is found, None is
returned.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# First occurrence of one list in another

# Using next() + set()

 

# initializing lists

test_list1 = [1, 6, 3, 7, 8, 9, 2]

test_list2 = [4, 10, 8, 2, 0, 11]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# converting test list to sets

test_list2 = set(test_list2)

 

# stops when 1st match element is found

res = next((ele for ele in test_list1 if ele in
test_list2), None)

 

# printing result

print("First element in list 1 from 2 : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list 1 is : [1, 6, 3, 7, 8, 9, 2]
    The original list 2 is : [4, 10, 8, 2, 0, 11]
    First element in list 1 from 2 : 8

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


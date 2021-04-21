Python – Elements with same index



Given a List, get all elements which are at its index value.

>  **Input** : test_list = [3, 1, 8, 5, 4, 10, 6, 9]  
> **Output** : [1, 4, 6]  
> **Explanation** : These elements are at same position as its number.
>
>  **Input** : test_list = [3, 10, 8, 5, 14, 10, 16, 9]  
> **Output** : []  
> **Explanation** : No number at its index.

**Method #1: Using loop**

In this, we check for each element, if it equates to its index, it’s added to
result list.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Elements with same index

# Using loop

 

# initializing list

test_list = [3, 1, 2, 5, 4, 10, 6, 9]

 

# printing original list

print("The original list is : " + str(test_list))

 

# enumerate to get index and element

res = []

for idx, ele in enumerate(test_list):

 if idx == ele:

 res.append(ele)

 

# printing result 

print("Filtered elements : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [3, 1, 2, 5, 4, 10, 6, 9]
    Filtered elements : [1, 2, 4, 6]
    
    

**Method #2 : Using** **list comprehension** **+** **enumerate()**

In this, we perform a similar function as the above method, change being we
use list comprehension to make the solution compact.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Elements with same index

# Using list comprehension + enumerate()

 

# initializing list

test_list = [3, 1, 2, 5, 4, 10, 6, 9]

 

# printing original list

print("The original list is : " + str(test_list))

 

# enumerate to get index and element

res = [ele for idx, ele in enumerate(test_list) if idx
== ele]

 

# printing result 

print("Filtered elements : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [3, 1, 2, 5, 4, 10, 6, 9]
    Filtered elements : [1, 2, 4, 6]
    
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


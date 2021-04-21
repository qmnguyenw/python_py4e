Python prorgam to remove duplicate elements index from other list



Given two lists, the task is to write a Python program to remove all the index
elements from 2nd list which are duplicate element indices from 1st list.

 **Examples:**

>  **Input** : test_list1 = [3, 5, 6, 5, 3, 7, 8, 6], test_list2 = [1, 7, 6,
> 3, 7, 9, 10, 11]  
> **Output** : [1, 7, 6, 9, 10]  
> **Explanation** : 3, 7 and 11 correspond to 2nd occurrence of 5, 3 and 6,
> hence removed.
>
>  **Input** : test_list1 = [3, 5, 6, 5, 3, 7, 8], test_list2 = [1, 7, 6, 3,
> 7, 9, 10]  
> **Output** : [1, 7, 6, 9, 10]  
> **Explanation** : 3 and 7 correspond to 2nd occurrence of 5 and 3 hence
> removed.  
>

**Method 1: Using** **list comprehension** **+** **loop** **+**
**enumerate()**

  

  

In this, we perform task of getting all the indices using enumerate() and loop
using set to store already occurred elements. Then, same indices from other
list are omitted.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove duplicate elements index from other list

# Using list comprehension + loop + enumerate()

 

# initializing lists

test_list1 = [3, 5, 6, 5, 3, 7, 8, 6]

test_list2 = [1, 7, 6, 3, 7, 9, 10, 11]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

oc_set = set() 

temp = [] 

 

# getting duplicate elements list

for idx, val in enumerate(test_list1): 

 if val not in oc_set: 

 oc_set.add(val) 

 else: 

 temp.append(idx)

 

# excluding duplicate indices from other list

res = [ele for idx, ele in enumerate(test_list2) if idx
not in temp]

 

# printing result

print("The list after removing duplicate indices : " + str(res))  
  
---  
  
 __

 __

**Output:**

    
    
    The original list 1 is : [3, 5, 6, 5, 3, 7, 8, 6]
    The original list 2 is : [1, 7, 6, 3, 7, 9, 10, 11]
    The list after removing duplicate indices : [1, 7, 6, 9, 10]

**Method 2: Using** **list comprehension** **+** **enumerate()**

In this, we perform similar task as above just in a shorthand manner,
extracting indices using enumerate() and list comprehension.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove duplicate elements index from other list

# Using list comprehension + enumerate()

 

# initializing lists

test_list1 = [3, 5, 6, 5, 3, 7, 8, 6]

test_list2 = [1, 7, 6, 3, 7, 9, 10, 11]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# getting duplicate elements list using list comprehension

temp = [idx for idx, val in enumerate(test_list1) if val
in test_list1[:idx]]

 

# excluding duplicate indices from other list

res = [ele for idx, ele in enumerate(test_list2) if idx
not in temp]

 

# printing result

print("The list after removing duplicate indices : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list 1 is : [3, 5, 6, 5, 3, 7, 8, 6]
    The original list 2 is : [1, 7, 6, 3, 7, 9, 10, 11]
    The list after removing duplicate indices : [1, 7, 6, 9, 10]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


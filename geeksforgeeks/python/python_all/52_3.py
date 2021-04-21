Python – Frequency of elements from other list



Given two lists, compute frequency of elements of list 2 that occur in list 1.

>  **Input** : test_list1 = [4, 6, 8, 9], test_list2 = [4, 6, 6, 5, 8, 10, 4,
> 9, 8, 10, 1]  
>  **Output** : {4: 2, 6: 2, 8: 2, 9: 1}  
>  **Explanation** : 4 occurs 2 times, 6 occurs 2 times in second list and so
> on.
>
>  **Input** : test_list1 = [4, 6, 8, 9], test_list2 = [4, 6, 5, 8, 10, 4, 9,
> 8, 10, 1]  
>  **Output** : {4: 2, 6: 1, 8: 2, 9: 1}  
>  **Explanation** : 4 occurs 2 times, 6 occurs 1 time in second list and so
> on.

 **Method #1 : Using dictionary comprehension + count()**

This is one of the ways in which this task can be performed. In this, count()
is used to extract count of elements in list 2 and dictionary comprehension is
used to compile result and iterate through list 1 values.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Frequency of elements from other list

# Using dictionary comprehension + count()

 

# initializing lists

test_list1 = [4, 6, 8, 9, 10]

test_list2 = [4, 6, 6, 5, 8, 10, 4, 9,
8, 10, 1]

 

# printing original lists

print("The original list 1 : " + str(test_list1))

print("The original list 2 : " + str(test_list2))

 

# count() used to perform count.

# returns 0 is no occurrence.

# ignores different new elements in list 2

res = {key : test_list2.count(key) for key in test_list1}

 

# printing result 

print("Lists elements Frequency : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list 1 : [4, 6, 8, 9, 10]
    The original list 2 : [4, 6, 6, 5, 8, 10, 4, 9, 8, 10, 1]
    Lists elements Frequency : {4: 2, 6: 2, 8: 2, 9: 1, 10: 2}
    

**Method #2 : Using Counter() + setdefault() + loop**

This is another way in which this task can be performed. In this, we compute
the frequency using Counter() and assign values using loop. The setdefault()
is used to initialize the counter to 0 for not present values.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Frequency of elements from other list

# Using Counter() + setdefault() + loop

from collections import Counter

 

# initializing lists

test_list1 = [4, 6, 8, 9, 10]

test_list2 = [4, 6, 6, 5, 8, 10, 4, 9,
8, 10, 1]

 

# printing original lists

print("The original list 1 : " + str(test_list1))

print("The original list 2 : " + str(test_list2))

 

# Counter() used to perform count on list 2

res = dict(Counter(test_list2))

 

# filtering only list 1 keys

res = {key : val for key, val in res.items() if key in
test_list1} 

 

for key in test_list1:

 

 # initializing elements not present in list 2 of list 1 to 0

 res.setdefault(key, 0) 

 

 

# printing result 

print("Lists elements Frequency : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list 1 : [4, 6, 8, 9, 10]
    The original list 2 : [4, 6, 6, 5, 8, 10, 4, 9, 8, 10, 1]
    Lists elements Frequency : {4: 2, 6: 2, 8: 2, 10: 2, 9: 1}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


Python – Cross Join every Kth segment



Given two lists, extract alternate elements at every Kth possition.

>  **Input** : test_list1 = [4, 3, 8, 2, 6, 7], test_list2 = [5, 6, 7, 4, 3,
> 1], K = 3  
>  **Output** : [4, 3, 8, 5, 6, 7, 2, 6, 7, 4, 3, 1]  
>  **Explanation** : 4, 3, 8 after that 5, 6 from other list are extracted,
> and so on.
>
>  **Input** : test_list1 = [4, 3, 8, 2], test_list2 = [5, 6, 7, 4], K = 2  
>  **Output** : [4, 3, 5, 6, 8, 2, 7, 4]  
>  **Explanation** : 4, 3 after that 5, 6 from other list are extracted, and
> so on.

 **Method #1 : Using generator [yield] + loop**

In this, we iterate for all elements, nested to get K elements at each pass
from both list. The yield is used to dynamically return segements as they get
processed.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Cross Join every Kth segment

# Using yield + loop

 

# helper function

def pair_merge(test_list1, test_list2, K):

 idx1 = 0

 idx2 = 0

 while(idx1 < len(test_list1)):

 

 # get K segments

 for i in range(K):

 yield test_list1[idx1]

 idx1 += 1

 for i in range(K):

 yield test_list2[idx2]

 idx2 += 1

 

# initializing lists

test_list1 = [4, 3, 8, 2, 6, 7]

test_list2 = [5, 6, 7, 4, 3, 1]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# initializing K 

K = 2

 

# calling helper func. in generator expression

res = [ele for ele in pair_merge(test_list1, test_list2, K)]

 

# printing result 

print("The cross joined list : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list 1 is : [4, 3, 8, 2, 6, 7]
    The original list 2 is : [5, 6, 7, 4, 3, 1]
    The cross joined list : [4, 3, 5, 6, 8, 2, 7, 4, 6, 7, 3, 1]
    

**Method #2 : Using zip_longest() + list comprehension**

In this, we get all the elements for each list using zip_longest, and list
comprehension is used for the task of iteration in both list.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Cross Join every Kth segment

# Using zip_longest() + list comprehension

from itertools import zip_longest, chain

 

# initializing lists

test_list1 = [4, 3, 8, 2, 6, 7]

test_list2 = [5, 6, 7, 4, 3, 1]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# initializing K 

K = 2

 

# zip_longest to get segments

res = [y for idx in zip(zip_longest(*[iter(test_list1)]
* K), 

 zip_longest(*[iter(test_list2)] * K)) for y in
chain.from_iterable(idx) if y]

 

# printing result 

print("The cross joined list : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list 1 is : [4, 3, 8, 2, 6, 7]
    The original list 2 is : [5, 6, 7, 4, 3, 1]
    The cross joined list : [4, 3, 5, 6, 8, 2, 7, 4, 6, 7, 3, 1]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


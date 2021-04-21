Python – Find the sum of Length of Strings at given indices



Given the String list, write a Python program to compute sum of lengths of
custom indices of list.

 **Examples:**

>  **Input** : test_list = [“gfg”, “is”, “best”, “for”, “geeks”], idx_list =
> [0, 1, 4]  
> **Output** : 10  
> **Explanation** : 3 + 2 + 5 = 10. (Sizes of strings at idx.)  
>
>
> **Input** : test_list = [“gfg”, “is”, “best”, “for”, “geeks”], idx_list =
> [0, 2, 4]  
> **Output** : 12  
> **Explanation** : 3 + 4 + 5 = 12.

**Method #1 : Using** **len()** **\+ loop**

  

  

In this, we iterate for all indices and check if they occur in index list, if
yes, increment frequency in summation counter.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Length sum of custom indices Strings

# Using len() + loop

 

# initializing list

test_list = ["gfg", "is", "best", "for", "geeks"]

 

# printing original lists

print("The original list is : " + str(test_list))

 

# initializing idx list

idx_list = [0, 1, 4]

 

res = 0

for idx, ele in enumerate(test_list):

 

 # adding length if index in idx_list

 if idx in idx_list:

 res += len(ele)

 

# printing result

print("Computed Strings lengths sum : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : ['gfg', 'is', 'best', 'for', 'geeks']
    Computed Strings lengths sum : 10

 **Method #2 : Using** **sum()** **+** **len()** **+** **list comprehension**

In this, we perform task of performing summation using sum(), rest all the
functionalities are performed as per above method, just as one-liner.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Length sum of custom indices Strings

# Using sum() + len() + list comprehension

 

# initializing list

test_list = ["gfg", "is", "best", "for", "geeks"]

 

# printing original lists

print("The original list is : " + str(test_list))

 

# initializing idx list

idx_list = [0, 1, 4]

 

# performing summation using sum()

# len() used to get strings lengths

res = sum([len(ele) for idx, ele in enumerate(test_list)
if idx in idx_list])

 

# printing result

print("Computed Strings lengths sum : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : ['gfg', 'is', 'best', 'for', 'geeks']
    Computed Strings lengths sum : 10

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


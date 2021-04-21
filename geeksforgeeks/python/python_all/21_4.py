Python – Test for Incrementing Dictionary



Given a dictionary, test if it is incrementing, i.e its key and values are
increasing by 1.

>  **Input** : test_dict = {1:2, 3:4, 5:6, 7:8}  
> **Output** : True  
> **Explanation** : All keys and values in order differ by 1.  
>
>
> **Input** : test_dict = {1:2, 3:10, 5:6, 7:8}  
> **Output** : False  
> **Explanation** : Irregular items.

**Method : Using items() + loop + extend() + list comprehension**

In this, 1st step is to get the dictionary to list conversion using _items()_
\+ list comprehension and _extend()_ , next loop is used to test if converted
list is incremental.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test for Incrementing Dictionary

# Using extend() + list comprehension

 

# initializing dictionary

test_dict = {1: 2, 3: 4, 5: 6, 7: 8}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

temp = []

 

# forming list from dictionary

[temp.extend([key, val]) for key, val in test_dict.items()]

 

# checking for incrementing elements

res = True

for idx in range(0, len(temp) - 1):

 

 # test for increasing list

 if temp[idx + 1] - 1 != temp[idx]:

 res = False

 

# printing result

print("Is dictionary incrementing : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original dictionary is : {1: 2, 3: 4, 5: 6, 7: 8}
    Is dictionary incrementing : True

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


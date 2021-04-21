Python Program to repeat elements at custom indices



Given a List, the following program repeats those elements which are at a
custom index, these custom indices are provided to it as a separate list.

>  **Input** : test_list = [4, 6, 7, 3, 1, 9, 2, 19], idx_list = [3, 1, 6]  
> **Output** : [4, 6, 6, 7, 3, 3, 1, 9, 2, 2, 19]  
> **Explanation** : All required index elements repeated, Eg. 6 repeated as it
> is at index 1.  
>  **Input** : test_list = [4, 6, 7, 3, 1, 9, 2, 19], idx_list = [1, 6]  
> **Output** : [4, 6, 6, 7, 3, 1, 9, 2, 2, 19]  
> **Explanation** : All required index elements repeated, 6 repeated as it is
> at index 1.  
>

**Method :** _Using_ _loop_ _and_ _extend()_

In this, we perform the task of repeating each element in case it is the
required index to be repeated using extend() and loop is used to iterate for
every index. The enumerate() is used to get all the indices along with
elements.

 **Program:**

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# initializing list

test_list = [4, 6, 7, 3, 1, 9, 2, 19]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing index list 

idx_list = [3, 1, 4, 6]

 

res = []

for idx, ele in enumerate(test_list):

 if idx in idx_list:

 

 # incase of repetition

 res.extend([ele, ele])

 else :

 res.append(ele)

 

# printing result 

print("The Custom elements repetition : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [4, 6, 7, 3, 1, 9, 2, 19]
>
> The Custom elements repetition : [4, 6, 6, 7, 3, 3, 1, 1, 9, 2, 2, 19]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


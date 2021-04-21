Python – Convert Lists into Similar key value lists



Given two lists, one of key and other values, convert it to dictionary with
list values, if keys map to different values on basis of index, add in its
value list.

>  **Input** : test_list1 = [5, 6, 6, 6], test_list2 = [8, 3, 2, 9]  
>  **Output** : {5: [8], 6: [3, 2, 9]}  
>  **Explanation** : Elements with index 6 in corresponding list, are mapped
> to 6.
>
>  **Input** : test_list1 = [6, 6, 6, 6], test_list2 = [8, 3, 2, 9]  
>  **Output** : {6: [8, 3, 2, 9]}  
>  **Explanation** : All mapped to single number.

 **Method #1 : Using zip() + loop**

This is one of the ways in which this task can be performed. In this, we
perform mapping the keys to required values using zip() and loop is used to
perform iteration of keys.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert Lists into Similar key value lists

# Using loop + zip()

 

# initializing lists

test_list1 = [5, 6, 6, 4, 5, 6] 

test_list2 = [8, 3, 2, 9, 10, 4]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# creating a mesh of keys with empty values list

res = {key: [] for key in test_list1}

 

# loop to iterate through keys and values

for key, val in zip(test_list1, test_list2):

 res[key].append(val)

 

# printing result 

print("The mapped dictionary : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original list 1 is : [5, 6, 6, 4, 5, 6]
    The original list 2 is : [8, 3, 2, 9, 10, 4]
    The mapped dictionary : {5: [8, 10], 6: [3, 2, 4], 4: [9]}
    

**Method #2 : Using defaultdict() + list comprehension + zip()**

The combination of above functions can be used to solve this problem. In this,
we perform task as one liner and defaultdict() is used to preassign values
with empty lists.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert Lists into Similar key value lists

# Using defaultdict() + list comprehension + zip()

from collections import defaultdict

 

# initializing lists

test_list1 = [5, 6, 6, 4, 5, 6] 

test_list2 = [8, 3, 2, 9, 10, 4]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# creating a mesh of keys using defaultdict

res = defaultdict(list)

[res[key].append(val) for key, val in zip(test_list1, test_list2)]

 

# printing result 

print("The mapped dictionary : " + str(dict(res)))   
  
---  
  
__

__

**Output**

    
    
    The original list 1 is : [5, 6, 6, 4, 5, 6]
    The original list 2 is : [8, 3, 2, 9, 10, 4]
    The mapped dictionary : {5: [8, 10], 6: [3, 2, 4], 4: [9]}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


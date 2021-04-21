Python – Convert each list element to key-value pair



Given list of elements, convert each element to a key-value pair dictionary,
dividing digits equally.

>  **Input** : test_list = [2323, 82, 129388, 234, 95]  
> **Output** : {23: 23, 8: 2, 129: 388, 2: 34, 9: 5}  
> **Explanation** : Digits distributed equally to keys and values.
>
>  **Input** : test_list = [2323, 82, 129388]  
> **Output** : {23: 23, 8: 2, 129: 388}  
> **Explanation** : Digits distributed equally to keys and values.  
>

**Approach: Using list slicing + loop**

In this, we form key-value pair by getting the sliced values from each element
by dividing by half the digits for keys and values.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert each list element to key-value pair

# Using loop + list slicing

 

# initializing list

test_list = [2323, 82, 129388, 234, 95]

 

# printing original list

print("The original list is : " + str(test_list))

 

res = dict()

for ele in test_list:

 

 # constructing key and values

 mid_idx = len(str(ele)) // 2

 key = int(str(ele)[:mid_idx])

 val = int(str(ele)[mid_idx:])

 

 # item assignment

 res[key] = val

 

# printing result

print("Constructed Dictionary : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [2323, 82, 129388, 234, 95]
    Constructed Dictionary : {23: 23, 8: 2, 129: 388, 2: 34, 9: 5}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


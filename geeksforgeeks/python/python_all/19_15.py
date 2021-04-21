Python – Redistribute Trimmed Values



Given a List, redistribute values trimmed by K.

 **Examples:**

>  **Input** : test_list = [4, 5, 2, 8, 9, 3, 1, 2, 4], K = 2  
> **Output** : [5.0, 11.0, 12.0, 6.0, 4.0]  
> **Explanation** : 4, 5, 2, 4 are trimmed, totalling to 15, which dividing by
> 5 ( size left ) equates 3, which is added to each element.
>
>  **Input** : test_list = [4, 5, 2, 8, 9], K = 2  
> **Output** : [28.0]  
> **Explanation** : 4, 5, 8, 9 are trimmed, totalling to 26, which dividing by
> 1 ( size left ) equates 26, which is added to each element.  
>

**Approach: Using** **slice()** **+** **sum()**

  

  

In this, the total sum is computed using sum, and the list is trimmed using
slice(), then trimmed weight is computed by subtraction by total weight.
Redistributed by adding uniform weight to each element.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Redistribute Trimmed Values

# Using slice() + sum()

 

# initializing list

test_list = [4, 5, 2, 8, 9, 3, 1, 2,
4]

 

# printing original lists

print("The original list is : " + str(test_list))

 

# initializing K

K = 2

 

# getting full list sum

full_sum = sum(test_list)

 

# trimming list

trimd_list = test_list[K:len(test_list) - K]

 

# getting trimmed list sum

trim_sum = sum(trimd_list)

 

# getting value to add to each element

add_val = (full_sum - trim_sum) / len(trimd_list)

 

# adding values

res = [ele + add_val for ele in trimd_list]

 

# printing result

print("Redistributed list : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [4, 5, 2, 8, 9, 3, 1, 2, 4]
    Redistributed list : [5.0, 11.0, 12.0, 6.0, 4.0]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


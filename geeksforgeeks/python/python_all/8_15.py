Python program to compute the power by Index element in List



Given a list, the task is to write a Python program to compute the power of
each element by its index value.

>  **Input :** test_list = [6, 9, 1, 8, 4, 7]
>
>  **Output :** [1, 9, 1, 512, 256, 16807]
>
>  **Explanation :** 8 * 8 * 8 = 512, as 8 is at 3rd index.
>
>  **Input :** test_list = [6, 9, 1, 8]
>
>  
>
>
>  
>
>
>  **Output :** [1, 9, 1, 512]
>
>  **Explanation :** 9**1 = 9, as 9 is at 1st index.

 **Method 1 : Using** **** operator** **+** **loop** **+** **enumerate()**

In this, the task of getting power is done using the ** operator and loop is
used to iterate through elements. The enumerate() is used to get index along
with values.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Index Power List

# Using ** operator + loop + enumerate()

 

# initializing list

test_list = [6, 9, 1, 8, 4, 7]

 

# printing original list

print("The original list is : " + str(test_list))

 

# ** does task of getting power

res = []

for idx, ele in enumerate(test_list):

 res.append(ele ** idx)

 

# printing result

print("Powered elements : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [6, 9, 1, 8, 4, 7]
    Powered elements : [1, 9, 1, 512, 256, 16807]

 **Method 2 : Using** **pow()** **+** **list comprehension** **+**
**enumerate()**

In this, we perform the task of getting power using pow(), enumerate() is used
to get index with values.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Index Power List

# Using pow() + list comprehension + enumerate()

from math import pow

 

# initializing list

test_list = [6, 9, 1, 8, 4, 7]

 

# printing original list

print("The original list is : " + str(test_list))

 

# pow() does task of getting power

# list comprehension for 1 liner alternative

res = [int(pow(ele, idx)) for idx, ele in
enumerate(test_list)]

 

# printing result

print("Powered elements : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [6, 9, 1, 8, 4, 7]
    Powered elements : [1, 9, 1, 512, 256, 16807]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


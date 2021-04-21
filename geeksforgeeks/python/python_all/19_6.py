Python – Reform K digit elements



Given the Python list, reform element to have K digits in a single element.

>  **Input** : test_list = [223, 67, 332, 1, 239, 2, 931], K = 2  
> **Output** : [22, 36, 73, 32, 12, 39, 29, 31]  
> **Explanation** : Elements reformed to assign 2 digits to each element.
>
>  **Input** : test_list = [223, 67, 3327], K = 3  
> **Output** : [223, 673, 327]  
> **Explanation** : Elements reformed to assign 3 digits to each element.

**Method #1 : Using** **slicing** **+** **join()** **\+ loop**

In this, we perform task of joining all elements to single string, then slice
K digits, and reconvert to list.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Reform K digit elements

# Using slicing + join() + loop

 

# initializing list

test_list = [223, 67, 332, 1, 239, 2, 931]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K

K = 2

 

# converting to string

temp = ''.join([str(ele) for ele in test_list])

 

# getting K digit slices

res = []

for idx in range(0, len(temp), K):

 res.append(int(temp[idx: idx + K]))

 

# printing result

print("Reforming K digits : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [223, 67, 332, 1, 239, 2, 931]
    Reforming K digits : [22, 36, 73, 32, 12, 39, 29, 31]
    

**Method #2 : Using** **list comprehension** **\+ join()**

In this, task of reforming the list is done using list comprehension.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Reform K digit elements

# Using list comprehension + join()

 

# initializing list

test_list = [223, 67, 332, 1, 239, 2, 931]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K

K = 2

 

# converting to string

temp = ''.join([str(ele) for ele in test_list])

 

# getting K digit slices

# using 1 liner list comprehension

res = [int(temp[idx: idx + K]) for idx in range(0,
len(temp), K)]

 

# printing result

print("Reforming K digits : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [223, 67, 332, 1, 239, 2, 931]
    Reforming K digits : [22, 36, 73, 32, 12, 39, 29, 31]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


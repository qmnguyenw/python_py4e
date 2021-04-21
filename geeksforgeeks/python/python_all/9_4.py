Python – Maximum difference across lists



Given two lists, the task is to write a Python program to find maximum
difference among like index elements.

**Examples:**

>  **Input :** test_list1 = [3, 4, 2, 1, 7], test_list2 = [6, 2, 1, 9, 1]
>
>  **Output :** 8
>
>  **Explanation :** 9 – 1 = 8 is maximum differece across lists in same
> index.
>
>  
>
>
>  
>
>
>  **Input :** test_list1 = [3, 4, 2, 1, 17], test_list2 = [6, 2, 1, 9, 1]
>
>  **Output :** 16
>
>  **Explanation :** 17 – 1 = 16 is maximum differece across lists in same
> index.

 **Method 1 : Using** **list comprehension** **+** **max()**

In this, difference is computed using abs() and iteration is done using list
comprehension. The max() is used for the task of getting maximum difference
among computed sub result.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Maximum difference across lists

# Using list comprehension + max()

 

# initializing lists

test_list1 = [3, 4, 2, 1, 7]

test_list2 = [6, 2, 1, 9, 1]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# using max() to get maximum of extracted difference

res = max(abs(test_list2[idx] - test_list1[idx])

 for idx in range(0, len(test_list1) - 1))

 

# printing result

print("Maximum difference among lists : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list 1 is : [3, 4, 2, 1, 7]
    The original list 2 is : [6, 2, 1, 9, 1]
    Maximum difference among lists : 8

 **Method 2 : Using** **zip()** **+** **max()**

In this pairing of like index elements is done using zip(). Rest all the
functionality is similar to above method.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Maximum difference across lists

# Using zip() + max()

 

# initializing lists

test_list1 = [3, 4, 2, 1, 7]

test_list2 = [6, 2, 1, 9, 1]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# using max() to get maximum of extracted difference

# zip() used to bind elements

res = max(abs(ele1 - ele2) for ele1, ele2 in
zip(test_list1, test_list2))

 

# printing result

print("Maximum difference among lists : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list 1 is : [3, 4, 2, 1, 7]
    The original list 2 is : [6, 2, 1, 9, 1]
    Maximum difference among lists : 8

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


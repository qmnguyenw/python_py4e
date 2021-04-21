Python program to Swap i’th with j’th elements in List



Given a list, the task is to write a Python program to the given list of
elements, toggle every i and j elements in the list.

 **Examples:**

>  **Input** : test_list = [4, 7, 8, 0, 8, 4, 2, 9, 4, 8, 4], i, j = 4, 8  
> **Output** : [8, 7, 4, 0, 4, 8, 2, 9, 8, 4, 8]  
> **Explanation** : 4 is swapped by 8 at each occurrence.
>
>  **Input** : test_list = [4, 7, 8, 0, 8, 4], i, j = 4, 8  
> **Output** : [8, 7, 4, 0, 4, 8]  
> **Explanation** : 4 is swapped by 8 at each occurrence.  
>

**Method 1: Using loop + conditional statements**

  

  

In this, we perform the task of toggling using conditional if-else statements,
and the task of iteration is performed using a loop.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Toggle i,j elements in List

# Using loop + conditional statements

 

# initializing list

test_list = [4, 7, 8, 0, 8, 4, 2, 9,
4, 8, 4]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing i, j 

i, j = 4, 8

 

for idx in range(len(test_list)):

 

 # perform toggling

 if int(test_list[idx]) == i:

 test_list[idx] = j

 elif int(test_list[idx]) == j:

 test_list[idx] = i

 

# printing result

print("The altered list : " + str(test_list))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [4, 7, 8, 0, 8, 4, 2, 9, 4, 8, 4]
    The altered list : [8, 7, 4, 0, 4, 8, 2, 9, 8, 4, 8]

 **Method 2: Using** **list comprehension** **\+ external function**

In this, we perform the task of toggling using the external toggle function,
and list comprehension is used to iterate through the list.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Toggle i,j elements in List

# Using list comprehension + external function

 

# external toggle 

def toggle(ele, i, j):

 

 # performing toggle

 if ele == i:

 return j

 elif ele == j:

 return i

 return ele

 

# initializing list

test_list = [4, 7, 8, 0, 8, 4, 2, 9,
4, 8, 4]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing i, j 

i, j = 4, 8

 

# list comprehension for 1 liner

res = [toggle(ele, i, j) for ele in test_list]

 

# printing result

print("The altered list : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [4, 7, 8, 0, 8, 4, 2, 9, 4, 8, 4]
    The altered list : [8, 7, 4, 0, 4, 8, 2, 9, 8, 4, 8]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


Python – Custom Lower bound a List



Given a list, assign a custom lower-bound value to it.

>  **Input** : test_list = [5, 7, 8, 2, 3, 5, 1], K = 3  
> **Output** : [5, 7, 8, 3, 3, 5, 3]  
> **Explanation** : All elements less than 3, assigned 3.
>
>  **Input** : test_list = [5, 7, 8, 2, 3, 5, 1], K = 5  
> **Output** : [5, 7, 8, 5, 5, 5, 5]  
> **Explanation** : All elements less than 5, assigned 5.

**Method #1: Using** **list comprehension**

In this, we check for each element if it’s lower than lower-bound, if yes,
then assign the decided lower-bound to that element.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Custom Lowerbound a List

# Using list comprehension

 

# initializing list

test_list = [5, 7, 8, 2, 3, 5, 1]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing Lowerbound

K = 4

 

# checking for elements and assigning Lowerbounds

res = [ele if ele >= K else K for ele in test_list]

 

# printing result 

print("List with Lowerbounds : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [5, 7, 8, 2, 3, 5, 1]
    List with Lowerbounds : [5, 7, 8, 4, 4, 5, 4]
    

**Method #2 : Using list comprehension +** **max()**

In this, we perform comparison using max(), assign max of the element, or the
lower-bound as decided.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Custom Lowerbound a List

# Using list comprehension + max()

 

# initializing list

test_list = [5, 7, 8, 2, 3, 5, 1]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing Lowerbound

K = 4

 

# max() is used to compare for Lowerbound

res = [max(ele, K) for ele in test_list]

 

# printing result 

print("List with Lowerbounds : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [5, 7, 8, 2, 3, 5, 1]
    List with Lowerbounds : [5, 7, 8, 4, 4, 5, 4]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


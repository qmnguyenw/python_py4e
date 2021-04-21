Python – Append Multiple elements in set



In this article given a set and list of elements, the task is to write a
Python program to append multiple elements in set at once.

 **Example:**

>  **Input :** test_set = {6, 4, 2, 7, 9}, up_ele = [1, 5, 10]
>
>  **Output :** {1, 2, 4, 5, 6, 7, 9, 10}
>
>  **Explanation :** All elements are updated and reordered. (5 at 3rd
> position).
>
>  
>
>
>  
>
>
>  **Input :** test_set = {6, 4, 2, 7, 9}, up_ele = [1, 5, 8]
>
>  **Output :** {1, 2, 4, 5, 6, 7, 8, 9, 10}
>
>  **Explanation :** All elements are updated and reordered. (8 at 7th
> position).

 **Method #1 : Using** **update()**

In this, we use in built update() to get all the elements in list aligned with
the existing set.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Append Multiple elements in set

# Using update()

 

# initializing set

test_set = {6, 4, 2, 7, 9}

 

# printing original set

print("The original set is : " + str(test_set))

 

# initializing adding elements

up_ele = [1, 5, 10]

 

# update() appends element in set

# internally reorders

test_set.update(up_ele)

 

# printing result

print("Set after adding elements : " + str(test_set))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original set is : {2, 4, 6, 7, 9}
    Set after adding elements : {1, 2, 4, 5, 6, 7, 9, 10}

 **Method #2 : Using | operator ( Pipe operator )**

The pipe operator internally calls union(), which can be used to perform task
of updating set with newer elements.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Append Multiple elements in set

# Using | operator ( Pipe operator )

 

# initializing set

test_set = {6, 4, 2, 7, 9}

 

# printing original set

print("The original set is : " + str(test_set))

 

# initializing adding elements

up_ele = [1, 5, 10]

 

# | performing task of updating

test_set |= set(up_ele)

 

# printing result

print("Set after adding elements : " + str(test_set))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original set is : {2, 4, 6, 7, 9}
    Set after adding elements : {1, 2, 4, 5, 6, 7, 9, 10}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


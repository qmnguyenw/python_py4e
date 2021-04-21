Python – Test for all Even elements in the List for the given Range



Given a List of elements, test if all elements are even in a range.

>  **Input** : test_list = [3, 1, 4, 6, 8, 10, 1, 9], i, j = 2, 5  
> **Output** : True  
> **Explanation** : 4, 6, 8, 10, all are even elements in range.
>
>  **Input** : test_list = [3, 1, 4, 6, 87, 10, 1, 9], i, j = 2, 5  
> **Output** : False  
> **Explanation** : All not even in Range.

**Method #1: Using loop**

In this, we iterate for part of list in the specified range, and flag off the
list even if we find anyone odd occurrence in list.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test for all Even elements in List Range

# Using loop

 

# initializing list

test_list = [3, 1, 4, 6, 8, 10, 1, 9]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing range 

i, j = 2, 5

 

res = True

for idx in range(i, j + 1):

 

 # check if any odd

 if test_list[idx] % 2 :

 res = False

 break

 

# printing result 

print("Are all elements even in range : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [3, 1, 4, 6, 8, 10, 1, 9]
    Are all elements even in range : True
    

**Method #2: Using** **all()** **+** **list comprehension**

In this, all elements to be even are checked using all(), and list
comprehension is used to loop over the elements in the range.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test for all Even elements in List Range

# Using all() + list comprehension

 

# initializing list

test_list = [3, 1, 4, 6, 8, 10, 1, 9]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing range 

i, j = 2, 5

 

# all() checks for all even elements 

res = all(test_list[idx] % 2 == 0 for idx in
range(i, j + 1))

 

# printing result 

print("Are all elements even in range : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [3, 1, 4, 6, 8, 10, 1, 9]
    Are all elements even in range : True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


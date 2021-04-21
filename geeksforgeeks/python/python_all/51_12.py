Python – K difference Consecutive elements



Given a list of integer elements, check for each element if its difference
with successive element is K.

>  **Input** : test_list = [5, 6, 3, 2, 5, 3, 4], K = 1  
>  **Output** : [True, False, True, False, False, True]  
>  **Explanation** : 5, 6; 3, 2; and 3, 4 have 1 diff. between them.
>
>  **Input** : test_list = [5, 6, 3, 2, 5, 3, 4], K = 2  
>  **Output** : [False, False, False, False, True, False]  
>  **Explanation** : Only 5, 3 has 2 diff between it.

 **Method #1 : Using list comprehension**

This is one of the ways in which this task can be performed. In this, we check
for each element with next one, if difference is K then we tag it True, else
False.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# K difference Consecutive elements

# Using list comprehension

 

# initializing list

test_list = [5, 6, 3, 2, 5, 3, 4]

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing K 

K = 3

 

# using list comprehension and abs() to compute result

res = [True if abs(test_list[idx] - test_list[idx + 1])
== K else False

 for idx in range(len(test_list) - 1)]

 

# printing result 

print("The difference list result : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : [5, 6, 3, 2, 5, 3, 4]
    The difference list result : [False, True, False, True, False, False]
    

**Method #2 : Using zip() + list comprehension**

This is another way in which this task can be performed. In this the
consecutive list is paired using zip() and computations run through list
comprehension.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# K difference Consecutive elements

# Using zip() + list comprehension

 

# initializing list

test_list = [5, 6, 3, 2, 5, 3, 4]

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing K 

K = 3

 

# using list comprehension and abs() to compute result

# zip() used to pair Consecutive elements list

res = [abs(a - b) == K for a, b in zip(test_list,
test_list[1:])]

 

# printing result 

print("The difference list result : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : [5, 6, 3, 2, 5, 3, 4]
    The difference list result : [False, True, False, True, False, False]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


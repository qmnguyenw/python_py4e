Python | Tail Sliced List Summation



We often come to the situations in which we need to decrease the size of the
list by truncating the last elements of the list and perform remaining list
summatioon. This particular problem occurs when we need to optimize memory.
This has its application in the day-day programming when sometimes we require
to get all the lists of similar size. Let’s discuss certain ways in which this
task can be performed.

 **Method #1 : Usinglen() + list slicing + sum()**  
List slicing can perform this particular task in which we just slice the first
len(list) – K elements to be in the list and hence removing the last K
elements. The task of performing tail summation is performed using sum().

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# Tail Sliced List Summation

# using len() + list slicing + sum()

 

# initializing list 

test_list = [1, 4, 6, 3, 5, 8]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# initializing K 

K = 3

 

# using len() + list slicing + sum()

# Tail Sliced List Summation

res = sum(test_list[: len(test_list) - K])

 

# printing result 

print ("The tail removed list summation : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [1, 4, 6, 3, 5, 8]
    The tail removed list summation : 11
    

**Method #2 : Using Negative list slicing +sum()**  
We can perform this particular task using the negative list slicing in which
we start removing the elements from the last index of the list and hence
remove all the K elements from the last. We remove None if 0 elements are
asked to be removed. The task of performing tail summation is performed using
sum().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# Tail Sliced List Summation

# using negative list slicing + sum()

 

# initializing list 

test_list = [1, 4, 6, 3, 5, 8]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# initializing K 

K = 3

 

# using negative list slicing + sum()

# Tail Sliced List Summation

res = sum(test_list[: -K or None])

 

# printing result 

print ("The tail removed list summation : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [1, 4, 6, 3, 5, 8]
    The tail removed list summation : 11
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


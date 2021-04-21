Python | Cropped list Minimum



Sometimes, we require to shrink a list by deletion of its certain elements.
One of the methods that is employed to perform this particular task is front
and rear element deletion and we also desire to find minimum of this list. It
is a good utility whose solution can be useful to have. Let’s discuss certain
ways in which this can be performed.

 **Method #1 : Using list slicing + del operator + min()**  
The del operator can be clubbed with the slicing action to delete the front
and rear elements from a list to obtain a cropped version of list. The task of
finding minimum is found using min().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Cropped list Minimum

# using del operator + list slicing + min()

 

# initializing list 

test_list = [2, 3, 5, 7, 9, 10, 8, 6]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# initializing K 

K = 2

 

# using del operator + list slicing + min()

# Cropped list Minimum

del test_list[-K:], test_list[:K]

res = min(test_list)

 

# printing result 

print ("The cropped list minimum is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [2, 3, 5, 7, 9, 10, 8, 6]
    The cropped list minimum is : 5
    

**Method #2 : Using list slicing + min()**  
Above method can be modified and the use of del operator can be omitted to
achieve this particular task. We can slice a list in a way that specific
number of elements are removed from the list. The task of finding minimum is
found using min().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Cropped list Minimum

# using list slicing + min()

 

# initializing list 

test_list = [2, 3, 5, 7, 9, 10, 8, 6]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# initializing K 

K = 2

 

# using list slicing + min()

# front and rear deletion 

res = min(test_list[K : -K])

 

# printing result 

print ("The cropped list minimum is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [2, 3, 5, 7, 9, 10, 8, 6]
    The cropped list minimum is : 5
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


Python | Check for Nth index existence in list



Sometimes, while working with lists, we can have a problem in which we require
to insert a particular element at an index. But, before that it is essential
to know that particular index is part of list or not. Let’s discuss certain
shorthands that can perform this task error free.

 **Method #1 : Usinglen()**  
This task can be performed easily by finding the length of list using len().
We can check if the desired index is smaller than length which would prove
it’s existence.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Check for Nth index existence in list

# Using len()

 

# initializing list

test_list = [4, 5, 6, 7, 10]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing N 

N = 6

 

# Check for Nth index existence in list

# Using len()

res = len(test_list) >= N

 

# printing result 

print("Is Nth index available? : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [4, 5, 6, 7, 10]
    Is Nth index available? : False
    

**Method #2 : Using try-except block +IndexError exception**  
This task can also be solved using the try except block which raises a
IndexError exception if we try to access an index not a part of list i.e out
of bound.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Check for Nth index existence in list

# Using try-except block + IndexError exception

 

# initializing list

test_list = [4, 5, 6, 7, 10]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing N 

N = 6

 

# Check for Nth index existence in list

# Using try-except block + IndexError exception

try:

 val = test_list[N]

 res = True

except IndexError:

 res = False

 

# printing result 

print("Is Nth index available? : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [4, 5, 6, 7, 10]
    Is Nth index available? : False
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


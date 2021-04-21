Python | Check if variable is tuple



Sometimes, while working with Python, we can have a problem in which we need
to check if a variable is single or a record. This has applications in domains
in which we need to restrict the type of data we work on. Let’s discuss
certain ways in which this task can be performed.

 **Method #1 : Usingtype()**  
This inbuilt function can be used as shorthand to perform this task. It checks
for the type of variable and can be employed to check tuple as well.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Check if variable is tuple

# using type()

 

# initialize tuple 

test_tup = (4, 5, 6)

 

# printing original tuple

print("The original tuple : " + str(test_tup))

 

# Check if variable is tuple

# using type()

res = type(test_tup) is tuple

 

# printing result

print("Is variable tuple ? : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple : (4, 5, 6)
    Is variable tuple ? : True
    

**Method #2 : Usingisinstance()**  
Yet another function that can be employed to perform this task. It also
returns true, in case the parent class of variable(if exists) is a tuple.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Check if variable is tuple

# using isinstance()

 

# initialize tuple 

test_tup = (4, 5, 6)

 

# printing original tuple

print("The original tuple : " + str(test_tup))

 

# Check if variable is tuple

# using isinstance()

res = isinstance(test_tup, tuple) 

 

# printing result

print("Is variable tuple ? : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple : (4, 5, 6)
    Is variable tuple ? : True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


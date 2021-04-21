Python | Check if element is present in tuple



Sometimes, while working with data, we can have a problem in which we need to
check if data we are working with has a particular element. Let’s discuss
certain ways in which this task can be performed.

 **Method #1 : Using loop**  
This is brute force method to perform this task. In this, we iterate through
the tuple and check each element if it’s our, if found we return True.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Check if element is present in tuple

# using loop

 

# initialize tuple

test_tup = (10, 4, 5, 6, 8)

 

# printing original tuple

print("The original tuple : " + str(test_tup))

 

# initialize N 

N = 6

 

# Check if element is present in tuple

# using loop

res = False

for ele in test_tup :

 if N == ele :

 res = True

 break

 

# printing result

print("Does tuple contain required value ? : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple : (10, 4, 5, 6, 8)
    Does tuple contain required value ? : True
    

**Method #2 : Using in operator**  
Using in operator is most Pythonic way to perform this task. It is a one-liner
and recommened to perform this task.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Check if element is present in tuple

# Using in operator

 

# initialize tuple

test_tup = (10, 4, 5, 6, 8)

 

# printing original tuple

print("The original tuple : " + str(test_tup))

 

# initialize N 

N = 6

 

# Check if element is present in tuple

# Using in operator

res = N in test_tup

 

# printing result

print("Does tuple contain required value ? : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple : (10, 4, 5, 6, 8)
    Does tuple contain required value ? : True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


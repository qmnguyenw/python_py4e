Python – Check if all values are K in dictionary



While working with dictionary, we might come to a problem in which we require
to ensure that all the values are K in dictionary. This kind of problem can
occur while checking status of start or checking for a bug/action that could
have occurred. Let’s discuss certain ways in which this task can be performed.

 **Method #1 : Usingall() \+ dictionary comprehension**  
The combination of above functions can be used to perform the following task.
The all function checks for each key and dictionary comprehension checks for
the K value.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test if all values are K in dictionary

# Using all() + dictionary comprehension

 

# Initialize dictionary

test_dict = {'gfg' : 8, 'is' : 8, 'best' : 8}

 

# Printing original dictionary 

print("The original dictionary is : " + str(test_dict))

 

# Initialize K 

K = 8

 

# using all() + dictionary comprehension

# Test if all values are K in dictionary

res = all(x == K for x in test_dict.values())

 

# printing result 

print("Does all keys have K value ? : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary is : {'gfg': 8, 'best': 8, 'is': 8}
    Does all keys have K value ? : True
    

**Method #2 : Using loop**  
This problem can be solved using brute force strategy using loop and we equate
each key with K and return True if all elements match K.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test if all values are K in dictionary

# Using loop

 

# Initialize dictionary

test_dict = {'gfg' : 8, 'is' : 8, 'best' : 8}

 

# Printing original dictionary 

print("The original dictionary is : " + str(test_dict))

 

# Initialize K 

K = 8

 

# using loop

# Test if all values are K in dictionary

res = True

for key in test_dict:

 if test_dict[key] != K:

 res = False

 

# printing result 

print("Does all keys have K value ? : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary is : {'gfg': 8, 'best': 8, 'is': 8}
    Does all keys have K value ? : True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


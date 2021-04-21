Python | Check if all values are 0 in dictionary



While working with dictionary, we might come to a problem in which we require
to ensure that all the values are 0 in dictionary. This kind of problem can
occur while checking status of start or checking for a bug/action that could
have occurred. Let’s discuss certain ways in which this task can be performed.

 **Method #1 : Usingall() \+ dictionary comprehension**  
The combination of above functions can be used to perform the following task.
The all function checks for each key and dictionary comprehension checks for
the 0 value.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Check if all values are 0 in dictionary

# Using all() + dictionary comprehension

 

# Initialize dictionary

test_dict = {'gfg' : 0, 'is' : 0, 'best' : 0}

 

# Printing original dictionary 

print("The original dictionary is : " + str(test_dict))

 

# using all() + dictionary comprehension

# Check if all values are 0 in dictionary

res = all(x == 0 for x in test_dict.values())

 

# printing result 

print("Does all keys have 0 value ? : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary is : {'gfg': 0, 'is': 0, 'best': 0}
    Does all keys have 0 value ? : True
    

**Method #2 : Usingany() + not operator**  
The combination of above functions can be used to perform this particular
task. Rather than checking for all 0, we check for any one non zero value, and
negate the result.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Check if all values are 0 in dictionary

# Using any() + not operator

 

# Initialize dictionary

test_dict = {'gfg' : 0, 'is' : 1, 'best' : 0}

 

# Printing original dictionary 

print("The original dictionary is : " + str(test_dict))

 

# using any() + not operator

# Check if all values are 0 in dictionary

res = not any(test_dict.values())

 

# printing result 

print("Does all keys have 0 value ? : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary is : {'gfg': 0, 'is': 1, 'best': 0}
    Does all keys have 0 value ? : False
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


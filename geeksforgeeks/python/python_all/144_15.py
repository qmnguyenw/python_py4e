Python | Check if dictionary is empty



Sometimes, we need to check if a particular dictionary is empty or not. And
this particular task has its application in web development domain in which we
sometimes need to test for results of a particular query or check whether we
have any key to add info into database. Let’s discuss certain ways in which
this task can be performed.

 **Method #1 : Usingbool()**

The bool function can be used to perform this particular task. As name
suggests it performs the task of converting an object to a boolean value, but
here, passing an empty string returns a False, as failure to convert something
that is empty.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Check if dictionary is empty

# using bool()

 

# initializing empty dictionary

test_dict = {}

 

# printing original dictionary

print("The original dictionary : " + str(test_dict))

 

# using bool()

# Check if dictionary is empty 

res = not bool(test_dict)

 

# print result

print("Is dictionary empty ? : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary : {}
    Is dictionary empty ? : True
    

  

  

**Method #2 : Usingnot operator**

This task can also be performed using the not operator that checks for a
dictionary existence, this evaluates to True, if any key in the dictionary is
not found.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Check if dictionary is empty

# using not operator

 

# initializing empty dictionary

test_dict = {}

 

# printing original dictionary

print("The original dictionary : " + str(test_dict))

 

# using not operator

# Check if dictionary is empty 

res = not test_dict

 

# print result

print("Is dictionary empty ? : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary : {}
    Is dictionary empty ? : True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


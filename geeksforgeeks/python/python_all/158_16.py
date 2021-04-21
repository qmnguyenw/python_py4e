Python | Filter the negative values from given dictionary



Given a dictionary, the task is to filter all the negative values from given
dictionary. Let’s discuss few methods to do this task.

 **Method #1: Using dict comprehension**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# return the filtered dictionary

# on certain criteria

 

from six import iteritems

# Initialising dictionary

ini_dict = {'a':1, 'b':-2, 'c':-3,
'd':7, 'e':0}

 

# printing initial dictionary

print ("initial lists", str(ini_dict))

 

# filter dictionary such that no value is greater than 0

result = dict((k, v) for k, v in ini_dict.items() if v
>= 0)

 

print("resultant dictionary : ", str(result))  
  
---  
  
 __

 __

 **Output:**

    
    
    initial lists {'a': 1, 'c': -3, 'd': 7, 'b': -2, 'e': 0}
    resultant dictionary :  {'a': 1, 'd': 7, 'e': 0}
    

  
**Method #2: Using lambda and filter**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# return the filtered dictionary

# on certain criteria

 

from six import iteritems

# Initialising dictionary

ini_dict = {'a':1, 'b':-2, 'c':-3,
'd':7, 'e':0}

 

# printing initial dictionary

print ("initial lists", str(ini_dict))

 

# filter dictionary such that no value is greater than 0

result = dict(filter(lambda x: x[1] >= 0.0,
ini_dict.items()))

result = dict(result)

 

print("resultant dictionary : ", str(result))  
  
---  
  
 __

 __

 **Output:**

    
    
    initial lists {'c': -3, 'd': 7, 'e': 0, 'a': 1, 'b': -2}
    resultant dictionary :  {'e': 0, 'a': 1, 'd': 7}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save


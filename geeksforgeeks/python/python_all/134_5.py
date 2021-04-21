Python | Extract key-value of dictionary in variables



Sometimes, while working with dictionaries, we can face a problem in which we
may have just a singleton dictionary, i.e dictionary with just a single key-
value pair and require to get the pair in separate variables. This kind of
problem can come in day-day programming. Let’s discuss certain ways in which
this can be done.

 **Method #1 : Usingitems()**  
This problem can be solved using the items function which does the task of
extracting a key-value pair and using the 0th index gives us the first key-
value pair. Works only in Python2.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate working of

# Extracting key-value of dictionary in variables

# Using items()

 

# Initialize dictionary

test_dict = {'gfg' : 1}

 

# printing original dictionary

print("The original dictionary : " + str(test_dict))

 

# Using items()

# Extracting key-value of dictionary in variables

key, val = test_dict.items()[0]

 

# printing result 

print("The 1st key of dictionary is : " + str(key))

print("The 1st value of dictionary is : " + str(val))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary : {'gfg': 1}
    The 1st key of dictionary is : gfg
    The 1st value of dictionary is : 1
    

**Method #2 : Usingiter() + next()**  
The combination of above functions can be used to perform this particular
task. It uses iterators to perform this task. The next() is used to fetch
the pairs till dictionary is exhausted. It works with Python3.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extracting key-value of dictionary in variables

# Using iter() + next()

 

# Initialize dictionary

test_dict = {'gfg' : 1}

 

# printing original dictionary

print("The original dictionary : " + str(test_dict))

 

# Using iter() + next()

# Extracting key-value of dictionary in variables

key, val = next(iter(test_dict.items()))

 

# printing result 

print("The 1st key of dictionary is : " + str(key))

print("The 1st value of dictionary is : " + str(val))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary : {'gfg': 1}
    The 1st key of dictionary is : gfg
    The 1st value of dictionary is : 1
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


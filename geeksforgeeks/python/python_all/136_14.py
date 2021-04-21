Python | Search Key from Value



The problem of finding a value from a given key is quite common. But we may
have a problem in which we wish to get the back key from the input key we
feed. Let’s discuss certain ways in which this problem can be solved.

 **Method #1 : Using Naive Method**  
In this method, we just run a loop for each of the values and return the
corresponding key or keys whose value match. This is the brute force way to
perform this particular task.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Search Key from Value

# Using naive method

 

# initializing dictionary

test_dict = {'Gfg' : 1, 'for' : 2, 'CS' : 3}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing value

val = 3

 

# Using naive method 

# Search key from Value

for key in test_dict:

 if test_dict[key] == val:

 res = key

 

# printing result 

print("The key correspoding to value : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary is : {'CS': 3, 'for': 2, 'Gfg': 1}
    The key correspoding to value : CS
    

**Method #2 : Usingitems() \+ list comprehension**  
This problem can be easily solved using the items(), which is used to
extract both keys and values at once, hence making the search easy and can be
executed using list comprehension making it a one liner.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Search Key from Value

# Using items() + list comprehension

 

# initializing dictionary

test_dict = {'Gfg' : 1, 'for' : 2, 'CS' : 3}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing value

val = 3

 

# Using items() + list comprehension

# Search key from Value

res = [key for key, value in test_dict.items() if value
== val]

 

# printing result 

print("The key correspoding to value : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary is : {'CS': 3, 'for': 2, 'Gfg': 1}
    The key correspoding to value : ['CS']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


Python | Add keys to nested dictionary



Addition of keys in dictionaries have been discussed many times, but
sometimes, we might have a problem in which we require to alter/add keys in
the nested dictionary. This type of problem is common in today’s world with
advent of NoSQL databases. Let’s discuss certain ways in which this problem
can be solved.

 **Method #1 : Using dictionary brackets**  
This task can be easily performed using the naive method of just keep nesting
the dictionary brackets with the new value and new key is created on the go
and the dictionary is updated.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Update nested dictionary keys

# Using dictionary brackets

 

# initializing dictionary

test_dict = {'GFG' : {'rate' : 4, 'since' : 2012}}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Using dictionary brackets

# Update nested dictionary keys

test_dict['GFG']['rank'] = 1

 

# printing result 

print("Dictionary after nested key update : " + str(test_dict))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary is : {'GFG': {'rate': 4, 'since': 2012}}
    Dictionary after nested key update : {'GFG': {'rate': 4, 'since': 2012, 'rank': 1}}
    

**Method #2 : Usingupdate()**  
This method is used in cases where more than one keys need to be added to the
nested dictionaries. The update function accepts the dictionary and added
the dictionary with the keys in it.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Update nested dictionary keys

# Using update()

 

# initializing dictionaries

test_dict = {'GFG' : {'rate' : 4, 'since' : 2012}}

upd_dict = {'rank' : 1, 'popularity' : 5}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Using update()

# Update nested dictionary keys

test_dict['GFG'].update(upd_dict)

 

# printing result 

print("Dictionary after nested key update : " + str(test_dict))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary is : {'GFG': {'rate': 4, 'since': 2012}}
    Dictionary after nested key update : {'GFG': {'popularity': 5, 'rate': 4, 'since': 2012, 'rank': 1}}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


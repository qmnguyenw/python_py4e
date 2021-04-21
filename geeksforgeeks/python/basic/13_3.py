Python | Extract specific keys from dictionary



We have a lot of variations and applications of dictionary container in Python
and sometimes, we wish to perform a filter of keys in dictionary, i.e
extracting just the keys which are present in particular container. Let’s
discuss certain ways in which this can be performed.

 **Method #1 : Using dictionary comprehension +items()**

This problem can be performed by reconstruction using the keys extracted
through items function that wish to be filtered and dictionary function makes
the desired dictionary.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Extracting specifix keys from dictionary

# Using dictionary comprehension + items()

 

# initializing dictionary

test_dict = {'nikhil' : 1, "akash" : 2, 'akshat' :
3, 'manjeet' : 4}

 

# printing original list

print("The original dictionary : " + str(test_dict))

 

# Using dictionary comprehension + items()

# Extracting specifix keys from dictionary

res = {key: test_dict[key] for key in test_dict.keys()

 & {'akshat', 'nikhil'}}

 

# print result

print("The filtered dictionary is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary : {'manjeet': 4, 'akshat': 3, 'akash': 2, 'nikhil': 1}
    The filtered dictionary is : {'akshat': 3, 'nikhil': 1}
    

  

  

**Method #2 : Usingdict()**

The dict function can be used to perform this task by converting the logic
performed using list comprehension into a dictionary.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Extracting specifix keys from dictionary

# Using dict()

 

# initializing dictionary

test_dict = {'nikhil' : 1, "akash" : 2, 'akshat' :
3, 'manjeet' : 4}

 

# printing original list

print("The original dictionary : " + str(test_dict))

 

# Using dict()

# Extracting specifix keys from dictionary

res = dict((k, test_dict[k]) for k in ['nikhil',
'akshat']

 if k in test_dict)

 

# print result

print("The filtered dictionary is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary : {'manjeet': 4, 'akshat': 3, 'akash': 2, 'nikhil': 1}
    The filtered dictionary is : {'akshat': 3, 'nikhil': 1}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


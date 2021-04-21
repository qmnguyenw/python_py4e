Python | Safe access nested dictionary keys



Sometimes, while working with Python we can have a problem in which we need to
get the 2nd degree key of dictionary i.e the nested key. This type of problem
is common in case of web development, especially with the advent of NoSQL
databases. Let’s discuss certain ways to safely get the nested available key
in dictionary.

 **Method #1 : Using nestedget()**

This method is used to solve this particular problem, we just take advantage
of the functionality of get() to check and assign in absence of value to
achieve this particular task. Just returns non-error None if any key is not
present.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Safe access nested dictionary key

# Using nested get()

 

# initializing dictionary

test_dict = {'Gfg' : {'is' : 'best'}}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# using nested get()

# Safe access nested dictionary key

res = test_dict.get('Gfg', {}).get('is')

 

# printing result

print("The nested safely accessed value is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary is : {'Gfg': {'is': 'best'}}
    The nested safely accessed value is :  best
    

  

  

**Method #2 : Usingreduce() \+ lambda**

The combination of above functions can be used to perform this particular
task. It just checks using lambda function for the available keys. The plus of
this method is that more than 1 key can be queried at once i.e more nested
level keys, but the negative is that it does only work with Python2.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate working of

# Safe access nested dictionary key

# Using reduce() + lambda

 

# initializing dictionary

test_dict = {'Gfg' : {'is' : 'best'}}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# using reduce() + lambda

# Safe access nested dictionary key

keys = ['Gfg', 'is']

res = reduce(lambda val, key: val.get(key) if val else
None, keys, test_dict)

 

# printing result

print("The nested safely accessed value is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary is : {'Gfg': {'is': 'best'}}
    The nested safely accessed value is :  best
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


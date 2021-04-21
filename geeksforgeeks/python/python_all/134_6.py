Python | Check if one dictionary is subset of other



Sometimes, while working with Python, we might have a problem in which we need
to find, if a particular dictionary is a part of other i.e it is subset of
other. A problem that have a huge potential in web development domain, having
knowledge of solving can be useful. Let’s discuss certain ways in which this
task can be performed.

 **Method #1 : Usingall() + items()**  
This task can be performed using the combination of above two functions, in
which we check for all the items of the subdict with the original dict using
all() and fetch it’s each pair using items().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Check if one dictionary is subset of other

# Using all() + items()

 

# Initialize dictionaries

test_dict1 = {'gfg' : 1, 'is' : 2, 'best' : 3,
'for' : 4, 'CS' : 5}

test_dict2 = {'gfg' : 1, 'is' : 2, 'best' : 3}

 

# printing original dictionaries

print("The original dictionary 1 : " + str(test_dict1))

print("The original dictionary 2 : " + str(test_dict2))

 

# Using all() + items()

# Check if one dictionary is subset of other

res = all(test_dict1.get(key, None) == val for key, val

 in test_dict2.items())

 

# printing result 

print("Does dict2 lie in dict1 ? : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original dictionary 1 : {‘CS’: 5, ‘is’: 2, ‘best’: 3, ‘gfg’: 1, ‘for’:
> 4}  
> The original dictionary 2 : {‘is’: 2, ‘best’: 3, ‘gfg’: 1}  
> Does dict2 lie in dict1 ? : True

  

  

**Method #2 : Usingitems() + <= operator**  
Another alternative to perform the above task can be using the items() along
with <= operator. This just checks for less than or all values of all the
key value matched.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Check if one dictionary is subset of other

# Using items() + <= operator

 

# Initialize dictionaries

test_dict1 = {'gfg' : 1, 'is' : 2, 'best' : 3,
'for' : 4, 'CS' : 5}

test_dict2 = {'gfg' : 1, 'is' : 2, 'best' : 3}

 

# printing original dictionaries

print("The original dictionary 1 : " + str(test_dict1))

print("The original dictionary 2 : " + str(test_dict2))

 

# Using items() + <= operator

# Check if one dictionary is subset of other

res = test_dict2.items() <= test_dict1.items()

 

# printing result 

print("Does dict2 lie in dict1 ? : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original dictionary 1 : {‘CS’: 5, ‘is’: 2, ‘best’: 3, ‘gfg’: 1, ‘for’:
> 4}  
> The original dictionary 2 : {‘is’: 2, ‘best’: 3, ‘gfg’: 1}  
> Does dict2 lie in dict1 ? : True

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


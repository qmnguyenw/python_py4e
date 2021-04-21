Python | Minimum value keys in Dictionary



Many times, we may have problem in which we require to find not just the
value, but the corresponding keys to the minimum value in the entire
dictionary. Let’s discuss certain ways in which this task can be performed.

 **Method #1 : Using min() + list comprehension + values()**  
The combination of above functions can be used to perform this particular
task. In this, minimum value is extracted using the min function, while
values of dictionary is extracted using values(). The list comprehension is
used to iterate through the dictionary for matching keys with min value.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Finding min value keys in dictionary

# Using min() + list comprehension + values()

 

# initializing dictionary

test_dict = {'Gfg' : 11, 'for' : 2, 'CS' : 11,
'geeks':8, 'nerd':2}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Using min() + list comprehension + values()

# Finding min value keys in dictionary

temp = min(test_dict.values())

res = [key for key in test_dict if test_dict[key] ==
temp]

 

# printing result 

print("Keys with minimum values are : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original dictionary is : {‘nerd’: 2, ‘Gfg’: 11, ‘geeks’: 8, ‘CS’: 11,
> ‘for’: 2}  
> Keys with minimum values are : [‘nerd’, ‘for’]

  

  

**Method #2 : Usingall() \+ list comprehension**  
This task can also be performed using list comprehension and all function. In
this, we take all the elements values, using all function that are greater
than values with keys and return the keys with smallest values using list
comprehension.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Finding min value keys in dictionary

# Using all() + list comprehension

 

# initializing dictionary

test_dict = {'Gfg' : 1, 'for' : 2, 'CS' : 1}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Using all() + list comprehension

# Finding min value keys in dictionary

res = [key for key in test_dict if

 all(test_dict[temp] >= test_dict[key]

 for temp in test_dict)]

 

# printing result 

print("Keys with minimum values are : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original dictionary is : {‘Gfg’: 1, ‘CS’: 1, ‘for’: 2}  
> Keys with minimum values are : [‘Gfg’, ‘CS’]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


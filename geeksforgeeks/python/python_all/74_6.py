Python – Distinct Flatten dictionaries



Sometimes, while working with dictionaries, we can have keys which in itself
is a part of very complex nestings and we wish to extract all the keys and
values of particular key nesting into a separate list. This kind of problem
can have applications in many domains such as web development. Lets discuss
certain ways in which this task can be performed.

 **Method #1 : Using loop +isinstance() \+ list comprehension**  
The combination of above functions can be used to solve this problem. In this,
we perform the task of flattening dictionary using checks with isinstance()
and loop. At last list comprehension is used to compile the result in the form
of dictionary list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Distinct Flatten dictionaries

# Using loop + isinstance() + list comprehension

 

def flatten(temp_dict, temp_list):

 for key, val in temp_dict.items():

 if isinstance(val, dict):

 temp_list.append(key)

 flatten(val, temp_list)

 else:

 temp_list.extend([key, val])

 return temp_list

 

# initializing dictionary

test_dict = {'gfg' : {'is' : 4, "best" : 10}, 'is'
: {'for' : { 'geeks' : 8 }}}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Distinct Flatten dictionaries

# Using loop + isinstance() + list comprehension

res = [flatten(val, [key]) for key, val in test_dict.items()]

 

# printing result 

print("The flattened dictionary elements : " + str(res))   
  
---  
  
__

__

**Output :**

> The original dictionary is : {‘is’: {‘for’: {‘geeks’: 8}}, ‘gfg’: {‘is’: 4,
> ‘best’: 10}}  
> The flattened dictionary elements : [[‘is’, ‘for’, ‘geeks’, 8], [‘gfg’,
> ‘is’, 4, ‘best’, 10]]

  

  

**Method #2 : Usingyield + isinstance()**  
This task can also be performed using combination of above functions. In this,
we use dynamic data rendering using yeild to make process compact and
readable.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Distinct Flatten dictionaries

# Using yield + isinstance()

 

def flatten(temp_dict):

 if isinstance(temp_dict, dict):

 for key, val in temp_dict.items():

 yield key

 yield from flatten(val)

 else:

 yield temp_dict

 

# initializing dictionary

test_dict = {'gfg' : {'is' : 4, "best" : 10}, 'is'
: {'for' : { 'geeks' : 8 }}}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Distinct Flatten dictionaries

# Using yield + isinstance()

res = [[key, *flatten(val)] for key, val in
test_dict.items()]

 

# printing result 

print("The flattened dictionary elements : " + str(res))   
  
---  
  
__

__

**Output :**

> The original dictionary is : {‘is’: {‘for’: {‘geeks’: 8}}, ‘gfg’: {‘is’: 4,
> ‘best’: 10}}  
> The flattened dictionary elements : [[‘is’, ‘for’, ‘geeks’, 8], [‘gfg’,
> ‘is’, 4, ‘best’, 10]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


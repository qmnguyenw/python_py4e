Python | Iterate through value lists dictionary



While working with dictionary, we can have a case in which we need to iterate
through the lists, which are in the keys of dictionaries. This kind of problem
can occur in web development domain. Let’s discuss certain ways in which this
problem can be solved.

 **Method #1 : Using list comprehension**  
List comprehension can be used to perform this particular task. It is just the
shorthand to the conventional nested loops. we iterate for each key’s list and
store the result.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Iterating through value lists dictionary

# Using list comprehension

 

# Initialize dictionary

test_dict = {'gfg' : [1, 2], 'is' : [4, 5],
'best' : [7, 8]}

 

# printing original dictionary

print("The original dictionary : " + str(test_dict))

 

# Using list comprehension

# Iterating through value lists dictionary

res = [[i for i in test_dict[x]] for x in
test_dict.keys()]

 

# printing result 

print("The list values of keys are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original dictionary : {‘best’: [7, 8], ‘is’: [4, 5], ‘gfg’: [1, 2]}  
> The list values of keys are : [[7, 8], [4, 5], [1, 2]]

  

  

**Method #2 : Usingfrom_iterable() + product() + items()**  
The combination of above functions can be used to perform this particular
task. The from_iterable() can be used to reduce inner loop and items
function is used to extract key value pairs in the dictionary.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Iterating through value lists dictionary

# Using from_iterable() + product() + items()

import itertools

 

# Initialize dictionary

test_dict = {'gfg' : [1, 2], 'is' : [4, 5],
'best' : [7, 8]}

 

# printing original dictionary

print("The original dictionary : " + str(test_dict))

 

# Iterating through value lists dictionary

# Using from_iterable() + product() + items()

res = []

for key, value in (

 itertools.chain.from_iterable(

 [itertools.product((k, ), v) for k, v in test_dict.items()])):

 res.append(value)

 

# printing result 

print("The list values of keys are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original dictionary : {‘best’: [7, 8], ‘is’: [4, 5], ‘gfg’: [1, 2]}  
> The list values of keys are : [7, 8, 1, 2, 4, 5]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


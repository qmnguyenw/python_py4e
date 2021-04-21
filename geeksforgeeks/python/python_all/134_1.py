Python | Updating value list in dictionary



While working with dictionary with list as value is always vulnerable of
getting it’s value updated. The ways or shorthands to perform this task can be
handy in such situations. This can occur in web development domain. Let’s
discuss certain ways in which this task can be performed.

 **Method #1 : Using list comprehension**  
The naive method to perform this particular task, in this, we just extract the
key and then iterate over it’s value in list comprehensive format in packed
list. This solved the problem.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Updating value list in dictionary

# Using list comprehension

 

# Initialize dictionary

test_dict = {'gfg' : [1, 5, 6], 'is' : 2,
'best' : 3}

 

# printing original dictionary

print("The original dictionary : " + str(test_dict))

 

# Using list comprehension

# Updating value list in dictionary

test_dict['gfg'] = [x * 2 for x in test_dict['gfg']]

 

# printing result 

print("Dictionary after updation is : " + str(test_dict))  
  
---  
  
 __

 __

 **Output :**

> The original dictionary : {‘is’: 2, ‘gfg’: [1, 5, 6], ‘best’: 3}  
> Dictionary after updation is : {‘is’: 2, ‘gfg’: [2, 10, 12], ‘best’: 3}

  

  

**Method #2 : Usingmap() \+ lambda**  
This task can be performed using the combination of above two functions in
which we use the map() to link the function of updation to each of element of
value list and lambda is used to specify the updation.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Updating value list in dictionary

# Using map() + lambda

 

# Initialize dictionary

test_dict = {'gfg' : [1, 5, 6], 'is' : 2,
'best' : 3}

 

# printing original dictionary

print("The original dictionary : " + str(test_dict))

 

# Using map() + lambda

# Updating value list in dictionary

test_dict['gfg'] = list(map(lambda x:x * 2,
test_dict['gfg']))

 

# printing result 

print("Dictionary after updation is : " + str(test_dict))  
  
---  
  
 __

 __

 **Output :**

> The original dictionary : {‘is’: 2, ‘gfg’: [1, 5, 6], ‘best’: 3}  
> Dictionary after updation is : {‘is’: 2, ‘gfg’: [2, 10, 12], ‘best’: 3}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


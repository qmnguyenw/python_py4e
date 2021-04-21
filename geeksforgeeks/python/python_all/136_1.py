Python | Remove multiple keys from dictionary



While working with Python dictionaries, we can have utility in which we
require to remove more than one keys at once. This type of problem can occur
while working in Web Development domain with NoSQL Databases. Let’s discuss
certain ways in which this task can be performed.

 **Method #1 : Usingpop() \+ list comprehension**  
In this method, we just use the pop function which is used to remove a single
key along with the list comprehension which iterates for the entire list to
perform the remove operation.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove multiple keys from dictionary

# Using pop() + list comprehension

 

# initializing dictionary

test_dict = {'Gfg' : 1, 'is' : 2, 'best' : 3,
'for' : 4, 'CS' : 5}

 

# initializing Remove keys

rem_list = ['is', 'for', 'CS']

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Using pop() + list comprehension

# Remove multiple keys from dictionary

[test_dict.pop(key) for key in rem_list]

 

# printing result 

print("Dictionary after removal of keys : " + str(test_dict))  
  
---  
  
 __

 __

 **Output :**

> The original dictionary is : {‘is’: 2, ‘best’: 3, ‘for’: 4, ‘Gfg’: 1, ‘CS’:
> 5}  
> Dictionary after removal of keys : {‘best’: 3, ‘Gfg’: 1}

  

  

**Method #2 : Usingitems() \+ list comprehension + dict()**  
In this method, rather than removal of keys, we reconstruct the dictionary
using the dict function, by extracting key and value pairs using items()
and iterating over them using list comprehension.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove multiple keys from dictionary

# Using items() + list comprehension + dict()

 

# initializing dictionary

test_dict = {'Gfg' : 1, 'is' : 2, 'best' : 3,
'for' : 4, 'CS' : 5}

 

# initializing Remove keys

rem_list = ['is', 'for', 'CS']

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Using items() + list comprehension + dict()

# Remove multiple keys from dictionary

res = dict([(key, val) for key, val in

 test_dict.items() if key not in rem_list])

 

# printing result 

print("Dictionary after removal of keys : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original dictionary is : {‘is’: 2, ‘best’: 3, ‘for’: 4, ‘Gfg’: 1, ‘CS’:
> 5}  
> Dictionary after removal of keys : {‘best’: 3, ‘Gfg’: 1}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


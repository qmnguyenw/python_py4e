Python – Convert Key-Value list Dictionary to List of Lists



Sometimes, while working with Python dictionary, we can have a problem in
which we need to perform the flattening a key value pair of dictionary to a
list and convert to lists of list. This can have applications in domains in
which we have data. Lets discuss certain ways in which this task can be
performed.

 **Method #1 : Using loop +items()**  
This brute force way in which we can perform this task. In this, we loop
through all the pairs and extract list value elements using items() and render
in a new list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert Key-Value list Dictionary to Lists of List

# Using loop + items()

 

# initializing Dictionary

test_dict = {'gfg' : [1, 3, 4], 'is' : [7,
6], 'best' : [4, 5]}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Convert Key-Value list Dictionary to Lists of List

# Using loop + items()

res = []

for key, val in test_dict.items():

 res.append([key] + val)

 

# printing result 

print("The converted list is : " + str(res))   
  
---  
  
__

__

**Output :**

> The original dictionary is : {‘gfg’: [1, 3, 4], ‘is’: [7, 6], ‘best’: [4,
> 5]}  
> The converted list is : [[‘gfg’, 1, 3, 4], [‘is’, 7, 6], [‘best’, 4, 5]]

  

  

**Method #2 : Using list comprehension**  
This task can also be performed using list comprehension. In this, we perform
the task similar to above method just in one-liner shorter way.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert Key-Value list Dictionary to Lists of List

# Using list comprehension

 

# initializing Dictionary

test_dict = {'gfg' : [1, 3, 4], 'is' : [7,
6], 'best' : [4, 5]}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Convert Key-Value list Dictionary to Lists of List

# Using list comprehension

res = [[key] + val for key, val in test_dict.items()]

 

# printing result 

print("The converted list is : " + str(res))   
  
---  
  
__

__

**Output :**

> The original dictionary is : {‘gfg’: [1, 3, 4], ‘is’: [7, 6], ‘best’: [4,
> 5]}  
> The converted list is : [[‘gfg’, 1, 3, 4], [‘is’, 7, 6], [‘best’, 4, 5]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


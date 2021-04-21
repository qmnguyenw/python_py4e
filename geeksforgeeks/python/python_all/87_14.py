Python – Group elements from Dual List Matrix



Sometimes, while working with Python list, we can have a problem in which we
need to group the elements in list with the first element of Matrix and
perform the Grouping in form of dictionary. This can have advantage in many
domains. Lets discuss certain ways in which this task can be performed.

 **Method #1 : Using loop + list comprehension**  
The combination of above methods can be used in performing this task. In this,
we iterate through the dual element row and compute the dictionary with
mapping of elements from list and 2nd column of dual row matrix.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Group elements from Dual List Matrix

# using loop + list comprehension

 

# Initializing lists

test_list1 = ['Gfg', 'is', 'best']

test_list2 = [['Gfg', 1], ['is', 2], ['best', 1],
['Gfg', 4], ['is', 8], ['Gfg', 7]]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# Group elements from Dual List Matrix

# using loop + list comprehension

res = {key: [] for key in test_list1}

for key in res:

 res[key] = [sub[1] for sub in test_list2 if key
== sub[0]]

 

# printing result 

print ("The dictionary after grouping : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list 1 is : [‘Gfg’, ‘is’, ‘best’]  
> The original list 2 is : [[‘Gfg’, 1], [‘is’, 2], [‘best’, 1], [‘Gfg’, 4],
> [‘is’, 8], [‘Gfg’, 7]]  
> The dictionary after grouping : {‘is’: [2, 8], ‘Gfg’: [1, 4, 7], ‘best’:
> [1]}

  

  

**Method #2 : Using dictionary comprehension**  
This is yet another way in which this task can be performed. In this, we
compile the logic performed above into one single dictionary comprehension for
better readability.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Group elements from Dual List Matrix

# using dictionary comprehension

 

# Initializing lists

test_list1 = ['Gfg', 'is', 'best']

test_list2 = [['Gfg', 1], ['is', 2], ['best', 1],
['Gfg', 4], ['is', 8], ['Gfg', 7]]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# Group elements from Dual List Matrix

# using dictionary comprehension

res = {key: [sub[1] for sub in test_list2 if key ==
sub[0]] for key in test_list1}

 

# printing result 

print ("The dictionary after grouping : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list 1 is : [‘Gfg’, ‘is’, ‘best’]  
> The original list 2 is : [[‘Gfg’, 1], [‘is’, 2], [‘best’, 1], [‘Gfg’, 4],
> [‘is’, 8], [‘Gfg’, 7]]  
> The dictionary after grouping : {‘is’: [2, 8], ‘Gfg’: [1, 4, 7], ‘best’:
> [1]}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


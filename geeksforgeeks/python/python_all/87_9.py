Python – Flatten List to individual elements



Sometimes, while working with Python list, we can have a problem in which we
need to perform flatten of list, i.e convert a mixed list to flattened one.
This can have application in domains which use 1D lists as input. Lets discuss
certain ways in which this task can be performed.

 **Method #1 : Using loop +isinstance()**  
The combination of above functionalities can be used to perform this task. In
this, we check for instance of list and flatten it and rest of elements we add
to list brutely.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Flatten List to individual elements

# using loop + isinstance()

 

def flatten(test_list):

 if isinstance(test_list, list):

 temp = []

 for ele in test_list:

 temp.extend(flatten(ele))

 return temp

 else:

 return [test_list]

 

# Initializing list

test_list = ['gfg', 1, [5, 6, 'geeks'], 67.4,
[5], 'best']

 

# printing original list

print("The original list is : " + str(test_list))

 

# Flatten List to individual elements

# using loop + isinstance()

res = flatten(test_list)

 

# printing result 

print ("The List after flattening : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list is : [‘gfg’, 1, [5, 6, ‘geeks’], 67.4, [5], ‘best’]  
> The List after flattening : [‘gfg’, 1, 5, 6, ‘geeks’, 67.4, 5, ‘best’]

  

  

**Method #2 : Usingchain() + isinstance()**  
This is yet another way in which this task can be performed. In this we
perform the task of iteration using chain() and checking for list instance is
done using isinstance().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Flatten List to individual elements

# using chain() + isinstance()

from itertools import chain

 

# Initializing list

test_list = ['gfg', 1, [5, 6, 'geeks'], 67.4,
[5], 'best']

 

# printing original list

print("The original list is : " + str(test_list))

 

# Flatten List to individual elements

# using chain() + isinstance()

res = list(chain(*[ele if isinstance(ele, list) else
[ele] for ele in test_list]))

 

# printing result 

print ("The List after flattening : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list is : [‘gfg’, 1, [5, 6, ‘geeks’], 67.4, [5], ‘best’]  
> The List after flattening : [‘gfg’, 1, 5, 6, ‘geeks’, 67.4, 5, ‘best’]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


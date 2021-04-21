Python – Nested Records List from Lists



Sometimes, while working with Python Data, we can have problem in which we
have data incoming in different formats. In this, we can receive data as key
and value in separate dictionary and we require to make values as list of
records with a new key. Lets discuss certain ways in which this task can be
performed.

 **Method #1 : Usingzip() \+ loop**  
The combination of above functionalities can be used to solve this problem. In
this, we perform the pairing using zip and manual intervention of adding key
is done in brute way.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Nested Records List from Lists

# Using zip() + loop

 

# initializing lists

test_list1 = ['gfg', 'best']

test_list2 = [[1, 2], [3, 4]]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# initializing add_key 

add_key = 'id'

 

# Nested Records List from Lists

# Using zip() + loop

res = dict()

for key, val in zip(test_list1, test_list2):

 res[key]=[{add_key : idx} for idx in val]

 

# printing result 

print("The constructed dictionary is : " + str(res))   
  
---  
  
__

__

**Output :**

> The original list 1 is : [‘gfg’, ‘best’]  
> The original list 2 is : [[1, 2], [3, 4]]  
> The constructed dictionary is : {‘gfg’: [{‘id’: 1}, {‘id’: 2}], ‘best’:
> [{‘id’: 3}, {‘id’: 4}]}

  

  

**Method #2 : Using dictionary comprehension +zip()**  
This is yet another way to perform this task. This is similar to above method,
just a one-liner alternative of above.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Nested Records List from Lists

# Using dictionary comprehension + zip()

 

# initializing lists

test_list1 = ['gfg', 'best']

test_list2 = [[1, 2], [3, 4]]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# initializing add_key 

add_key = 'id'

 

# Nested Records List from Lists

# Using dictionary comprehension + zip()

res = {key : [{add_key : idx} for idx in val] 

 for key, val in zip(test_list1, test_list2)}

 

# printing result 

print("The constructed dictionary is : " + str(res))   
  
---  
  
__

__

**Output :**

> The original list 1 is : [‘gfg’, ‘best’]  
> The original list 2 is : [[1, 2], [3, 4]]  
> The constructed dictionary is : {‘gfg’: [{‘id’: 1}, {‘id’: 2}], ‘best’:
> [{‘id’: 3}, {‘id’: 4}]}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


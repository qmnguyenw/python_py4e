Python – Assign list items to Dictionary



Sometimes, while working with Python dictionaries, we can have a problem in
which we need to assign list elements as a new key in dictionary. This task
can occur in web development domain. Lets discuss certain ways in which this
task can be performed.

 **Method #1 : Using zip() + loop**  
The combination of above functions can be used to solve this problem. In this,
we combine list elements with dictionary using zip() and loop is used to
combine iteration logic.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Assign list items to Dictionary

# Using zip() + loop

 

# initializing list

test_list = [{'Gfg' : 1, 'id' : 2 }, 

 {'Gfg' : 4, 'id' : 4 }]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing key 

new_key = 'best'

 

# initializing list 

add_list = [12, 2]

 

# Assign list items to Dictionary

# Using zip() + loop

res = []

for sub, val in zip(test_list, add_list):

 sub[new_key] = val

 res.append(sub)

 

# printing result 

print("The modified dictionary : " + str(res))   
  
---  
  
__

__

**Output :**

> The original list is : [{‘Gfg’: 1, ‘id’: 2}, {‘Gfg’: 4, ‘id’: 4}]  
> The modified dictionary : [{‘best’: 12, ‘Gfg’: 1, ‘id’: 2}, {‘best’: 2,
> ‘Gfg’: 4, ‘id’: 4}]

  

  

**Method #2 : Using list comprehension + zip()**  
The combination of above functions can be used to solve this problem. In this,
we perform the iteration of elements using list comprehension and hence a
shorthand.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Assign list items to Dictionary

# Using list comprehension + zip()

 

# initializing list

test_list = [{'Gfg' : 1, 'id' : 2 }, 

 {'Gfg' : 4, 'id' : 4 }]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing key 

new_key = 'best'

 

# initializing list 

add_list = [12, 2]

 

# Assign list items to Dictionary

# Using list comprehension + zip()

res = [{**sub, new_key : ele} for sub, ele in
zip(test_list, add_list)]

 

# printing result 

print("The modified dictionary : " + str(res))   
  
---  
  
__

__

**Output :**

> The original list is : [{‘Gfg’: 1, ‘id’: 2}, {‘Gfg’: 4, ‘id’: 4}]  
> The modified dictionary : [{‘best’: 12, ‘Gfg’: 1, ‘id’: 2}, {‘best’: 2,
> ‘Gfg’: 4, ‘id’: 4}]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


Python – All possible items combination dictionary



Sometimes, while working with data, we can have a problem in which we are
provided with sample data of key and value list and we require to construct
actual data as all possible combination of keys and value list of similar
size. Lets discuss certain ways in which this task can be performed.

 **Method #1 : Using loop +set()**  
The combination of above functionalities can be employed to solve this
problem. In this, we initially extract all items flattened in list of sets.
Then we construct each dictionary using set subtraction.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# All possible items combination dictionary

# Using loop + set()

 

# initializing Dictionary

test_dict = {'gfg' : [1, 3], 'is' : [5, 6],
'best' : [4, 7]}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# All possible items combination dictionary

# Using loop + set()

temp = [set([key]) | set(value) for key, value in
test_dict.items() ]

res = {}

for sub in temp:

 for key in sub:

 res[key] = list(sub - set([key]))

 

# printing result 

print("The all possible items dictionary : " + str(res))   
  
---  
  
__

__

**Output :**

> The original dictionary is : {‘is’: [5, 6], ‘gfg’: [1, 3], ‘best’: [4, 7]}  
> The all possible items dictionary : {1: [3, ‘gfg’], 3: [1, ‘gfg’], 4:
> [‘best’, 7], 5: [‘is’, 6], 6: [‘is’, 5], 7: [4, ‘best’], ‘best’: [4, 7],
> ‘is’: [5, 6], ‘gfg’: [1, 3]}

  

  

**Method #2 : Usingremove() + loop + update()**  
This is yet another way in which this task can be performed. In this, we
perform the task of removal of values already present using remove() and
construct new dictionary items.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# All possible items combination dictionary

# Using remove() + loop + update()

 

# initializing Dictionary

test_dict = {'gfg' : [1, 3], 'is' : [5, 6],
'best' : [4, 7]}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# All possible items combination dictionary

# Using remove() + loop + update()

res = {}

for key, val in test_dict.items():

 for ele in val:

 temp = val[:]

 temp.remove(ele)

 res.update({ele: [key] + temp})

test_dict.update(res)

 

# printing result 

print("The all possible items dictionary : " + str(test_dict))   
  
---  
  
__

__

**Output :**

> The original dictionary is : {‘is’: [5, 6], ‘gfg’: [1, 3], ‘best’: [4, 7]}  
> The all possible items dictionary : {1: [3, ‘gfg’], 3: [1, ‘gfg’], 4:
> [‘best’, 7], 5: [‘is’, 6], 6: [‘is’, 5], 7: [4, ‘best’], ‘best’: [4, 7],
> ‘is’: [5, 6], ‘gfg’: [1, 3]}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


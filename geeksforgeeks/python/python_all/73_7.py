Python – Convert Records List to Segregated Dictionary



Sometimes, while working with Python records, we can have a problem in which
we need to convert each element of tuple records into a separate key in
dictionary, with each index having different value. This kind of problem can
have application in data domains. Lets discuss certain ways in which this task
can be performed.

 **Method #1 : Using loop**  
This is one of the way to solve this problem. In this, we iterate for list of
tuples and assign the required value to each key for newly constructed
dictionary.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert Records List to Segregated Dictionary

# Using loop

 

# initializing list

test_list = [(1, 2), (3, 4), (5, 6)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing index value

frst_idx = "Gfg"

scnd_idx = 'best'

 

# Convert Records List to Segregated Dictionary

# Using loop

res = dict()

for sub in test_list:

 res[sub[0]] = frst_idx

 res[sub[1]] = scnd_idx

 

# printing result 

print("The constructed Dictionary list : " + str(res))   
  
---  
  
__

__

**Output :**

> The original list is : [(1, 2), (3, 4), (5, 6)]  
> The constructed Dictionary list : {1: ‘Gfg’, 2: ‘best’, 3: ‘Gfg’, 4: ‘best’,
> 5: ‘Gfg’, 6: ‘best’}

  

  

**Method #2 : Usingzip() + chain() + cycle() \+ list comprehension**  
The combination of above functions can be used to perform this task. In this,
we unpack the values using chain() and then alternate cycle the values to be
initialized and then zip back the values using zip().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert Records List to Segregated Dictionary

# Using zip() + chain() + cycle() + list comprehension

from itertools import chain, cycle

 

# initializing list

test_list = [(1, 2), (3, 4), (5, 6)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing index value

frst_idx = "Gfg"

scnd_idx = 'best'

 

# Convert Records List to Segregated Dictionary

# Using zip() + chain() + cycle() + list comprehension

res = dict(zip(chain(*test_list), cycle([frst_idx,
scnd_idx])))

 

# printing result 

print("The constructed Dictionary list : " + str(res))   
  
---  
  
__

__

**Output :**

> The original list is : [(1, 2), (3, 4), (5, 6)]  
> The constructed Dictionary list : {1: ‘Gfg’, 2: ‘best’, 3: ‘Gfg’, 4: ‘best’,
> 5: ‘Gfg’, 6: ‘best’}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


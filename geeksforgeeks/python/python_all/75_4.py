Python – Value Dictionary from Record List



Sometimes, while working with Python Records lists, we can have problem in
which, we need to reform the dictionary taking just values of binary
dictionary. This can have application in many domains which work with data.
Lets discuss certain ways in which this task can be performed.

 **Method #1 : Using loop +values() + update()**  
The combination of above functions can be used to perform this task. In this
the values are extracted using values() and updating new dictionary is done
using update().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Value Dictionary from Record List

# Using loop + values() + update()

 

# initializing list

test_list = [{1 : 'gfg', 2 : 'best'}, {3 : 'for',
4 : 'geeks'}]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Value Dictionary from Record List

# Using loop + values() + update()

res = dict()

for sub in test_list:

 res.update((sub.values(), ))

 

# printing result 

print("The values dictionary is : " + str(dict(res)))   
  
---  
  
__

__

**Output :**

> The original list is : [{1: ‘gfg’, 2: ‘best’}, {3: ‘for’, 4: ‘geeks’}]  
> The values dictionary is : {‘gfg’: ‘best’, ‘for’: ‘geeks’}

  

  

**Method #2 : Usingzip() + iter()**  
The combination of above functions can also be used to perform this task. In
this, we perform convert the list to iterator and pairing of values is done
using zip().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Value Dictionary from Record List

# Using zip() + iter()

 

# initializing list

test_list = [{1 : 'gfg', 2 : 'best'}, {3 : 'for',
4 : 'geeks'}]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Value Dictionary from Record List

# Using zip() + iter()

res = dict()

for sub in test_list:

 itr = iter(sub.values())

 res.update(dict(zip(itr, itr)))

 

# printing result 

print("The values dictionary is : " + str(res))   
  
---  
  
__

__

**Output :**

> The original list is : [{1: ‘gfg’, 2: ‘best’}, {3: ‘for’, 4: ‘geeks’}]  
> The values dictionary is : {‘gfg’: ‘best’, ‘for’: ‘geeks’}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


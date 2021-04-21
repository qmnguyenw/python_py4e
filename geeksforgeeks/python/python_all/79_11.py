Python – Keys with shortest length lists in dictionary



Sometimes, while working with Python lists, we can have problem in which we
need to return the keys which have minimum lengths of lists as values. This
can have application in domains in which we work with data. Lets discuss
certain ways in which this task can be performed.

 **Method #1 : Usinglen() + loop + items()**  
The combination of above functions can be used to perform this task. In this,
we iterate the keys of dictionary and return all the keys whose lengths
equates the length of smallest list using len().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Keys with shortest length lists in dictionary

# Using len() + loop + items()

 

# initializing dictionary

test_dict = {'gfg' : [4, 5],

 'is' : [9, 7, 3, 10],

 'best' : [11, 34],

 'for' : [6, 8, 2], 

 'geeks' : [12, 24]}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Keys with shortest length lists in dictionary

# Using len() + loop + items()

min_val = min([len(test_dict[ele]) for ele in test_dict])

res = []

for ele in test_dict:

 if len(test_dict[ele]) == min_val:

 res.append(ele)

 

# printing result 

print("The required keys are : " + str(res))   
  
---  
  
__

__

**Output :**

> The original dictionary is : {‘is’: [9, 7, 3, 10], ‘gfg’: [4, 5], ‘best’:
> [11, 34], ‘for’: [6, 8, 2], ‘geeks’: [12, 24]}  
> The required keys are : [‘gfg’, ‘best’, ‘geeks’]

  

  

**Method #2 : Using list comprehension**  
This task can also be performed using a shorthand of list comprehension. In
this, we perform the task similar to above task but in shorthand manner.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Keys with shortest length lists in dictionary

# Using list comprehension

 

# initializing dictionary

test_dict = {'gfg' : [4, 5],

 'is' : [9, 7, 3, 10],

 'best' : [11, 34],

 'for' : [6, 8, 2], 

 'geeks' : [12, 24]}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Keys with shortest length lists in dictionary

# Using list comprehension

min_val = min([len(test_dict[ele]) for ele in test_dict])

res = [key for key, val in test_dict.items() if len(val)
== min_val] 

 

# printing result 

print("The required keys are : " + str(res))   
  
---  
  
__

__

**Output :**

> The original dictionary is : {‘is’: [9, 7, 3, 10], ‘gfg’: [4, 5], ‘best’:
> [11, 34], ‘for’: [6, 8, 2], ‘geeks’: [12, 24]}  
> The required keys are : [‘gfg’, ‘best’, ‘geeks’]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


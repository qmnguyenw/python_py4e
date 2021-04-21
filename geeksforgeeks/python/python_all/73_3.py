Python – Inner Nested Value List Mean in Dictionary



Sometimes, while working with Python Dictionaries, we can have a problem in
which we need to extract the mean of nested value lists in dictionary. This
problem can have application in many domains including web development and
competitive programming. Lets discuss certain ways in which this task can be
performed.

 **Method #1 : Usingmean() + loop**  
The combination of above functions provide the brute way to solve this
problem. In this, we perform the task of finding mean using inbuilt mean()
library and iterate for nesting using loop.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Inner Nested Value List Mean in Dictionary

# Using mean() + loop

from statistics import mean

 

# initializing dictionary

test_dict = {'Gfg' : {'a' : [1, 5, 6, 7], 'b'
: [6, 7, 8, 9]}, 'is' : {'best' :[2, 8,
9, 0]}}

 

# printing original dictionary

print("The original dictionary : " + str(test_dict))

 

# Inner Nested Value List Mean in Dictionary

# Using mean() + loop

for sub in test_dict.values():

 for key in sub:

 sub[key] = mean(sub[key])

 

# printing result 

print("The modified dictionary : " + str(test_dict))   
  
---  
  
__

__

**Output :**

> The original dictionary : {‘Gfg’: {‘a’: [1, 5, 6, 7], ‘b’: [6, 7, 8, 9]},
> ‘is’: {‘best’: [2, 8, 9, 0]}}  
> The modified dictionary : {‘Gfg’: {‘a’: 4.75, ‘b’: 7.5}, ‘is’: {‘best’:
> 4.75}}

  

  

**Method #2 : Using dictionary comprehension +mean()**  
This is yet another way to solve this problem. In this, we perform similar
task as above method. But difference is that in compact way and as one-liner.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Inner Nested Value List Mean in Dictionary

# Using dictionary comprehension + mean()

from statistics import mean

 

# initializing dictionary

test_dict = {'Gfg' : {'a' : [1, 5, 6, 7], 'b'
: [6, 7, 8, 9]}, 'is' : {'best' :[2, 8,
9, 0]}}

 

# printing original dictionary

print("The original dictionary : " + str(test_dict))

 

# Inner Nested Value List Mean in Dictionary

# Using dictionary comprehension + mean()

res = {idx: {key: mean(idx) for key, idx in j.items()} for
idx, j in test_dict.items()}

 

# printing result 

print("The modified dictionary : " + str(res))   
  
---  
  
__

__

**Output :**

> The original dictionary : {‘Gfg’: {‘a’: [1, 5, 6, 7], ‘b’: [6, 7, 8, 9]},
> ‘is’: {‘best’: [2, 8, 9, 0]}}  
> The modified dictionary : {‘Gfg’: {‘a’: 4.75, ‘b’: 7.5}, ‘is’: {‘best’:
> 4.75}}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


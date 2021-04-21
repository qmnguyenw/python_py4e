Python program to group keys with similar values in a dictionary



Given a dictionary with values as a list. Group all the keys together with
similar values.

>  **Input** : test_dict = {“Gfg”: [5, 6], “is”: [8, 6, 9], “best”: [10, 9],
> “for”: [5, 2], “geeks”: [19]}  
> **Output** : [[‘Gfg’, ‘is’, ‘for’], [‘is’, ‘Gfg’, ‘best’], [‘best’, ‘is’],
> [‘for’, ‘Gfg’]]  
> **Explanation** : Gfg has 6, is has 6, and for has 5 which is also in Gfg
> hence, grouped.
>
>  **Input** : test_dict = {“Gfg”: [6], “is”: [8, 6, 9], “best”: [10, 9],
> “for”: [5, 2]}  
> **Output** : [[‘Gfg’, ‘is’], [‘is’, ‘Gfg’, ‘best’], [‘best’, ‘is’]]  
> **Explanation** : Gfg has 6, is has 6, hence grouped.  
>

**Method : Using loop + any() + len()**

The combination of the above functions can be used to solve this problem. In
this, we check for each key if it matches any value using any(), len() is used
to check if the matching keys exceed 1. The iteration part is carried using a
loop.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Group keys with similar values in Dictionary

# Using loop + any() + len()

 

# initializing dictionary

test_dict = {"Gfg": [5, 6], "is": [8, 6, 9],


 "best": [10, 9], "for": [5, 2], 

 "geeks": [19]}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

res = []

for key in test_dict:

 chr = [key]

 for ele in test_dict:

 

 # check with other keys 

 if key != ele:

 

 # checking for any match in values

 if any(i == j for i in test_dict[key] for j in
test_dict[ele]):

 chr.append(ele)

 if len(chr) > 1:

 res.append(chr)

 

# printing result 

print("The dictionary after values replacement : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original dictionary is : {‘Gfg’: [5, 6], ‘is’: [8, 6, 9], ‘best’: [10,
> 9], ‘for’: [5, 2], ‘geeks’: [19]}
>
> The dictionary after values replacement : [[‘Gfg’, ‘is’, ‘for’], [‘is’,
> ‘Gfg’, ‘best’], [‘best’, ‘is’], [‘for’, ‘Gfg’]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


Python – Dictionary Key Value lists combinations



Given dictionary with values as list, extract all the possible combinations,
both cross keys and with values.

>  **Input** : test_dict = {“Gfg” : [4, 5], “is” : [1, 2], “Best” : [9, 4]}  
>  **Output** : {0: [[‘Gfg’, 4], [‘is’, 1], [‘Best’, 9]], 1: [[‘Gfg’, 4],
> [‘is’, 1], [‘Best’, 4]], 2: [[‘Gfg’, 4], [‘is’, 2], [‘Best’, 9]], 3:
> [[‘Gfg’, 4], [‘is’, 2], [‘Best’, 4]], 4: [[‘Gfg’, 5], [‘is’, 1], [‘Best’,
> 9]], 5: [[‘Gfg’, 5], [‘is’, 1], [‘Best’, 4]], 6: [[‘Gfg’, 5], [‘is’, 2],
> [‘Best’, 9]], 7: [[‘Gfg’, 5], [‘is’, 2], [‘Best’, 4]]}  
>  **Explanation** : Prints all possible combination of key with values and
> cross values as well.
>
>  **Input** : test_dict = {“Gfg” : [4], “is” : [1], “Best” : [4]}  
>  **Output** : {0: [[‘Gfg’, 4], [‘is’, 1], [‘Best’, 4]]}  
>  **Explanation** : Prints all possible combination of key with values and
> cross values as well.

 **Method #1 : Using product() + zip() + loop**

The combination of above functions can be used to solve this problem. In this,
we perform the first combination of keys with all values using product() and
cross key combinations are performed using zip() and loop.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Dictionary Key Value lists combinations

# Using product() + zip() + loop

from itertools import product

 

# initializing dictionary

test_dict = {"Gfg" : [4, 5, 7],

 "is" : [1, 2, 9],

 "Best" : [9, 4, 2]}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

temp = list(test_dict.keys()) 

res = dict()

cnt = 0

 

# making key-value combinations using product

for combs in product (*test_dict.values()):

 

 # zip used to perform cross keys combinations.

 res[cnt] = [[ele, cnt] for ele, cnt in zip(test_dict,
combs)]

 cnt += 1

 

# printing result 

print("The computed combinations : " + str(res))   
  
---  
  
__

__

**Output**

> The original dictionary is : {‘Gfg’: [4, 5, 7], ‘is’: [1, 2, 9], ‘Best’: [9,
> 4, 2]}  
> The computed combinations : {0: [[‘Gfg’, 4], [‘is’, 1], [‘Best’, 9]], 1:
> [[‘Gfg’, 4], [‘is’, 1], [‘Best’, 4]], 2: [[‘Gfg’, 4], [‘is’, 1], [‘Best’,
> 2]], 3: [[‘Gfg’, 4], [‘is’, 2], [‘Best’, 9]], 4: [[‘Gfg’, 4], [‘is’, 2],
> [‘Best’, 4]], 5: [[‘Gfg’, 4], [‘is’, 2], [‘Best’, 2]], 6: [[‘Gfg’, 4],
> [‘is’, 9], [‘Best’, 9]], 7: [[‘Gfg’, 4], [‘is’, 9], [‘Best’, 4]], 8:
> [[‘Gfg’, 4], [‘is’, 9], [‘Best’, 2]], 9: [[‘Gfg’, 5], [‘is’, 1], [‘Best’,
> 9]], 10: [[‘Gfg’, 5], [‘is’, 1], [‘Best’, 4]], 11: [[‘Gfg’, 5], [‘is’, 1],
> [‘Best’, 2]], 12: [[‘Gfg’, 5], [‘is’, 2], [‘Best’, 9]], 13: [[‘Gfg’, 5],
> [‘is’, 2], [‘Best’, 4]], 14: [[‘Gfg’, 5], [‘is’, 2], [‘Best’, 2]], 15:
> [[‘Gfg’, 5], [‘is’, 9], [‘Best’, 9]], 16: [[‘Gfg’, 5], [‘is’, 9], [‘Best’,
> 4]], 17: [[‘Gfg’, 5], [‘is’, 9], [‘Best’, 2]], 18: [[‘Gfg’, 7], [‘is’, 1],
> [‘Best’, 9]], 19: [[‘Gfg’, 7], [‘is’, 1], [‘Best’, 4]], 20: [[‘Gfg’, 7],
> [‘is’, 1], [‘Best’, 2]], 21: [[‘Gfg’, 7], [‘is’, 2], [‘Best’, 9]], 22:
> [[‘Gfg’, 7], [‘is’, 2], [‘Best’, 4]], 23: [[‘Gfg’, 7], [‘is’, 2], [‘Best’,
> 2]], 24: [[‘Gfg’, 7], [‘is’, 9], [‘Best’, 9]], 25: [[‘Gfg’, 7], [‘is’, 9],
> [‘Best’, 4]], 26: [[‘Gfg’, 7], [‘is’, 9], [‘Best’, 2]]}

 **Method #2 : Using product() + loop**

The combination of above functions can also be used to solve this problem. In
this, we perform the task of performing inner and cross keys combination using
product(). Difference is that container of grouping is tuple rather than list.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Dictionary Key Value lists combinations

# Using product() + loop

from itertools import product

 

# initializing dictionary

test_dict = {"Gfg" : [4, 5, 7],

 "is" : [1, 2, 9],

 "Best" : [9, 4, 2]}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

res = {}

for key, val in test_dict.items():

 

 # for key-value combinations 

 res[key] = product([key], val)

 

# computing cross key combinations

res = product(*res.values())

 

# printing result 

print("The computed combinations : " + str(list(res)))   
  
---  
  
__

__

**Output**

> The original dictionary is : {‘Gfg’: [4, 5, 7], ‘is’: [1, 2, 9], ‘Best’: [9,
> 4, 2]}  
> The computed combinations : [((‘Gfg’, 4), (‘is’, 1), (‘Best’, 9)), ((‘Gfg’,
> 4), (‘is’, 1), (‘Best’, 4)), ((‘Gfg’, 4), (‘is’, 1), (‘Best’, 2)), ((‘Gfg’,
> 4), (‘is’, 2), (‘Best’, 9)), ((‘Gfg’, 4), (‘is’, 2), (‘Best’, 4)), ((‘Gfg’,
> 4), (‘is’, 2), (‘Best’, 2)), ((‘Gfg’, 4), (‘is’, 9), (‘Best’, 9)), ((‘Gfg’,
> 4), (‘is’, 9), (‘Best’, 4)), ((‘Gfg’, 4), (‘is’, 9), (‘Best’, 2)), ((‘Gfg’,
> 5), (‘is’, 1), (‘Best’, 9)), ((‘Gfg’, 5), (‘is’, 1), (‘Best’, 4)), ((‘Gfg’,
> 5), (‘is’, 1), (‘Best’, 2)), ((‘Gfg’, 5), (‘is’, 2), (‘Best’, 9)), ((‘Gfg’,
> 5), (‘is’, 2), (‘Best’, 4)), ((‘Gfg’, 5), (‘is’, 2), (‘Best’, 2)), ((‘Gfg’,
> 5), (‘is’, 9), (‘Best’, 9)), ((‘Gfg’, 5), (‘is’, 9), (‘Best’, 4)), ((‘Gfg’,
> 5), (‘is’, 9), (‘Best’, 2)), ((‘Gfg’, 7), (‘is’, 1), (‘Best’, 9)), ((‘Gfg’,
> 7), (‘is’, 1), (‘Best’, 4)), ((‘Gfg’, 7), (‘is’, 1), (‘Best’, 2)), ((‘Gfg’,
> 7), (‘is’, 2), (‘Best’, 9)), ((‘Gfg’, 7), (‘is’, 2), (‘Best’, 4)), ((‘Gfg’,
> 7), (‘is’, 2), (‘Best’, 2)), ((‘Gfg’, 7), (‘is’, 9), (‘Best’, 9)), ((‘Gfg’,
> 7), (‘is’, 9), (‘Best’, 4)), ((‘Gfg’, 7), (‘is’, 9), (‘Best’, 2))]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


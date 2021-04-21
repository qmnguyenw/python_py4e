Python – Sort Dictionary ignoring Key



Sometimes, while working with Python dictionaries, we can have problem in
which we need to perform sorting of dictionary elements. This is quite
straight forward, but sometimes, we can have certain stray keys, which we
don’t wish to alter order while sorting. This works for Python >= 3.6 as keys
are ordered in dictionary this version onwards. This can have applications in
data domains. Let’s discuss a way in which this task can be performed.

>  **Input** : test_dict = {“*-*” : “stray”, 70 : ‘is’}  
>  **Output** : {“*-*” : “stray”, 70 : ‘is’}
>
>  **Input** : test_dict = {54 : “gfg”, “*-*” : “stray”, 20 : ‘best’}  
>  **Output** : {20: ‘best’, ‘*-*’: ‘stray’, 54: ‘gfg’}

 **Method : Usingnext() + sorted() + insert()**  
The combination of above methods, can be used to solve this problem. In this,
we perform sorting using sorted(), insert() is used to insert the stray
element at its position and next() is used to get next key in order in case of
initial stray key.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort Dictionary ignoring Key

# Using next() + sorted() + insert()

 

# initializing dictionary

test_dict = {45 : 'is', 12 : 'gfg', 100 : 'best',


 "*-*" : "stray", 150 : 'geeks', 120 : 'for'}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# strary key 

stray_key = '*-*'

 

# Sort Dictionary ignoring Key

# Using next() + sorted() + insert()

temp = next(idx for idx, val in enumerate(test_dict) if
val == stray_key)

idx = sorted(ele for ele in test_dict if ele !=
stray_key)

idx.insert(temp, stray_key)

res = {ele: test_dict[ele] for ele in idx}

 

# printing result 

print("The dictionary after sorting : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

> The original dictionary is : {45: ‘is’, 12: ‘gfg’, 100: ‘best’, ‘*-*’:
> ‘stray’, 150: ‘geeks’, 120: ‘for’}
>
> The dictionary after sorting : {12: ‘gfg’, 45: ‘is’, 100: ‘best’, ‘*-*’:
> ‘stray’, 120: ‘for’, 150: ‘geeks’}


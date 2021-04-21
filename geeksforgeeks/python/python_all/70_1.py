Python – Remove duplicate values across Dictionary Values



Sometimes, while working with Python dictionaries, we can have a problem in
which we need to remove all the duplicate values across all the dictionary
value lists. This problem can have application in data domains and web
development domains. Let’s discuss certain ways in which this task can be
performed.

>  **Input** : test_dict = {‘Manjeet’: [1], ‘Akash’: [1, 8, 9]}  
>  **Output** : {‘Manjeet’: [], ‘Akash’: [8, 9]}
>
>  **Input** : test_dict = {‘Manjeet’: [1, 1, 1], ‘Akash’: [1, 1, 1]}  
>  **Output** : {‘Manjeet’: [], ‘Akash’: []}

 **Method #1 : UsingCounter() \+ list comprehension**  
The combination of above functions can be used to solve this problem. In this,
we use Counter() to extract all frequencies and list comprehension to assign
the value with single occurrence in value list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove duplicate values across Dictionary Values

# Using Counter() + list comprehension

from collections import Counter

 

# initializing dictionary

test_dict = {'Manjeet' : [1, 4, 5, 6],

 'Akash' : [1, 8, 9],

 'Nikhil': [10, 22, 4],

 'Akshat': [5, 11, 22]}

 

# printing original dictionary

print("The original dictionary : " + str(test_dict))

 

# Remove duplicate values across Dictionary Values

# Using Counter() + list comprehension

cnt = Counter()

for idx in test_dict.values():

 cnt.update(idx)

res = {idx: [key for key in j if cnt[key] == 1] 

 for idx, j in test_dict.items()}

 

# printing result 

print("Uncommon elements records : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

> The original dictionary : {‘Akshat’: [5, 11, 22], ‘Nikhil’: [10, 22, 4],
> ‘Manjeet’: [1, 4, 5, 6], ‘Akash’: [1, 8, 9]}  
> Uncommon elements records : {‘Akshat’: [11], ‘Nikhil’: [10], ‘Manjeet’: [6],
> ‘Akash’: [8, 9]}


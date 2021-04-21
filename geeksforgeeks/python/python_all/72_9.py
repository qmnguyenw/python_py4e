Python – Maximum value assignment in Nested Dictionary



Sometimes, while working with Python dictionaries, we can have a problem in
which we need to assign to the outer key, the item with maximum value in inner
keys. This kind of problem can occur in day-day programming and web
development domains. Let’s discuss a way in which this task can be performed.

>  **Input** : test_dict = {‘Manjeet’: {‘English’: 19, ‘Maths’: 1}, ‘Himani’:
> {‘English’: 18, ‘Maths’: 17}}  
>  **Output** : [{‘Manjeet’: (‘English’, 19)}, {‘Himani’: (‘English’, 18)}]
>
>  **Input** : test_dict = {‘Manjeet’ : {‘Maths’:10}}  
>  **Output** : [{‘Manjeet’: (‘Maths’, 10)}]

 **Method : UsingCounter().most_common() + items() \+ loop**  
The combination of above functions constitute the brute way to solve this
problem. In this, we extract the maximum element using most_common() and
items() is used to extract key-value pair.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Maximum value assignment in Nested Dictionary

# Using Counter().most_common() + items() + loop

from collections import Counter

 

# initializing dictionary

test_dict = {'Manjeet' : {'Maths':1, 'English':0,
'Physics':2, 'Chemistry':3},

 'Akash' : {'Maths':0, 'English':0, 'Physics':3,
'Chemistry':2},

 'Nikhil': {'Maths':4, 'English':2, 'Physics':2,
'Chemistry':3},

 'Akshat': {'Maths':1, 'English':0, 'Physics':2,
'Chemistry':0}}

 

# printing original dictionary

print("The original dictionary : " + str(test_dict))

 

# Maximum value assignment in Nested Dictionary

# Using Counter().most_common() + items() + loop

res = []

for key, val in test_dict.items():

 cnt = Counter(val)

 res.append({key : cnt.most_common(1)[0]})

 

# printing result 

print("Maximum element key : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

> The original dictionary : {‘Nikhil’: {‘Chemistry’: 3, ‘Physics’: 2, ‘Maths’:
> 4, ‘English’: 2}, ‘Akash’: {‘Chemistry’: 2, ‘Physics’: 3, ‘Maths’: 0,
> ‘English’: 0}, ‘Akshat’: {‘Chemistry’: 0, ‘Physics’: 2, ‘Maths’: 1,
> ‘English’: 0}, ‘Manjeet’: {‘Chemistry’: 3, ‘Physics’: 2, ‘Maths’: 1,
> ‘English’: 0}}
>
> Maximum element key : [{‘Nikhil’: (‘Maths’, 4)}, {‘Akash’: (‘Physics’, 3)},
> {‘Akshat’: (‘Physics’, 2)}, {‘Manjeet’: (‘Chemistry’, 3)}]


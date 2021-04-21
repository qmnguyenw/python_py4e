Python – Dictionary List Values Frequency



Sometimes, while working with Python dictionaries, we can have a problem in
which we need to perform the task of computing frequency of all the values in
dictionary values lists. This is quite common problem and can have use cases
in many domains. Let’s discuss certain ways in which this task can be
performed.

>  **Input** : test_dict = {1: [‘gfg’, ‘CS’, ‘cool’], 2: [‘gfg’, ‘CS’]}  
>  **Output** : {‘gfg’: 2, ‘CS’: 2, ‘cool’: 1}
>
>  **Input** : test_dict = {1 : [‘gfg’, ‘CS’]}  
>  **Output** : {‘gfg’: 1, ‘CS’: 1}

 **Method #1 : Usingdefaultdict() \+ loop**  
The combination of above functions can be used to solve this problem. In this,
we use defaultdict() to initialize the counter for each value and brute force
is used to increment the counter in dicitonary lists.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Dictionary List Values Frequency

# Using loop + defaultdict()

from collections import defaultdict

 

# initializing dictionary

test_dict = {1 : ['gfg', 'best', 'geeks'], 

 2 : ['gfg', 'CS'], 

 3 : ['best', 'for', 'CS'], 

 4 : ['test', 'ide', 'success'],

 5 : ['gfg', 'is', 'best']}

 

# printing original dictionary

print("The original dictionary : " + str(test_dict))

 

# Dictionary List Values Frequency

# Using loop + defaultdict()

res = defaultdict(int)

for key, val in test_dict.items():

 for sub in val:

 res[sub] += 1

 

# printing result 

print("Values Frequency : " + str(dict(res)))   
  
---  
  
__

__

**Output :**

  

  

> The original dictionary : {1: [‘gfg’, ‘best’, ‘geeks’], 2: [‘gfg’, ‘CS’], 3:
> [‘best’, ‘for’, ‘CS’], 4: [‘test’, ‘ide’, ‘success’], 5: [‘gfg’, ‘is’,
> ‘best’]}  
> Values Frequency : {‘gfg’: 3, ‘best’: 3, ‘geeks’: 1, ‘CS’: 2, ‘for’: 1,
> ‘test’: 1, ‘ide’: 1, ‘success’: 1, ‘is’: 1}


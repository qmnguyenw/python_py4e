Python – All possible concatenations in String List



Sometimes, while working with String lists, we can have a problem in which we
need to perform all possible concatenations of all the strings that occur in
list. This kind of problem can occur in domains such as day-day programming
and school programming. Let’s discuss a way in which this task can be
performed.

>  **Input** : test_list = [‘Gfg’, ‘Best’]  
>  **Output** : [‘Gfg’, ‘Best’, ‘GfgBest’, ‘BestGfg’]
>
>  **Input** : test_list = [‘Gfg’]  
>  **Output** : [‘Gfg’]

 **Method : Usingpermutations() + join() \+ loop**  
The combination of above functions can be used to solve this problem. In this,
we perform the task of concatenation using join() and all possible combination
extraction using permutations().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# All possible concatenations in String List

# Using permutations() + loop

from itertools import permutations

 

# initializing list

test_list = ['Gfg', 'is', 'Best']

 

# printing original list 

print("The original list : " + str(test_list))

 

# All possible concatenations in String List

# Using permutations() + loop

temp = []

for idx in range(1, len(test_list) + 1):

 temp.extend(list(permutations(test_list, idx)))

res = []

for ele in temp:

 res.append("".join(ele))

 

# printing result 

print("All Sring combinations : " + str(res))  
  
---  
  
 __

 __

 **Output :**

  

  

> The original list : [‘Gfg’, ‘is’, ‘Best’]  
> All Sring combinations : [‘Gfg’, ‘is’, ‘Best’, ‘Gfgis’, ‘GfgBest’, ‘isGfg’,
> ‘isBest’, ‘BestGfg’, ‘Bestis’, ‘GfgisBest’, ‘GfgBestis’, ‘isGfgBest’,
> ‘isBestGfg’, ‘BestGfgis’, ‘BestisGfg’]


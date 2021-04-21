Python – Frequency Grouping Dictionary



Sometimes, while working with Python dictionaries, we can have a problem in
which we need to perform the grouping of dictionary data, in a way in which we
need to group all the similar dictionaries key with its frequency. This kind
of problem has its application in web development domain. Let’s discuss
certain ways in which this task can be performed.

>  **Input** : test_list = [{‘best’: 2, ‘Gfg’: 1}, {‘best’: 2, ‘Gfg’: 1}]  
>  **Output** : [{‘freq’: 2, ‘Gfg’: 1}]
>
>  **Input** : test_list = [{‘Gfg’: 1, ‘best’: 2}, {‘Gfg’: 2, ‘best’: 1}]  
>  **Output** : [{‘Gfg’: 1, ‘freq’: 1}, {‘Gfg’: 2, ‘freq’: 1}]

 **Method #1 : Usingdefaultdict() \+ list comprehension**  
The combination of above functions can be used to perform this task. In this,
we initialize the defaultdict with integer to get the frequency and list
comprehension is used to compile the resultant dictionary.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Frequency Grouping Dictionary

# Using defaultdict() + list comprehension

from collections import defaultdict

 

# initializing list

test_list = [{'Gfg' : 1, 'best' : 2}, 

 {'Gfg' : 1, 'best' : 2},

 {'Gfg' : 2, 'good' : 3},

 {'Gfg' : 2, 'best' : 2},

 {'Gfg' : 2, 'good' : 3}]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Frequency Grouping Dictionary

# Using defaultdict() + list comprehension

temp = defaultdict(int)

for sub in test_list:

 key = sub['Gfg']

 temp[key] += 1

 

res = [{"Gfg": key, "freq": val} for (key, val) in
temp.items()]

 

# printing result 

print("The frequency dictionary : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

> The original list is : [{‘Gfg’: 1, ‘best’: 2}, {‘Gfg’: 1, ‘best’: 2},
> {‘good’: 3, ‘Gfg’: 2}, {‘Gfg’: 2, ‘best’: 2}, {‘good’: 3, ‘Gfg’: 2}]  
> The frequency dictionary : [{‘Gfg’: 1, ‘freq’: 2}, {‘Gfg’: 2, ‘freq’: 3}]


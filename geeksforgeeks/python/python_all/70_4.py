Python – Concatenate String values in Dictionary List



Sometimes, while working with Python records data, we can have a problem in
which we require to perform concatenation of string values of keys by matching
at particular key like ID. This kind of problem can have application in web
development domain. Let’s discuss certain way in which this task can be
performed.

>  **Input** : test_list = [{‘id’: 17, ‘gfg’: ‘geeksfor’}, {‘id’: 12, ‘gfg’:
> ‘geeks’}, {‘id’: 34, ‘gfg’: ‘good’}]  
>  **Output** : [{‘id’: 17, ‘gfg’: ‘geeksfor’}, {‘id’: 12, ‘gfg’: ‘geeks’},
> {‘id’: 34, ‘gfg’: ‘good’}]
>
>  **Input** : test_list = [{‘id’: 1, ‘gfg’: ‘geeksfor’}, {‘id’: 1, ‘gfg’:
> ‘geeks’}, {‘id’: 1, ‘gfg’: ‘good’}]  
>  **Output** : [{‘id’: 1, ‘gfg’: ‘geeksforgeeksgood’}]

 **Method #1 : Using loop**  
This is one way to solve this problem. In this, we check each key and then
perform merge on basis of equality key and perform concatenation of particular
required key in brute force approach.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Concatenate String values in Dictionary List

# Using loop

 

# initializing list

test_list = [{'gfg' : "geeksfor", 'id' : 12, 'best' :
(1, 2)}, 

 {'gfg' : "geeks", 'id' : 12, 'best' : (6,
2)},

 {'gfg' : "good", 'id' : 34, 'best' : (7, 2)}]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing compare key 

comp_key = 'id'

 

# initializing concat key 

conc_key = 'gfg'

 

# Concatenate String values in Dictionary List

# Using loop

res = []

for ele in test_list:

 temp = False

 for ele1 in res:

 if ele1[comp_key] == ele[comp_key]:

 ele1[conc_key] = ele1[conc_key] + ele[conc_key]

 temp = True

 break

 if not temp:

 res.append(ele)

 

# printing result 

print("The converted Dictionary list : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

> The original dictionary : {‘gfg’: {‘is’: [6, 7, 8], ‘best’: [1, 9, 4]}}
>
> The possible combinations : {‘gfg5’: {‘is’: 7, ‘best’: 4}, ‘gfg3’: {‘is’: 7,
> ‘best’: 1}, ‘gfg8’: {‘is’: 8, ‘best’: 4}, ‘gfg2’: {‘is’: 6, ‘best’: 4},
> ‘gfg6’: {‘is’: 8, ‘best’: 1}, ‘gfg0’: {‘is’: 6, ‘best’: 1}, ‘gfg1’: {‘is’:
> 6, ‘best’: 9}, ‘gfg7’: {‘is’: 8, ‘best’: 9}, ‘gfg4’: {‘is’: 7, ‘best’: 9}}


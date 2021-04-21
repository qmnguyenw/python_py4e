Python – Summation Grouping in Dictionary List



Sometimes, while working with Python Dictionaries, we can have a problem in
which we need to perform the grouping of dictionaries according to specific
key, and perform summation of certain keys while grouping similar key’s value.
This is s peculiar problem but can have applications in domains such as web
development. Let’s discuss a certain way in which this task can be performed.

>  **Input :** test_list = [{‘geeks’: 10, ‘best’: 8, ‘Gfg’: 6}, {‘geeks’: 12,
> ‘best’: 11, ‘Gfg’: 4}]  
>  **Output :** {4: {‘geeks’: 12, ‘best’: 11}, 6: {‘geeks’: 10, ‘best’: 8}}
>
>  **Input :** test_list = [{‘CS’: 14, ‘best’: 9, ‘geeks’: 7, ‘Gfg’: 14}]  
>  **Output :** {14: {‘best’: 9, ‘geeks’: 7}}

 **Method #1 : Using loop**  
This is brute force way in which this task can be performed. In this we
manually loop through each key from dictionary and perform required grouping
according to the key and construct the required grouped and summed dictionary.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Summation Grouping in Dictionary List

# Using loop

 

# initializing list

test_list = [{'Gfg' : 1, 'id' : 2, 'best' : 8,
'geeks' : 10}, 

 {'Gfg' : 4, 'id' : 4, 'best': 10, 'geeks' :
12}, 

 {'Gfg' : 4, 'id' : 8, 'best': 11, 'geeks' :
15}]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing group key 

grp_key = 'Gfg'

 

# initializing sum keys 

sum_keys = ['best', 'geeks']

 

# Summation Grouping in Dictionary List

# Using loop

res = {}

for sub in test_list:

 ele = sub[grp_key]

 if ele not in res:

 res[ele] = {x: 0 for x in sum_keys}

 for y in sum_keys:

 res[ele][y] += int(sub[y])

 

# printing result 

print("The grouped list : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

> The original list is : [{‘geeks’: 10, ‘id’: 2, ‘best’: 8, ‘Gfg’: 1},
> {‘geeks’: 12, ‘id’: 4, ‘best’: 10, ‘Gfg’: 4}, {‘geeks’: 15, ‘id’: 8, ‘best’:
> 11, ‘Gfg’: 4}]  
> The grouped list : {1: {‘geeks’: 10, ‘best’: 8}, 4: {‘geeks’: 27, ‘best’:
> 21}}


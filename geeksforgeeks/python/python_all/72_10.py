Python – Binary operation on specific keys in Dictionary List



Sometimes, while working with Python dictionaries, we can have a problem in
which we need to perform certain operations over some keys in dictionary
throughout the list and return the result. This kind of problem is common in
domains involving data like web development. Let’s discuss certain ways in
which this task can be performed.

>  **Input** : test_list = [{‘best’: 8, ‘Gfg’: 13}, {‘is’: 5, ‘for’: 9,
> ‘best’: 15, ‘Gfg’: 7, ‘geeks’: 7}]  
>  **Output** : [(0, 104), (1, 105)]
>
>  **Input** : test_list = [{‘Gfg’ : 3, ‘best’ : 10}]  
>  **Output** : [(0, 30)]

 **Method #1 : loop +enumerate()**  
The combination of above functions can be used to solve this problem. This is
a brute force approach in which we loop through each dictionary list and
perform operation and store result.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Binary operation on specific keys in Dictionary List

# Using loop + enumerate()

 

# initializing list

test_list = [{'Gfg' : 5, 'is' : 6, 'best' : 7,
'for' : 8, 'geeks' : 10},

 {'Gfg' : 9, 'is' : 4, 'best' : 10, 'for' :
4, 'geeks' :7},

 {'Gfg' : 2, 'is' : 10, 'best' : 8, 'for' :
9, 'geeks' : 3}]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing keys 

op1_key = 'Gfg'

op2_key = 'best'

 

# Binary operation on specific keys in Dictionary List

# Using loop + enumerate()

res = []

for idx, val in enumerate(test_list):

 res.append((idx, val[op1_key] * val[op2_key]))

 

# printing result 

print("The constructed result list : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

> The original list is : [{‘geeks’: 10, ‘for’: 8, ‘Gfg’: 5, ‘is’: 6, ‘best’:
> 7}, {‘geeks’: 7, ‘for’: 4, ‘Gfg’: 9, ‘is’: 4, ‘best’: 10}, {‘geeks’: 3,
> ‘for’: 9, ‘Gfg’: 2, ‘is’: 10, ‘best’: 8}]
>
> The constructed result list : [(0, 35), (1, 90), (2, 16)]


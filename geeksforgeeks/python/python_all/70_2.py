Python – Unique Values of Key in Dictionary



Sometimes, while working with Python dictionaries, we can have a problem in
which we need to extract the unique values of a particular key in Dictionary
List. This kind of problem in very common in day-day programming and web
development domain. Lets discuss certain ways in which this task can be
performed.

>  **Input** : test_list = [{‘geeks’: 10, ‘for’: 8, ‘best’: 10}, {‘best’: 10}]  
>  **Output** : [10]
>
>  **Input** : test_list = [{‘best’: 11}]  
>  **Output** : [11]

 **Method #1 : Using loop +set()**  
The combination of above functions can be used to solve this problem. In this,
we extract all the elements of key in loop and then convert the extracted list
to set to get unique values.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Unique Values of Key in Dictionary

# Using loop + set()

 

# initializing list

test_list = [{'Gfg' : 5, 'is' : 6, 'best' : 7,
'for' : 8, 'geeks' : 10},

 {'Gfg' : 9, 'is' : 4, 'best' : 7, 'for' :
4, 'geeks' :7},

 {'Gfg' : 2, 'is' : 10, 'best' : 8, 'for' :
9, 'geeks' : 3}]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing key

op_key = 'best'

 

# Unique Values of Key in Dictionary

# Using loop + set()

res = []

for sub in test_list:

 res.append(sub[op_key])

res = list(set(res))

 

# printing result 

print("The unique values of key : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

> The original list is : [{‘for’: 8, ‘best’: 7, ‘is’: 6, ‘Gfg’: 5, ‘geeks’:
> 10}, {‘for’: 4, ‘best’: 7, ‘is’: 4, ‘Gfg’: 9, ‘geeks’: 7}, {‘for’: 9,
> ‘best’: 8, ‘is’: 10, ‘Gfg’: 2, ‘geeks’: 3}]  
> The unique values of key : [8, 7]


Python – Filter key’s value from other key



Sometimes, while working with Python dictionary, we can have a problem in
which we need to extract a value from dictionary list of the key on basis of
some other key equality. This kind of problem is common in domains that
include data, for e.g web development. Let’s discuss certain ways in which
this task can be performed.

>  **Input** :  
> test_list = [{‘gfg’ : 5, ‘is’ : 8, ‘best’ : 24}, {‘gfg’ : 7, ‘is’ : 12,
> ‘best’ : 24}]  
> req_key = ‘gfg’ [ Requested Key ]  
> fil_key = ‘best’ [ Filtering Key ]  
> fil_val = 24 [ Filtering value to be checked ]  
>  **Output** : [5, 7]
>
>  **Input** :  
> test_list = [{‘gfg’ : 5, ‘is’ : 8, ‘best’ : 24}]  
> req_key = ‘gfg’ [ Requested Key ]  
> fil_key = ‘best’ [ Filtering Key ]  
> fil_val = 24 [ Filtering value to be checked ]  
>  **Output** : [5]

 **Method #1 : Using loop**  
This is brute force way to solve this problem. In this, we manually iterate
the entire list and check for filter key’s value, on equality we extract the
required key’s value.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Filter key's value from other key

# Using loop

 

# initializing list

test_list = [{'gfg' : 5, 'is' : 8, 'best' : 12},


 {'gfg' : 7, 'is' : 12, 'best' : 24},

 {'gfg' : 20, 'is' : 17, 'best' : 18}]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing required key

req_key = 'gfg'

 

# initializing filter key

fil_key = 'best'

 

# initializing filter val 

fil_val = 24

 

# Filter key's value from other key

# Using loop

res = []

for sub in test_list:

 if sub[fil_key] == fil_val:

 res.append(sub[req_key])

 

# printing result 

print("The required value : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

> The original list is : [{‘gfg’: 5, ‘is’: 8, ‘best’: 12}, {‘gfg’: 7, ‘is’:
> 12, ‘best’: 24}, {‘gfg’: 20, ‘is’: 17, ‘best’: 18}]  
> The required value : [7]


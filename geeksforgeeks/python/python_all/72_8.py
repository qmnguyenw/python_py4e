Python – Remove Disjoint Tuple keys from Dictionary



Sometimes, while working with Python dictionaries, we can have a problem in
which we need to remove tuple keys from records on the basis of key presence
matching any one of element present key from other lists. This kind of problem
can have applications in data domains. Let’s discuss certain ways in which
this task can be performed.

>  **Input** : test_dict = {(9, 3) : 4, (‘is’, 6) : 2, (‘for’, 9) : ‘geeks’}  
>  **Output** : {}
>
>  **Input** : test_dict = {(‘is’, 9): 2, (‘for’, 8): 7}  
>  **Output** : {(‘for’, 8): 7}

 **Method #1 : Using loop**  
This is one of the ways in which this task can be performed. In this we
perform an iteration of dictionary key and check for the presence of any key
in required and perform removal accordingly.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove Disjoint Tuple keys from Dictionary

# Using loop

 

# initializing dictionary

test_dict = {('Gfg', 3) : 4, ('is', 6) : 2,
('best', 10) : 3, ('for', 9) : 'geeks'}

 

# printing original dictionary

print("The original dictionary : " + str(test_dict))

 

# initializing List 

rem_list = [9, 'is']

 

# Remove Disjoint Tuple keys from Dictionary

# Using loop

res = dict()

for idx in test_dict:

 if idx[0] not in rem_list and idx[1] not in
rem_list:

 res[idx] = test_dict[idx]

 

# printing result 

print("Dictionary after removal : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

> The original dictionary : {(‘Gfg’, 3): 4, (‘best’, 10): 3, (‘for’, 9):
> ‘geeks’, (‘is’, 6): 2}  
> Dictionary after removal : {(‘Gfg’, 3): 4, (‘best’, 10): 3}


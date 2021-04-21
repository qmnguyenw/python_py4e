Python – Unlist Single Valued Dictionary List



Given list of dictionaries, perform the unlisting of records in which we just
have 1 dictionary as record element.

>  **Input** : test_list = [{‘best’: [{‘a’: 6}], ‘Gfg’: 15}]  
>  **Output** : [{‘best’: {‘a’: 6}, ‘Gfg’: 15}]  
>  **Explanation** : The value list associated with ‘best’ key is changed to
> dicationary.
>
>  **Input** : test_list = [{‘Gfg’: [{‘best’ : 17}]}]  
>  **Output** : [{‘Gfg’: {‘best’: 17}}]  
>  **Explanation** : ‘Gfg’ key’s value changed to single dictionary.

 **Method #1 : Using loop + isinstance()**  
This is brute force way in which this task can be performed. In this, we test
for the list type using isinstance() and loop is used for iterations.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Unlist Single Valued Dictionary List

# Using loop + isinstance()

 

# initializing list

test_list = [{'Gfg': 1,

 'is': [{'a': 2, 'b': 3}]},

 {'best': [{'c': 4, 'd': 5}],

 'CS': 6}]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Using loop + isinstance()

for dicts in test_list:

 for key, val in dicts.items():

 

 # isinstance() is used to check for list to convert

 if isinstance(val, list):

 dicts[key] = val[0]

 

# printing result 

print("The converted Dictionary list : " + str(test_list))   
  
---  
  
__

__

**Output :**

  

  

    
    
    The original list is : [{'Gfg': 1, 'is': [{'b': 3, 'a': 2}]}, {'CS': 6, 'best': [{'d': 5, 'c': 4}]}]
    The converted Dictionary list : [{'Gfg': 1, 'is': {'b': 3, 'a': 2}}, {'CS': 6, 'best': {'d': 5, 'c': 4}}]
    


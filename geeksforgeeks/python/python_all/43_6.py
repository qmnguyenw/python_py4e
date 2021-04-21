Python – Dictionaries with Unique Value Lists



Given List of dictionaries with list values, extract unique dictionaries.

>  **Input** : [{‘Gfg’: [2, 3], ‘is’ : [7, 8], ‘best’ : [10]}, {‘Gfg’: [2, 3],
> ‘is’ : [7, 8], ‘best’ : [10]}]  
>  **Output** : [{‘Gfg’: [2, 3], ‘is’: [7, 8], ‘best’: [10]}]  
>  **Explanation** : Both are similar dictionaries, and hence 1 is removed.
>
>  **Input** : [{‘Gfg’: [2, 3], ‘is’ : [7, 8], ‘best’ : [10]}, {‘Gfg’: [2, 3],
> ‘is’ : [7, 8], ‘best’ : [10, 11]}]  
>  **Output** : [{‘Gfg’: [2, 3], ‘is’: [7, 8], ‘best’: [10]}, {‘Gfg’: [2, 3],
> ‘is’: [7, 8], ‘best’: [10, 11]}]  
>  **Explanation** : None duplicate.

 **Method #1 : Using loop**

This is one of the ways in which this task can be performed. In this, we
iterate for each dictionary and memoize it, and prevent it from adding to
result.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Unique Value Lists Dictionaries

# Using loop

 

# initializing lists

test_list = [{'Gfg': [2, 3], 'is' : [7, 8],
'best' : [10]}, 

 {'Gfg': [2, 3], 'is' : [7], 'best' : [10]}, 

 {'Gfg': [2, 3], 'is' : [7, 8], 'best' :
[10]}]

 

# printing original list

print("The original list : " + str(test_list))

 

# Using loop to iterate through elements

# result array to also keep track of already occurred elements

res = []

for sub in test_list:

 if sub not in res:

 res.append(sub)

 

# printing result 

print("List after duplicates removal : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : [{'Gfg': [2, 3], 'is': [7, 8], 'best': [10]}, {'Gfg': [2, 3], 'is': [7], 'best': [10]}, {'Gfg': [2, 3], 'is': [7, 8], 'best': [10]}]
    List after duplicates removal : [{'Gfg': [2, 3], 'is': [7, 8], 'best': [10]}, {'Gfg': [2, 3], 'is': [7], 'best': [10]}]
    

**Method #2 : Using list comprehension**

This is yet another way in which this task can be performed. In this, similar
approach is employed as above, just the difference of encapsulating result in
list comprehension for one-liner.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Unique Value Lists Dictionaries

# Using list comprehension

 

# initializing lists

test_list = [{'Gfg': [2, 3], 'is' : [7, 8],
'best' : [10]}, 

 {'Gfg': [2, 3], 'is' : [7], 'best' : [10]}, 

 {'Gfg': [2, 3], 'is' : [7, 8], 'best' :
[10]}]

 

# printing original list

print("The original list : " + str(test_list))

 

# list comprehension to encapsulate logic in one liner

res = []

[res.append(val) for val in test_list if val not in res]

 

# printing result 

print("List after duplicates removal : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : [{'Gfg': [2, 3], 'is': [7, 8], 'best': [10]}, {'Gfg': [2, 3], 'is': [7], 'best': [10]}, {'Gfg': [2, 3], 'is': [7, 8], 'best': [10]}]
    List after duplicates removal : [{'Gfg': [2, 3], 'is': [7, 8], 'best': [10]}, {'Gfg': [2, 3], 'is': [7], 'best': [10]}]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


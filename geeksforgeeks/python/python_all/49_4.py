Python – Cross mapping of Two dictionary value lists



GIven two dictionaries with list values, perform mapping of keys of first list
with values of other list, by checking values-key linkage.

>  **Input** : test_dict1 = {“Gfg” : [4, 10], “Best” : [8, 6], “is” : [9, 3]},
> test_dict2 = {6 : [15, 9], 8 : [6, 3], 7 : [9, 8], 9 : [10, 11]}  
>  **Output** : {‘Best’: [6, 3, 15, 9], ‘is’: [10, 11]}  
>  **Explanation** : “Best” has 8 and 6, which are mapped to 6, 3 and 15, 9
> hence output for that key.
>
>  **Input** : test_dict1 = {“Gfg” : [4, 10], “Best” : [18, 16], “is” : [9,
> 3]}, test_dict2 = {6 : [15, 9], 8 : [6, 3], 7 : [9, 8], 9 : [10, 11]}  
>  **Output** : {‘is’: [10, 11]}  
>  **Explanation** : Only 9 present as possible key.

 **Method #1 : Using loop + setdefault() + extend()**

The combination of above functions can be used to solve this problem. In this,
we perform the task of getting the matching keys with values using get() and
setdefault is used to construct empty list for mapping.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Cross mapping of Two dictionary value lists

# Using loop + setdefault() + extend()

 

# initializing dictionaries

test_dict1 = {"Gfg" : [4, 7], "Best" : [8, 6],
"is" : [9, 3]}

test_dict2 = {6 : [15, 9], 8 : [6, 3], 7 :
[9, 8], 9 : [10, 11]}

 

# printing original lists

print("The original dictionary 1 is : " + str(test_dict1))

print("The original dictionary 2 is : " + str(test_dict2))

 

res = {}

 

# getting all values of first dictionary 

for key, val in test_dict1.items():

 for key1 in val:

 

 # getting result with default value list and extending 

 # according to value optained from get()

 res.setdefault(key, []).extend(test_dict2.get(key1, []))

 

# printing result 

print("The constructed dictionary : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original dictionary 1 is : {'Gfg': [4, 7], 'Best': [8, 6], 'is': [9, 3]}
    The original dictionary 2 is : {6: [15, 9], 8: [6, 3], 7: [9, 8], 9: [10, 11]}
    The constructed dictionary : {'Gfg': [9, 8], 'Best': [6, 3, 15, 9], 'is': [10, 11]}
    

**Method #2 : Using list comprehension + dictionary comprehension**

This is one more way in which this problem can be solved. In this, we extract
all the mapping using list comprehension and then contruct new dictionary by
cross-mapping the extracted values.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Cross mapping of Two dictionary value lists

# Using list comprehension + dictionary comprehension

 

# initializing dictionaries

test_dict1 = {"Gfg" : [4, 7], "Best" : [8, 6],
"is" : [9, 3]}

test_dict2 = {6 : [15, 9], 8 : [6, 3], 7 :
[9, 8], 9 : [10, 11]}

 

# printing original lists

print("The original dictionary 1 is : " + str(test_dict1))

print("The original dictionary 2 is : " + str(test_dict2))

 

# using internal and external comprehension to 

# solve problem 

res = {key: [j for i in val if i in test_dict2 for j
in test_dict2[i]]

 for key, val in test_dict1.items()}

 

# printing result 

print("The constructed dictionary : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original dictionary 1 is : {'Gfg': [4, 7], 'Best': [8, 6], 'is': [9, 3]}
    The original dictionary 2 is : {6: [15, 9], 8: [6, 3], 7: [9, 8], 9: [10, 11]}
    The constructed dictionary : {'Gfg': [9, 8], 'Best': [6, 3, 15, 9], 'is': [10, 11]}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


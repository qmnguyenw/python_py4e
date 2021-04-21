Python – Key with maximum unique values



Given a dictionary with values list, extract key whose value has most unique
values.

>  **Input** : test_dict = {“Gfg” : [5, 7, 9, 4, 0], “is” : [6, 7, 4, 3, 3],
> “Best” : [9, 9, 6, 5, 5]}  
>  **Output** : “Gfg”  
>  **Explanation** : “Gfg” having max unique elements i.e 5.
>
>  **Input** : test_dict = {“Gfg” : [5, 7, 7, 7, 7], “is” : [6, 7, 7, 7],
> “Best” : [9, 9, 6, 5, 5]}  
>  **Output** : “Best”  
>  **Explanation** : 3 (max) unique elements, 9, 6, 5 of “Best”.

 **Method #1 : Using loop**

This is brute way in which this task can be performed. In this, we iterate for
all the list values and check for each key’s value count, extract key with
maximum unique values.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Key with maximum unique values

# Using loop

 

# initializing dictionary

test_dict = {"Gfg" : [5, 7, 5, 4, 5],

 "is" : [6, 7, 4, 3, 3], 

 "Best" : [9, 9, 6, 5, 5]}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

max_val = 0

max_key = None

for sub in test_dict:

 

 # test for length using len()

 # converted to set for duplicates removal

 if len(set(test_dict[sub])) > max_val:

 max_val = len(set(test_dict[sub]))

 max_key = sub

 

# printing result 

print("Key with maximum unique values : " + str(max_key))   
  
---  
  
__

__

**Output**

> The original dictionary is : {‘Gfg’: [5, 7, 5, 4, 5], ‘is’: [6, 7, 4, 3, 3],
> ‘Best’: [9, 9, 6, 5, 5]}  
> Key with maximum unique values : is

 **Method #2 : Using sorted() + lambda() + set() + values() + len()**

The combination of above functions can be used to solve this problem. In this,
we reverse sort the dictionary keys on basis of set length and return the
first result.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Key with maximum unique values

# Using sorted() + lambda() + set() + values() + len()

 

# initializing dictionary

test_dict = {"Gfg" : [5, 7, 5, 4, 5],

 "is" : [6, 7, 4, 3, 3], 

 "Best" : [9, 9, 6, 5, 5]}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# one-liner to solve a problem

# sorted used to reverse sort dictionary

max_key = sorted(test_dict, key = lambda ele: len(

 set(test_dict[ele])), reverse = True)[0]

 

# printing result 

print("Key with maximum unique values : " + str(max_key))   
  
---  
  
__

__

**Output**

> The original dictionary is : {‘Gfg’: [5, 7, 5, 4, 5], ‘is’: [6, 7, 4, 3, 3],
> ‘Best’: [9, 9, 6, 5, 5]}  
> Key with maximum unique values : is

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


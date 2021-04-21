Python – Slice till K dictionary value lists



Given dictionary with value as lists, slice each list till K.

>  **Input** : test_dict = {“Gfg” : [1, 6, 3, 5, 7], “Best” : [5, 4, 2, 8, 9],
> “is” : [4, 6, 8, 4, 2]}, K = 3  
>  **Output** : {‘Gfg’: [1, 6, 3], ‘Best’: [5, 4, 2], ‘is’: [4, 6, 8]}  
>  **Explanation** : The extracted 3 length dictionary value list.
>
>  **Input** : test_dict = {“Gfg” : [1, 6, 3, 5, 7], “Best” : [5, 4, 2, 8, 9],
> “is” : [4, 6, 8, 4, 2]}, K = 2  
>  **Output** : {‘Gfg’: [1, 6], ‘Best’: [5, 4], ‘is’: [4, 6]}  
>  **Explanation** : The extracted 2 length dictionary value list.

 **Method #1 : Using loop + list slicing**

The combination of above functionalities can be used to solve this problem. In
this, we perform task of list slicing using slice operation and loop to
iterate through all the keys.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Slice till K dictionary value lists

# Using loop + list slicing 

 

# initializing dictionary

test_dict = {"Gfg" : [1, 6, 3, 5, 7], 

 "Best" : [5, 4, 2, 8, 9],

 "is" : [4, 6, 8, 4, 2]}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing K 

K = 4

 

res = dict()

for sub in test_dict:

 

 # slicing till K and reassigning

 res[sub] = test_dict[sub][:K]

 

# printing result 

print("The dictionary after conversion " + str(res))   
  
---  
  
__

__

**Output**

> The original dictionary is : {‘Gfg’: [1, 6, 3, 5, 7], ‘Best’: [5, 4, 2, 8,
> 9], ‘is’: [4, 6, 8, 4, 2]}  
> The dictionary after conversion {‘Gfg’: [1, 6, 3, 5], ‘Best’: [5, 4, 2, 8],
> ‘is’: [4, 6, 8, 4]}

 **Method #2 : Using dictionary comprehension + list slicing**

This is yet another way in which this task can be performed. In this, we
perform task of reassigning using dictionary comprehension and provides one
liner approach to this problem.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Slice till K dictionary value lists

# Using dictionary comprehension + list slicing

 

# initializing dictionary

test_dict = {"Gfg" : [1, 6, 3, 5, 7],

 "Best" : [5, 4, 2, 8, 9], 

 "is" : [4, 6, 8, 4, 2]}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing K 

K = 4

 

# one-liner to slice elements of list 

# items() used to get all key-value pair of dictionary

res = {key: val[:K] for key, val in test_dict.items()}

 

# printing result 

print("The dictionary after conversion " + str(res))   
  
---  
  
__

__

**Output**

> The original dictionary is : {‘Gfg’: [1, 6, 3, 5, 7], ‘Best’: [5, 4, 2, 8,
> 9], ‘is’: [4, 6, 8, 4, 2]}  
> The dictionary after conversion {‘Gfg’: [1, 6, 3, 5], ‘Best’: [5, 4, 2, 8],
> ‘is’: [4, 6, 8, 4]}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


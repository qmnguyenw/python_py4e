Python – Summation of Custom nested keys in Dictionary



Given dictionary with keys as nested dictionaries, find the sum of values of
certain custom keys inside nested dictionary.

>  **Input** : test_dict = {‘Gfg’ : {1 : 6, 5: 9, 9: 12}, ‘is’ : {1 : 9, 5: 7,
> 9: 2}, ‘best’ : {1 : 3, 5: 4, 9: 14}}, sum_key = [1]  
>  **Output** : 18  
>  **Explanation** : 6 + 9 + 3 = 18, only values with key 1 are summed.
>
>  **Input** : test_dict = {‘Gfg’ : {1 : 6, 5: 9, 9: 12}, ‘is’ : {1 : 9, 5: 7,
> 9: 2}, ‘best’ : {1 : 3, 5: 4, 9: 14}}, sum_key = [5, 9]  
>  **Output** : 48  
>  **Explanation** : Keys 5, 9 are summed.

 **Method #1 : loop**

This is brute way in which this problem can be solved. In this, we employ a
loop for all the list elements and keep updating sum value from all the nested
dictionaries.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Summation of Custom nested keys in Dictionary

# Using loop

 

# initializing dictionary

test_dict = {'Gfg' : {1 : 6, 5: 9, 9: 12},

 'is' : {1 : 9, 5: 7, 9: 2}, 

 'best' : {1 : 3, 5: 4, 9: 14}}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing sum keys 

sum_key = [1, 9]

 

sum = 0

for ele in sum_key:

 for key, val in test_dict.items():

 

 # extracting summation of required values

 sum = sum + val[ele]

 

# printing result 

print("The required summation : " + str(sum))   
  
---  
  
__

__

**Output**

> The original dictionary is : {‘Gfg’: {1: 6, 5: 9, 9: 12}, ‘is’: {1: 9, 5: 7,
> 9: 2}, ‘best’: {1: 3, 5: 4, 9: 14}}  
> The required summation : 46

 **Method #2 : Using list comprehension + sum()**

The combination of above functions can also be employed to solve this problem.
In this, we perform the task of summation using sum() and rest logic is also
encapsulated as one-liner using list comprehension.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Summation of Custom nested keys in Dictionary

# Using list comprehension + sum()

 

# initializing dictionary

test_dict = {'Gfg' : {1 : 6, 5: 9, 9: 12},

 'is' : {1 : 9, 5: 7, 9: 2}, 

 'best' : {1 : 3, 5: 4, 9: 14}}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing sum keys 

sum_key = [1, 9]

 

# sum() used to get cumulative summation

res = sum([val[ele] for ele in sum_key for key, val in
test_dict.items()])

 

# printing result 

print("The required summation : " + str(res))   
  
---  
  
__

__

**Output**

> The original dictionary is : {‘Gfg’: {1: 6, 5: 9, 9: 12}, ‘is’: {1: 9, 5: 7,
> 9: 2}, ‘best’: {1: 3, 5: 4, 9: 14}}  
> The required summation : 46

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


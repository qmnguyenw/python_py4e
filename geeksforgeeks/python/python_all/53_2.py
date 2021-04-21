Python – Dictionary value lists lengths product



Given a dictionary with values as lists, compute lengths of each list, and
find product of all lengths.

>  **Input** : test_dict = {‘Gfg’ : [6, 5, 9, 3], ‘is’ : [1, 3, 4], ‘best’
> :[9, 16]}  
>  **Output** : 24  
>  **Explanation** : 4 * 3 * 2 = 24. Length of lists are 4, 3, and 2.
>
>  **Input** : test_dict = {‘Gfg’ : [6, 5, 3], ‘is’ : [1, 3, 4], ‘best’ :[9,
> 16]}  
>  **Output** : 18  
>  **Explanation** : 3 * 3 * 2 = 18. Length of lists are 3, 3, and 2.

 **Method #1 : Using loop + len()**

This is one of the ways in which this task can be performed. In this, we
iterate for all the values and use len() to get length of all value lists,
post which we perform multiplication of whole data.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Dictionary value lists lengths product

# Using loop + len()

 

# initializing dictionary

test_dict = {'Gfg' : [6, 5, 9, 3, 10],

 'is' : [1, 3, 4], 

 'best' :[9, 16]}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# using loop to iterate through all keys 

res = 1

for key in test_dict:

 

 # len() used to get length of each value list

 res = res * len(test_dict[key]) 

 

# printing result 

print("The computed product : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original dictionary is : {'Gfg': [6, 5, 9, 3, 10], 'is': [1, 3, 4], 'best': [9, 16]}
    The computed product : 30
    

**Method #2 : Using map() + lambda + reduce()**

The combination of above functions provide one-liner approach to solve this
problem. In this, we use map() to get lengths of all lists extending len() to
each list, lambda is used to get product and reduce to combine.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Dictionary value lists lengths product

# Using map() + lambda + reduce() 

from functools import reduce

 

# initializing dictionary

test_dict = {'Gfg' : [6, 5, 9, 3, 10],

 'is' : [1, 3, 4], 

 'best' :[9, 16]}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# values() used to get all lists of keys

res = reduce(lambda sub1, sub2: sub1 * sub2, map(len,
test_dict.values()))

 

# printing result 

print("The computed product : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original dictionary is : {'Gfg': [6, 5, 9, 3, 10], 'is': [1, 3, 4], 'best': [9, 16]}
    The computed product : 30
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


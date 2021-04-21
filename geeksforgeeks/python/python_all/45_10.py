Python – Extract Dictionary Items with Summation Greater than K



Given dictionary with value lists, extract all those items with values summing
over K.

>  **Input** : {“Gfg” : [6, 3, 4], “is” : [8, 10, 12], “Best” : [10, 16, 14],
> “for” : [7, 4, 3], “geeks” : [1, 2, 3, 4]}, K = 10  
>  **Output** : {“Gfg” : [6, 3, 4], “is” : [8, 10, 12], “Best” : [10, 16, 14],
> “for” : [7, 4, 3], “geeks” : [1, 2, 3, 4]}  
>  **Explanation** : All elements are greater than 10.
>
>  **Input** : {“Gfg” : [6, 3, 4], “is” : [8, 10, 12], “Best” : [10, 16, 14],
> “for” : [7, 4, 3], “geeks” : [1, 2, 3, 4]}, K = 50  
>  **Output** : {}  
>  **Explanation** : No elements are greater than 50.

 **Method #1 : Using dictionary comprehension + sum()**

This is one of the ways in which this problem can be solved. In this one-
liner, we iterate through the keys and append the dictionary item only if its
value’s total crosses K computed using sum().

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract Dictionary Items with Summation Greater than K

# Using dictionary comprehension + sum()

 

# initializing dictionary

test_dict = {"Gfg" : [6, 3, 4], 

 "is" : [8, 10, 12], 

 "Best" : [10, 16, 14], 

 "for" : [7, 4, 3], 

 "geeks" : [1, 2, 3, 4]}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing K 

K = 15

 

# summation using sum(), values extracted using items()

res = {key: val for key, val in test_dict.items() if
sum(val) > K}

 

# printing result 

print("The computed dictionary : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original dictionary is : {'Gfg': [6, 3, 4], 'is': [8, 10, 12], 'Best': [10, 16, 14], 'for': [7, 4, 3], 'geeks': [1, 2, 3, 4]}
    The computed dictionary : {'is': [8, 10, 12], 'Best': [10, 16, 14]}
    

**Method #2 : Using filter() + lambda() + sum() + dict()**

This is another way in which this task can be performed. In this, computation
part is done using filter() and lambda, summation using sum() and result
converted to dictionary using dict().

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract Dictionary Items with Summation Greater than K

# Using filter() + lambda() + sum() + dict()

 

# initializing dictionary

test_dict = {"Gfg" : [6, 3, 4], 

 "is" : [8, 10, 12], 

 "Best" : [10, 16, 14], 

 "for" : [7, 4, 3], 

 "geeks" : [1, 2, 3, 4]}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing K 

K = 15

 

# summation using sum(), values extracted using items()

# filter() + lambda used for computation

res = dict(filter(lambda ele: sum(ele[1]) > K,
test_dict.items()))

 

# printing result 

print("The computed dictionary : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original dictionary is : {'Gfg': [6, 3, 4], 'is': [8, 10, 12], 'Best': [10, 16, 14], 'for': [7, 4, 3], 'geeks': [1, 2, 3, 4]}
    The computed dictionary : {'is': [8, 10, 12], 'Best': [10, 16, 14]}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


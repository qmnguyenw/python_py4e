Python – All Position Character Combination



Given a character K, append to each index and all lengths combinations.

>  **Input** : test_str = ‘gfg’, K = ‘$’  
>  **Output** : [‘gfg’, ‘gf$’, ‘g$g’, ‘g$$’, ‘$fg’, ‘$f$’, ‘$$g’, ‘$$$’]  
>  **Explanation** : All possible pairs with replacement occurrences.
>
>  **Input** : test_str = ‘gfg’, K = ‘*’  
>  **Output** : [‘gfg’, ‘gf*’, ‘g*g’, ‘g**’, ‘*fg’, ‘*f*’, ‘**g’, ‘***’]  
>  **Explanation** : All possible pairs with replacement occurrences.

 **Method #1 : Using loop + zip() + join() + product()**

In this, the task of forming combination is done using product(), loop is used
for iteration of elements, join() used to get the desired result and zip()
used to combine each extracted product with original String.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# All Position Character Combination

# Using loop + zip() + join() + product()

import itertools

 

# initializing strings

test_str = 'gfg'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing K 

K = "$"

 

res = [] 

 

# True and false represent Character from String and K respectively.

for sub in itertools.product((True, False), repeat =
len(test_str)):

 res.append("".join(chr if ele else K for chr, ele in
zip(test_str, sub)))

 

# printing result 

print("The required Combinations : " + str(res))   
  
---  
  
__

__

**Output:**

    
    
    The original string is : gfg
    The required Combinations : ['gfg', 'gf$', 'g$g', 'g$$', '$fg', '$f$', '$$g', '$$$']
    

**Method #2 : Using list comprehension**

This is similar to above method, the only difference being it’s a shorthand
all the functionality in a single line.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# All Position Character Combination

# Using list comprehension

import itertools

 

# initializing strings

test_str = 'abc'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing K 

K = "$"

 

# one liner to perform this task 

res = ["".join(chr if ele else K for chr, ele in
zip(test_str, sub)) \

 for sub in itertools.product((True, False), repeat =
len(test_str))]

 

# printing result 

print("The required Combinations : " + str(res))   
  
---  
  
__

__

**Output:**

    
    
    The original string is : abc
    The required Combinations : ['abc', 'ab$', 'a$c', 'a$$', '$bc', '$b$', '$$c', '$$$']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


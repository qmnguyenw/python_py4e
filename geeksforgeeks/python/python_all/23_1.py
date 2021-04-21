Python – K length Combinations from given characters



Given a string, generate K length combinations in a one-liner.

>  **Input** : test_str = ‘gfg’, K = 3  
> **Output** : [‘ggg’, ‘ggf’, ‘ggg’, ‘gfg’, ‘gff’, ‘gfg’, ‘ggg’, ‘ggf’, ‘ggg’,
> ‘fgg’, ‘fgf’, ‘fgg’, ‘ffg’, ‘fff’, ‘ffg’, ‘fgg’, ‘fgf’, ‘fgg’, ‘ggg’, ‘ggf’,
> ‘ggg’, ‘gfg’, ‘gff’, ‘gfg’, ‘ggg’, ‘ggf’, ‘ggg’]  
> **Explanation** : All combinations of K length extracted.
>
>  **Input** : test_str = ‘G4G’, K = 2  
> **Output** : [‘GG’, ‘G4’, ‘GG’, ‘4G’, ’44’, ‘4G’, ‘GG’, ‘G4’, ‘GG’]  
> **Explanation** : All combinations of K length extracted.  
>

**Method #1 : Using** **itertools.product()** **+** **join()** **+** **map()**

The task can be performed by product() using repeat param, but returns result
in tuples list of individual characters. These all can be joined using join()
and map().

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# K length Combinations from given characters shorthand

# Using itertools.product() + join() + map()

from itertools import product

 

# initializing string

test_str = 'gf4g'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing K 

K = 2

 

# map and join() used to change return data type

res = list(map(''.join, product(test_str, repeat = K)))

 

# printing result 

print("The generated Combinations : " + str(res))   
  
---  
  
__

__

**Output:**

> The original string is : gf4g  
> The generated Combinations : [‘gg’, ‘gf’, ‘g4’, ‘gg’, ‘fg’, ‘ff’, ‘f4’,
> ‘fg’, ‘4g’, ‘4f’, ’44’, ‘4g’, ‘gg’, ‘gf’, ‘g4’, ‘gg’]

 **Method #2 : Using itertools.product() + list comprehension**

In this, list comprehension is used for the task of joining elements.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# K length Combinations from given characters shorthand

# Using itertools.product() + join() + map()

from itertools import product

 

# initializing string

test_str = 'gfg'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing K 

K = 2

 

# list comprehension + join() used to change return data type

res = [''.join(ele) for ele in product(test_str, repeat =
K)]

 

# printing result 

print("The generated Combinations : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original string is : gfg  
> The generated Combinations : [‘gg’, ‘gf’, ‘gg’, ‘fg’, ‘ff’, ‘fg’, ‘gg’,
> ‘gf’, ‘gg’]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


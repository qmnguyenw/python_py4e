Python – Shuffle dictionary Values



Given a dictionary, the task is to write a python program to shuffle its
values to different keys.

 **Examples:**

>  **Input:** test_dict = {“gfg” : 1, “is” : 7, “best” : 8, “for” : 3, “geeks”
> : 9}
>
>  **Output :** {“gfg” : 9, “is” : 8, “best” : 7, “for” : 3, “geeks” : 1}
>
>  **Explanation :** Keys are at same position but values are shuffled.
>
>  
>
>
>  
>
>
>  **Input :** test_dict = {“gfg” : 7, “is” : 1, “best” : 8, “for” : 3,
> “geeks” : 9}
>
>  **Output :** {“gfg” : 9, “is” : 8, “best” : 7, “for” : 3, “geeks” : 1}
>
>  **Explanation :** Keys are at same position but values are shuffled.

 **Method #1 : Using** **shuffle()** **+** **zip()** **+** **dict()**

In this, we perform the task of shuffling elements using _shuffle()_ , and
_zip()_ is used to map the shuffled values to keys. In the end, _dict()_ is
used to convert the result to a dictionary.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Shuffle dictionary Values

# Using shuffle() + zip() + dict()

import random

 

# initializing dictionary

test_dict = {"gfg": 1, "is": 7, "best": 8, 

 "for": 3, "geeks": 9}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# shuffling values

temp = list(test_dict.values())

random.shuffle(temp)

 

# reassigning to keys

res = dict(zip(test_dict, temp))

 

# printing result

print("The shuffled dictionary : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original dictionary is : {‘gfg’: 1, ‘is’: 7, ‘best’: 8, ‘for’: 3,
> ‘geeks’: 9}
>
> The shuffled dictionary : {‘gfg’: 1, ‘is’: 7, ‘best’: 3, ‘for’: 9, ‘geeks’:
> 8}
>
>  
>
>
>  
>

 **Method #2 : Using** **sample()** **+** **zip()**

In this, the task of shuffling values is done using _sample()_ of _random_
library.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Shuffle dictionary Values

# Using sample() + zip()

from random import sample

 

# initializing dictionary

test_dict = {"gfg": 1, "is": 7, "best": 8, 

 "for": 3, "geeks": 9}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# reassigning to keys

res = dict(zip(test_dict, sample(list(test_dict.values()), 

 len(test_dict))))

 

# printing result

print("The shuffled dictionary : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original dictionary is : {‘gfg’: 1, ‘is’: 7, ‘best’: 8, ‘for’: 3,
> ‘geeks’: 9}
>
> The shuffled dictionary : {‘gfg’: 8, ‘is’: 9, ‘best’: 1, ‘for’: 3, ‘geeks’:
> 7}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


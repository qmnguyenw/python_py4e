Python – Combine list with other list elements



Given two lists, combine list with each element of the other list.

 **Examples:**

>  **Input** : test_list = [3, 5, 7], pair_list = [‘Gfg’, ‘is’, ‘best’]  
> **Output** : [([3, 5, 7], ‘Gfg’), ([3, 5, 7], ‘is’), ([3, 5, 7], ‘best’)]  
> **Explanation** : All lists paired with each element from other list.
>
>  **Input** : test_list = [3, 5, 7], pair_list = [‘Gfg’, ‘best’]  
> **Output** : [([3, 5, 7], ‘Gfg’), ([3, 5, 7], ‘best’)]  
> **Explanation** : All lists paired with each element from other list.

**Method #1 : Using** **zip()** **+** **len()** **\+ list()**

  

  

In this, we pair each element using zip(), with all the elements of other list
using len(), and picking each element at once.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Combine list with other list elements

# Using zip() + len() + list()

 

# initializing list

test_list = [3, 5, 7, 9]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing pair list 

pair_list = ['Gfg', 'is', 'best']

 

# using zip() to pair element with pair list size

res = list(zip([test_list] * len(pair_list), pair_list))

 

# printing result 

print("The paired list : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [3, 5, 7, 9]  
> The paired list : [([3, 5, 7, 9], ‘Gfg’), ([3, 5, 7, 9], ‘is’), ([3, 5, 7,
> 9], ‘best’)]

 **Method #2 : Using** **product()**

In this, we pair the elements using product(), and map each list with each
element in pair list.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Combine list with other list elements

# Using product()

from itertools import product

 

# initializing list

test_list = [3, 5, 7, 9]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing pair list 

pair_list = ['Gfg', 'is', 'best']

 

# product() performs pairing of elements

res = list(product([test_list], pair_list))

 

# printing result 

print("The paired list : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [3, 5, 7, 9]  
> The paired list : [([3, 5, 7, 9], ‘Gfg’), ([3, 5, 7, 9], ‘is’), ([3, 5, 7,
> 9], ‘best’)]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


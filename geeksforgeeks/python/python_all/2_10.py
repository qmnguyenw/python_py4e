Python – Character repetition string combinations



Given a string list and list of numbers, the task is to write a Python program
to generate all possible strings by repeating each character of each string by
each number in the list.

>  **Input :** test_list = [“gfg”, “is”, “best”], rep_list = [3, 5, 2]
>
>  **Output :** [‘gggfffggg’, ‘iiisss’, ‘bbbeeesssttt’, ‘gggggfffffggggg’,
> ‘iiiiisssss’, ‘bbbbbeeeeesssssttttt’, ‘ggffgg’, ‘iiss’, ‘bbeesstt’]
>
>  **Explanation :** Each element of ‘gfg’ is repeated 3, 5 and 2 times to
> output different strings.
>
> **Input :** test_list = [“gfg”, “is”, “best”], rep_list = [3, 1, 2]
>
>  
>
>
>  
>
>
>  **Output :** [‘gggfffggg’, ‘iiisss’, ‘bbbeeesssttt’, ‘gfg’, ‘is’, ‘best’,
> ‘ggffgg’, ‘iiss’, ‘bbeesstt’]
>
>  **Explanation :** Each element of ‘gfg’ is repeated 3, 1 and 2 times to
> output different strings.

**Method #1 : Using** **join()** **+** **loop** **+** **list comprehension**
**\+ * operator**

In this, the task of constructing each string is done using join(). The *
operator performs the task of creating multiple character occurrences. The
nested loop is used to combine each number with each string.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Character repetition string combinations

# Using join() + nested loop + list comprehension + * operator

 

# initializing list

test_list = ["gfg", "is", "best"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# repeat list

rep_list = [3, 5, 2]

 

# * operator performs repetitions

# list comprehension encapsulates logic

res = [''.join(sub * ele1 for sub in ele2)

 for ele1 in rep_list for ele2 in test_list]

 

# printing result

print("All repetition combinations strings : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [‘gfg’, ‘is’, ‘best’]
>
> All repetition combinations strings : [‘gggfffggg’, ‘iiisss’,
> ‘bbbeeesssttt’, ‘gggggfffffggggg’, ‘iiiiisssss’, ‘bbbbbeeeeesssssttttt’,
> ‘ggffgg’, ‘iiss’, ‘bbeesstt’]

 **Method #2 : Using** **product()** **+** **join()** **+** **loop**

The nested loop for generating pairs is avoiding in this method by the use of
the product() method. Rest all the functionality remains same as the above
method.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Character repetition string combinations

# Using product() + join() + loop

from itertools import product

 

# initializing list

test_list = ["gfg", "is", "best"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# repeat list

rep_list = [3, 5, 2]

 

# * operator performs repetitions

# list comprehension encapsulates logic

res = [''.join(sub * ele1 for sub in ele2)

 for ele2, ele1 in product(test_list, rep_list)]

 

# printing result

print("All repetition combinations strings : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [‘gfg’, ‘is’, ‘best’]
>
> All repetition combinations strings : [‘gggfffggg’, ‘gggggfffffggggg’,
> ‘ggffgg’, ‘iiisss’, ‘iiiiisssss’, ‘iiss’, ‘bbbeeesssttt’,
> ‘bbbbbeeeeesssssttttt’, ‘bbeesstt’]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


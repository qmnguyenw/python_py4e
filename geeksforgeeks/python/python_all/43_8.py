Python – Assign Alphabet to each element



Given a list of elements, assign similar alphabet to same element.

>  **Input** : test_list = [4, 5, 2, 4, 2, 6]  
>  **Output** : [‘a’, ‘b’, ‘c’, ‘a’, ‘c’, ‘d’]  
>  **Explanation** : Alphabets assigned to elements as occurring.
>
>  **Input** : test_list = [4, 5, 2, 4, 2, 6]  
>  **Output** : [‘a’, ‘b’, ‘c’, ‘a’, ‘c’]  
>  **Explanation** : Alphabets assigned to elements as occurring.

 **Method #1 : Using ascii_lowecase() + loop + list comprehension**

In this, we extract all lowercase alphabets using lowercase(), and create
dictionary mapping same element to similar character, post that we flatten
that to appropriate index using list comprehension.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Assign Alphabet to each element

# Using ascii_lowecase() + loop + list comprehension

import string

 

# initializing list

test_list = [4, 5, 2, 4, 2, 6, 5, 2,
5]

 

# printing list

print("The original list : " + str(test_list))

 

temp = {}

cntr = 0

for ele in test_list:

 if ele in temp:

 continue

 

 # assiging same Alphabet to same element

 temp[ele] = string.ascii_lowercase[cntr]

 cntr += 1

 

# flattening 

res = [temp.get(ele) for ele in test_list]

 

# printing results 

print("The mapped List : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : [4, 5, 2, 4, 2, 6, 5, 2, 5]
    The mapped List : ['a', 'b', 'c', 'a', 'c', 'd', 'b', 'c', 'b']
    

**Method #2 : Using defaultdict() + ascii_lowercase() + iter()**

In this we use defaultdict() to assign values to similar elements,
ascii_lowercase() is used to get all lowercase all lowercased alphabets.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Assign Alphabet to each element

# Using defaultdict() + ascii_lowercase() + iter()

from collections import defaultdict

import string 

 

# initializing list

test_list = [4, 5, 2, 4, 2, 6, 5, 2,
5]

 

# printing list

print("The original list : " + str(test_list))

 

# assigning lowecases as iterator

temp = iter(string.ascii_lowercase)

 

# lambda functions fits to similar elements 

res = defaultdict(lambda: next(temp))

 

# flatten in list 

res = [res[key] for key in test_list]

 

# printing results 

print("The mapped List : " + str(list(res)))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : [4, 5, 2, 4, 2, 6, 5, 2, 5]
    The mapped List : ['a', 'b', 'c', 'a', 'c', 'd', 'b', 'c', 'b']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


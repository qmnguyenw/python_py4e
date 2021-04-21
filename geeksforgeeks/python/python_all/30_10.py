Python – Character indices Mapping in String List



Given a String list, map each character in strings, to indices it occurs.

>  **Input** : test_list = [‘g f g’, ‘b e s t’, ‘f o r’, ‘g e e k s’]  
>  **Output** : {‘g’: [1, 4], ‘f’: [1, 3], ‘s’: [2, 4], ‘b’: [2], ‘e’: [2, 4],
> ‘t’: [2], ‘o’: [3], ‘r’: [3], ‘k’: [4]}  
>  **Explanation** : Characters mapped with their occurring elements indices.
>
>  **Input** : test_list = [‘g f g’, ‘i s’, ‘b e s t’, ‘f o r’, ‘g e e k s’]  
>  **Output** : {‘g’: [1, 5], ‘f’: [1, 4], ‘i’: [2], ‘s’: [2, 3, 5], ‘b’: [3],
> ‘e’: [3, 5], ‘t’: [3], ‘o’: [4], ‘r’: [4], ‘k’: [5]}  
>  **Explanation** : Characters mapped with their occurring elements indices.

 **Method #1 : Using defaultdict() + enumerate() + split()**

The combination of above functions can be used to solve this problem. In this,
we use defaultdict() to get empty list to store indices, enumerate() is used
to check for indices and split() can be used for splitting characters.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Charatacter indices Mapping in String List

# Using defaultdict() + enumerate() + split()

from collections import defaultdict

 

# initializing list

test_list = ['g f g', 'i s', 'b e s t', 'f o r', 'g e e
k s'] 

 

# printing original list

print("The original list is : " + str(test_list))

 

res = defaultdict(set)

 

# loop for assigning indices

for idx, ele in enumerate(test_list):

 for sub in ele.split():

 res[sub].add(idx + 1)

 

# dictionary comprehension to remake result 

res = {key: list(val) for key, val in res.items()}

 

# printing result 

print("The mapped dictionary : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : ['g f g', 'i s', 'b e s t', 'f o r', 'g e e k s']
    The mapped dictionary : {'g': [1, 5], 'f': [1, 4], 'i': [2], 's': [2, 3, 5], 'b': [3], 'e': [3, 5], 't': [3], 'o': [4], 'r': [4], 'k': [5]}
    

**Method #2 : Using enumerate() + dictionary comprehension**

This is another way in which this task can be performed. This performs task in
similar way, just in one liner way in dictionary comprehension.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Charatacter indices Mapping in String List

# Using enumerate() + dictionary comprehension

 

# initializing list

test_list = ['g f g', 'i s', 'b e s t', 'f o r', 'g e e
k s'] 

 

# printing original list

print("The original list is : " + str(test_list))

 

# using dictionary comprehension to bind result

res = {sub : [key + 1 for key, val in enumerate(test_list)
if sub in val] 

 for ele in test_list for sub in ele.split()}

 

# printing result 

print("The mapped dictionary : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : ['g f g', 'i s', 'b e s t', 'f o r', 'g e e k s']
    The mapped dictionary : {'g': [1, 5], 'f': [1, 4], 'i': [2], 's': [2, 3, 5], 'b': [3], 'e': [3, 5], 't': [3], 'o': [4], 'r': [4], 'k': [5]}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


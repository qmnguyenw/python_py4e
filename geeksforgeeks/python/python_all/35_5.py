Python – Specific Characters Frequency in String List



Given String list, extract frequency of specific characters in whole strings
list.

>  **Input** : test_list = [“geeksforgeeks is best for geeks”], chr_list =
> [‘e’, ‘b’, ‘g’, ‘f’]  
>  **Output** : {‘g’: 3, ‘e’: 7, ‘b’: 1, ‘f’ : 1}  
>  **Explanation** : Frequency of certain characters extracted.
>
>  **Input** : test_list = [“geeksforgeeks], chr_list = [‘e’, ‘g’]  
>  **Output** : {‘g’: 2, ‘e’: 4}  
>  **Explanation** : Frequency of certain characters extracted.

 **Method #1 : Using join() + Counter()**

In this, we concatenate all the strings, and then Counter() performs task of
getting all frequencies. Last step is to get only specific characters from
List in dictionary using dictionary comprehension.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Specific Characters Frequency in String List

# Using join() + Counter()

from collections import Counter

 

# initializing lists

test_list = ["geeksforgeeks is best for geeks"]

 

# printing original list

print("The original list : " + str(test_list))

 

# char list 

chr_list = ['e', 'b', 'g']

 

# dict comprehension to retrieve on certain Frequencies

res = {key:val for key, val in
dict(Counter("".join(test_list))).items() if key in chr_list}

 

# printing result 

print("Specific Characters Frequencies : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : ['geeksforgeeks is best for geeks']
    Specific Characters Frequencies : {'g': 3, 'e': 7, 'b': 1}
    

**Method #2 : Using chain.from_iterable() + Counter() + dictionary
comprehension**

In this, task of concatenation is done using chain.from_iterable() rather than
join(). Rest all tasks are done as above method.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Specific Characters Frequency in String List

# Using chain.from_iterable() + Counter() + dictionary comprehension

from collections import Counter

from itertools import chain

 

# initializing lists

test_list = ["geeksforgeeks is best for geeks"]

 

# printing original list

print("The original list : " + str(test_list))

 

# char list 

chr_list = ['e', 'b', 'g']

 

# dict comprehension to retrieve on certain Frequencies

# from_iterable to flatten / join

res = {key:val for key, val in
dict(Counter(chain.from_iterable(test_list))).items() if key in
chr_list}

 

# printing result 

print("Specific Characters Frequencies : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : ['geeksforgeeks is best for geeks']
    Specific Characters Frequencies : {'g': 3, 'e': 7, 'b': 1}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


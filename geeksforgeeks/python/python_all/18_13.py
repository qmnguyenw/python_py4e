Python – Resize Keys in dictionary



Given Dictionary, resize keys to K by getting starting k elements from keys.

>  **Input** : test_dict = {“geeksforgeeks” :3, “best” :3, “coding” :4,
> “practice” :3}, K = 3  
> **Output** : {‘gee’: 3, ‘bes’: 3, ‘cod’: 4, ‘pra’: 3}  
> **Explanation** : Keys resized to have 3 elements.
>
>  **Input** : test_dict = {“geeksforgeeks” :3, “best” :3, “coding” :4,
> “practice” :3}, K = 4  
> **Output** : {‘geek’: 3, ‘best’: 3, ‘codi’: 4, ‘prac’: 3}  
> **Explanation** : Keys resized to have 4 elements.

**Method #1 : Using slicing + loop**

In this, resizing is done using slicing of dictionary keys, loop is used to
iterate for all the keys of dictionary.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Resize Keys in dictionary

# Using slicing + loop

 

# initializing dictionary

test_dict = {"geeksforgeeks": 3, "best": 3, "coding":
4, "practice": 3}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing K

K = 2

 

# reforming dictionary

res = dict()

for key in test_dict:

 

 # resizing to K prefix keys

 res[key[:K]] = test_dict[key]

 

# printing result

print("The required result : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original dictionary is : {‘geeksforgeeks’: 3, ‘best’: 3, ‘coding’: 4,
> ‘practice’: 3}  
> The required result : {‘ge’: 3, ‘be’: 3, ‘co’: 4, ‘pr’: 3}

 **Method #2 : Using** **dictionary comprehension** **\+ slicing**

In this, we perform task of reforming dictionary in one liner using dictionary
comprehension.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Resize Keys in dictionary

# Using dictionary comprehension + slicing

 

# initializing dictionary

test_dict = {"geeksforgeeks": 3, "best": 3, "coding":
4, "practice": 3}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing K

K = 2

 

# reforming dictionary

res = {key[:K]: test_dict[key] for key in test_dict}

 

# printing result

print("The required result : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original dictionary is : {‘geeksforgeeks’: 3, ‘best’: 3, ‘coding’: 4,
> ‘practice’: 3}  
> The required result : {‘ge’: 3, ‘be’: 3, ‘co’: 4, ‘pr’: 3}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


Python Program to Remove Nth element from Kth key’s value from the dictionary



Given a dictionary with value lists, our task is to write a Python program to
remove N element from Kth key’s values.

 **Examples:**

>  **Input :** test_dict = {“gfg” : [9, 4, 5, 2, 3, 2], “is” : [1, 2, 3, 4, 3,
> 2], “best” : [2, 2, 2, 3, 4]}, K, N = “gfg”, 2
>
>  **Output :** {‘gfg’: [9, 4, 5, 3], ‘is’: [1, 2, 3, 4, 3, 2], ‘best’: [2, 2,
> 2, 3, 4]}
>
>  **Explanation :** 2 removed from “gfg” key’s value list.
>
>  
>
>
>  
>
>
>  **Input :** test_dict = {“gfg” : [9, 4, 5, 2, 3, 2], “is” : [1, 2, 3, 4, 3,
> 2], “best” : [2, 2, 2, 3, 4]}, K, N = “gfg”, 4
>
>  **Output :** {‘gfg’: [9, 5, 2, 3, 2], ‘is’: [1, 2, 3, 4, 3, 2], ‘best’: [2,
> 2, 2, 3, 4]}
>
>  **Explanation :** 4 removed from “gfg” key’s value list.

 **Method #1 : Using** **loop** **\+ conditional statements**

In this, reassignment of all the key along with their values is done, when K
key occurs, N’s occurrence from its value list is omitted.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove N from K key's value in dictionary values list

# Using loop + conditional statements

 

# initializing dictionary

test_dict = {"gfg" : [9, 4, 5, 2, 3, 2],

 "is" : [1, 2, 3, 4, 3, 2],

 "best" : [2, 2, 2, 3, 4]}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing K, N 

K, N = "gfg", 2

 

res = dict()

for key, val in test_dict.items():

 

 # reassigning omitting desired number

 res[key] = (val if key != K else [idx for idx in
val if idx != N])

 

# printing result

print("The altered dictionary : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original dictionary is : {‘gfg’: [9, 4, 5, 2, 3, 2], ‘is’: [1, 2, 3, 4,
> 3, 2], ‘best’: [2, 2, 2, 3, 4]}
>
> The altered dictionary : {‘gfg’: [9, 4, 5, 3], ‘is’: [1, 2, 3, 4, 3, 2],
> ‘best’: [2, 2, 2, 3, 4]}
>
>  
>
>
>  
>

 **Method #2 : Using** **dictionary comprehension**

In this, we perform similar task to above method, difference being use of
dictionary comprehension instead of looping through keys using conventional
loop.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove N from K key's value in dictionary values list

# Using dictionary comprehension

 

# initializing dictionary

test_dict = {"gfg" : [9, 4, 5, 2, 3, 2],

 "is" : [1, 2, 3, 4, 3, 2], 

 "best" : [2, 2, 2, 3, 4]}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing K, N 

K, N = "gfg", 2

 

# dictionary comprehension used for shorthand

res = {key : (val if key != K else [idx for idx in
val if idx != N]) for key, val in test_dict.items()}

 

# printing result

print("The altered dictionary : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original dictionary is : {‘gfg’: [9, 4, 5, 2, 3, 2], ‘is’: [1, 2, 3, 4,
> 3, 2], ‘best’: [2, 2, 2, 3, 4]}
>
> The altered dictionary : {‘gfg’: [9, 4, 5, 3], ‘is’: [1, 2, 3, 4, 3, 2],
> ‘best’: [2, 2, 2, 3, 4]}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


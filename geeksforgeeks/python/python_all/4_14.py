Python – Custom space size padding in Strings List



In this article given a Strings List, the task is to write a Python program to
pad each string with spaces with specified leading and trailing number of
spaces required.

 **Examples:**

>  **Input:** test_list = [“Gfg”, “is”, “Best”], lead_size = 3, trail_size = 2
>
>  **Output:** [‘ Gfg ‘, ‘ is ‘, ‘ Best ‘]
>
>  **Explanation:** Each word starts after 3 spaces and add 2 spaces after
> completion.
>
>  
>
>
>  
>
>
>  **Input:** test_list = [“Gfg”, “Best”], lead_size = 3, trail_size = 2
>
>  **Output:** [‘ Gfg ‘, ‘ Best ‘]
>
>  **Explanation:** Each word starts after 3 spaces and add 2 spaces after
> completion.

 **Method #1: Using loop**

In this, we perform the task of adding trailing and leading required spaces
using loop. The * operator is used to get required number of spaces.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Custom space size padding in Strings List

# Using loop

 

# initializing lists

test_list = ["Gfg", "is", "Best"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing padding numbers

lead_size = 3

trail_size = 2

 

res = []

for ele in test_list:

 

 # * operator handles number of spaces

 res.append((lead_size * ' ') + ele + (trail_size * '
'))

 

# printing result

print("Padded Strings : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : ['Gfg', 'is', 'Best']
    Padded Strings : ['   Gfg  ', '   is  ', '   Best  ']

 **Method #2: Using** **list comprehension**

Similar way as above, the only difference being the use of list comprehension
as a one-liner alternative to solve problems.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Custom space size padding in Strings List

# Using list comprehension

 

# initializing lists

test_list = ["Gfg", "is", "Best"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing padding numbers

lead_size = 3

trail_size = 2

 

# using list comprehension for one liner alternative

res = [(lead_size * ' ') + ele + (trail_size * ' ')
for ele in test_list]

 

# printing result

print("Padded Strings : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : ['Gfg', 'is', 'Best']
    Padded Strings : ['   Gfg  ', '   is  ', '   Best  ']

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


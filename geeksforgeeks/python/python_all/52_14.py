Python – Test for Even values dictionary values lists



Given a dictionary with lists as values, map Boolean values depending upon all
values in List are Even or not.

>  **Input** : {“Gfg” : [6, 8, 10], “is” : [8, 10, 12, 16], “Best” : [10, 16,
> 14, 6]}  
>  **Output** : {‘Gfg’: True, ‘is’: True, ‘Best’: True}  
>  **Explanation** : All lists have even numbers.
>
>  **Input** : {“Gfg” : [6, 5, 10], “is” : [8, 10, 11, 16], “Best” : [10, 16,
> 14, 6]}  
>  **Output** : {‘Gfg’: False, ‘is’: False, ‘Best’: True}  
>  **Explanation** : Only “Best” has even numbers.

 **Method #1 : Using loop**

This is brute way in which this task can be performed. In this, we iterate for
all the values and check if all list values are Even if yes, we assign key as
True else False.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test for Even values dictionary values lists

# Using loop

 

# initializing dictionary

test_dict = {"Gfg" : [6, 7, 3], 

 "is" : [8, 10, 12, 16], 

 "Best" : [10, 16, 14, 6]}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

res = dict()

for sub in test_dict:

 flag = 1

 

 # checking for even elements

 for ele in test_dict[sub]:

 if ele % 2 != 0:

 flag = 0

 break

 # adding True if all Even elements

 res[sub] = True if flag else False

 

# printing result 

print("The computed dictionary : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original dictionary is : {'Gfg': [6, 7, 3], 'is': [8, 10, 12, 16], 'Best': [10, 16, 14, 6]}
    The computed dictionary : {'Gfg': False, 'is': True, 'Best': True}
    

**Method #2 : Using all() + dictionary comprehension**

This is yet another way in which this task can be performed. In this, we check
for all the elements using all() and dictionary comprehension is used to
remake the result.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test for Even values dictionary values lists

# Using all() + dictionary comprehension

 

# initializing dictionary

test_dict = {"Gfg" : [6, 7, 3], 

 "is" : [8, 10, 12, 16], 

 "Best" : [10, 16, 14, 6]}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# using all to check for all even elements

res = {sub : all(ele % 2 == 0 for ele in
test_dict[sub]) for sub in test_dict}

 

# printing result 

print("The computed dictionary : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original dictionary is : {'Gfg': [6, 7, 3], 'is': [8, 10, 12, 16], 'Best': [10, 16, 14, 6]}
    The computed dictionary : {'Gfg': False, 'is': True, 'Best': True}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


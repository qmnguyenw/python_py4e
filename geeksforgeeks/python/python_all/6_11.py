Python – Set from dictionary values



Given a dictionary, the task is to write a Python program to get all the
values and convert to set.

 **Examples:**

>  **Input :** test_dict = {‘Gfg’ : 4, ‘is’ : 3, ‘best’ : 7, ‘for’ : 3, ‘geek’
> : 4}
>
>  **Output :** {3, 4, 7}
>
>  **Explanation :** 2nd occurrence of 3 is removed in transformation phase.
>
>  
>
>
>  
>
>
>  **Input :** test_dict = {‘Gfg’ : 4, ‘is’ : 3, ‘best’ : 7, ‘geek’ : 4}
>
>  **Output :** {3, 4, 7}
>
>  **Explanation :** 2nd occurrence of 4 is removed in transformation phase.

 **Method #1 : Using generator expression + {}**

In this, we perform task of getting all the values using generator expression
and {} operator performs task of removing duplicate elements and conversion to
set.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Set from dictionary values

# Using generator expression + {}

 

# initializing dictionary

test_dict = {'Gfg': 4, 'is': 3, 'best': 7,
'for': 3, 'geek': 4}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# {} converting to set

res = {test_dict[sub] for sub in test_dict}

 

# printing result

print("The converted set : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original dictionary is : {‘Gfg’: 4, ‘is’: 3, ‘best’: 7, ‘for’: 3,
> ‘geek’: 4}
>
> The converted set : {3, 4, 7}
>
>  
>
>
>  
>

 **Method #2 : Using** **values()** **+** **set()**

In this, we perform task of getting values from dictionary using values() and
set() is used to conversion to set.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Set from dictionary values

# Using values() + set()

 

# initializing dictionary

test_dict = {'Gfg': 4, 'is': 3, 'best': 7,
'for': 3, 'geek': 4}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# values() used to get values

res = set(test_dict.values())

 

# printing result

print("The converted set : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original dictionary is : {‘Gfg’: 4, ‘is’: 3, ‘best’: 7, ‘for’: 3,
> ‘geek’: 4}
>
> The converted set : {3, 4, 7}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


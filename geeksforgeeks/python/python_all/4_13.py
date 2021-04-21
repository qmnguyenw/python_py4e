Python – Symmetric Difference of Dictionaries



Given two Dictionaries, the task is to write a Python program to get the
symmetric difference.

 **Examples:**

>  **Input :** test_dict1 = {‘Gfg’ : 4, ‘is’ : 3, ‘best’ : 7, ‘for’ : 3,
> ‘geek’ : 4},
>
> test_dict2 = {‘Gfg’ : 4, ‘is’ : 3, ‘good’ : 7, ‘for’ : 3, ‘all’ : 4}
>
>  **Output :** {‘all’: 4, ‘good’: 7, ‘best’: 7, ‘geek’: 4}
>
>  
>
>
>  
>
>
>  **Explanation :** all, good, best and geek are mutually unique keys.
>
>  **Input :** test_dict1 = {‘Gfg’ : 4, ‘is’ : 3, ‘good’ : 7, ‘for’ : 3,
> ‘geek’ : 4},
>
> test_dict2 = {‘Gfg’ : 4, ‘is’ : 3, ‘good’ : 7, ‘for’ : 3, ‘all’ : 4}
>
>  **Output :** {‘all’: 4, ‘geek’: 4}
>
>  **Explanation :** all, geek are mutually unique keys.

 **Method #1 : Using ^ operator +** **keys()** **+** **dictionary
comprehension**

In this, We extract all the keys using keys(), and get symmetric difference of
all the keys using ^ operator. The required dictionary is compiled using
dictionary comprehension.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Symmetric Difference of Dictionaries

# Using ^ operator + keys() + dictionary comprehension

 

# initializing dictionaries

test_dict1 = {'Gfg': 4, 'is': 3, 'best': 7,
'for': 3, 'geek': 4}

test_dict2 = {'Gfg': 4, 'is': 3, 'good': 7,
'for': 3, 'all': 4}

 

# printing original dictionaries

print("The original dictionary 1 is : " + str(test_dict1))

print("The original dictionary 2 is : " + str(test_dict2))

 

# getting symmetric difference using ^ operation

res = {key: test_dict1[key] if key in test_dict1 else
test_dict2[key]

 for key in test_dict1.keys() ^ test_dict2.keys()}

 

# printing result

print("The symmetric difference : " + str(res))  
  
---  
  
 __

 __

 **Output:**

  

  

> The original dictionary 1 is : {‘Gfg’: 4, ‘is’: 3, ‘best’: 7, ‘for’: 3,
> ‘geek’: 4}
>
> The original dictionary 2 is : {‘Gfg’: 4, ‘is’: 3, ‘good’: 7, ‘for’: 3,
> ‘all’: 4}
>
> The symmetric difference : {‘geek’: 4, ‘best’: 7, ‘all’: 4, ‘good’: 7}

 **Method #2 : Using set.symmetric_difference() +** **keys()**

In this, we perform task of getting uncommon elements using inbuilt function
symmetric_difference().

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Symmetric Difference of Dictionaries

# Using set.symmetric_difference() + keys()

 

# initializing dictionaries

test_dict1 = {'Gfg': 4, 'is': 3, 'best': 7,
'for': 3, 'geek': 4}

test_dict2 = {'Gfg': 4, 'is': 3, 'good': 7,
'for': 3, 'all': 4}

 

# printing original dictionaries

print("The original dictionary 1 is : " + str(test_dict1))

print("The original dictionary 2 is : " + str(test_dict2))

 

# computing sym. difference using set inbuilt function

res = {key: test_dict1[key] if key in test_dict1 else
test_dict2[key] for key in

 set(test_dict1.keys()).symmetric_difference(test_dict2.keys())}

 

# printing result

print("The symmetric difference : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original dictionary 1 is : {‘Gfg’: 4, ‘is’: 3, ‘best’: 7, ‘for’: 3,
> ‘geek’: 4}
>
> The original dictionary 2 is : {‘Gfg’: 4, ‘is’: 3, ‘good’: 7, ‘for’: 3,
> ‘all’: 4}
>
> The symmetric difference : {‘good’: 7, ‘all’: 4, ‘geek’: 4, ‘best’: 7}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


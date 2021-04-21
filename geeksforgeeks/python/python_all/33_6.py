Python program to extract dictionary items for custom values



Given a dictionary, extract all the items that match given values in the list

 **Example:**

>  **Input** : test_dict = {“Gfg” : 3, “is” : 5, “for” : 8, “Geeks” : 10,
> “Best” : 16 }, sub_list = [5, 4, 10, 20, 16, 8]  
> **Output** : {‘is’: 5, ‘Geeks’: 10, ‘Best’: 16, “for” : 8}  
> **Explanation** : All values matching list values extracted along with keys.
>
>  **Input** : test_dict = {“Gfg” : 3, “is” : 5, “for” : 8, “Geeks” : 10,
> “Best” : 16 }, sub_list = [5, 4, 10]  
> **Output** : {‘is’: 5, ‘Geeks’: 10}  
> **Explanation** : All values matching list values extracted along with keys.  
>

**Method 1: Using a loop**

  

  

Use of a **‘for loop’** is one of the ways in which this task can be
performed. In this, we iterate for all the keys and check if the value is
present in a custom list, if yes, then it’s returned.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# initializing dictionary

test_dict = {"Gfg": 3, "is": 5, "for": 8,

 "Geeks": 10, "Best": 16}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing list

sub_list = [5, 4, 10, 20, 16]

 

# Using loop to perform iteration

res = dict()

 

for key in test_dict:

 

 if test_dict[key] in sub_list:

 res[key] = test_dict[key]

 

# printing result

print("Extracted items : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original dictionary is : {‘Gfg’: 3, ‘is’: 5, ‘for’: 8, ‘Geeks’: 10,
> ‘Best’: 16}  
> Extracted items : {‘is’: 5, ‘Geeks’: 10, ‘Best’: 16}

 **Method 2: Using dictionary comprehension**

This is a one-liner with the help of which this task can be performed. In
this, we iterate for all keys using dictionary comprehension in one-liner
approach.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# initializing dictionary

test_dict = {"Gfg": 3, "is": 5, "for": 8,

 "Geeks": 10, "Best": 16}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing list

sub_list = [5, 4, 10, 20, 16]

 

# dictionary comprehension to compile logic in one dictionary

# in operator used to check value existance

res = {key: val for key, val in test_dict.items() if val
in sub_list}

 

# printing result

print("Extracted items : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original dictionary is : {‘Gfg’: 3, ‘is’: 5, ‘for’: 8, ‘Geeks’: 10,
> ‘Best’: 16}  
> Extracted items : {‘is’: 5, ‘Geeks’: 10, ‘Best’: 16}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


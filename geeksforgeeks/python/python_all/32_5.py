Python – Combine two dictionaries having key of the first dictionary and value
of the second dictionary



Given two dictionaries. The task is to merge them in such a way that the
resulting dictionary contains the key from the first dictionary and value from
the second dictionary.

 **Examples:**

>  **Input** : test_dict1 = {“Gfg” : 20, “is” : 36, “best” : 100}, test_dict2
> = {“Gfg2” : 26, “is2” : 20, “best2” : 70}  
> **Output** : {‘Gfg’: 26, ‘is’: 20, ‘best’: 70}  
> **Explanation** : Similar index keys’ values assigned to dictionary 1.
>
>  **Input** : test_dict1 = {“Gfg” : 20, “best” : 100}, test_dict2 = {“Gfg2” :
> 26, “best2” : 70}  
> **Output** : {‘Gfg’: 26, ‘best’: 70}  
> **Explanation** : Similar index keys’ values assigned to dictionary 1.

**Method #1 : Using loop + keys()**

  

  

This is one way in which this task can be performed. In this, we extract all
the keys using keys() and then assign required values inside loop.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Assign similar index values in Dictionary

# Using loop + keys()

 

# initializing dictionaries

test_dict1 = {"Gfg" : 20, "is" : 36, "best" :
100}

test_dict2 = {"Gfg2" : 26, "is2" : 19, "best2" :
70}

 

# printing original dictionaries

print("The original dictionary 1 is : " + str(test_dict1))

print("The original dictionary 2 is : " + str(test_dict2))

 

# extracting keys and values

keys1 = list(test_dict1.keys())

vals2 = list(test_dict2.values())

 

# assigning new values 

res = dict()

for idx in range(len(keys1)):

 res[keys1[idx]] = vals2[idx]

 

# printing result 

print("Mapped dictionary : " + str(res))   
  
---  
  
__

__

**Output**

> The original dictionary 1 is : {‘Gfg’: 20, ‘is’: 36, ‘best’: 100}  
> The original dictionary 2 is : {‘Gfg2’: 26, ‘is2’: 19, ‘best2’: 70}  
> Mapped dictionary : {‘Gfg’: 26, ‘is’: 19, ‘best’: 70}

 **Method #2 : Using zip() + values()**

This is yet another way in which this task can be performed. In this, we
perform the task of mapping using zip(), extracting values using values().

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Assign similar index values in Dictionary

# Using zip() + values()

 

# initializing dictionaries

test_dict1 = {"Gfg" : 20, "is" : 36, "best" :
100}

test_dict2 = {"Gfg2" : 26, "is2" : 19, "best2" :
70}

 

# printing original dictionaries

print("The original dictionary 1 is : " + str(test_dict1))

print("The original dictionary 2 is : " + str(test_dict2))

 

# using zip() to perform required dict. mapping 

res = dict(zip(test_dict1, test_dict2.values()))

 

# printing result 

print("Mapped dictionary : " + str(res))   
  
---  
  
__

__

**Output**

> The original dictionary 1 is : {‘Gfg’: 20, ‘is’: 36, ‘best’: 100}  
> The original dictionary 2 is : {‘Gfg2’: 26, ‘is2’: 19, ‘best2’: 70}  
> Mapped dictionary : {‘Gfg’: 26, ‘is’: 19, ‘best’: 70}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


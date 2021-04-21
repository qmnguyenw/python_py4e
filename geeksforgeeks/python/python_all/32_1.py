Python program to find Maximum value from dictionary whose key is present in
the list



Given a list with dictionary keys and a dictionary, extract maximum from
dictionary values, whose key is present in list.

 **Examples:**

>  **Input** : test_dict = {“Gfg”: 4, “is” : 5, “best” : 10, “for” : 11,
> “geeks” : 3}, test_list = [“Gfg”, “best”, “geeks”]  
> **Output** : 10  
> **Explanation** : Max value is 11, but not present in list, 10 is of key
> best, which is also in list.
>
>  **Input** : test_dict = {“Gfg”: 4, “is” : 5, “best” : 10, “for” : 11,
> “geeks” : 3}, test_list = [“Gfg”, “best”, “geeks”, “for”]  
> **Output** : 11  
> **Explanation** : Max. value, 11, present in list as well.

**Method #1: Using loop**

  

  

This is one of the ways in which this task can be performed. In this, we check
for all the keys present in list and also maximum, then return the maximum
available.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Maximum value from List keys

# Using loop 

 

# initializing dictionary

test_dict = {"Gfg": 4, "is" : 5, "best" : 9,

 "for" : 11, "geeks" : 3}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing list 

test_list = ["Gfg", "best", "geeks"]

 

res = 0

for ele in test_list:

 

 # checking for key in dictionary

 if ele in test_dict:

 res = max(res, test_dict[ele])

 

# printing result 

print("The required maximum : " + str(res))   
  
---  
  
__

__

**Output:**

> The original dictionary is : {‘Gfg’: 4, ‘is’: 5, ‘best’: 9, ‘for’: 11,
> ‘geeks’: 3}  
> The required maximum : 9

 **Method #2 : Using max() + list comprehension**

This is yet another way in which this task can be performed. In this, we
extract maximum using max() and shorthand list comprehension is used to
iterate through values.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Maximum value from List keys

# Using max() + list comprehension

 

# initializing dictionary

test_dict = {"Gfg": 4, "is" : 5, "best" : 9, 

 "for" : 11, "geeks" : 3}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing list 

test_list = ["Gfg", "best", "geeks"]

 

# maximum is 11, but not present in list, 

# hence 9 is output.

res = max([test_dict[ele] for ele in test_list

 if ele in test_dict])

 

# printing result 

print("The required maximum : " + str(res))   
  
---  
  
__

__

**Output:**

> The original dictionary is : {‘Gfg’: 4, ‘is’: 5, ‘best’: 9, ‘for’: 11,
> ‘geeks’: 3}  
> The required maximum : 9

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


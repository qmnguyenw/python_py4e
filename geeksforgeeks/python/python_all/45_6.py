Python – Construct dictionary Key-Value pairs separated by delimiter



Given a String with key-value pairs separated by delim, construct a
dictionary.

>  **Input** : test_str = ‘gfg#3, is#9, best#10’, delim = ‘#’  
>  **Output** : {‘gfg’: ‘3’, ‘is’: ‘9’, ‘best’: ’10’}  
>  **Explanation** : gfg paired with 3, as separated with # delim.
>
>  **Input** : test_str = ‘gfg.10’, delim = ‘.’  
>  **Output** : {‘gfg’: ’10’}  
>  **Explanation** : gfg paired with 10, as separated with . delim.

 **Method #1 : Using split() + loop**

In this, we perform a split on comma, to get key value pairs, and again a
split on custom delim to get key value pairs separated. Then assigned to
dictionary using loop.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Contruct dictionary Key-Value pairs separated by delim

# Using split() + loop

 

# initializing strings

test_str = 'gfg$3, is$9, best$10'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing delim 

delim = "$"

 

# split by comma for getting differnt dict values

dicts = test_str.split(', ')

 

res = dict()

for sub in dicts:

 

 # 2nd split for forming Key-Values for dictionary

 res[sub.split(delim)[0]] = sub.split(delim)[1]

 

# printing result 

print("The constructed dictionary : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : gfg$3, is$9, best$10
    The constructed dictionary : {'gfg': '3', 'is': '9', 'best': '10'}
    

**Method #2 : Using dictionary comprehension + split()**

Similar to above method, just the difference being that dictionary
comprehension is used for performing task of dictionary construction.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Contruct dictionary Key-Value pairs separated by delim

# Using split() + dictionary comprehension

 

# initializing strings

test_str = 'gfg$3, is$9, best$10'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing delim 

delim = "$"

 

# split by comma for getting differnt dict values

dicts = test_str.split(', ')

 

# dictionary comprehension to form dictionary

res = {sub.split(delim)[0] : sub.split(delim)[1] for sub
in dicts}

 

# printing result 

print("The constructed dictionary : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : gfg$3, is$9, best$10
    The constructed dictionary : {'gfg': '3', 'is': '9', 'best': '10'}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


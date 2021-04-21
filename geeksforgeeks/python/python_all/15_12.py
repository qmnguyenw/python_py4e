Python – Replace value by Kth index value in Dictionary List



Given a dictionary list, the task is to write a Python program to replace the
value of a particular key with kth index of value if the value of the key is
list.

**Examples:**

>  **Input** : test_list = [{‘gfg’ : [5, 7, 9, 1], ‘is’ : 8, ‘good’ : 10},
> {‘gfg’ : 1, ‘for’ : 10, ‘geeks’ : 9}, {‘love’ : 3, ‘gfg’ : [7, 3, 9, 1]}], K
> = 2, key = “gfg”  
> **Output** : [{‘gfg’: 9, ‘is’: 8, ‘good’: 10}, {‘gfg’: 1, ‘for’: 10,
> ‘geeks’: 9}, {‘love’: 3, ‘gfg’: 9}]  
> **Explanation** : gfg is assigned with 9 which is 2nd index in list.  
>
>
> **Input** : test_list = [{‘gfg’ : [5, 7, 9, 1], ‘is’ : 8, ‘good’ : 10},
> {‘gfg’ : 1, ‘for’ : 10, ‘geeks’ : 9}], K = 2, key = “gfg”  
> **Output** : [{‘gfg’: 9, ‘is’: 8, ‘good’: 10}, {‘gfg’: 1, ‘for’: 10,
> ‘geeks’: 9}]  
> **Explanation** : gfg is assigned with 9 which is 2nd index in list.

**Method #1 : Using loop +** **isinstance()**

  

  

In this, we used isinstance() to check for list type of values and loop is
used to iterate through dictionaries.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Replace value by Kth index value in Dictionary List

# Using loop + isinstance()

 

# initializing list

test_list = [{'gfg': [5, 7, 9, 1], 'is': 8,
'good': 10},

 {'gfg': 1, 'for': 10, 'geeks': 9},

 {'love': 3, 'gfg': [7, 3, 9, 1]}]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K

K = 2

 

# initializing Key

key = "gfg"

 

for sub in test_list:

 

 # using isinstance() to check for list

 if isinstance(sub[key], list):

 sub[key] = sub[key][K]

 

# printing result

print("The Modified Dictionaries : " + str(test_list))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [{‘gfg’: [5, 7, 9, 1], ‘is’: 8, ‘good’: 10}, {‘gfg’:
> 1, ‘for’: 10, ‘geeks’: 9}, {‘love’: 3, ‘gfg’: [7, 3, 9, 1]}]  
> The Modified Dictionaries : [{‘gfg’: 9, ‘is’: 8, ‘good’: 10}, {‘gfg’: 1,
> ‘for’: 10, ‘geeks’: 9}, {‘love’: 3, ‘gfg’: 9}]

 **Method #2 : Using** **dictionary comprehension** **+** **isinstance()**

In this, we reconstruct dictionaries with modified dictionary values using
isinstance() and dictionary comprehension is used to form intermediate
dictionaries.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Replace value by Kth index value in Dictionary List

# Using dictionary comprehension + isinstance()

 

# initializing list

test_list = [{'gfg': [5, 7, 9, 1], 'is': 8,
'good': 10},

 {'gfg': 1, 'for': 10, 'geeks': 9},

 {'love': 3, 'gfg': [7, 3, 9, 1]}]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K

K = 2

 

# initializing Key

key = "gfg"

 

# intermediate Dictionaries constructed using dictionary comprehension

res = [{newkey: (val[K] if isinstance(val, list) and newkey
== key else val)

 for newkey, val in sub.items()} for sub in test_list]

 

# printing result

print("The Modified Dictionaries : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [{‘gfg’: [5, 7, 9, 1], ‘is’: 8, ‘good’: 10}, {‘gfg’:
> 1, ‘for’: 10, ‘geeks’: 9}, {‘love’: 3, ‘gfg’: [7, 3, 9, 1]}]  
> The Modified Dictionaries : [{‘gfg’: 9, ‘is’: 8, ‘good’: 10}, {‘gfg’: 1,
> ‘for’: 10, ‘geeks’: 9}, {‘love’: 3, ‘gfg’: 9}]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


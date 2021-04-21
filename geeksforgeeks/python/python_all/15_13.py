Python – Filter dictionaries with ordered values



Given the dictionary list, the task is to write a python program to filter
dictionaries with values in increasing order i.e sorted.

 **Examples:**

>  **Input** : test_list = [{‘gfg’ : 2, ‘is’ : 8, ‘good’ : 10}, {‘gfg’ : 1,
> ‘for’ : 10, ‘geeks’ : 9}, {‘love’ : 3, ‘gfg’ : 4}]  
> **Output** : [{‘gfg’: 2, ‘is’: 8, ‘good’: 10}, {‘love’: 3, ‘gfg’: 4}]  
> **Explanation** : 2, 8, 10 are in increasing order.  
>
>
> **Input** : test_list = [{‘gfg’ : 2, ‘is’ : 8, ‘good’ : 10}, {‘gfg’ : 1,
> ‘for’ : 10, ‘geeks’ : 9}, {‘love’ : 4, ‘gfg’ : 3}]  
> **Output** : [{‘gfg’: 2, ‘is’: 8, ‘good’: 10}]  
> **Explanation** : 2, 8, 10 are in increasing order.

**Method #1 : Using** **sorted()** **+** **values()** **+** **list
comprehension**

  

  

In this, we perform task of sorting using sorted() and extract values using
values(), list comprehension is used to perform iteration of all the
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

# Filter dictionaries with ordered values

# Using sorted() + values() + list comprehension

 

# initializing list

test_list = [{'gfg': 2, 'is': 8, 'good': 10},

 {'gfg': 1, 'for': 10, 'geeks': 9},

 {'love': 3, 'gfg': 4}]

 

# printing original list

print("The original list is : " + str(test_list))

 

# sorted to check with ordered values

# values() extracting dictionary values

res = [sub for sub in test_list if sorted(

 list(sub.values())) == list(sub.values())]

 

# printing result

print("The filtered Dictionaries : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [{‘gfg’: 2, ‘is’: 8, ‘good’: 10}, {‘gfg’: 1, ‘for’:
> 10, ‘geeks’: 9}, {‘love’: 3, ‘gfg’: 4}]  
> The filtered Dictionaries : [{‘gfg’: 2, ‘is’: 8, ‘good’: 10}, {‘love’: 3,
> ‘gfg’: 4}]

 **Method #2 : Using** **filter()** **+** **lambda** **\+ sorted()**

In this, we perform task of filtering using filter(), and lambda function is
used to perform task of injecting functionality necessary for checking
increasing values.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Filter dictionaries with ordered values

# Using filter() + lambda + sorted()

 

# initializing list

test_list = [{'gfg': 2, 'is': 8, 'good': 10},

 {'gfg': 1, 'for': 10, 'geeks': 9},

 {'love': 3, 'gfg': 4}]

 

# printing original list

print("The original list is : " + str(test_list))

 

# sorted to check with ordered values

# values() extracting dictionary values

# filter() and lambda function used to filter

res = list(filter(lambda sub:
sorted(list(sub.values()))

 == list(sub.values()), test_list))

 

# printing result

print("The filtered Dictionaries : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [{‘gfg’: 2, ‘is’: 8, ‘good’: 10}, {‘gfg’: 1, ‘for’:
> 10, ‘geeks’: 9}, {‘love’: 3, ‘gfg’: 4}]  
> The filtered Dictionaries : [{‘gfg’: 2, ‘is’: 8, ‘good’: 10}, {‘love’: 3,
> ‘gfg’: 4}]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


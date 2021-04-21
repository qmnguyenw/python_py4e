Python – Filter Strings within ASCII range



Given ASCII or alphabetical range, filter strings found in particular range.

>  **Input** : test_list = [“gfg”, “is”, “best”, “for”, “geeks”], strt_asc,
> end_asc = 105, 115  
> **Output** : [‘is’]  
> **Explanation** : i has 105, and s has 115, which is in range ASCII values.  
>  **Input** : test_list = [“gfg”, “is”, “best”, “for”, “geeks”], strt_asc,
> end_asc = 100, 115  
> **Output** : [‘gfg’, ‘is’, ‘for’, ‘geeks’]  
> **Explanation** : Strings with range characters included.  
>

**Method #1 : Using** **list comprehension** **+** **all()** **+** **ord()**

In this, we check for all characters to be in given ASCII range, computed
using ord(), and accordingly, strings are filtered.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Filter Strings within ASCII range

# Using list comprehension + ord() + all()

 

# initializing list

test_list = ["gfg", "is", "best", "for", "geeks"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing ASCII range

strt_asc, end_asc = 105, 115

 

# checking for all characters to be in ASCII range

res = [sub for sub in test_list if all(

 ord(ele) >= strt_asc and ord(ele) <= end_asc for ele
in sub)]

 

# printing result

print("Filtered Strings : " + str(res))  
  
---  
  
 __

 __

 **Output**

  

  

    
    
    The original list is : ['gfg', 'is', 'best', 'for', 'geeks']
    Filtered Strings : ['is']
    


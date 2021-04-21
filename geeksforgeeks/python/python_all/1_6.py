Python Program to create a sub-dictionary containing all keys from dictionary
list



Given the dictionary list, our task is to create a new dictionary list that
contains all the keys, if not, then assign None to the key and persist of each
dictionary.

 **Example:**

>  **Input :** test_list = [{‘gfg’ : 3, ‘is’ : 7}, {‘gfg’ : 3, ‘is’ : 1,
> ‘best’ : 5}, {‘gfg’ : 8}]
>
>  **Output :** [{‘is’: 7, ‘best’: None, ‘gfg’: 3}, {‘is’: 1, ‘best’: 5,
> ‘gfg’: 3}, {‘is’: None, ‘best’: None, ‘gfg’: 8}]
>
>  **Explanation :** The items with “is” and “best” are added to all lists,
> whereever missing as None if no values populated.
>
>  
>
>
>  
>
>
>  **Input :** test_list = [{‘gfg’ : 3}, {‘gfg’ : 3, ‘best’ : 5}, {‘gfg’ : 8}]
>
>  **Output :** [{‘best’: None, ‘gfg’: 3}, {‘best’: 5, ‘gfg’: 3}, {‘best’:
> None, ‘gfg’: 8}]
>
>  **Explanation :** The items with “best” are added to all lists, whereever
> missing as None if no values populated.

 **Method #1 : Using** **set()** **+** **chain.from_iterable()** **+**
**get()** **+** **list comprehension**

In this, we perform task of getting all the required keys using set() and
chain.from_iterable(). The next step is to update all the dictionaries with
not found keys using list comprehension and get().

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Ensure all keys in dictionary list

# Using set() + chain.from_iterable() + get() + list comprehension

from itertools import chain

 

# initializing list

test_list = [{'gfg' : 3, 'is' : 7}, 

 {'gfg' : 3, 'is' : 1, 'best' : 5}, 

 {'gfg' : 8}]

 

# printing original list

print("The original list is : " + str(test_list))

 

# extracting all keys

all_keys = set(chain.from_iterable(test_list))

 

# assigning None using get() if key's value is not found

res = [dict((key, sub.get(key, None)) for key in
all_keys) for sub in test_list]

 

# printing result

print("Reformed dictionaries list : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [{‘gfg’: 3, ‘is’: 7}, {‘gfg’: 3, ‘is’: 1, ‘best’: 5},
> {‘gfg’: 8}]
>
> Reformed dictionaries list : [{‘gfg’: 3, ‘best’: None, ‘is’: 7}, {‘gfg’: 3,
> ‘best’: 5, ‘is’: 1}, {‘gfg’: 8, ‘best’: None, ‘is’: None}]
>
>  
>
>
>  
>

 **Method #2 : Using set() + chain.from_iterable() + update()**

In this, the updation and checking of all the keys from dictionary is done
using update(), rest all the functions remain similar.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Ensure all keys in dictionary list

# Using set() + chain.from_iterable() + update()

from itertools import chain

 

# initializing list

test_list = [{'gfg' : 3, 'is' : 7}, 

 {'gfg' : 3, 'is' : 1, 'best' : 5}, 

 {'gfg' : 8}]

 

# printing original list

print("The original list is : " + str(test_list))

 

# extracting all keys

all_keys = set(chain.from_iterable(test_list))

 

# assigning None using update() if key is not found 

for sub in test_list:

 sub.update({key: None for key in all_keys if key not in
sub})

 

# printing result

print("Reformed dictionaries list : " + str(test_list))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [{‘gfg’: 3, ‘is’: 7}, {‘gfg’: 3, ‘is’: 1, ‘best’: 5},
> {‘gfg’: 8}]
>
> Reformed dictionaries list : [{‘gfg’: 3, ‘best’: None, ‘is’: 7}, {‘gfg’: 3,
> ‘best’: 5, ‘is’: 1}, {‘gfg’: 8, ‘best’: None, ‘is’: None}]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


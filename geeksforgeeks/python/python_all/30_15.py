Python – Filter Tuples with Strings of specific characters



Given a Tuple List, extract tuples, which have strings made up of certain
characters.

>  **Input** : test_list = [(‘gfg’, ‘best’), (‘gfg’, ‘good’), (‘fest’,
> ‘gfg’)], char_str = ‘gfestb’  
> **Output** : [(‘gfg’, ‘best’), (‘fest’, ‘gfg’)]  
> **Explanation** : All tuples contain characters from char_str.
>
>  **Input** : test_list = [(‘gfg’, ‘best’), (‘gfg’, ‘good’), (‘fest’,
> ‘gfg’)], char_str = ‘gfstb’  
> **Output** : []  
> **Explanation** : No tuples with given characters.

**Method #1 : Using** **all()** **+** **list comprehension**

In this, we check for characters in strings, using in operator and all() is
used to check if all elements in tuple have strings made up of certain
characters.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Filter Tuples with Strings of specific characters

# Using all() + list comprehension

 

# initializing lists

test_list = [('gfg', 'best'), ('gfg', 'good'),
('fest', 'gfg')]

 

# printing original lists

print("The original list is : " + str(test_list))

 

# initializing char_str

char_str = 'gfestb'

 

# nested all(), to check for all characters in list, 

# and for all strings in tuples

res = [sub for sub in test_list if all(

 all(el in char_str for el in ele) for ele in sub)]

 

# printing result

print("The filtered tuples : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [(‘gfg’, ‘best’), (‘gfg’, ‘good’), (‘fest’, ‘gfg’)]  
> The filtered tuples : [(‘gfg’, ‘best’), (‘fest’, ‘gfg’)]

 **Method #2 : Using** **filter()** **\+ lambda + all()**

Similar to the above method, difference being filter() + lambda is used to
perform task of filtering.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Filter Tuples with Strings of specific characters

# Using filter() + lambda + all()

 

# initializing lists

test_list = [('gfg', 'best'), ('gfg', 'good'),
('fest', 'gfg')]

 

# printing original lists

print("The original list is : " + str(test_list))

 

# initializing char_str

char_str = 'gfestb'

 

# nested all(), to check for all characters in list, 

# and for all strings in tuples filter() is used 

# to extract tuples

res = list(filter(lambda sub: all(all(el in
char_str for el in ele)

 for ele in sub), test_list))

 

# printing result

print("The filtered tuples : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [(‘gfg’, ‘best’), (‘gfg’, ‘good’), (‘fest’, ‘gfg’)]  
> The filtered tuples : [(‘gfg’, ‘best’), (‘fest’, ‘gfg’)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


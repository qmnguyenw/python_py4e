Python – Remove Non-English characters Strings from List



Given a List of Strings, perform removal of all Strings with non-english
characters.

>  **Input** : test_list = [‘Good| ????’, ‘??Geeks???’]  
>  **Output** : []  
>  **Explanation** : Both contain non-English characters
>
>  **Input** : test_list = [“Gfg”, “Best”]  
>  **Output** : [“Gfg”, “Best”]  
>  **Explanation** : Both are valid English words.

 **Method #1 : Using regex + findall() + list comprehension**

In this, we create a regex of unicodes and check for occurrence in String
List, extract each String without unicode using findall().

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove Non-English characters Strings from List

# Using regex + findall() + list comprehension

import re

 

# initializing list

test_list = ['Gfg', 'Good| ????', "for", '??Geeks???']

 

# printing original list

print("The original list is : " + str(test_list))

 

# using findall() to neglect unicode of Non-English alphabets

res = [idx for idx in test_list if not
re.findall("[^\u0000-\u05C0\u2100-\u214F]+", idx)]

 

# printing result 

print("The extracted list : " + str(res))  
  
---  
  
 __

 __

 **Method #2 : Using regex + search() + filter() + lambda**

In this, we search for only English alphabets in String, and extract only
those that have those. We use filter() + lambda to perform the task of passing
filter functionality and iteration.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove Non-English characters Strings from List

# Using regex + search() + filter() + lambda

import re

 

# initializing list

test_list = ['Gfg', 'Good| ????', "for", '??Geeks???']

 

# printing original list

print("The original list is : " + str(test_list))

 

# using search() to get only those strings with alphabets

res = list(filter(lambda ele: re.search("[a-zA-Z\s]+", ele)
is not None, test_list))

 

# printing result 

print("The extracted list : " + str(res))  
  
---  
  
 __

 __

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


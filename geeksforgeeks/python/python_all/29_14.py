Python program to extract characters in given range from a string list



Given a Strings List, extract characters in index range spanning entire
Strings list.

>  **Input** : test_list = [“geeksforgeeks”, “is”, “best”, “for”, “geeks”],
> strt, end = 14, 20  
> **Output** : sbest  
> **Explanation** : Once concatenated, 14 – 20 range is extracted.
>
>  **Input** : test_list = [“geeksforgeeks”, “is”, “best”, “for”, “geeks”],
> strt, end = 11, 20  
> **Output** : sbesbest  
> **Explanation** : Once concatenated, 11 – 20 range is extracted.  
>

**Method 1 : Using join() + list comprehension**

In this, we perform concatenation of all the strings using join() and list
comprehension and post that, the required character range is extracted.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# initializing list

test_list = ["geeksforgeeks", "is", "best", "for",
"geeks"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing char range 

strt, end = 14, 30

 

# strt and end used to get desired characters

res = ''.join([sub for sub in test_list])[strt : end]

 

# printing result 

print("Range characters : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : ['geeksforgeeks', 'is', 'best', 'for', 'geeks']
    Range characters : sbestforgeeks
    
    

**Method 2 : Using chain.from_iterable() + join()**

In this, we perform the task of flattening of characters using
chain.from_iterable(), after that join() is used for concatenation of all
strings and indices are extracted in range.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import module

from itertools import chain

 

# initializing list

test_list = ["geeksforgeeks", "is", "best", "for",
"geeks"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing char range 

strt, end = 14, 30

 

# strt and end used to get desired characters

res = ''.join(chain.from_iterable(test_list))[strt : end]

 

# printing result 

print("Range characters : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : ['geeksforgeeks', 'is', 'best', 'for', 'geeks']
    Range characters : sbestforgeeks
    
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


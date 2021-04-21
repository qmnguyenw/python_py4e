Python program to find the character position of Kth word from a list of
strings



Given a list of strings. The task is to find the index of the character
position for the word, which lies at the Kth index in the list of strings.

 **Examples:**

>  **Input** : test_list = [“geekforgeeks”, “is”, “best”, “for”, “geeks”], K =
> 21  
> **Output** : 0  
>  **Explanation** : 21st index occurs in “geeks” and point to “g” which is
> 0th element of word.
>
>  **Input** : test_list = [“geekforgeeks”, “is”, “best”, “for”, “geeks”], K =
> 15  
> **Output** : 1  
>  **Explanation** : 15th index occurs in “best” and point to “e” which is 1st
> element of word.

 **Method #1 : Using enumerate() + list comprehension**

  

  

In this, we use nested enumerate() to check indices for words, and strings in
the list, list comprehension is used to encapsulate logic in 1 liner.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Word Index for K position in Strings List

# Using enumerate() + list comprehension

 

# initializing list

test_list = ["geekforgeeks", "is", "best", "for",
"geeks"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K

K = 20

 

# enumerate to get indices of all inner and outer list

res = [ele[0] for sub in enumerate(test_list) for ele
in enumerate(sub[1])]

 

# getting index of word

res = res[K]

 

# printing result

print("Index of character at Kth position word : " + str(res))  
  
---  
  
 __

 __

 **Output**

> The original list is : [‘geekforgeeks’, ‘is’, ‘best’, ‘for’, ‘geeks’]  
> Index of character at Kth position word : 2

**Method #2 : Using next() + zip() + count()**

In this, we pair up the number of words with its counts using zip(), and
accumulate till we don’t reach Kth Index.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Word Index for K position in Strings List

# Using next() + zip() + count()

from itertools import count

 

# initializing list

test_list = ["geekforgeeks", "is", "best", "for",
"geeks"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K

K = 20

 

# count() for getting count

# pairing using zip()

cnt = count()

res = next(j for sub in test_list for j, idx in zip(

 range(len(sub)), cnt) if idx == K)

 

# printing result

print("Index of character at Kth position word : " + str(res))  
  
---  
  
 __

 __

 **Output**

> The original list is : [‘geekforgeeks’, ‘is’, ‘best’, ‘for’, ‘geeks’]  
> Index of character at Kth position word : 2

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


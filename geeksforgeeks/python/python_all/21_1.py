Python – Remove charcters greater than K



Given Strings list, remove all the characters from each string that have
characters greater than K.

>  **Input** : test_list = [“geeksforgeeks”, “is”, “best”, “for”, “geeks”], K
> = 13  
> **Output** : [‘geekfgeek’, ‘i’, ‘be’, ‘f’, ‘geek’]  
> **Explanation** : ASCII Characters above m are removed.
>
>  **Input** : test_list = [“geeksforgeeks”, “is”, “best”, “for”, “geeks”], K
> = 10  
> **Output** : [‘geekfgeek’, ‘i’, ‘be’, ‘f’, ‘geek’]  
> **Explanation** : ASCII Characters above j are removed.  
>

**Method #1 : Using loop + ord()**

In this, we check for the character’s ASCII value using ord(), and then
compare with K, if the character is greater than K, the character is not
included in the result string.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove charcters greater than K 

# Using loop + ord()

 

# initializing list

test_list = ["geeksforgeeks", "is", "best", "for",
"geeks"]

 

# printing original lists

print("The original list is : " + str(test_list))

 

# initializing K 

K = 13

 

res = []

for ele in test_list:

 res_str = ''

 for sub in ele:

 

 # check for string characters 

 if (ord(sub) - 97 <= K):

 res_str += sub

 res.append(res_str)

 

# printing result 

print("Filtered List " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [‘geeksforgeeks’, ‘is’, ‘best’, ‘for’, ‘geeks’]  
> Filtered List [‘geekfgeek’, ‘i’, ‘be’, ‘f’, ‘geek’]

 **Method #2 : Using join() + list comprehension + ord()**

This is a shorthand way in which this task can be performed. In this, we
perform tasks of filtering and joining to form string using join().

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove charcters greater than K 

# Using join() + list comprehension + ord()

 

# initializing list

test_list = ["geeksforgeeks", "is", "best", "for",
"geeks"]

 

# printing original lists

print("The original list is : " + str(test_list))

 

# initializing K 

K = 13

 

# using list comprehension for 1 liner 

res = [''.join([ele for ele in sub if ord(ele) - 97
<= K]) for sub in test_list]

 

# printing result 

print("Filtered List " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [‘geeksforgeeks’, ‘is’, ‘best’, ‘for’, ‘geeks’]  
> Filtered List [‘geekfgeek’, ‘i’, ‘be’, ‘f’, ‘geek’]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


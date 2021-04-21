Python – N sized substrings with K distinct characters



Given a String, the task is to write a Python program to extract strings of N
size and have K distinct characters.

 **Examples:**

>  **Input** : test_str = ‘geeksforgeeksforgeeks’, N = 3, K = 2  
> **Output** : [‘gee’, ‘eek’, ‘gee’, ‘eek’, ‘gee’, ‘eek’]  
> **Explanation** : 3 lengths have 2 unique characters are extracted.  
>
>
> **Input** : test_str = ‘geeksforgeeksforgeeks’, N = 4, K = 2  
> **Output** : []  
> **Explanation** : No strings with 4 length and just have 2 elements.

**Method #1 : Using** **slicing** **+** **set()** **\+ loop**

  

  

In this we perform task of getting N chunks using slicing, set() is used to
check for unique elements. Loop is used to interate for all the possible
chunks.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# N sized substrings with K distinct characters

# Using slicing + set() + loop

 

# initializing string

test_str = 'geeksforgeeksforgeeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing N

N = 3

 

# initializing K

K = 2

 

res = []

for idx in range(0, len(test_str) - N + 1):

 

 # getting unique elements off sliced string

 if (len(set(test_str[idx: idx + N])) == K):

 res.append(test_str[idx: idx + N])

 

# printing result

print("Extracted Strings : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original string is : geeksforgeeksforgeeks
    Extracted Strings : ['gee', 'eek', 'gee', 'eek', 'gee', 'eek']

 **Method #2 : Using** **list comprehension** **+** **len()** **+** **set()**
**+** **slicing**

Similar to above method, only difference being list comprehension is used
instead of loop, just to provide shorthand to solve this task.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# N sized substrings with K distinct characters

# Using list comprehension + len() + set() + slicing

 

# initializing string

test_str = 'geeksforgeeksforgeeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing N

N = 3

 

# initializing K

K = 2

 

# list comprehension used to slice

res = [test_str[idx: idx + N]

 for idx in range(0, len(test_str) - N + 1) 

 if len(set(test_str[idx: idx + N])) == K]

 

# printing result

print("Extracted Strings : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original string is : geeksforgeeksforgeeks
    Extracted Strings : ['gee', 'eek', 'gee', 'eek', 'gee', 'eek']

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


Python – Possible Substring count from String



Given target string and argument substring, count how many substrings can be
constructed using string charaters, repetitions not allowed.

>  **Input** : test_str = “geksefokesgergeeks”, arg_str = “geeks”  
>  **Output** : 3  
>  **Explanation** : “geeks” can be created 3 times using string characters.
>
>  **Input** : test_str = “gefroksefokesgergeeks”, arg_str = “for”  
>  **Output** : 2  
>  **Explanation** : “for” can be created 2 times using string characters.

 **Method #1 : Using count() + min() + set()**

The combination of above functions can be used to solve this problem. In this,
we divide the count of each element of arg string with count of target string
character, and using min(), the lowest element is returned. The logic behind
is that any element above min would mean the minimum element would miss from
that string onwards.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Possible Substring count from String

# Using min() + list comprehension + count()

 

# initializing string

test_str = "gekseforgeeks"

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing arg string 

arg_str = "geeks"

 

# using min and count to get minimum possible 

# occurrence of character

res = min(test_str.count(char) // arg_str.count(char) for
char in set(arg_str))

 

# printing result 

print("Possible substrings count : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : gekseforgeeks
    Possible substrings count : 2
    

**Method #2 : Using Counter() + list comprehension**

This is yet another way in which this task can be performed. In this, we
perform the task of counting using Counter() and list comprehension is used to
bind the result together, using min() performing similar task as previous
method.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Possible Substring count from String

# Using Counter() + list comprehension

from collections import Counter

 

# initializing string

test_str = "gekseforgeeks"

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing arg string 

arg_str = "geeks"

 

# using Counter to get character frequencies

temp1 = Counter(test_str)

temp2 = Counter(arg_str)

res = min(temp1[char] // temp2[char] for char in
temp2.keys())

 

# printing result 

print("Possible substrings count : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : gekseforgeeks
    Possible substrings count : 2
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


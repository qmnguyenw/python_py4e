Python – Sort Strings by maximum frequency character



Given a string, the task is to write a Python program to perform sort by
maximum occurring character.

>  **Input** : test_list = [“geekforgeeks”, “bettered”, “for”, “geeks”]  
> **Output** : [‘for’, ‘geeks’, ‘bettered’, ‘geekforgeeks’]  
> **Explanation** : 1 < 2 < 3 < 4, is ordering of maximum character occurrence
> frequency.
>
>  **Input** : test_list = [“geekforgeeks”, “for”, “geeks”]  
> **Output** : [‘for’, ‘geeks’, ‘geekforgeeks’]  
> **Explanation** : 1 < 2 < 4, is ordering of maximum character occurrence
> frequency.  
>

**Method #1 :** Using sort() + Counter() + max()

In this, we perform inplace sorting using sort(), and Counter() is used to
compute characters frequency, max() used to get maximum of computed
frequencies.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort Strings by maximum frequency character

# Using sort() + Counter() + max()

from collections import Counter

 

# getting maximum character frequency

def max_freq(arg_str):

 res = Counter(arg_str) 

 return arg_str.count(max(res, key = res.get))

 

# initializing list

test_list = ["geekforgeeks", "bettered", "for", "geeks"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# performing sort 

test_list.sort(key = max_freq)

 

# printing result 

print("Sorted List : " + str(test_list))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : ['geekforgeeks', 'bettered', 'for', 'geeks']
    Sorted List : ['for', 'geeks', 'bettered', 'geekforgeeks']

 **Method #2 :** Using sorted() \+ lambda \+ Counter()

In this, we perform the task of performing sort using sorted(), and lambda
function to get a single statement logical expression, avoiding external
function call.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort Strings by maximum frequency character

# Using sorted() + lambda + Counter()

from collections import Counter

 

# getting maximum character frequency

def max_freq(arg_str):

 res = Counter(arg_str) 

 return arg_str.count(max(arg_str, key = arg_str.get))

 

# initializing list

test_list = ["geekforgeeks", "bettered", "for", "geeks"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# performing sort 

# lambda function to drive logic

res = sorted(test_list, 

 key = lambda arg_str : arg_str.count(

 max(Counter(arg_str), key = Counter(arg_str).get)))

 

# printing result 

print("Sorted List : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : ['geekforgeeks', 'bettered', 'for', 'geeks']
    Sorted List : ['for', 'geeks', 'bettered', 'geekforgeeks']

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


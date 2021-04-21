Python – Filter rows with only Alphabets from List of Lists



Given Matrix, write a Python program to extract rows which only contains
alphabets in its strings.

 **Examples:**

>  **Input** : test_list = [[“gfg”, “is”, “best”], [“Geeks4Geeks”, “good”],
> [“Gfg is good”], [“love”, “gfg”]]  
> **Output** : [[‘gfg’, ‘is’, ‘best’], [‘love’, ‘gfg’]]  
> **Explanation** : All strings with just alphabets are extracted.  
>
>
> **Input** : test_list = [[“gfg”, “is”, “!best”], [“Geeks4Geeks”, “good”],
> [“Gfg is good”], [“love”, “gfg”]]  
> **Output** : [[‘love’, ‘gfg’]]  
> **Explanation** : All strings with just alphabets are extracted.

**Method #1: Using** **isalpha()** **+** **all()** **+** **list
comprehension**

  

  

In this, we check for all the alphabets using isalpha() and all() is used to
ensure all the strings contain just the alphabets. The list comprehension is
used to iterate through rows.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Filter rows with only Alphabets

# Using isalpha() + all() + list comprehension

 

# initializing list

test_list = [["gfg", "is", "best"], ["Geeks4Geeks",
"good"],

 ["Gfg is good"], ["love", "gfg"]]

 

# printing original lists

print("The original list is : " + str(test_list))

 

# all() checks for all strings to contain alphabets

res = [sub for sub in test_list if all(ele.isalpha() for
ele in sub)]

 

# printing result

print("Filtered Rows : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[‘gfg’, ‘is’, ‘best’], [‘Geeks4Geeks’, ‘good’],
> [‘Gfg is good’], [‘love’, ‘gfg’]]  
> Filtered Rows : [[‘gfg’, ‘is’, ‘best’], [‘love’, ‘gfg’]]

 **Method #2 : Using** **filter()** **+** **lambda** **+** **join()** **+**
**isalpha()**

In this, we concatenate each string using join() and test if its all alphabets
using isalpha(), and add if the verdict returns true.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Filter rows with only Alphabets

# Using filter() + lambda + join() + isalpha()

 

# initializing list

test_list = [["gfg", "is", "best"], ["Geeks4Geeks",
"good"],

 ["Gfg is good"], ["love", "gfg"]]

 

# printing original lists

print("The original list is : " + str(test_list))

 

# join() used to concatenate strings

res = list(filter(lambda sub: ''.join(

 [ele for ele in sub]).isalpha(), test_list))

 

# printing result

print("Filtered Rows : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[‘gfg’, ‘is’, ‘best’], [‘Geeks4Geeks’, ‘good’],
> [‘Gfg is good’], [‘love’, ‘gfg’]]  
> Filtered Rows : [[‘gfg’, ‘is’, ‘best’], [‘love’, ‘gfg’]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


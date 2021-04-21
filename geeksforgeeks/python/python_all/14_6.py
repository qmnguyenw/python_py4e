Python – Filter Similar Case Strings



Given the Strings list, the task is to write a Python program to filter all
the strings which have a similar case, either upper or lower.

 **Examples:**

>  **Input** : test_list = [“GFG”, “Geeks”, “best”, “FOr”, “all”, “GEEKS”]  
> **Output** : [‘GFG’, ‘best’, ‘all’, ‘GEEKS’]  
> **Explanation** : GFG is all uppercase, best is all lowercase.
>
>  **Input** : test_list = [“GFG”, “Geeks”, “best”]  
> **Output** : [‘GFG’, ‘best’]  
> **Explanation** : GFG is all uppercase, best is all lowercase.  
>

**Method #1 : Using** **islower()** **+** **isupper()** **+** **list
comprehension**

  

  

In this, we check for each string to be lower or upper case using islower()
and isupper(), and list comprehension is used to iterate through strings.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Filter Similar Case Strings

# Using islower() + isupper() + list comprehension

 

# initializing Matrix

test_list = ["GFG", "Geeks", 

 "best", "FOr", "all", "GEEKS"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# islower() and isupper() used to check for cases

res = [sub for sub in test_list if sub.islower() or
sub.isupper()]

 

# printing result

print("Strings with same case : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [‘GFG’, ‘Geeks’, ‘best’, ‘FOr’, ‘all’, ‘GEEKS’]  
> Strings with same case : [‘GFG’, ‘best’, ‘all’, ‘GEEKS’]

 **Method #2 : Using** **islower()** **+** **isupper()** **+** **filter()**
**+** **lambda**

In this, we perform the task of filtering strings using filter() and lambda
function. Rest all the functionality is similar to the above method.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Filter Similar Case Strings

# Using islower() + isupper() + filter() + lambda

 

# initializing Matrix

test_list = ["GFG", "Geeks", "best",

 "FOr", "all", "GEEKS"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# islower() and isupper() used to check for cases

# filter() and lambda function used for filtering

res = list(filter(lambda sub : sub.islower() or
sub.isupper(), test_list))

 

# printing result

print("Strings with same case : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [‘GFG’, ‘Geeks’, ‘best’, ‘FOr’, ‘all’, ‘GEEKS’]  
> Strings with same case : [‘GFG’, ‘best’, ‘all’, ‘GEEKS’]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


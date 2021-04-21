Python Program to print element with maximum vowels from a List



Given a list containing string elements, the task is to write a Python program
to print string with maximum vowels.

>  **Input** : test_list = [“gfg”, “best”, “for”, “geeks”]  
> **Output** : geeks  
> **Explanation** : geeks has 2 e’s which is a maximum number of vowels
> compared to other strings.
>
>  **Input** : test_list = [“gfg”, “best”]  
> **Output** : best  
> **Explanation** : best has 1 e which is a maximum number of vowels compared
> to other strings.  
>

**Approach :** _Using_ _loop_

In this, we iterate for all the strings and keep a counter to check number of
vowel in each string. Then, return the string with maximum vowels at end of
the loop.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# initializing Matrix

test_list = ["gfg", "best", "for", "geeks"]

 

# printing original list

print("The original list is : " + str(test_list))

 

res = ""

max_len = 0

for ele in test_list:

 

 # getting maximum length and element

 # iteratively

 vow_len = len([el for el in ele if el in ['a',
'e', 'o', 'u', 'i']])

 if vow_len > max_len:

 max_len = vow_len

 res = ele

 

# printing result

print("Maximum vowels word : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [‘gfg’, ‘best’, ‘for’, ‘geeks’]
>
> Maximum vowels word : geeks

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


Python – Selective consecutive Suffix Join



Given a list of elements, the task is to write a Python program to perform a
join of consecutive strings according to the suffix of each string.

>  **Input** : test_list = [“Geeks-“, “for-“, “Geeks”, “is”, “best-“, “for”,
> “geeks”, suff = ‘-‘  
> **Output** : [‘Geeks-for-Geeks’, ‘is’, ‘best-for’, ‘geeks’]  
> **Explanation** : Strings are joined to next which have “-” as suffix.
>
>  **Input** : test_list = [“Geeks*”, “for*”, “Geeks”, “is”, “best*”, “for”,
> “geeks”, suff = ‘*’  
> **Output** : [‘Geeks*for*Geeks’, ‘is’, ‘best*for’, ‘geeks’]  
> **Explanation** : Strings are joined to next which have “*” as suffix.

**Approach : Using** **loop** **+** **endswith()** **+** **join()**

In this we perform the task of joining using _join()_ and _endswith()_
performs the task of conditional checks for suffix as defined.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Selective consecutive Suffix Join

# Using loop + endswith() + join()

 

# initializing list

test_list = ["Geeks-", "for-", "Geeks", "is",

 "best-", "for", "geeks"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing suffix

suff = '-'

 

res = []

temp = []

for ele in test_list:

 temp.append(ele)

 

 # conditionally test values

 if not ele.endswith(suff):

 res.append(''.join(temp))

 temp = []

if temp:

 res.append(''.join(temp))

 

# printing result

print("The joined result : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [‘Geeks-‘, ‘for-‘, ‘Geeks’, ‘is’, ‘best-‘, ‘for’,
> ‘geeks’]  
> The joined result : [‘Geeks-for-Geeks’, ‘is’, ‘best-for’, ‘geeks’]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


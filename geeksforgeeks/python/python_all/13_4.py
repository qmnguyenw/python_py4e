Python Program to print strings with repetitive occurrence of an element in a
list



Given a strings List, write a Python program that extracts all the strings
with more than one occurrence of a specific value(here described using K) in
elements of a list.

 **Examples:**

>  **Input** : test_list = [“geeksforgeeks”, “best”, “for”, “geeks”], K = ‘e’  
> **Output** : [‘geeksforgeeks’, ‘geeks’]  
> **Explanation** : geeks and geeksforgeeks have 2 and 4 occurrences of K
> respectively.
>
> .  
>  **Input** : test_list = [“geeksforgeeks”, “best”, “for”, “geeks”], K = ‘k’  
> **Output** : [‘geeksforgeeks’]  
> **Explanation** : geeksforgeeks has 2 occurrences of K  
>

**Method 1 :** _Using_ _loop_ _and_ _count()_

  

  

In this, we check for all the occurrence of K in each string using count, and
check if any string has more than 1 occurrence of K and if found extract that
string.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# initializing Matrix

test_list = ["geeksforgeeks", "best", "for", "geeks"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K

K = 'e'

 

res = []

for ele in test_list:

 

 # checking for count greater than 1 (repetitive)

 if ele.count(K) > 1:

 res.append(ele)

 

# printing result

print("Repeated K strings : " + str(res))  
  
---  
  
 __

 __

**Output:**

> The original list is : [‘geeksforgeeks’, ‘best’, ‘for’, ‘geeks’]
>
> Repeated K strings : [‘geeksforgeeks’, ‘geeks’]

 **Method 2 :** _Using_ _list comprehension_ _and_ _count()_

This is short hand solution for this task, similar to above method, just
iteration using is done using list comprehension.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# initializing Matrix

test_list = ["geeksforgeeks", "best", "for", "geeks"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K

K = 'e'

 

# checking for count greater than 1 (repetitive)

# one-liner using list comprehension

res = [ele for ele in test_list if ele.count(K) > 1]

 

# printing result

print("Repeated K strings : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [‘geeksforgeeks’, ‘best’, ‘for’, ‘geeks’]
>
> Repeated K strings : [‘geeksforgeeks’, ‘geeks’]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


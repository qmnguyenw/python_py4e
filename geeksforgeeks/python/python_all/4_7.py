Python – Find all the strings that are substrings to the given list of strings



Given two lists, the task is to write a Python program to extract all the
strings which are possible substring to any of strings in another list.

 **Example:**

>  **Input :** test_list1 = [“Geeksforgeeks”, “best”, “for”, “geeks”],
> test_list2 = [“Geeks”, “win”, “or”, “learn”]
>
>  **Output :** [‘Geeks’, ‘or’]
>
>  **Explanation :** “Geeks” occurs in “Geeksforgeeks string as substring.
>
>  
>
>
>  
>
>
>  **Input :** test_list1 = [“geeksforgeeks”, “best”, “4”, “geeks”],
> test_list2 = [“Geeks”, “win”, “or”, “learn”]
>
>  **Output :** []
>
>  **Explanation :** No substrings found.

 **Method #1 : Using list comprehension**

In this, we perform task of using nested loop and testing using list
comprehension, extracting the string if its part of any substring of other
list.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Substring Intersections

# Using list comprehension

 

# initializing lists

test_list1 = ["Geeksforgeeks", "best", "for", "geeks"]

test_list2 = ["Geeks", "win", "or", "learn"]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# using list comprehension for nested loops

res = list(

 set([ele1 for sub1 in test_list1 for ele1 in test_list2
if ele1 in sub1]))

 

# printing result

print("Substrings Intersections : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list 1 is : [‘Geeksforgeeks’, ‘best’, ‘for’, ‘geeks’]
>
> The original list 2 is : [‘Geeks’, ‘win’, ‘or’, ‘learn’]
>
>  
>
>
>  
>
>
> Substrings Intersections : [‘or’, ‘Geeks’]

 **Method #2 : Using any() + generator expression**

In this, any() is used to check for substring matching in any of the strings
from the string list to be matched in.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Substring Intersections

# Using any() + generator expression

 

# initializing lists

test_list1 = ["Geeksforgeeks", "best", "for", "geeks"]

test_list2 = ["Geeks", "win", "or", "learn"]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# any() returns the string after match in any string

# as Substring

res = [ele2 for ele2 in test_list2 if any(ele2 in ele1
for ele1 in test_list1)]

 

# printing result

print("Substrings Intersections : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list 1 is : [‘Geeksforgeeks’, ‘best’, ‘for’, ‘geeks’]
>
> The original list 2 is : [‘Geeks’, ‘win’, ‘or’, ‘learn’]
>
> Substrings Intersections : [‘Geeks’, ‘or’]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


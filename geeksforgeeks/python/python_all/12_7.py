Python program to count the pairs of reverse strings



Given the String list, write a Python program to count pairs of reverse
strings.

 **Examples:**

>  **Input** : test_list = [“geeks”, “best”, “tseb”, “for”, “skeeg”]  
> **Output** : 2  
> **Explanation** : geeks, skeeg and best, tseb are 2 pairs of reverse strings
> available.
>
>  **Input** : test_list = [“geeks”, “best”, “for”, “skeeg”]  
> **Output** : 1  
> **Explanation** : geeks, skeeg is 1 pair of reverse strings available.

**Method #1 : Using** **reversed()** **\+ loop**

  

  

In this, we perform task of comparing strings to reversed version of it using
reversed() and conditional statements. In this, loop is used for task of
comparing with each string for pairing.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Reversed Pairs in Strings List

# Using reversed() + loop

 

# initializing Matrix

test_list = ["geeks", "best", "tseb", "for",
"skeeg"]

 

# printing original list

print("The original list is : " + str(test_list))

 

res = 0

for idx in range(0, len(test_list)):

 

 # nested loop to check with each element with possible reverse
counterpart

 for idxn in range(idx, len(test_list)):

 if test_list[idxn] ==
str(''.join(list(reversed(test_list[idx])))):

 res += 1

 

# printing result

print("Reversed Pairs : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [‘geeks’, ‘best’, ‘tseb’, ‘for’, ‘skeeg’]  
> Reversed Pairs : 2

 **Method #2 : Using list comprehension +** **sum()**

In this, list comprehension handles nested loop and sum() handles part of
increment counter for counting pairs.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Reversed Pairs in Strings List

# Using list comprehension + sum()

 

# initializing Matrix

test_list = ["geeks", "best", "tseb", "for",
"skeeg"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# list comprehension for nested loop

# sum increments counts

res = sum([1 for idx in range(0, len(test_list))
for idxn in range(idx, len(

 test_list)) if test_list[idxn] ==
str(''.join(list(reversed(test_list[idx]))))])

 

# printing result

print("Reversed Pairs : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [‘geeks’, ‘best’, ‘tseb’, ‘for’, ‘skeeg’]  
> Reversed Pairs : 2

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


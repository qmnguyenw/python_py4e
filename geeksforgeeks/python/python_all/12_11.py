Python Program to Count characters surrounding vowels



Given a String, the task is to write a Python program to count those
characters which have vowels as their neighbors.

 **Examples:**

>  **Input** : test_str = ‘geeksforgeeksforgeeks’  
> **Output** : 10  
> **Explanation** : g, k, f, r, g, k, f, r, g, k have surrounding vowels.
>
>  **Input** : test_str = ‘geeks’  
> **Output** : 2  
> **Explanation** : g, k have surrounding vowels.  
>

**Method 1 :** _Using_ _loop_

  

  

In this, we increment counter while checking previous and successive element
for vowels using loop.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# initializing string

test_str = 'geeksforgeeksforgeeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

res = 0

vow_list = ['a', 'e', 'i', 'o', 'u']

for idx in range(1, len(test_str) - 1):

 

 # checking for preceding and succeeding element to be vowel

 if test_str[idx] not in vow_list and (test_str[idx - 1]
in vow_list or test_str[idx + 1] in vow_list):

 res += 1

 

# solving for 1st and last element

if test_str[0] not in vow_list and test_str[1] in
vow_list:

 res += 1

 

if test_str[-1] not in vow_list and test_str[-2]
in vow_list:

 res += 1

 

# printing result

print("Characters around vowels count : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original string is : geeksforgeeksforgeeks
>
> Characters around vowels count : 10

 **Method 2 :** _Using_ _sum()_ _and_ _list comprehension_

In this, we perform the task of getting count using sum() and iteration and
filtering is done using list comprehension.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# initializing string

test_str = 'geeksforgeeksforgeeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

vow_list = ['a', 'e', 'i', 'o', 'u']

 

# sum() accumulates all vowels surround elements

res = sum([1 for idx in range(1, len(test_str) -
1) if test_str[idx]

 not in vow_list and (test_str[idx - 1] in vow_list or
test_str[idx + 1] in vow_list)])

 

# solving for 1st and last element

if test_str[0] not in vow_list and test_str[1] in
vow_list:

 res += 1

 

if test_str[-1] not in vow_list and test_str[-2]
in vow_list:

 res += 1

 

# printing result

print("Characters around vowels count : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original string is : geeksforgeeksforgeeks
>
> Characters around vowels count : 10

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


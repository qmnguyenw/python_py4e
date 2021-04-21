Python – Formable Strings Count in Matrix



Given Strings Matrix, the task is to write a Python program to count strings
which can be made from letters from given list.

 **Examples:**

>  **Input** : test_list = [[“gfg”, “best”], [“all”, “love”, “gfg”], [“gfg”,
> “is”, “good”], [“geeksforgeeks”]], tar_list = [“g”, “f”, “s”, “b”, “o”, “d”,
> “e”, “t”]  
> **Output** : 5  
> **Explanation** : gfg, best, gfg, gfg, good are strings that can be formed
> from target list chars.  
>
>
> **Input** : test_list = [[“gfg”, “best”], [“all”, “love”, “gfg”], [“gfg”,
> “is”, “good”], [“geeksforgeeks”]], tar_list = [“g”, “f”, “s”, “b”, “d”, “e”,
> “t”]  
> **Output** : 4  
> **Explanation** : gfg, best, gfg, gfg are strings that can be formed from
> target list chars.

**Method #1 : Using loop +** **all()**

  

  

In this, we perform task of iterating through the loop using for loop, all()
is used to check if each element of string has all the letters from target
list. If found, the counter is incremented.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Formable Strings Count in Matrix

# Using loop

 

# initializing list

test_list = [["gfg", "best"], ["all", "love",
"gfg"],

 ["gfg", "is", "good"], ["geeksforgeeks"]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing target list

tar_list = ["g", "f", "s", "b", "o", "d",
"e", "t"]

 

res = 0

for sub in test_list:

 for ele in sub:

 

 # checking for all elements present using all()

 if all(el in tar_list for el in ele):

 res += 1

 

# printing result

print("The computed count : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[‘gfg’, ‘best’], [‘all’, ‘love’, ‘gfg’], [‘gfg’,
> ‘is’, ‘good’], [‘geeksforgeeks’]]  
> The computed count : 5

 **Method #2 : Using** **list comprehension** **+** **all()** **+** **sum()**

In this, problem is solved in one line using list comprehension, all() is used
to check for all characters present and sum() is used to compute number of
strings after strings filteration.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Formable Strings Count in Matrix

# Using list comprehension + all() + sum()

 

# initializing list

test_list = [["gfg", "best"], ["all", "love",
"gfg"],

 ["gfg", "is", "good"], ["geeksforgeeks"]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing target list

tar_list = ["g", "f", "s", "b", "o", "d",
"e", "t"]

 

# computing summation using sum()

# list comprehension used to provide one liner solution

res = sum([sum([1 for ele in sub if all(el in
tar_list for el in ele)])

 for sub in test_list])

 

# printing result

print("The computed count : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[‘gfg’, ‘best’], [‘all’, ‘love’, ‘gfg’], [‘gfg’,
> ‘is’, ‘good’], [‘geeksforgeeks’]]  
> The computed count : 5

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


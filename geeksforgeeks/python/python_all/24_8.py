Python – Disjoint Strings across Lists



Given two lists, extract all the string pairs which are disjoint across i.e.
which don’t have any character in common.

>  **Input** : test_list1 = [“haritha”, “is”, “best”], test_list2 = [“she”,
> “loves”, “papaya”]  
> **Output** : [(‘haritha’, ‘loves’), (‘is’, ‘papaya’), (‘best’, ‘papaya’)]  
> **Explanation** : “is” and “papaya” has no character in common.
>
>  **Input** : test_list1 = [aa, cab], test_list2 = [“a”, “c”]  
> **Output** : []  
> **Explanation** : No pair of disjoint Strings.

**Approach: Using** **set()** **+** **yield** **[ generator ] +** **reduce()**
**+** **recursion**

In this, we perform tasks of getting the disjoint strings using set &
operation and extract dynamically using yield. Each subsequent string is
checked for disjoint using recursion.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Disjoint Strings across Lists

# Using set() + yield [ generator ] + reduce() + recursion

from functools import reduce

 

# helper function

def dis_pairs(dpair, res=[]):

 

 # checking for disjoint pair

 if not dpair and not reduce(lambda a, b: set(a) &
set(b), res):

 yield tuple(res)

 

 # recurring for subsequent pairs

 elif dpair:

 yield from [idx for k in dpair[0] for idx in
dis_pairs(dpair[1:], res + [k])]

 

 

# initializing lists

test_list1 = ["haritha", "is", "best"]

test_list2 = ["she", "loves", "papaya"]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# calling function

res = list(dis_pairs([test_list1, test_list2]))

 

# printing result

print("All possible Disjoint pairs : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list 1 is : [‘haritha’, ‘is’, ‘best’]  
> The original list 2 is : [‘she’, ‘loves’, ‘papaya’]  
> All possible Disjoint pairs : [(‘haritha’, ‘loves’), (‘is’, ‘papaya’),
> (‘best’, ‘papaya’)]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


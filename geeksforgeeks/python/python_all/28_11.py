Python program to concatenate every elements across lists



Given 2 lists, perform concatenations of all strings with each other across
list.

>  **Input** : test_list1 = [“gfg”, “is”, “best”], test_list2 = [“love”, “CS”]  
> **Output** : [‘gfg love’, ‘gfg CS’, ‘is love’, ‘is CS’, ‘best love’, ‘best
> CS’]  
> **Explanation** : All strings are coupled with one another.
>
>  **Input** : test_list1 = [“gfg”, “best”], test_list2 = [“love”, “CS”]  
> **Output** : [‘gfg love’, ‘gfg CS’, ‘best love’, ‘best CS’]  
> **Explanation** : All strings are coupled with one another.  
>

**Method #1 : Using** **list comprehension**

In this, we form pairs with each using list comprehension and then perform
task of concatenation using another list comprehension.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# All elements concatenation across lists

# Using list comprehension

 

# initializing lists

test_list1 = ["gfg", "is", "best"]

test_list2 = ["love", "CS"]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# forming pairs

temp = [(a, b) for a in test_list1 for b in test_list2]

 

# performing concatenation

res = [x + ' ' + y for (x, y) in temp]

 

# printing result 

print("The paired combinations : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list 1 is : [‘gfg’, ‘is’, ‘best’]  
> The original list 2 is : [‘love’, ‘CS’]  
> The paired combinations : [‘gfg love’, ‘gfg CS’, ‘is love’, ‘is CS’, ‘best
> love’, ‘best CS’]

 **Method #2 : Using** **product()** **\+ list comprehension**

In this, we perform task of forming combination using product() and list
comprehension performs task of concatenation.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# All elements concatenation across lists

# Using product() + list comprehension

from itertools import product

 

# initializing lists

test_list1 = ["gfg", "is", "best"]

test_list2 = ["love", "CS"]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# concatenation using formatting and pairing using product

res = ['%s %s' % (ele[0], ele[1]) for ele in
product(test_list1, test_list2)]

 

# printing result 

print("The paired combinations : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list 1 is : [‘gfg’, ‘is’, ‘best’]  
> The original list 2 is : [‘love’, ‘CS’]  
> The paired combinations : [‘gfg love’, ‘gfg CS’, ‘is love’, ‘is CS’, ‘best
> love’, ‘best CS’]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


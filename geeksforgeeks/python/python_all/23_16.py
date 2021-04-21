Python – Sort by Uppercase Frequency



Given a list of strings, perform sorting by frequency of uppercase characters.

> **Input** : test_list = [“Gfg”, “is”, “FoR”, “GEEKS”]  
> **Output** : [‘is’, ‘Gfg’, ‘FoR’, ‘GEEKS’]  
> **Explanation** : 0, 1, 2, 5 uppercase letters in strings respectively.  
>
>
> **Input** : test_list = [“is”, “GEEKS”]  
> **Output** : [‘is’, ‘GEEKS’]  
> **Explanation** : 0, 5 uppercase letters in strings respectively.

**Method #1 : Using sort() + isupper()**

In this, we perform task of checking for uppercase using _isupper()_ , and
_sort()_ to perform task of sorting.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort by Uppercase Frequency

# Using isupper() + sort()

 

 

# helper function

def upper_sort(sub):

 

 # len() to get total uppercase characters

 return len([ele for ele in sub if ele.isupper()])

 

 

# initializing list

test_list = ["Gfg", "is", "BEST", "FoR", "GEEKS"]

 

# printing original list

print("The original list is: " + str(test_list))

 

# using external function to perform sorting

test_list.sort(key=upper_sort)

 

# printing result

print("Elements after uppercase sorting: " + str(test_list))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is: ['Gfg', 'is', 'BEST', 'FoR', 'GEEKS']
    Elements after uppercase sorting: ['is', 'Gfg', 'FoR', 'BEST', 'GEEKS']

 **Method #2 : Using sorted() + lambda function**

In this, we perform the task of sorting using _sorted()_ , and _lambda_
function is used rather than external _sort()_ function to perform task of
sorting.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort by Uppercase Frequency

# Using sorted() + lambda function

 

 

# initializing list

test_list = ["Gfg", "is", "BEST", "FoR", "GEEKS"]

 

# printing original list

print("The original list is: " + str(test_list))

 

# sorted() + lambda function used to solve problem

res = sorted(test_list, key=lambda sub: len(

 [ele for ele in sub if ele.isupper()]))

 

# printing result

print("Elements after uppercase sorting: " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is: ['Gfg', 'is', 'BEST', 'FoR', 'GEEKS']
    Elements after uppercase sorting: ['is', 'Gfg', 'FoR', 'BEST', 'GEEKS']

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


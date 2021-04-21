Python – Sort Strings by Case difference



Given Strings List, the task is to write a Python program to perform sort on
basis of difference of cases i.e count of lower case and upper case.

 **Examples:**

>  **Input** : test_list = [“GFG”, “GeeKs”, “best”, “FOr”, “alL”, “GEEKS”]  
> **Output** : [‘GeeKs’, ‘FOr’, ‘alL’, ‘GFG’, ‘best’, ‘GEEKS’]  
> **Explanation** : ees(3) – GK(2) = 1, hence at 1st index, others are ordered
> accordingly.  
>
>
> **Input** : test_list = [“GFG”, “GeeKs”, “best”]  
> **Output** : [‘GeeKs’, ‘GFG’, ‘best’]  
> **Explanation** : ees(3) – GK(2) = 1, hence at 1st index, others are ordered
> accordingly.

**Method #1 : Using sort() +** **islower()** **+** **isupper()** **+**
**abs()**

  

  

In this inplace sorting is performed using sort(), and islower() and isupper()
is used to check for cases and count. Then abs() is used to get the absolute
difference for providing parameters to perform sort over.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort Strings by Case difference

# Using sort() + islower() + isupper() + abs()

 

 

def get_case_diff(string):

 

 # getting case count and difference

 lower_cnt = len([ele for ele in string if
ele.islower()])

 upper_cnt = len([ele for ele in string if
ele.isupper()])

 return abs(lower_cnt - upper_cnt)

 

 

# initializing Matrix

test_list = ["GFG", "GeeKs", "best", "FOr", "alL",
"GEEKS"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# inplace sort using sort()

test_list.sort(key=get_case_diff)

 

# printing result

print("Sorted Strings by case difference : " + str(test_list))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [‘GFG’, ‘GeeKs’, ‘best’, ‘FOr’, ‘alL’, ‘GEEKS’]  
> Sorted Strings by case difference : [‘GeeKs’, ‘FOr’, ‘alL’, ‘GFG’, ‘best’,
> ‘GEEKS’]

 **Method #2 : Using sorted() + lambda + islower() + len() + isupper() +
abs()**

Similar to above method, difference being way of sorting used, sorted() and
lambda used as a way of injecting functionality.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Python3 code to demonstrate working of

# Sort Strings by Case difference

# Using sorted() + lambda + islower() + len() + isupper() + abs()

 

# initializing Matrix

test_list = ["GFG", "GeeKs", "best", "FOr", "alL",
"GEEKS"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# sorting using sorted()

# lambda function to inject functionality

res = sorted(test_list, key = lambda string : \

 abs(len([ele for ele in string if ele.islower()]) -
\

 len([ele for ele in string if ele.isupper()])))

 

# printing result

print("Sorted Strings by case difference : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [‘GFG’, ‘GeeKs’, ‘best’, ‘FOr’, ‘alL’, ‘GEEKS’]  
> Sorted Strings by case difference : [‘GeeKs’, ‘FOr’, ‘alL’, ‘GFG’, ‘best’,
> ‘GEEKS’]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


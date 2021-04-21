Python – Sort Matrix by None frequency



Given a Matrix, sort according to None elements frequency.

>  **Input** : test_list = [[None, None, 3, None], [12, 4, 5], [None, 3, 4]]  
> **Output** : [[12, 4, 5], [None, 3, 4], [None, None, 3, None]]  
> **Explanation** : 0, 1, 3 counts of None respectively.
>
>  **Input** : test_list = [[None, None, 3, None], [None, 3, 4]]  
> **Output** : [[12, 4, 5], [None, None, 3, None]]  
> **Explanation** : 0, 3 counts of None respectively.

**Method #1 : Using sort()**

In this, we perform sort using sort(), and task of extracting None elements
frequency using external function in each row. This performs inplace sorting.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort Matrix by None frequency

# Using sort()

 

# external sort function

def get_None_freq(row):

 

 # getting length of None characters

 return len([ele for ele in row if not ele])

 

# initializing list

test_list = [[None, None, 4], [None, None, 3,
None],

 [12, 4, 5], [None, 3, 4]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# sorting using sort()

test_list.sort(key = get_None_freq)

 

# printing result 

print("List after sorting : " + str(test_list))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[None, None, 4], [None, None, 3, None], [12, 4, 5],
> [None, 3, 4]]  
> List after sorting : [[12, 4, 5], [None, 3, 4], [None, None, 4], [None,
> None, 3, None]]

 **Method #2 : Using sorted() + lambda**

In this, instead of external function, lambda function is used to solve this
problem. The sorted() is used to perform task of sorting.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort Matrix by None frequency

# Using sorted() + lambda

 

# initializing list

test_list = [[None, None, 4], [None, None, 3,
None],

 [12, 4, 5], [None, 3, 4]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# sorting using sorted()

# lambda function for None frequency logic

res = sorted(test_list, key=lambda row: len([ele for ele
in row if not ele]))

 

# printing result

print("List after sorting : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[None, None, 4], [None, None, 3, None], [12, 4, 5],
> [None, 3, 4]]  
> List after sorting : [[12, 4, 5], [None, 3, 4], [None, None, 4], [None,
> None, 3, None]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


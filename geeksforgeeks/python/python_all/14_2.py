Python – Check alternate peak elements in List



Given a list, the task is to write a Python program to test if it’s alternate,
i.e next and previous elements are either both smaller or larger across the
whole list.

>  **Input** : test_list = [2, 4, 1, 6, 4, 8, 0]  
> **Output** : True  
> **Explanation** : 4, 6, 8 are alternate and peaks (2 1).
>
>  **Input** : test_list = [2, 4, 1, 6, 4, 1, 0]  
> **Output** : False  
> **Explanation** : 1 is not peak ( 4 < 1 < 0).  
>

**Method #1: Using** **loop** **.**

In this, we check for each element for next and previous elements using
conditional if statement to be either smaller or larger, if any variation is
found, the result is flagged false and loop is exited.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test for alternate peak List

# Using loop

 

# initializing list

test_list = [2, 4, 1, 6, 4, 8, 0]

 

# printing original list

print("The original list is : " + str(test_list))

 

res = True

for idx in range(1, len(test_list) - 1):

 

 # breaking if not alternate peaks

 if not ((test_list[idx - 1] < test_list[idx] 

 and test_list[idx + 1] < test_list[idx])

 or (test_list[idx - 1] > test_list[idx] 

 and test_list[idx + 1] > test_list[idx])):

 

 res = False

 

# printing result

print("Is list forming alternate peaks ? : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [2, 4, 1, 6, 4, 8, 0]
    Is list forming alternate peaks ? : True

 **Method #2 : Using** **all()** **+** **generator expression** **.**

In this, we perform the task of checking for all the elements for getting
alternate peaks using all(), and generator expression is used to iterate
through the entire list.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test for alternate peak List

# Using all() + generator expression

 

# initializing list

test_list = [2, 4, 1, 6, 4, 8, 0]

 

# printing original list

print("The original list is : " + str(test_list))

 

# checking for all the elements for alternate peaks 

# one liner solution to problem

res = all(((test_list[idx - 1] < test_list[idx]

 and test_list[idx + 1] < test_list[idx]) 

 or (test_list[idx - 1] > test_list[idx] 

 and test_list[idx + 1] > test_list[idx]))

 for idx in range(1, len(test_list) - 1))

 

# printing result

print("Is list forming alternate peaks ? : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [2, 4, 1, 6, 4, 8, 0]
    Is list forming alternate peaks ? : True

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


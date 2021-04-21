Python – Adjacent elements in List



Given a List extract both next and previous element for each element.

>  **Input** : test_list = [3, 7, 9, 3]  
> **Output** : [(None, 7), (3, 9), (7, 3), (9, None)]  
> **Explanation** : for 7 left element is 3 and right, 9.
>
>  **Input** : test_list = [3, 7, 3]  
> **Output** : [(None, 7), (3, 3), (7, None)]  
> **Explanation** : for 7 left element is 3 and right, 3.

**Method : Using loop**

In this, we iterate for each element and get next and previous element using
element access.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Adjacent elements in List

# Using loop

 

 

# Function to find adjacent

# elements in List

def findAdjacentElements(test_list):

 res = []

 for idx, ele in enumerate(test_list):

 

 # Checking for all cases to append

 if idx == 0:

 res.append((None, test_list[idx + 1]))

 elif idx == len(test_list) - 1:

 res.append((test_list[idx - 1], None))

 else:

 res.append((test_list[idx - 1], test_list[idx + 1]))

 return res

 

 

# Initializing list

input_list = [3, 7, 8, 2, 1, 5, 8, 9,
3]

 

# Printing original list

print("The original list is:", input_list)

 

 

# printing result

print("The Adjacent elements list:", findAdjacentElements(input_list))  
  
---  
  
 __

 __

 **Output:**

> The original list is: [3, 7, 8, 2, 1, 5, 8, 9, 3]  
> The Adjacent elements list: [(None, 7), (3, 8), (7, 2), (8, 1), (2, 5), (1,
> 8), (5, 9), (8, 3), (9, None)]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


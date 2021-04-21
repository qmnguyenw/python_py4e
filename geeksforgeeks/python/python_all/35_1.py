Python program to find all the Combinations in the list with the given
condition



Given a list with some elements being a list of optional elements. The task is
to find all the possible combinations from all options.

 **Examples:**

>  **Input** : test_list = [“geekforgeeks”, [5, 4, 3], “is”, [“best”, “good”,
> “better”]], K = 3  
> **Output** : [[‘geekforgeeks’, 5, ‘is’, ‘best’], [‘geekforgeeks’, 4, ‘is’,
> ‘good’], [‘geekforgeeks’, 3, ‘is’, ‘better’]]  
> **Explanation** : Inner elements picked and paired with similar indices. 5
> -> “best”.
>
>  **Input** : test_list = [“geekforgeeks”, [5, 4], “is”, [“best”, “good”]], K
> = 2  
> **Output** : [[‘geekforgeeks’, 5, ‘is’, ‘best’], [‘geekforgeeks’, 4, ‘is’,
> ‘good’]]  
> **Explanation** : Inner elements picked and paired with similar indices. 5
> -> “best”.  
>

**Method: Using a loop**

  

  

In this, we use a nested loop to get index wise combinations from each nested
option list, and then the outer loop is used to get default values in all
combinations.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Optional Elements Combinations

# Using loop

 

# initializing list

test_list = ["geekforgeeks", [5, 4, 3, 4], "is",


 ["best", "good", "better", "average"]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing size of inner Optional list 

K = 4

 

res = []

cnt = 0

while cnt <= K - 1:

 temp = []

 

 # inner elements selections

 for idx in test_list:

 

 # checks for type of Elements

 if not isinstance(idx, list):

 temp.append(idx)

 else:

 temp.append(idx[cnt])

 cnt += 1

 res.append(temp)

 

# printing result 

print("All index Combinations : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [‘geekforgeeks’, [5, 4, 3, 4], ‘is’, [‘best’, ‘good’,
> ‘better’, ‘average’]]
>
> All index Combinations : [[‘geekforgeeks’, 5, ‘is’, ‘best’],
> [‘geekforgeeks’, 4, ‘is’, ‘good’], [‘geekforgeeks’, 3, ‘is’, ‘better’],
> [‘geekforgeeks’, 4, ‘is’, ‘average’]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


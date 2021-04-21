Python – Consecutive Kth column Difference in Tuple List



Sometimes, while working with Python list, we can have a task in which we need
to work with tuple list and get the absolute difference of it’s Kth index.
This problem has application in web development domain while working with data
informations. Let’s discuss certain ways in which this task can be performed.

 **Examples:**

>  **Input** : test_list = [(5, 4, 2), (1, 3, 4), (5, 7, 8), (7, 4, 3)], K = 0  
> **Output** : [4, 4, 2]  
> **Explanation** : 5 – 1 = 4, hence 4.  
>
>
> **Input** : test_list = [(5, 4, 2), (1, 3, 4), (5, 7, 8), (7, 4, 3)], K = 2  
> **Output** : [2, 4, 5]  
> **Explanation** : 8 – 3 = 5, hence 5.

**Method #1: Using loop**

  

  

In this, for each tuple we subtract and find absolute difference of Kth column
tuples with consecutive tuples in list.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Consecutive Kth column Difference in Tuple List

# Using loop

 

# initializing list

test_list = [(5, 4, 2), (1, 3, 4), (5, 7,
8), (7, 4, 3)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K 

K = 1

 

res = []

for idx in range(0, len(test_list) - 1):

 

 # getting difference using abs()

 res.append(abs(test_list[idx][K] - test_list[idx + 1][K]))

 

# printing result 

print("Resultant tuple list : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [(5, 4, 2), (1, 3, 4), (5, 7, 8), (7, 4, 3)]  
> Resultant tuple list : [1, 4, 3]

 **Method #2 : Using zip() + list comprehension**

In this, we iterate for all the element in list using list comprehension and
compare elements paired using zip().

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Consecutive Kth column Difference in Tuple List

# Using zip() + list comprehension

 

# initializing list

test_list = [(5, 4, 2), (1, 3, 4), (5, 7,
8), (7, 4, 3)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K 

K = 1

 

# zip used to pair each tuple with subsequent tuple

res = [abs(x[K] - y[K]) for x, y in zip(test_list,
test_list[1:])]

 

# printing result 

print("Resultant tuple list : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [(5, 4, 2), (1, 3, 4), (5, 7, 8), (7, 4, 3)]  
> Resultant tuple list : [1, 4, 3]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


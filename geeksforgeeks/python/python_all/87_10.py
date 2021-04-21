Python – Custom Rows Removal depending on Kth Column



Sometimes, while working with Python Matrix, we can have a problem in which we
need to remove elements from Matrix depending on its Kth Column element
present in argument list. This can have application in many domains. Lets
discuss certain ways in which this task can be performed.

 **Method #1 : Using loop**  
This is brute way in which this task can be performed. In this, we iterate
rows of matrix and check for Kth column matching value from list and exclude
from new list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Custom Rows Removal depending on Kth Column

# using loop

 

# Initializing lists

test_list1 = [[3, 4, 5], [2, 6, 8], [1,
10, 2], [5, 7, 9], [10, 1, 2]]

test_list2 = [12, 4, 6]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# Initializing K 

K = 1

 

# Custom Rows Removal depending on Kth Column

# using loop

res = []

for ele in test_list1:

 if ele[K] not in test_list2:

 res.append(ele)

 

# printing result 

print ("The matrix after rows removal is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list 1 is : [[3, 4, 5], [2, 6, 8], [1, 10, 2], [5, 7, 9], [10,
> 1, 2]]  
> The original list 2 is : [12, 4, 6]  
> The matrix after rows removal is : [[1, 10, 2], [5, 7, 9], [10, 1, 2]]

  

  

**Method #2 : Using list comprehension**  
This is yet another way in which this task can be performed. In this, we
perform similar task in shortened format using list comprehension in one line.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Custom Rows Removal depending on Kth Column

# using list comprehension

 

# Initializing lists

test_list1 = [[3, 4, 5], [2, 6, 8], [1,
10, 2], [5, 7, 9], [10, 1, 2]]

test_list2 = [12, 4, 6]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# Initializing K 

K = 1

 

# Custom Rows Removal depending on Kth Column

# using list comprehension

res = [ele for ele in test_list1 if ele[K] not in
test_list2]

 

# printing result 

print ("The matrix after rows removal is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list 1 is : [[3, 4, 5], [2, 6, 8], [1, 10, 2], [5, 7, 9], [10,
> 1, 2]]  
> The original list 2 is : [12, 4, 6]  
> The matrix after rows removal is : [[1, 10, 2], [5, 7, 9], [10, 1, 2]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


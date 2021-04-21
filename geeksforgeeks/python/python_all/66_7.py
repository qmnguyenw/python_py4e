Python – Fill gaps in consecutive Records



Sometimes, while working with Python records, we can have a problem in which
we have consecutive records, but a few missing and needs to be filled with any
constant K. This kind of problem can have application in domains such as web
development. Let’s discuss certain ways in which we need to perform this task.

>  **Input** :  
> test_list = [(1, 4), (9, 11)]  
> K = None  
>  **Output** : [(1, 4), (2, None), (3, None), (4, None), (5, None), (6,
> None), (7, None), (8, None), (9, 11)]
>
>  **Input** :  
> test_list = [(1, 4), (2, 11)]  
> K = None  
>  **Output** : [(1, 4), (2, 11)]

 **Method #1 : Using loop**  
This is one way in which this problem can be solved. In this, we check at each
iteration if the element exists, if no, then it is filled with required value,
if yes, the original value is retained.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Fill gaps in consecutive Records

# Using loop

 

# initializing list

test_list = [(1, 4), (3, 5), (4, 6), (7,
8), (9, 11)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K value

K = "New"

 

# Fill gaps in consecutive Records

# Using loop

res = []

cnt = 0

for i, j in test_list:

 if i - cnt > 1:

 for k in range(cnt + 1, i):

 res.append((k, K))

 res.append((i, j))

 cnt = i

 

# printing result 

print("The list after filling gaps : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

> The original list is : [(1, 4), (3, 5), (4, 6), (7, 8), (9, 11)]  
> The list after filling gaps : [(1, 4), (2, ‘New’), (3, 5), (4, 6), (5,
> ‘New’), (6, ‘New’), (7, 8), (8, ‘New’), (9, 11)]


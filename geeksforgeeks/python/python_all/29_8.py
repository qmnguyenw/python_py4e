Python – Rows with K string in Matrix



Given a matrix, extract row numbers with particular string occurrence.

>  **Input** : test_list = [[“GFG”, “best”, “geeks”], [“geeks”, “rock”],
> [“GFG”, “for”, “CS”], [“Keep”, “learning”]], K = “GFG”  
> **Output** : [0, 2]  
> **Explanation** : 0th index and 2nd index have “GFG” in them as element.
>
>  **Input** : test_list = [[“GFG”, “best”, “geeks”], [“geeks”, “rock”,
> “GFG”], [“GFG”, “for”, “CS”], [“Keep”, “learning”]], K = “GFG”  
> **Output** : [0, 1, 2]  
> **Explanation** : 0th index, 1st index and 2nd index have “GFG” in them as
> element.

**Method #1 : Using loop**

In this, we iterate for each element in Matrix and get the indices of all the
rows which match the K string.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Rows with K string in Matrix

# Using loop

 

# initializing list

test_list = [["GFG", "best", "geeks"], ["geeks",
"rock"],

 ["GFG", "for", "CS"], ["Keep", "learning"]]

 

# printing original list

print("The original list is : ", test_list)

 

# initializing K

K = "GFG"

 

res = []

 

# enumerate() used for getting both index and ele

for idx, ele in enumerate(test_list):

 

 # checking for K String

 if K in ele:

 res.append(idx)

 

# printing result

print("Rows with K : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[‘GFG’, ‘best’, ‘geeks’], [‘geeks’, ‘rock’], [‘GFG’,
> ‘for’, ‘CS’], [‘Keep’, ‘learning’]]  
> Rows with K : [0, 2]

 **Method #2 : Using list comprehension**

This is similar to above method, difference being its a shorthand to solve
problem.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Rows with K string in Matrix

# Using list comprehension

 

# initializing list

test_list = [["GFG", "best", "geeks"], ["geeks",
"rock"],

 ["GFG", "for", "CS"], ["Keep", "learning"]]

 

# printing original list

print("The original list is : ", test_list)

 

# initializing K

K = "GFG"

 

# shorthand to get result

res = [idx for idx, ele in enumerate(test_list) if K in
ele]

 

# printing result

print("Rows with K : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[‘GFG’, ‘best’, ‘geeks’], [‘geeks’, ‘rock’], [‘GFG’,
> ‘for’, ‘CS’], [‘Keep’, ‘learning’]]  
> Rows with K : [0, 2]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


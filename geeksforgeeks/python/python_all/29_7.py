Python Program to Merge a Matrix By the Elements of First Column



Given a Matrix, perform merge on the basis of the element in the first column.

>  **Input** : test_list = [[4, “geeks”], [3, “Gfg”], [4, “CS”], [4, “cs”],
> [3, “best”]]  
> **Output** : [[4, ‘geeks’, ‘CS’, ‘cs’], [3, ‘Gfg’, ‘best’]]  
> **Explanation** : 4 is paired with geeks, CS and cs hence are merged into 1
> row.
>
>  **Input** : test_list = [[4, “geeks”], [3, “Gfg”], [4, “CS”], [5, “cs”],
> [3, “best”]]  
> **Output** : [[4, ‘geeks’, ‘CS’, ‘cs’], [3, ‘Gfg’, ‘best’], [5, ‘cs’]]  
> **Explanation** : 4 is paired with geeks and CS hence are merged into 1 row.  
>

**Method 1 :** Using setdefault() and list comprehension

In this, the task of grouping is done using setdefault(), which assigns key as
first column element and rest of elements as values of list. List
comprehension is used post that to get all the values from dictionary
constructed.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# initializing list

test_list = [[4, "geeks"], [3, "Gfg"], [4, "CS"],


 [4, "cs"], [3, "best"]]

 

# printing original list

print("The original list is : " + str(test_list))

 

res = {}

for key, val in test_list:

 

 # setdefault used to merge similar values

 res.setdefault(key, []).append(val)

 

# getting all values

res = [[key] + val for key, val in res.items()]

 

# printing result

print("Merged Matrix : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[4, ‘geeks’], [3, ‘Gfg’], [4, ‘CS’], [4, ‘cs’], [3,
> ‘best’]]  
> Merged Matrix : [[4, ‘geeks’, ‘CS’, ‘cs’], [3, ‘Gfg’, ‘best’]]

 **Method 2 :** Using values() and setdefault()

Here, we extract the values using values(), rest all the operations are
performed in a similar manner as explained above. This program omits from the
list the first column element based on which grouping was performed.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# initializing list

test_list = [[4, "geeks"], [3, "Gfg"], [4,
"CS"],

 [4, "cs"], [3, "best"]]

 

# printing original list

print("The original list is : " + str(test_list))

 

res = {}

for key, val in test_list:

 

 # setdefault used to merge similar values

 res.setdefault(key, []).append(val)

 

# fetch values using value()

res = list(res.values())

 

# printing result

print("Merged Matrix : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[4, ‘geeks’], [3, ‘Gfg’], [4, ‘CS’], [4, ‘cs’], [3,
> ‘best’]]  
> Merged Matrix : [[‘geeks’, ‘CS’, ‘cs’], [‘Gfg’, ‘best’]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


Python – Surrounding elements to K



Given Matrix, from each row, get surrounding elements of K, if present.

>  **Input** : test_list = [[7, 6, 3, 2], [5, 6], [2, 1], [6, 1, 2]], K = 6  
> **Output** : [[7, 3], [5], [], [1]]  
> **Explanation** : All elements surrounded by 6 are extracted.
>
>  **Input** : test_list = [[7, 6, 3, 2], [5, 6], [2, 1], [6, 1, 2]], K = 1  
> **Output** : [[], [], [2], [6, 2]]  
> **Explanation** : All elements surrounded by 1 are removed.  
>

**Method #1: Using** **index()** **\+ loop +** **try/except**

In this, we check for the index of elements using index(), and then get the
required surrounding elements by accessing next and previous elements. If the
element is not present, an empty list is returned.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Surrounding elements to K

# Using index() + loop + try/except

 

# initializing list

test_list = [[7, 6, 3, 2], [5, 6], [2,
1], [6, 1, 2]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K 

K = 6

 

res = []

for sub in test_list:

 

 # getting index 

 try :

 idx = sub.index(K)

 except Exception as e :

 res.append([])

 continue

 

 # appending Surrounding elements

 if idx != 0 and idx != len(sub) - 1:

 res.append([sub[idx - 1], sub[idx + 1]])

 elif idx == 0:

 res.append([sub[idx + 1]])

 else : res.append([sub[idx - 1]])

 

# printing result 

print("The Surrounding elements : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[7, 6, 3, 2], [5, 6], [2, 1], [6, 1, 2]]  
> The Surrounding elements : [[7, 3], [5], [], [1]]

 **Method #2 : Using index() + in operator + loop**

In this, we check if the element is present in a row before application of
index(), to avoid using try/except block. Rest all functionalities are the
same as the above method.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Surrounding elements to K

# Using index() + in operator + loop

 

# initializing list

test_list = [[7, 6, 3, 2], [5, 6], [2,
1], [6, 1, 2]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K

K = 6

 

res = []

for sub in test_list:

 

 # getting index

 # checking for element presence in row

 if K in sub:

 idx = sub.index(K)

 else:

 res.append([])

 continue

 

 # appending Surrounding elements

 if idx != 0 and idx != len(sub) - 1:

 res.append([sub[idx - 1], sub[idx + 1]])

 elif idx == 0:

 res.append([sub[idx + 1]])

 else:

 res.append([sub[idx - 1]])

 

# printing result

print("The Surrounding elements : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[7, 6, 3, 2], [5, 6], [2, 1], [6, 1, 2]]  
> The Surrounding elements : [[7, 3], [5], [], [1]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


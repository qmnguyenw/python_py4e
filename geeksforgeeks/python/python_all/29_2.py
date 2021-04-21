Python – Filter Tuples Product greater than K



Given a Tuple list, extract all with product greater than K.

>  **Input** : test_list = [(4, 5, 7), (1, 2, 3), (8, 4, 2), (2, 3, 4)], K =
> 50  
> **Output** : [(4, 5, 7), (8, 4, 2)]  
> **Explanation** : 140 and 64 are greater than 50, hence tuples extracted.
>
>  **Input** : test_list = [(4, 5, 7), (1, 2, 3), (8, 4, 2), (2, 3, 4)], K =
> 100  
> **Output** : [(4, 5, 7)]  
> **Explanation** : 140 is greater than 100, hence tuple extracted.

**Method #1 : Using list comprehension**

In this, we extract all the tuples, greater than K product using external
function.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Filter Tuples Product greater than K

# Using list comprehension

 

# getting product

def prod(box):

 res = 1

 for ele in box:

 res *= ele

 return res

 

 

# initializing list

test_list = [(4, 5, 7), (1, 2, 3), (8, 4,
2), (2, 3, 4)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K

K = 50

 

res = [sub for sub in test_list if prod(sub) > K]

 

# printing result

print("Tuples with product greater than K : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [(4, 5, 7), (1, 2, 3), (8, 4, 2), (2, 3, 4)]  
> Tuples with product greater than K : [(4, 5, 7), (8, 4, 2)]

 **Method #2 : Using filter() + lambda**

In this, task of filtering tuples is done using _filter()_ and _lambda_ ,
product is computed in similar way.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Filter Tuples Product greater than K

# Using filter() + lambda

 

# getting product 

def prod(box):

 res = 1

 for ele in box:

 res *= ele 

 return res 

 

# initializing list

test_list = [(4, 5, 7), (1, 2, 3), (8, 4,
2), (2, 3, 4)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K 

K = 50

 

# using filter() to get products greater than K

res = list(filter(lambda sub : prod(sub) > K, test_list))

 

# printing result 

print("Tuples with product greater than K : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [(4, 5, 7), (1, 2, 3), (8, 4, 2), (2, 3, 4)]  
> Tuples with product greater than K : [(4, 5, 7), (8, 4, 2)]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


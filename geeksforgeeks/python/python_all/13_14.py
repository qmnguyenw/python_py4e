Python – Sort rows by Frequency of K



Given a Matrix, the task is to write a Python program to perform sorting on
rows depending on the frequency of K.

>  **Input** : test_list = [[10, 2, 3, 2, 3], [5, 5, 4, 7, 7, 4], [1, 2], [1,
> 1, 2, 2, 2]], K = 2  
> **Output** : [[5, 5, 4, 7, 7, 4], [1, 2], [10, 2, 3, 2, 3], [1, 1, 2, 2, 2]]  
> **Explanation** : 0 < 1 < 2 < 3, count of K in Matrix order.  
>
>
> **Input** : test_list = [[5, 5, 4, 7, 7, 4], [1, 2], [1, 1, 2, 2, 2]], K = 2  
> **Output** : [[5, 5, 4, 7, 7, 4], [1, 2], [1, 1, 2, 2, 2]]  
> **Explanation** : 0 < 1 < 3, count of K in Matrix order.

**Method #1 : Using** **sort()** **+** **count()**

In this, we perform the task of in-place sorting using _sort()_ , capturing
frequency is done using _count()_.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort rows by Frequency of K

# Using sort() + count()

 

 

def get_Kfreq(row):

 

 # return Frequency

 return row.count(K)

 

 

# initializing list

test_list = [[10, 2, 3, 2, 3], [5, 5, 4,
7, 7, 4], [1, 2], [1, 1, 2, 2, 2]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K

K = 2

 

# performing inplace sort

test_list.sort(key=get_Kfreq)

 

# printing result

print("Sorted List : " + str(test_list))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[10, 2, 3, 2, 3], [5, 5, 4, 7, 7, 4], [1, 2], [1, 1,
> 2, 2, 2]]  
> Sorted List : [[5, 5, 4, 7, 7, 4], [1, 2], [10, 2, 3, 2, 3], [1, 1, 2, 2,
> 2]]

 **Method #2 : Using** **sorted()** **+** **lambda** **+** **count()**

In this, we perform the task of sorting using _sorted()_ and _lambda_ ,
eliminates the external function call and _lambda_ function used for
computation.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort rows by Frequency of K

# Using sorted() + lambda + count()

 

# initializing list

test_list = [[10, 2, 3, 2, 3], [5, 5, 4,
7, 7, 4], [1, 2], [1, 1, 2, 2, 2]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K

K = 2

 

# performing inplace sort

res = sorted(test_list, key=lambda row: row.count(K))

 

# printing result

print("Sorted List : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[10, 2, 3, 2, 3], [5, 5, 4, 7, 7, 4], [1, 2], [1, 1,
> 2, 2, 2]]  
> Sorted List : [[5, 5, 4, 7, 7, 4], [1, 2], [10, 2, 3, 2, 3], [1, 1, 2, 2,
> 2]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


Python program to remove rows with duplicate element in Matrix



Given Matrix, remove all rows which have duplicate elements in them.

>  **Input** : test_list = [[4, 3, 2], [7, 6, 7], [2, 4, 4], [8, 9, 9]]  
> **Output** : [[4, 3, 2]]  
> **Explanation** : [4, 3, 2] is the only unique row.
>
>  **Input** : test_list = [[4, 3, 3, 2], [7, 6, 7], [2, 4, 4], [8, 9, 9]]  
> **Output** : []  
> **Explanation** : No unique row.  
>

**Method 1 : Using list comprehension + set() + len()**

In this, we extract only the rows which remain in the same length after
converting it into a set.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# initializing list

test_list = [[4, 3, 2], [7, 6, 7], [2, 4,
5], [8, 9, 9]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# set() removing all elements

# list comprehension used to filter

res = [sub for sub in test_list if len(set(sub))
== len(sub)]

 

# printing result

print("Rows after removal : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [[4, 3, 2], [7, 6, 7], [2, 4, 5], [8, 9, 9]]
    Rows after removal : [[4, 3, 2], [2, 4, 5]]
    
    

**Method #2 : Using filter() + lambda + set() + len()**

In this, we perform the task of filtering using filter() \+ lambda function,
and set and len() are used to check.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# initializing list

test_list = [[4, 3, 2], [7, 6, 7], [2, 4,
5], [8, 9, 9]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# set() removing all elements

# filter() used to filter

res = list(filter(lambda ele: len(set(ele)) ==
len(ele), test_list))

 

# printing result

print("Rows after removal : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [[4, 3, 2], [7, 6, 7], [2, 4, 5], [8, 9, 9]]
    Rows after removal : [[4, 3, 2], [2, 4, 5]]
    
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


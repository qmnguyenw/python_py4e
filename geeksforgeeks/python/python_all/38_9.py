Python – Cross Pairing in Tuple List



Given 2 tuples, perform cross pairing of corresponding tuples, convert to
single tuple if 1st element of both tuple matches.

>  **Input** : test_list1 = [(1, 7), (6, 7), (8, 100), (4, 21)], test_list2 =
> [(1, 3), (2, 1), (9, 7), (2, 17)]  
>  **Output** : [(7, 3)]  
>  **Explanation** : 1 occurs as tuple element at pos. 1 in both tuple, its
> 2nd elements are paired and returned.
>
>  **Input** : test_list1 = [(10, 7), (6, 7), (8, 100), (4, 21)], test_list2 =
> [(1, 3), (2, 1), (9, 7), (2, 17)]  
>  **Output** : []  
>  **Explanation** : NO pairing possible.

 **Method #1 : Using list comprehension**

In this, we check for 1st element using conditional statements and, and
construct new tuple in list comprehension.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Cross Pairing in Tuple List

# Using list comprehension

 

# initializing lists

test_list1 = [(1, 7), (6, 7), (9, 100), (4,
21)]

test_list2 = [(1, 3), (2, 1), (9, 7), (2,
17)]

 

# printing original lists

print("The original list 1 : " + str(test_list1))

print("The original list 2 : " + str(test_list2))

 

# corresponding loop in list comprehension

res = [(sub1[1], sub2[1]) for sub2 in test_list2 for
sub1 in test_list1 if sub1[0] == sub2[0]]

 

# printing result 

print("The mapped tuples : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list 1 : [(1, 7), (6, 7), (9, 100), (4, 21)]
    The original list 2 : [(1, 3), (2, 1), (9, 7), (2, 17)]
    The mapped tuples : [(7, 3), (100, 7)]
    

**Method #2 : Using zip() + list comprehension**

In this, the task of pairing is done using zip() and conditional check is done
inside list comprehension.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Cross Pairing in Tuple List

# Using zip() + list comprehension

 

# initializing lists

test_list1 = [(1, 7), (6, 7), (9, 100), (4,
21)]

test_list2 = [(1, 3), (2, 1), (9, 7), (2,
17)]

 

# printing original lists

print("The original list 1 : " + str(test_list1))

print("The original list 2 : " + str(test_list2))

 

# zip() is used for pairing 

res = [(a[1], b[1]) for a, b in zip(test_list1,
test_list2) if a[0] == b[0]]

 

# printing result 

print("The mapped tuples : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list 1 : [(1, 7), (6, 7), (9, 100), (4, 21)]
    The original list 2 : [(1, 3), (2, 1), (9, 7), (2, 17)]
    The mapped tuples : [(7, 3), (100, 7)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


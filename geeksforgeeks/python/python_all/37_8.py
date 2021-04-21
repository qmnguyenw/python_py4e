Python – Ordered tuples extraction



Given a tuple list, get all the tuples which are sorted in ascending order.

>  **Input** : test_list = [(5, 4, 6, 2, 4), (3, 4, 6), (2, 5, 6), (9, 1)]  
>  **Output** : [(3, 4, 6), (2, 5, 6)]  
>  **Explanation** : Sorted tuples are extracted.
>
>  **Input** : test_list = [(5, 4, 6, 2, 4), (3, 4, 1), (2, 5, 4), (9, 1)]  
>  **Output** : []  
>  **Explanation** : No Sorted tuples.

 **Method #1 : Using list comprehension + sorted()**

In this, we check if tuple is ordered using sorted(), and list comprehension
is used to iterate for each tuple.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Ordered tuples extraction

# Using list comprehension + sorted()

 

# initializing list

test_list = [(5, 4, 6, 2, 4), (3, 4, 6),
(9, 10, 34), (2, 5, 6), (9, 1)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# sorted() used to order, comparison operator to test 

res = [sub for sub in test_list if tuple(sorted(sub))
== sub]

 

# printing result 

print("Ordered Tuples : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [(5, 4, 6, 2, 4), (3, 4, 6), (9, 10, 34), (2, 5, 6), (9, 1)]
    Ordered Tuples : [(3, 4, 6), (9, 10, 34), (2, 5, 6)]
    

**Method #2 : Using filter() + lambda + sorted()**

In this, the task of filtering is done using filter(), sorted() fed to lambda
for with comparison to get required result.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Ordered tuples extraction

# Using filter() + lambda + sorted()

 

# initializing list

test_list = [(5, 4, 6, 2, 4), (3, 4, 6),
(9, 10, 34), (2, 5, 6), (9, 1)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# sorted() used to order, comparison operator to test 

res = list(filter(lambda sub: tuple(sorted(sub))
== sub, test_list))

 

# printing result 

print("Ordered Tuples : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [(5, 4, 6, 2, 4), (3, 4, 6), (9, 10, 34), (2, 5, 6), (9, 1)]
    Ordered Tuples : [(3, 4, 6), (9, 10, 34), (2, 5, 6)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


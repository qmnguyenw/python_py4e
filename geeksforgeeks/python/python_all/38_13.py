Python – Filter unique valued tuples



Given a Tuple list, filter tuples that don’t contain duplicates.

>  **Input** : test_list = [(3, 5, 6, 7), (3, 2, 4, 3), (9, 4, 9), (2, 3, 2)]  
>  **Output** : [(3, 5, 6, 7)]  
>  **Explanation** : Rest all tuples have duplicate values.
>
>  **Input** : test_list = [(3, 5, 6, 7, 7), (3, 2, 4, 3), (9, 4, 9), (2, 3,
> 2)]  
>  **Output** : []  
>  **Explanation** : All tuples have duplicate values.

 **Method #1 : Using loop + set()**

In this, all the tuples are iterated, and duplicacy test is done using set(),
if length of set is same as tuple, it does’nt contain duplicate.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Filter unique valued tuples

# Using loop + set()

 

# initializing list

test_list = [(3, 5, 6, 7), (3, 2, 4, 3),
(9, 4), (2, 3, 2)]

 

# printing original list

print("The original list is : " + str(test_list))

 

res = []

 

for sub in test_list:

 

 # checking lengths to be equal

 if len(set(sub)) == len(sub):

 res.append(sub)

 

# printing results

print("Filtered tuples : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [(3, 5, 6, 7), (3, 2, 4, 3), (9, 4), (2, 3, 2)]
    Filtered tuples : [(3, 5, 6, 7), (9, 4)]
    

**Method #2 : Using list comprehension**

This performs similar task as above, difference being that this is one liner
and compact.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Filter unique valued tuples

# Using list comprehension

 

# initializing list

test_list = [(3, 5, 6, 7), (3, 2, 4, 3),
(9, 4), (2, 3, 2)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# list comprehension used to filter

res = [sub for sub in test_list if len(set(sub))
== len(sub)]

 

# printing results

print("Filtered tuples : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [(3, 5, 6, 7), (3, 2, 4, 3), (9, 4), (2, 3, 2)]
    Filtered tuples : [(3, 5, 6, 7), (9, 4)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


Python | Remove similar element rows in tuple Matrix



Sometimes, while working with data, we can have a problem in which we need to
remove elements from tuple matrix on a condition that if all elements in row
of tuple matrix is same. Let’s discuss certain ways in which this task can be
performed.

 **Method #1 : Using list comprehension +all()**  
This task can be performed using combination of above functions. In this, we
traverse all rows using list comprehension and remove all elements that match
the initial element in row’s column with help of all().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove similar element rows in tuple Matrix

# using list comprehension + all()

 

# initialize tuple

test_tup = ((1, 3, 5), (2, 2, 2),

 (9, 10, 10), (4, 4, 4))

 

# printing original tuple

print("The original tuple : " + str(test_tup))

 

# Remove similar element rows in tuple Matrix

# using list comprehension + all()

res = tuple(ele for ele in test_tup if not all(sub
== ele[0] for sub in ele))

 

# printing result

print("The tuple after removal of like-element rows : " +
str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple : ((1, 3, 5), (2, 2, 2), (9, 10, 10), (4, 4, 4))
    The tuple after removal of like-element rows : ((1, 3, 5), (9, 10, 10))
    

**Method #2 : Usingset() \+ generator expression**  
This task can also be performed using the given functionalities. In this, we
just check for length of reduced row using set() to be greater than 1. If yes,
we know that it is the target row to be removed.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove similar element rows in tuple Matrix

# using set() + generator expression

 

# initialize tuple

test_tup = ((1, 3, 5), (2, 2, 2), 

 (9, 10, 10), (4, 4, 4))

 

# printing original tuple

print("The original tuple : " + str(test_tup))

 

# Remove similar element rows in tuple Matrix

# using set() + generator expression

res = tuple(ele for ele in test_tup if len(set(ele))
> 1)

 

# printing result

print("The tuple after removal of like-element rows : " +
str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple : ((1, 3, 5), (2, 2, 2), (9, 10, 10), (4, 4, 4))
    The tuple after removal of like-element rows : ((1, 3, 5), (9, 10, 10))
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


Python | Filter tuples according to list element presence



Sometimes, while working with records, we can have a problem in which we have
to filter all the tuples from a list of tuples, which contains atleast one
element from a list. This can have application in many domains working with
data. Let’s discuss certain ways in which this task can be performed.

 **Method #1 : Using list comprehension**  
Using list comprehension is brute force method to perform this task in a
shorthand. In this, we just check for each tuple and check if it contains any
element from the target list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Filter tuples according to list element presence

# using list comprehension

 

# initialize list of tuple

test_list = [(1, 4, 6), (5, 8), (2, 9),
(1, 10)]

 

# initialize target list 

tar_list = [6, 10]

 

# printing original tuples list

print("The original list : " + str(test_list))

 

# Filter tuples according to list element presence

# using list comprehension

res = [tup for tup in test_list if any(i in tup for
i in tar_list)]

 

# printing result

print("Filtered tuple from list are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [(1, 4, 6), (5, 8), (2, 9), (1, 10)]
    Filtered tuple from list are : [(1, 4, 6), (1, 10)]
    

**Method #2 : Usingset() \+ list comprehension**  
Above approach can be optimized by converting the containers to a set()
reducing duplicates and performing a & operation to fetch the desired records.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Filter tuples according to list element presence

# using set() + list comprehension

 

# initialize list of tuple

test_list = [(1, 4, 6), (5, 8), (2, 9),
(1, 10)]

 

# initialize target list 

tar_list = [6, 10]

 

# printing original tuples list

print("The original list : " + str(test_list))

 

# Filter tuples according to list element presence

# using set() + list comprehension

res = [tup for tup in test_list if (set(tar_list) &
set(tup))]

 

# printing result

print("Filtered tuple from list are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [(1, 4, 6), (5, 8), (2, 9), (1, 10)]
    Filtered tuple from list are : [(1, 4, 6), (1, 10)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


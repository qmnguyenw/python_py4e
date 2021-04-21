Python – Flag None Element Rows in Matrix



Given a Matrix, return True for rows which contain a None Value, else return
False.

>  **Input** : test_list = [[2, 4, None, 3], [3, 4, 1, None], [2, 4, 7, 4],
> [2, 8, None]]  
>  **Output** : [True, True, False, True]  
>  **Explanation** : 1, 2 and 4th index contain None occurrence.
>
>  **Input** : test_list = [[2, 4, None, 3], [3, 4, 1, None], [2, 4, None, 4],
> [2, 8, None]]  
>  **Output** : [True, True, True, True]  
>  **Explanation** : All rows have None.

 **Method #1 : Using List comprehension**

In this, we iterate for each row and use in operator to check for None in
these. If found, True is returned, else False is returned.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Flag None Element Rows in Matrix

# Using list comprehension

 

# initializing list

test_list = [[2, 4, None, 3], [3, 4, 1,
None], [2, 4, 7, 4], [2, 8]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# in operator to check None value 

# True if any None is found 

res = [True if None in sub else False for sub in
test_list]

 

# printing result 

print("None Flagged List : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [[2, 4, None, 3], [3, 4, 1, None], [2, 4, 7, 4], [2, 8]]
    None Flagged List : [True, True, False, False]
    

**Method #2 : Using all() + list comprehension**

In this, we check for all values to be True using all(), if yes, its not
flagged True and list comprehension is used to check for each row.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Flag None Element Rows in Matrix

# Using all() + list comprehension

 

# initializing list

test_list = [[2, 4, None, 3], [3, 4, 1,
None], [2, 4, 7, 4], [2, 8]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# all() checks for all non none values 

res = [False if all(sub) else True for sub in
test_list]

 

# printing result 

print("None Flagged List : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [[2, 4, None, 3], [3, 4, 1, None], [2, 4, 7, 4], [2, 8]]
    None Flagged List : [True, True, False, False]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


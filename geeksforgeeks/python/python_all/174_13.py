Python program to create a list of tuples from given list having number and
its cube in each tuple



Given a list of numbers of list, write a Python program to create a list of
tuples having first element as the number and second element as the cube of
the number.

 **Example:**

    
    
    Input: list = [1, 2, 3]
    Output: [(1, 1), (2, 8), (3, 27)]
    
    Input: list = [9, 5, 6]
    Output: [(9, 729), (5, 125), (6, 216)]

We can use list comprehension to create a list of tuples. The first element
will be simply an element and second element will be cube of that number.

Below is the Python implementation:

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to create a list of tuples

# from given list having number and

# its cube in each tuple

 

# creating a list

list1 = [1, 2, 5, 6]

 

# using list comprehension to iterate each

# values in list and create a tuple as specified

res = [(val, pow(val, 3)) for val in list1]

 

# print the result

print(res)  
  
---  
  
 __

 __

 **Output:**

    
    
    [(1, 1), (2, 8), (5, 125), (6, 216)]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


Python | Remove particular element from tuple list



Since the advent of popularity of Python in data analysis, we have list of
tuples as a container in many of our problems. Sometimes, while data
preprocessing, we might have a problem in which we need to completely remove a
particular element from a list of tuple. Let’s discuss a way in which this
task can be performed.

 **Method : Using list comprehension**  
This task can be used using brute force manner using loop, but a better
alternative shorthand would be an approach which could perform this task in
one line. List comprehension can help us achieve it and hence it’s recommended
to use this method to perform this task. This just checks for element and
removes if it’s the selected element.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove particular element from tuple list

# using list comprehension

 

# initialize list

test_list = [(5, 6, 7), (7, 2, 4, 6), (6,
6, 7), (6, 10, 8)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# declaring remove element

N = 6

 

# Remove particular element from tuple list

# using list comprehension

res = [tuple(ele for ele in sub if ele != N) for
sub in test_list]

 

# printing result

print("The Tuple List after removal of element : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [(5, 6, 7), (7, 2, 4, 6), (6, 6, 7), (6, 10, 8)]
    The Tuple List after removal of element : [(5, 7), (7, 2, 4), (7, ), (10, 8)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


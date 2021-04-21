Python | Maximum Sum Sublist



We can have an application for finding the lists with the maximum value and
print it. This seems quite an easy task and may also be easy to code, but
having shorthands to perform the same are always helpful as this kind of
problem can come in web development.

 **Method #1 : Usingreduce() \+ lambda**  
The above two functions can help us achieve this particular task. The lambda
function does the task of logic and iteration and reduce function does the
task of returning the required result. Works in Python 2 only.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# maximum sum sublist 

# using reduce() + lambda

 

# importing functools for reduce()

import functools

 

# initializing matrix 

test_matrix = [[1, 3, 1], [4, 5, 3], [1,
2, 4]]

 

# printing the original matrix

print ("The original matrix is : " + str(test_matrix))

 

# using reduce() + lambda

# maximum sum sublist 

res = functools.reduce(lambda i, j: i if sum(i) >
sum(j) 

 else j, test_matrix)

 

# printing result

print ("Maximum sum sublist is : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original matrix is : [[1, 3, 1], [4, 5, 3], [1, 2, 4]]
    Maximum sum sublist is : [4, 5, 3]
    

**Method #2 : Usingmax() \+ key**  
The max function can get the maximum of all the list and key is used to
specify on what the max condition has to be applied that is summation in this
case.  

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# maximum sum sublist 

# using max() + key

 

# initializing matrix 

test_matrix = [[1, 3, 1], [4, 5, 3], [1,
2, 4]]

 

# printing the original matrix

print ("The original matrix is : " + str(test_matrix))

 

# using max() + key

# maximum sum sublist 

res = max(test_matrix, key = sum)

 

# printing result

print ("Maximum sum sublist is : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original matrix is : [[1, 3, 1], [4, 5, 3], [1, 2, 4]]
    Maximum sum sublist is : [4, 5, 3]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


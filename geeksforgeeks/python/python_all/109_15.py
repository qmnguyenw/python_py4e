Python – Row with Minimum Sum in Matrix



We can have an application for finding the lists with the minimum value and
print it. This seems quite an easy task and may also be easy to code, but
having shorthands to perform the same are always helpful as this kind of
problem can come in web development.

 **Method #1 : Usingreduce() \+ lambda**  
The above two function can help us achieving this particular task. The lambda
function does the task of logic and iteration and reduce function does the
task of returning the required result. Works in python 2 only.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# Minimum Sum row in Matrix

# using reduce() + lambda

 

# initializing matrix 

test_matrix = [[1, 3, 1], [4, 5, 3], [1,
2, 4]]

 

# printing the original matrix

print ("The original matrix is : " + str(test_matrix))

 

# using reduce() + lambda

# Minimum Sum row in Matrix

res = reduce(lambda i, j: i if sum(i) < sum(j) else
j, test_matrix)

 

# printing result

print ("Minimum sum row is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original matrix is : [[1, 3, 1], [4, 5, 3], [1, 2, 4]]
    Minimum sum row is : [1, 3, 1]
    

**Method #2 : Usingmin() \+ key**  
The min function can get the minimum of all the list and key is used to
specify on what the min condition has to be applied that is summation in this
case.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Minimum Sum row in Matrix

# using min() + key

 

# initializing matrix 

test_matrix = [[1, 3, 1], [4, 5, 3], [1,
2, 4]]

 

# printing the original matrix

print ("The original matrix is : " + str(test_matrix))

 

# using min() + key

# Minimum Sum row in Matrix

res = min(test_matrix, key = sum)

 

# printing result

print ("Minimum sum row is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original matrix is : [[1, 3, 1], [4, 5, 3], [1, 2, 4]]
    Minimum sum row is : [1, 3, 1]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


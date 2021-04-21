Python | Row with Minimum element in Matrix



We can have an application for finding the lists with the minimum value and
print it. This seems quite an easy task and may also be easy to code, but
sometimes we need to print the entire row containing it and having shorthands
to perform the same are always helpful as this kind of problem can come in web
development. Let’s discuss certain ways in which this task can be performed.

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

# Row with Minimum element in Matrix

# using reduce() + lambda

 

# initializing matrix 

test_matrix = [[1, 3, 1], [4, 5, 3], [7,
2, 4]]

 

# printing the original matrix

print ("The original matrix is : " + str(test_matrix))

 

# using reduce() + lambda

# Row with Minimum element in Matrix

res = reduce(lambda i, j: i if min(i) < min(j) else
j, test_matrix)

 

# printing result

print ("Minimum element sublist is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original matrix is : [[1, 3, 1], [4, 5, 3], [7, 2, 4]]
    Minimum element sublist is : [1, 3, 1]
    

**Method #2 : Usingmin() \+ key**  
The min function can get the minimum of all the list and key is used to
specify on what the min condition has to be applied that is on rows in this
case.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Row with Minimum element in Matrix

# using min() + key

 

# initializing matrix 

test_matrix = [[1, 3, 1], [4, 5, 3], [7,
2, 4]]

 

# printing the original matrix

print ("The original matrix is : " + str(test_matrix))

 

# using min() + key

# Row with Minimum element in Matrix 

res = min(test_matrix, key = min)

 

# printing result

print ("Minimum element sublist is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original matrix is : [[1, 3, 1], [4, 5, 3], [7, 2, 4]]
    Minimum element sublist is : [1, 3, 1]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


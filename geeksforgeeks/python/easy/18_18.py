Nested List Comprehensions in Python



List Comprehensions are one of the most amazing features of Python. It is a
smart and concise way of creating lists by iterating over an iterable object.
Nested List Comprehensions are nothing but a list comprehension within another
list comprehension which is quite similar to nested for loops.

Let’s take a look at some examples to understand what nested list
comprehensions can do:

 **Example 1:**

    
    
    I want to create a matrix which looks like below:
    
    matrix = [[0, 1, 2, 3, 4],
              [0, 1, 2, 3, 4],
              [0, 1, 2, 3, 4],
              [0, 1, 2, 3, 4],
              [0, 1, 2, 3, 4]]
    

The below code uses nested for loops for the given task:

 __

 __  
 __

 __

 __  
 __  
 __

matrix= []

 

for i in range(5):

 

 # Append an empty sublist inside the list

 matrix.append([])

 

 for j in range(5):

 matrix[i].append(j)

 

print(matrix)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]
    


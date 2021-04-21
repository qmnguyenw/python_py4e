Python program to add two matrices



 **Prerequisite :** Arrays in Python, Loops, List Comprehension

Program to compute the sum of two matrices and then print it in Python. We can
perform matrix addition in various ways in Python. Here are a two of them.  
Examples:

    
    
    Input :
     X= [[1,2,3],
        [4 ,5,6],
        [7 ,8,9]]
     
    Y = [[9,8,7],
        [6,5,4],
        [3,2,1]]
     
    Output :
     result= [[10,10,10],
             [10,10,10],
             [10,10,10]]
    
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Using NestedLoops**

 __

 __  
 __

 __

 __  
 __  
 __

# Program to add two matrices using nested loop

 

X = [[1,2,3],

 [4 ,5,6],

 [7 ,8,9]]

 

Y = [[9,8,7],

 [6,5,4],

 [3,2,1]]

 

 

result = [[0,0,0],

 [0,0,0],

 [0,0,0]]

 

# iterate through rows

for i in range(len(X)):

 

 # iterate through columns

 for j in range(len(X[0])):

 result[i][j] = X[i][j] + Y[i][j]

 

for r in result:

 print(r)  
  
---  
  
 __

 __

Output:

  

  

    
    
    [10, 10, 10]
    [10, 10, 10]
    [10, 10, 10]
    

**Explanation :-**  
In this program we have used nested for loops to iterate through each row and
each column. At each point we add the corresponding elements in the two
matrices and store it in the result.

 **Using nestedlist comprehension**

Here is another approach for addition of two matrix addition using nested list
comprehension.

 __

 __  
 __

 __

 __  
 __  
 __

# Program to add two matrices

# using list comprehension

 

X = [[1,2,3],

 [4 ,5,6],

 [7 ,8,9]]

 

Y = [[9,8,7],

 [6,5,4],

 [3,2,1]]

 

result = [[X[i][j] + Y[i][j] for j in
range(len(X[0]))] for i in range(len(X))]

 

for r in result:

 print(r)  
  
---  
  
 __

 __

Output:

    
    
    [10, 10, 10]
    [10, 10, 10]
    [10, 10, 10]
    

**Explanation :-** The output of this program is the same as above. We have
used nested list comprehension to iterate through each element in the matrix.  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


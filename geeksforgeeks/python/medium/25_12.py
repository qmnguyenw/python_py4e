Python program to add two Matrices



Aim : Program to compute the sum of two matrices and then print it in Python.  
Examples:

    
    
    **Input :**
     X= [[1,2,3],
        [4 ,5,6],
        [7 ,8,9]]
     
    Y = [[9,8,7],
        [6,5,4],
        [3,2,1]]
     
    **Output :**
     result= [[10,10,10],
             [10,10,10],
             [10,10,10]]

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **We can perform matrix addition in following ways in Python.**

  1. **Using** **for loop** **:**

## Python

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

 **Output:**

    
    
    [10, 10, 10]
    [10, 10, 10]
    [10, 10, 10]

 _ **Time Complexity:** O(len(X) * len(X[0]))_

 _ **Auxiliary Space:**_ O(len(X) * len(X[0]))

 **Another Approach:**

  

  

  1.  **Explanation :-**  
In this program we have used nested for loops to iterate through each row and
each column. At each point we add the corresponding elements in the two
matrices and store it in the result.

  2.  **Using nested** **list comprehension** **:** In Python, we can implement a matrix as nested list (list inside a list). We can treat each element as a row of the matrix.   

## Python

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

result = [[X[i][j] + Y[i][j] for j in range

(len(X[0]))] for i in range(len(X))]

 

for r in result:

 print(r)  
  
---  
  
 __

 __

 **Output:**

    
    
    [10, 10, 10]
    [10, 10, 10]
    [10, 10, 10]

 **Another Approach:**

  1.  **Explanation :-**  
The output of this program is the same as above. We have used nested list
comprehension to iterate through each element in the matrix. List
comprehension allows us to write concise codes and we must try to use them
frequently in Python. They are very helpful.

  2.  **Using** **zip()** **and sum**

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Program to add two matrices

# using zip()

 

X = [[1,2,3],

 [4 ,5,6],

 [7 ,8,9]]

 

Y = [[9,8,7],

 [6,5,4],

 [3,2,1]]

result = [map(sum, zip(*t)) for t in zip(X,
Y)]

 

print(result)  
  
---  
  
 __

 __

 **Output:**

    
    
    [[10, 10, 10], [10, 10, 10], [10, 10, 10]]

 **Explanation :-**  
The zip function accepts iterator i of each element(list) of matrix, mapping
them, adding them using sum() and storing them in the map form.

This article is contributed by **ajay0007**. If you like GeeksforGeeks and
would like to contribute, you can also write an article using
contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.  
Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above..

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


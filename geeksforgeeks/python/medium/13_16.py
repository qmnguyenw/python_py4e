Data Science – Solving Linear Equations



 **Prerequisite:** Introduction to Data Science : Skills Required

Linear Algebra is a very fundamental part of Data Science. When one talks
about Data Science, data representation becomes an important aspect of Data
Science. Data is represented usually in a matrix form. The second important
thing in the perspective of Data Science is if this data contains several
variables of interest, then one is interested to know how many of these are
very important. And if there are relationships between these variables, then
how can one uncover these relationships. Linear algebraic tools allow us to
understand these data. So, a Data Science enthusiast needs to have a good
understanding of this concept before going to understand complex machine
learning algorithms.

 **Matrices and Linear Algebra**  
There are many ways to represent the data, matrices provide you with a
convenient way to organize these data.

  * Matrices can be used to represent samples with multiple attributes in a compact form
  * Matrices can also be used to represent linear equations in a compact and simple fashion
  * Linear algebra provides tools to understand and manipulate matrices to derive useful knowledge from data

 **Identification of Linear Relationships Among Attributes**  
We identify the linear relationship between attributes using the concept of
null space and nullity. Before proceeding further, go through Null Space and
Nullity of a Matrix.

 **Preliminaries**

  

  

    
    
    Generalized linear equations are represented as below:
    ![Ax = b](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-d4621016bc066a79daf20009d8052fdd_l3.png)
    ![A \(m * n\); x \(n * 1\); b \(m * 1\)](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-376bc40cc4c6ce7062f1061d5f8ffc46_l3.png)
    **m** and **n** are the number of equations and variables respectively
    **b** is the general RHS commonly used
    

In general there are three cases one need to understand:  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190902174222/Categorization.jpg)

We will consider these three cases independently.

 **Full row rank and full column rank**  
For a matrix A (m x n)Full Row Rank| Full Column Rank| When all the rows of
the matrix are linearly independent| When all the columns of the matrix are
linearly independent| Data sampling does not present a linear relationship –
samples are independent| Attributes are linearly independent  
---|---  
  
 **Note:** In general whatever be the size of the matrix it is established
that row rank is always equal to the column rank. It means for any size of the
matrix if we have certain number of independent rows, we will have those many
numbers of independent column.  
In general case if we have a matrix _**m x n**_ and _**m**_ is smaller than
_**n**_ then the maximum rank of the matrix can only be **m**. So, maximum
rank is always the less of the two numbers _**m**_ and **n**.

 **Case 1: m = n**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190902181707/case-11.jpg)  
 **Example 1.1:**

    
    
    Consider the given matrix equation:
    
    
     (1)    ![ \\begin{equation*} \\begin{bmatrix} 1&3\\\\ 2&4\\\\ \\end{bmatrix} % \\begin{bmatrix} x_1\\\\ x_2\\\\ \\end{bmatrix} = \\begin{bmatrix} 7\\\\ 10\\\\ \\end{bmatrix} \\end{equation*} ](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-0a734f36144ee34e0a4d69abc2943dff_l3.png)
    
    
    | **A** | is not equal to zero
    rank( **A** ) = 2 = no. of columns
    
    This implies that A is full rank
    ![ \\begin{bmatrix} x_1\\\\ x_2\\\\ \\end{bmatrix} = \\begin{bmatrix} 1&3\\\\ 2&4\\\\ \\end{bmatrix}^{-1} % \\begin{bmatrix} 7\\\\ 10\\\\ \\end{bmatrix} = \\begin{bmatrix} -2&1.5\\\\ 1&-0.5\\\\ \\end{bmatrix} % \\begin{bmatrix} 7\\\\ 10\\\\ \\end{bmatrix} = \\begin{bmatrix} 1\\\\ 2\\\\ \\end{bmatrix} ](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-47f045f7d4965ffd9fbf94f011711402_l3.png)
    Therefore, the solution for the given example is ![\(x_1, x_2\) = \(1, 2\)](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-73992e433fd2e447be871d39c88be117_l3.png)    
    

**Program to find rank and inverse of a matrix and solve the matrix equation
in Python:**

 __

 __  
 __

 __

 __  
 __  
 __

# First, import

# matrix_rank from numpy.linalg

from numpy.linalg import matrix_rank, inv, solve

 

# A 2 x 2 matrix

A = [[1, 3], 

 [2, 4]]

b = [7, 10]

 

# Rank of matrix A

print("Rank of the matrix is:", matrix_rank(A))

 

# Inverse of matrix A

print("\nInverse of A:\n", inv(A))

 

# Matrix equation solution

print("Solution of linear equations:", solve(A, b))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    Rank of the matrix is: 2
    
    Inverse of A:
     [[-2.   1.5]
     [ 1.  -0.5]]
    
    Solution of linear equation: [ 1.  2.]
    

You can refer Numpy | Linear Algebra article for various operations on matrix
and to solve linear equations in Python.  
 **Example 1.2:**

    
    
    Consider the given matrix equation:
    
    
     (2)    ![ \\begin{equation*} \\begin{bmatrix} 1&2\\\\ 2&4\\\\ \\end{bmatrix} % \\begin{bmatrix} x_1\\\\ x_2\\\\ \\end{bmatrix} = \\begin{bmatrix} 5\\\\ 10\\\\ \\end{bmatrix} \\end{equation*} ](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-d078d7e79e4279a96d52f2d8d4272096_l3.png)
    
    
    | **A** | is not equal to zero
    rank( **A** ) = 1
    nullity = 1
    Checking consistency
    
    ![ \\begin{bmatrix} x_1 + 2x_2\\\\ 2x_1 + 4x_2\\\\ \\end{bmatrix} = \\begin{bmatrix} 5\\\\ 10\\\\ \\end{bmatrix} ](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-93b01ba9959540e481471479da322ca4_l3.png)
    
    Row (2) = 2 Row (1)
    
    The equations are consistent with only one linearly independent equation
    The solution set for (![x_1](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-e214fae67ebe8130acc9b7b225c7745e_l3.png), ![x_2](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-655dbb321cd8c5c5bc16b586699178fa_l3.png)) is infinite because we have only
    one linearly independent equation and two variables    
    

**Explanation:** In the above example we have only one linearly independent
equation i.e. ![x_1+2x_2 = 5](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-cc7ba67315dba06e50305923a2f24f49_l3.png). So, if we take
![x_2 = 0](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-a68b0a290e0065767173e9d24bc4bb93_l3.png), then we have
![x_1 = 5](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-25d09244be3fd7cadde79b9f139479b2_l3.png); if we take
![x_2 = 1](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-1c1e3ddec7ddfc9e8d94be25bddacd18_l3.png), then we have
![x_1 = 3](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-4d6417cc9afd1c19cc2d1f3596149867_l3.png). In the similar
fashion we can have many solutions to this equation. We can take any value of
![x_2](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-655dbb321cd8c5c5bc16b586699178fa_l3.png) ( we have
infinite choices for ![x_2](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-655dbb321cd8c5c5bc16b586699178fa_l3.png)) and
corespondingly for each value of ![x_2](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-655dbb321cd8c5c5bc16b586699178fa_l3.png) we
will get one ![x_1](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-e214fae67ebe8130acc9b7b225c7745e_l3.png). Hence, we can
say that this equation has infinite solutions.

 **Example 1.3:**

    
    
    Consider the given matrix equation:
    
    
     (3)    ![ \\begin{equation*} \\begin{bmatrix} 1&2\\\\ 2&4\\\\ \\end{bmatrix} % \\begin{bmatrix} x_1\\\\ x_2\\\\ \\end{bmatrix} = \\begin{bmatrix} 5\\\\ 9\\\\ \\end{bmatrix} \\end{equation*} ](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-9dae2ed20c57357e3972bd03780a8d76_l3.png)
    
    
    | **A** | is not equal to zero
    rank( **A** ) = 1
    nullity = 1
    Checking consistency
    
    ![ \\begin{bmatrix} x_1 + 2x_2\\\\ 2x_1 + 4x_2\\\\ \\end{bmatrix} = \\begin{bmatrix} 5\\\\ 9\\\\ \\end{bmatrix} ](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-91e110225465c1f7a55818020dad94f2_l3.png)
    
    2 Row (1) = ![2x_1 + 4x_2 = 10 \\neq 9](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-a79dc5e10a90436ce9a122313451aec3_l3.png)
    
    Therefore, the equations are inconsistent
    We cannot find the solution to (![x_1, x_2](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-f936ea9c199708a1dd9c66c71c738ecf_l3.png))
    

**Case 2: m > n**

  * In this case, the number of variables or the attributes is less than the number of equations.
  * Here, not all the equations can be satisfied.
  * So, it is sometimes termed as the case of no solution.
  * But, we can try to identify an appropriate solution by viewing this case from optimization perspective.

 **An optimization perspective**

    
    
    - Rather than finding a solution to ![Ax-b = 0](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-25ac19643fe46f1aeb5976a6831a0456_l3.png), we can find an ![x](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-4fdd037713ae07c442e4e7d7e059e818_l3.png) such that (![Ax-b](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-09d3de1b73e22f7d9617d37524596ea5_l3.png)) 
      is minimized
    - Here, ![Ax-b](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-09d3de1b73e22f7d9617d37524596ea5_l3.png) is a vector
    - There will be as many error terms as the number of equations
    - Denote ![Ax-b](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-09d3de1b73e22f7d9617d37524596ea5_l3.png) = e (m x 1); there are m errors ![e_i](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-3c71bf6f5aea6c3fc793404abf02b83d_l3.png), i = 1:m
    - We can minimize all the errors collectively by minimizing ![\\sum_{i=1}^{m} e_i^{2}](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-9dba9247da64ca82fbd34bf182ff6c27_l3.png)
    - This is the same as minimizing ![\(Ax-b\)^{T}\(Ax-b\)](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-78c79fb3a1854ff70c00105b634eafaa_l3.png)
    

So, the optimization problem becomes  
![min\[\(Ax-b\)^{T}\(Ax-b\)\]](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-2cb85785543a1c02b3888b9e3df7e969_l3.png)  
= ![min\[\(b^{T}-x^{T}A^{T}\)\(Ax-b\)\]](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-0f1df65314ccd7de75d6a41f61ea6552_l3.png)  
=
![min\[\(x^{T}A^{T}Ax2b^{T}Ax+b^{T}b\)=f\(x\)\]](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-66ef9806b0bcad3a03ceeaa9f4e84637_l3.png)

Here, we can notice that the optimization problem is a function of _x_. When
we solve this optimization problem, it will give us the solution for _x_. We
can obtain the solution to this optimization problem by differentiating
![f\(x\)](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-2094cfaa292b3ca4c03b01d8860213e6_l3.png) with respect to
_x_ and setting the differential to zero. ![ \\begin{document} \\nabla$ f\(x\)
= 0 \\end{document} ](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-0fe97a92fe739c0bab7b13f4678d7e18_l3.png)

– Now, differentiating f(x) and setting the differential to zero results in  
![2\(A^{T}A\)x - 2A^{T}b = 0](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-c4e3c92e701683bf9a558b813cbc2c5f_l3.png)  
![A^{T}Ax = A^{T}b](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-d3c59a611e7335022c722fbea6931f9d_l3.png)

– Assuming that all the columns are linearly independent  
![x = \(A^{T}A\)^{-1}A^{T}b](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-a61518823139e86b884e19cfe92efb6b_l3.png)

 **Note:** While this solution x might not satisfy all the equation but it
will ensure that the errors in the equations are collectively minimized.

 **Example 2.1:**

    
    
    Consider the given matrix equation:
    
    
     (4)    ![ \\begin{equation*} \\begin{bmatrix} 1&0\\\\ 2&0\\\\ 3&1\\\\ \\end{bmatrix} % \\begin{bmatrix} x_1\\\\ x_2\\\\ \\end{bmatrix} = \\begin{bmatrix} 1\\\\ -0.5\\\\ 5\\\\ \\end{bmatrix} \\end{equation*} ](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-98ff84e3441eb535bfda0cb96225bcaf_l3.png)
    
    
    m = 3, n = 2
    Using the optimization concept
    ![x = \(A^{T}A\)^{-1}A^{T}b](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-a61518823139e86b884e19cfe92efb6b_l3.png)
    
    ![ \\begin{bmatrix} x_1\\\\ x_2\\\\ \\end{bmatrix} = &&\(\\begin{bmatrix} 1&2&3\\\\ 0&0&1\\\\ \\end{bmatrix} % \\begin{bmatrix} 1&0\\\\ 2&0\\\\ 3&1\\\\ \\end{bmatrix}\)&&^{-1} \\begin{bmatrix} 1&2&3\\\\ 0&0&1\\\\ \\end{bmatrix} % \\begin{bmatrix} 1\\\\ -0.5\\\\ 5\\\\ \\end{bmatrix} ](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-1f7c2f81f24d14525ffecfe8769c33c4_l3.png)
    
    ![  \\begin{bmatrix} x_1\\\\ x_2\\\\ \\end{bmatrix} = \\begin{bmatrix} 0.2&-0.6\\\\ -0.6&2.8\\\\ \\end{bmatrix} % \\begin{bmatrix} 15\\\\ 5\\\\ \\end{bmatrix} ](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-426373d3443b9c67af754a2fede4600e_l3.png)
    ![  \\begin{bmatrix} x_1\\\\ x_2\\\\ \\end{bmatrix} = \\begin{bmatrix} 0\\\\ 5\\\\ \\end{bmatrix} ](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-410821f40352451a9566f1b6cb02de4a_l3.png)
    Therefore, the solution for the given linear equation is ![\(x_1, x_2\) = \(0, 5\)](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-e68a12a6365f532a9f7fb5b4f04d764f_l3.png)
    Substituting in the equation shows
    ![  \\begin{bmatrix} 1&0\\\\ 2&0\\\\ 3&1\\\\ \\end{bmatrix} % \\begin{bmatrix} 0\\\\ 5\\\\ \\end{bmatrix} = \\begin{bmatrix} 0\\\\ 0\\\\ 5\\\\ \\end{bmatrix} \\neq \\begin{bmatrix} 1\\\\ -0.5\\\\ 5\\\\ \\end{bmatrix}  ](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-aaa3eec0d2be5061af20815f73249239_l3.png)
    

**Example 2.2:**

    
    
    Consider the given matrix equation:
    
    
     (5)    ![ \\begin{equation*} \\begin{bmatrix} 1&0\\\\ 2&0\\\\ 3&1\\\\ \\end{bmatrix} % \\begin{bmatrix} x_1\\\\ x_2\\\\ \\end{bmatrix} = \\begin{bmatrix} 1\\\\ 2\\\\ 5\\\\ \\end{bmatrix} \\end{equation*} ](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-8ea3513122da2d5ca785dec2d751b281_l3.png)
    
    
    m = 3, n = 2
    Using the optimization concept
    ![x = \(A^{T}A\)^{-1}A^{T}b](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-a61518823139e86b884e19cfe92efb6b_l3.png)
    
    ![ \\begin{bmatrix} x_1\\\\ x_2\\\\ \\end{bmatrix} = &&\(\\begin{bmatrix} 1&2&3\\\\ 0&0&1\\\\ \\end{bmatrix} % \\begin{bmatrix} 1&0\\\\ 2&0\\\\ 3&1\\\\ \\end{bmatrix}\)&&^{-1} \\begin{bmatrix} 1&2&3\\\\ 0&0&1\\\\ \\end{bmatrix} % \\begin{bmatrix} 1\\\\ 2\\\\ 5\\\\ \\end{bmatrix} ](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-92115081759db3950f9c804f56932d5f_l3.png)
    
    ![  \\begin{bmatrix} x_1\\\\ x_2\\\\ \\end{bmatrix} = \\begin{bmatrix} 0.2&-0.6\\\\ -0.6&2.8\\\\ \\end{bmatrix} % \\begin{bmatrix} 20\\\\ 5\\\\ \\end{bmatrix} ](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-97d677c82d7089ab1f2c558052906eff_l3.png)
    ![  \\begin{bmatrix} x_1\\\\ x_2\\\\ \\end{bmatrix} = \\begin{bmatrix} 1\\\\ 2\\\\ \\end{bmatrix} ](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-58ea8f2e9c84ec8d195f360ff904af68_l3.png)
    Therefore, the solution for the given linear equation is ![\(x_1, x_2\) = \(1, 2\)](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-73992e433fd2e447be871d39c88be117_l3.png)
    Substituting in the equation shows
    ![  \\begin{bmatrix} 1&0\\\\ 2&0\\\\ 3&1\\\\ \\end{bmatrix} % \\begin{bmatrix} 1\\\\ 2\\\\ \\end{bmatrix} = \\begin{bmatrix} 1\\\\ 2\\\\ 5\\\\ \\end{bmatrix} = \\begin{bmatrix} 1\\\\ 2\\\\ 5\\\\ \\end{bmatrix} ](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-890b4c1eca4af09f8028d80e80c17a96_l3.png)
    

So, the important poin to notice in the case 2 is that if we have more
equations than variables then we can always use the least square solution
which is ![x = \(A^{T}A\)^{-1}A^{T}b](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-a61518823139e86b884e19cfe92efb6b_l3.png).
There is one thing to keep in mind is that
![\(A^{T}A\)^{-1}](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-421ab72e0e20a7ac0b10f4f078aebe24_l3.png) exists if the
columns of A are linearly independent.

 **Case 3: m < n**

* This case deals with more number of attributes or variables than equations
* Here, we can obtain multiple solutions for the attributes
* This is an infinite solution case
* We will see how we can choose one solution from the set of infinite possible solution

 **In this case also we have an optimization perspective.Know what is Lagrange
functionhere**.  
– Given below is the optimization problem

min(![\\frac{1}{2}x^{T}x](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-e0049fb0f45b61629e3c0f41122d2b6a_l3.png))  
such that,  
![ Ax = b ](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-d709e8d86afb9418f7517f04e4be35a5_l3.png)  
– We can define a Lagrangian function  
![  min\[ f\(x, \\lambda\) = \\frac{1}{2}x^{T}x + \\lambda^{T}\(Ax-b\)\]
](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-4f0b2dbf4eba482b57acaf6d0c533823_l3.png)

– Differentiate the Lagrangian with respect to x, and set it to zero, then we
will get,  
![ x + A^{T}\\lambda = 0 ](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-50e101eb099026191a60eba85300d2e7_l3.png)  
![ x = -A^{T}\\lambda  ](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-8768541d7ccbab1dcd7c67b3c0effbdb_l3.png)  
Pre – multiplying by A  
![ Ax=b=-AA^{T}\\lambda = 0 ](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-b02d042e667c68559b75ec68ee83d0dd_l3.png)  
From above we can obtain  
![ \\lambda = -\(AA^{T}\)^{-1}b ](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-a505f32af74ed4c42412e2cd14ec909e_l3.png) assuming that
all the rows are linearly independent  
![ x = -A^{T}\\lambda = A^{T}\(AA^{T}\)^{-1}b
](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-489db174ad501bc0a97de226ee23a56a_l3.png)

 **Example 3.1:**

    
    
    Consider the given matrix equation:
    
    
     (6)    ![ \\begin{equation*} \\begin{bmatrix} 1&2&3\\\\ 0&0&1\\\\ \\end{bmatrix} % \\begin{bmatrix} x_1\\\\ x_2\\\\ x_3\\\\ \\end{bmatrix} = \\begin{bmatrix} 2\\\\ 1\\\\ \\end{bmatrix} \\end{equation*} ](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-96ae07d489c7ef74b53c8aff41f10c08_l3.png)
    
    
    m = 2, n = 3
    Using the optimization concept,
    
    ![x = A^{T}\(AA^{T}\)^{-1}b](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-775772b5a0544699edbb105099b67472_l3.png)
    
    ![ x =  \\begin{bmatrix} 1&0\\\\ 2&0\\\\ 3&1\\\\ \\end{bmatrix} % \(\\begin{bmatrix} 1&2&3\\\\ 0&0&1\\\\ \\end{bmatrix} % \\begin{bmatrix} 1&0\\\\ 2&0\\\\ 3&1\\\\ \\end{bmatrix}\)^{-1} % \\begin{bmatrix} 2\\\\ 1\\\\ \\end{bmatrix}  ](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-3785cd590276adaa834b54518fa2b463_l3.png)
    
    ![ x =  \\begin{bmatrix} 1&0\\\\ 2&0\\\\ 3&1\\\\ \\end{bmatrix} % \\begin{bmatrix} 14&3\\\\ 3&1\\\\ \\end{bmatrix}^{-1} % \\begin{bmatrix} 2\\\\ 1\\\\ \\end{bmatrix} ](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-7bbf11a536613979b28d938f2064cbd2_l3.png)
    
    ![ x =  \\begin{bmatrix} 1&0\\\\ 2&0\\\\ 3&1\\\\ \\end{bmatrix} % \\begin{bmatrix} -0.2\\\\ 1.6\\\\ \\end{bmatrix} ](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-9d9324e89e87aa7c013f241480e369f8_l3.png)
    
    ![ \\begin{bmatrix} x_1\\\\ x_2\\\\ x_3\\\\ \\end{bmatrix} = \\begin{bmatrix} -0.2\\\\ -0.4\\\\ 1\\\\ \\end{bmatrix} ](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-c25b9440e5d088872c8f04a87e3b2d56_l3.png)
    
    The solution for given sample is (![x_1, x_2, x_3](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-a800f4adb9aac6bf4f68e9bb7e32d590_l3.png)) = (-0.2, -0.4, 1)
    You can easily verify that 
    ![ \\begin{bmatrix} 1&0\\\\ 2&0\\\\ 3&1\\\\ \\end{bmatrix} % \\begin{bmatrix} x_1\\\\ x_2\\\\ x_3\\\\ \\end{bmatrix} = \\begin{bmatrix} 2\\\\ 1\\\\ \\end{bmatrix} ](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-fdfe2396195b193ae3aa55b8ce0429fc_l3.png)
    

**Generalization**

* The above-described cases cover all the possible scenarios that one may encounter while solving linear equations.
* The concept we use to generalize the solutions for all the above cases is called Moore – Penrose Pseudoinverse of a matrix.
* Singular Value Decomposition can be used to calculate the psuedoinverse or the generalized inverse (![A^+](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-1afd6ca7c69e3d26404b4b438ee55411_l3.png)).

![machine-learning](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20210107141454/ML-Live-Article-Bottom-min.png)

My Personal Notes _arrow_drop_up_

Save


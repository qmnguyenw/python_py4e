Minimum number of integers required to fill the NxM grid



Given a grid of size (NxM) is to be filled with integers.

Filling of cells in the grid should be done in the following manner:

  1. let A, B and C are three cell and, B and C shared a side with A.
  2. Value of cell B and C must be distinct.
  3. Let L be the number of distinct integers in a grid.
  4. Each cell should contain value from 1 to L.

The task is to find the minimum value of L and any resulting grid.

 **Examples:**

    
    
    **Input:** N = 1, M = 2
    **Output:**
    L = 2
    grid = {1, 2}
    
    **Input:** 2 3
    **Output:**
    L = 3
    grid = {{1, 2, 3},
            {1, 2, 3}}
    **Explanation:** Integers in the neighbors 
    of cell (2, 2) are 1, 2 and 3.
    All numbers are pairwise distinct.
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:**  
It is given that two cells shared a side with another cell must be distinct.
For each such cell, there will be a possible maximum of 8 cells in a grid from
whom its value must be different.  
It will follow the 4 colour problem: Maximum colour required to fill the
regions will be 4.

  

  

  1. For N<4 or M<4  
Number of integers required may vary from 1 to 4.  
Checking 8 cells and then fill the current cell.  
If number of distinct integers in 8 cells is less than L then fill the current
cell with any remaining integer, otherwise fill the current cells with L+1
integer.

  2. For N>=4 and M>=4  
Number of integers required must be 4 according to 4 colour problem.  
Use the 4×4 matrix to fill the NxM matrix.

    
        1 2 3 4
    1 2 3 4
    3 4 1 2
    3 4 1 2

Below is the implementation of the above approach:

 **Implementation:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 implementation of

# above approach

 

 

# Function to display the matrix

def display_matrix(A):

 for i in A:

 print(*i)

 

 

# Function for calculation

def cal_main(A, L, x, i, j):

 s = set()

 

 # Checking 8 cells and

 # then fill the current cell.

 if (i - 2) >= 0:

 s.add(A[i - 2][j])

 if (i + 2) < N:

 s.add(A[i + 2][j])

 if (j - 2) >= 0:

 s.add(A[i][j - 2])

 if (j + 2) < M:

 s.add(A[i][j + 2])

 if (i - 1) >= 0 and (j - 1) >= 0:

 s.add(A[i - 1][j - 1])

 if (i - 1) >= 0 and (j + 1) < M:

 s.add(A[i - 1][j + 1])

 if (i + 1) < N and (j - 1) >= 0:

 s.add(A[i + 1][j - 1])

 if (i + 1) < N and (j + 1) < M:

 s.add(A[i + 1][j + 1])

 

 # Set to contain distinct value

 # of integers in 8 cells.

 s = s.difference({0})

 

 if len(s) < L:

 

 # Set contain remaining integers

 w = x.difference(s)

 

 # fill the current cell

 # with maximum remaining integer

 A[i][j] = max(w)

 else:

 

 # fill the current cells with L + 1 integer.

 A[i][j] = L + 1

 L += 1

 

 # Increase the value of L

 x.add(L)

 return A, L, x

 

 

# Function to find the number

# of distinct integers

def solve(N, M):

 

 # initialise the list (NxM) with 0.

 A = []

 for i in range(N):

 K = []

 for j in range(M):

 K.append(0)

 A.append(K)

 

 # Set to contain distinct

 # value of integers from 1-L

 x = set()

 L = 0

 

 # Number of integer required

 # may vary from 1 to 4.

 if N < 4 or M < 4:

 if N > M: # if N is greater

 for i in range(N):

 for j in range(M):

 cal_main(A, L, x, i, j)

 

 else:

 # if M is greater

 for j in range(M):

 for i in range(N):

 cal_main(A, L, x, i, j)

 else:

 

 # Number of integer required

 # must be 4

 L = 4

 

 # 4×4 matrix to fill the NxM matrix.

 m4 = [[1, 2, 3, 4], 

 [1, 2, 3, 4], 

 [3, 4, 1, 2], 

 [3, 4, 1, 2]]

 

 for i in range(4):

 for j in range(4):

 A[i][j] = m4[i][j]

 for i in range(4, N):

 for j in range(4):

 A[i][j] = m4[i % 4][j]

 for j in range(4, M):

 for i in range(N):

 A[i][j] = A[i][j % 4]

 print(L)

 display_matrix(A)

 

 

# Driver Code

if __name__ == "__main__":

 

 # sample input

 # Number of rows and columns

 N, M = 10, 5

 solve(N, M)  
  
---  
  
 __

 __

 **Output:**

    
    
    4
    1 2 3 4 1 2 3 4 1 2
    1 2 3 4 1 2 3 4 1 2
    3 4 1 2 3 4 1 2 3 4
    3 4 1 2 3 4 1 2 3 4
    1 2 3 4 1 2 3 4 1 2
    1 2 3 4 1 2 3 4 1 2
    3 4 1 2 3 4 1 2 3 4
    3 4 1 2 3 4 1 2 3 4
    1 2 3 4 1 2 3 4 1 2
    1 2 3 4 1 2 3 4 1 2
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


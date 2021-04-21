Python Program for Min Cost Path



Given a cost matrix cost[][] and a position (m, n) in cost[][], write a
function that returns cost of minimum cost path to reach (m, n) from (0, 0).
Each cell of the matrix represents a cost to traverse through that cell. Total
cost of a path to reach (m, n) is sum of all the costs on that path (including
both source and destination). You can only traverse down, right and diagonally
lower cells from a given cell, i.e., from a given cell (i, j), cells (i+1, j),
(i, j+1) and (i+1, j+1) can be traversed. You may assume that all costs are
positive integers.

For example, in the following figure, what is the minimum cost path to (2, 2)?  
![](https://media.geeksforgeeks.org/wp-content/cdn-uploads/dp.png)

The path with minimum cost is highlighted in the following figure. The path is
(0, 0) –> (0, 1) –> (1, 2) –> (2, 2). The cost of the path is 8 (1 + 2 + 2 +
3).

 __

 __  
 __

 __

 __  
 __  
 __

# Dynamic Programming Python implementation of Min Cost Path

# problem

R = 3

C = 3

 

def minCost(cost, m, n):

 

 # Instead of following line, we can use int tc[m + 1][n + 1] or

 # dynamically allocate memoery to save space. The following

 # line is used to keep te program simple and make it working

 # on all compilers.

 tc = [[0 for x in range(C)] for x in range(R)]

 

 tc[0][0] = cost[0][0]

 

 # Initialize first column of total cost(tc) array

 for i in range(1, m + 1):

 tc[i][0] = tc[i-1][0] + cost[i][0]

 

 # Initialize first row of tc array

 for j in range(1, n + 1):

 tc[0][j] = tc[0][j-1] + cost[0][j]

 

 # Construct rest of the tc array

 for i in range(1, m + 1):

 for j in range(1, n + 1):

 tc[i][j] = min(tc[i-1][j-1], tc[i-1][j],

 tc[i][j-1]) + cost[i][j]

 

 return tc[m][n]

 

# Driver program to test above functions

cost = [[1, 2, 3],

 [4, 8, 2],

 [1, 5, 3]]

print(minCost(cost, 2, 2))

 

# This code is contributed by Bhavya Jain  
  
---  
  
 __

 __

 **Output:**

    
    
    8
    

Please refer complete article on Dynamic Programming | Set 6 (Min Cost Path)
for more details!

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

  
  

  

My Personal Notes _arrow_drop_up_

Save


Unique paths covering every non-obstacle block exactly once in a grid



Given a grid **grid[][]** with **4** types of blocks:

  * **1** represents the starting block. There is exactly one starting block.
  *  **2** represents the ending block. There is exactly one ending block.
  *  **0** represents empty block we can walk over.
  *  **-1** represents obstacles that we cannot walk over.

The task is to count the number of paths from the starting block to the ending
block such that every non-obstacle block is covered exactly once.

 **Examples:**

> **Input:** grid[][] = {  
> {1, 0, 0, 0},  
> {0, 0, 0, 0},  
> {0, 0, 2, -1} }  
> **Output:** 2  
> Following are the only paths covering all the non-obstacle blocks:
>
> ![](https://media.geeksforgeeks.org/wp-content/cdn-uploads/UniquePath.png)
>
>  
>
>
>  
>
>
> **Input:** grid[][] = {  
> {1, 0, 0, 0},  
> {0, 0, 0, 0},  
> {0, 0, 0, 2} }  
> **Output:** 4

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.  

**Approach:** We can use simple DFS here with backtracking. We can check that
a particular path has covered all the non-obstacle blocks by counting all the
blocks encountered in the way and finally comparing it with the total number
of blocks available and if they match, then we add it as a valid solution.

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation of the approach

#include <bits/stdc++.h>

using namespace std;

// Function for dfs.

// i, j ==> Current cell indexes

// vis ==> To mark visited cells

// ans ==> Result

// z ==> Current count 0s visited

// z_count ==> Total 0s present

void dfs(int i, int j, vector<vector<int> >& grid,

 vector<vector<bool> >& vis, int& ans,

 int z, int z_count)

{

 int n = grid.size(), m = grid[0].size();

 // Mark the block as visited

 vis[i][j] = 1;

 if (grid[i][j] == 0)

 // update the count

 z++;

 // If end block reached

 if (grid[i][j] == 2) {

 // If path covered all the non-

 // obstacle blocks

 if (z == z_count)

 ans++;

 vis[i][j] = 0;

 return;

 }

 // Up

 if (i >= 1 && !vis[i - 1][j] && grid[i - 1][j] != -1)

 dfs(i - 1, j, grid, vis, ans, z, z_count);

 // Down

 if (i < n - 1 && !vis[i + 1][j] && grid[i + 1][j] != -1)

 dfs(i + 1, j, grid, vis, ans, z, z_count);

 // Left

 if (j >= 1 && !vis[i][j - 1] && grid[i][j - 1] != -1)

 dfs(i, j - 1, grid, vis, ans, z, z_count);

 // Right

 if (j < m - 1 && !vis[i][j + 1] && grid[i][j + 1] != -1)

 dfs(i, j + 1, grid, vis, ans, z, z_count);

 // Unmark the block (unvisited)

 vis[i][j] = 0;

}

// Function to return the count of the unique paths

int uniquePaths(vector<vector<int> >& grid)

{

 int z_count = 0; // Total 0s present

 int n = grid.size(), m = grid[0].size();

 int ans = 0;

 vector<vector<bool> > vis(n, vector<bool>(m, 0));

 int x, y;

 for (int i = 0; i < n; ++i) {

 for (int j = 0; j < m; ++j) {

 // Count non-obstacle blocks

 if (grid[i][j] == 0)

 z_count++;

 else if (grid[i][j] == 1) {

 // Starting position

 x = i, y = j;

 }

 }

 }

 dfs(x, y, grid, vis, ans, 0, z_count);

 return ans;

}

// Driver code

int main()

{

 vector<vector<int> > grid{ { 1, 0, 0, 0 },

 { 0, 0, 0, 0 },

 { 0, 0, 2, -1 } };

 cout << uniquePaths(grid);

 return 0;

}  
  
---  
  
 __

 __

## Java

 __

 __  
 __

 __

 __  
 __  
 __

// Java implementation of the approach

import java.util.Arrays;

class GFG

{

 static int ans = 0;

 // Function for dfs.

 // i, j ==> Current cell indexes

 // vis ==> To mark visited cells

 // ans ==> Result

 // z ==> Current count 0s visited

 // z_count ==> Total 0s present

 static void dfs(int i, int j, int[][] grid,

 boolean[][] vis, int z, int z_count)

 {

 int n = grid.length, m = grid[0].length;

 // Mark the block as visited

 vis[i][j] = true;

 if (grid[i][j] == 0)

 // update the count

 z++;

 // If end block reached

 if (grid[i][j] == 2)

 {

 // If path covered all the non-

 // obstacle blocks

 if (z == z_count)

 ans++;

 vis[i][j] = false;

 return;

 }

 // Up

 if (i >= 1 && !vis[i - 1][j] && grid[i - 1][j] != -1)

 dfs(i - 1, j, grid, vis, z, z_count);

 // Down

 if (i < n - 1 && !vis[i + 1][j] && grid[i + 1][j] !=
-1)

 dfs(i + 1, j, grid, vis, z, z_count);

 // Left

 if (j >= 1 && !vis[i][j - 1] && grid[i][j - 1] != -1)

 dfs(i, j - 1, grid, vis, z, z_count);

 // Right

 if (j < m - 1 && !vis[i][j + 1] && grid[i][j + 1] !=
-1)

 dfs(i, j + 1, grid, vis, z, z_count);

 // Unmark the block (unvisited)

 vis[i][j] = false;

 }

 // Function to return the count of the unique paths

 static int uniquePaths(int[][] grid)

 {

 int z_count = 0; // Total 0s present

 int n = grid.length, m = grid[0].length;

 boolean[][] vis = new boolean[n][m];

 for (int i = 0; i < n; i++)

 {

 Arrays.fill(vis[i], false);

 }

 int x = 0, y = 0;

 for (int i = 0; i < n; ++i)

 {

 for (int j = 0; j < m; ++j)

 {

 // Count non-obstacle blocks

 if (grid[i][j] == 0)

 z_count++;

 else if (grid[i][j] == 1)

 {

 // Starting position

 x = i;

 y = j;

 }

 }

 }

 dfs(x, y, grid, vis, 0, z_count);

 return ans;

 }

 // Driver code

 public static void main(String[] args)

 {

 int[][] grid = { { 1, 0, 0, 0 }, { 0, 0, 0,
0 }, { 0, 0, 2, -1 } };

 System.out.println(uniquePaths(grid));

 }

}

// This code is contributed by sanjeev2552  
  
---  
  
 __

 __

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 implementation of the approach

# Function for dfs.

# i, j ==> Current cell indexes

# vis ==> To mark visited cells

# ans ==> Result

# z ==> Current count 0s visited

# z_count ==> Total 0s present

def dfs(i, j, grid, vis, ans, z, z_count):

 n = len(grid)

 m = len(grid[0])

 # Mark the block as visited

 vis[i][j] = 1

 

 if (grid[i][j] == 0):

 # Update the count

 z += 1

 # If end block reached

 if (grid[i][j] == 2):

 # If path covered all the non-

 # obstacle blocks

 if (z == z_count):

 ans += 1

 

 vis[i][j] = 0

 

 return grid, vis, ans

 

 # Up

 if (i >= 1 and not vis[i - 1][j] and

 grid[i - 1][j] != -1):

 grid, vis, ans = dfs(i - 1, j, grid,

 vis, ans, z,

 z_count)

 # Down

 if (i < n - 1 and not vis[i + 1][j] and

 grid[i + 1][j] != -1):

 grid, vis, ans = dfs(i + 1, j, grid,

 vis, ans, z,

 z_count)

 # Left

 if (j >= 1 and not vis[i][j - 1] and

 grid[i][j - 1] != -1):

 grid, vis, ans = dfs(i, j - 1, grid,

 vis, ans, z,

 z_count)

 # Right

 if (j < m - 1 and not vis[i][j + 1] and

 grid[i][j + 1] != -1):

 grid, vis, ans = dfs(i, j + 1, grid,

 vis, ans, z,

 z_count)

 # Unmark the block (unvisited)

 vis[i][j] = 0

 

 return grid, vis, ans

# Function to return the count

# of the unique paths

def uniquePaths(grid):

 

 # Total 0s present

 z_count = 0

 n = len(grid)

 m = len(grid[0])

 ans = 0

 

 vis = [[0 for j in range(m)]

 for i in range(n)]

 

 x = 0

 y = 0

 

 for i in range(n):

 for j in range(m):

 

 # Count non-obstacle blocks

 if grid[i][j] == 0:

 z_count += 1

 

 elif (grid[i][j] == 1):

 

 # Starting position

 x = i

 y = j

 

 grid, vis, ans = dfs(x, y, grid,

 vis, ans, 0,

 z_count)

 

 return ans

# Driver code

if __name__=='__main__':

 grid = [ [ 1, 0, 0, 0 ],

 [ 0, 0, 0, 0 ],

 [ 0, 0, 2, -1 ] ]

 

 print(uniquePaths(grid))

 

# This code is contributed by rutvik_56  
  
---  
  
 __

 __

 **Output:**

    
    
    2

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


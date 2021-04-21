Find the number of distinct islands in a 2D matrix



Given a boolean 2D matrix. The task is to find the number of distinct islands
where a group of connected 1s (horizontally or vertically) forms an island.
Two islands are considered to be distinct if and only if one island is equal
to another (not rotated or reflected).

 **Examples:**

>  **Input:** grid[][] =  
> {{1, 1, 0, 0, 0},  
> 1, 1, 0, 0, 0},  
> 0, 0, 0, 1, 1},  
> 0, 0, 0, 1, 1}}
>
>  **Output:** 1  
> Island 1, 1 at the top left corner is same as island 1, 1 at the bottom
> right corner
>
>  **Input:** grid[][] =  
> {{1, 1, 0, 1, 1},  
> 1, 0, 0, 0, 0},  
> 0, 0, 0, 0, 1},  
> 1, 1, 0, 1, 1}}
>
>  
>
>
>  
>
>
>  **Output:** 3  
> Distinct islands in the example above are: 1, 1 at the top left corner; 1, 1
> at the top right corner and 1 at the bottom right corner. We ignore the
> island 1, 1 at the bottom left corner since 1, 1 it is identical to the top
> right corner.

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** This problem is an extension of the problem Number of Islands.

The core of the question is to know if 2 islands are equal. The primary
criteria is that the number of 1’s should be same in both. But this cannot be
the only criteria as we have seen in example 2 above. So how do we know? We
could use the position/coordinates of the 1’s.

If we take the first coordinates of any island as a base point and then
compute the coordinates of other points from the base point, we can eliminate
duplicates to get the distinct count of islands. So, using this approach, the
coordinates for the 2 islands in example 1 above can be represented as: [(0,
0), (0, 1), (1, 0), (1, 1)].

 **Below is the implementation of above approach:**  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation of above approach

#include <bits/stdc++.h>

using namespace std;

 

// 2D array for the storing the horizontal and vertical

// directions. (Up, left, down, right}

vector<vector<int> > dirs = { { 0, -1 },

 { -1, 0 },

 { 0, 1 },

 { 1, 0 } };

 

// Function to perform dfs of the input grid

void dfs(vector<vector<int> >& grid, int x0, int y0,

 int i, int j, vector<pair<int, int> >& v)

{

 int rows = grid.size(), cols = grid[0].size();

 

 if (i < 0 || i >= rows || j < 0

 || j >= cols || grid[i][j] <= 0)

 return;

 

 // marking the visited element as -1

 grid[i][j] *= -1;

 

 // computing coordinates with x0, y0 as base

 v.push_back({ i - x0, j - y0 });

 

 // repeat dfs for neighbors

 for (auto dir : dirs) {

 dfs(grid, x0, y0, i + dir[0], j + dir[1], v);

 }

}

 

// Main function that returns distinct count of islands in

// a given boolean 2D matrix

int countDistinctIslands(vector<vector<int> >& grid)

{

 int rows = grid.size();

 if (rows == 0)

 return 0;

 

 int cols = grid[0].size();

 if (cols == 0)

 return 0;

 

 set<vector<pair<int, int> > > coordinates;

 

 for (int i = 0; i < rows; ++i) {

 for (int j = 0; j < cols; ++j) {

 

 // If a cell is not 1

 // no need to dfs

 if (grid[i][j] != 1)

 continue;

 

 // vector to hold coordinates

 // of this island

 vector<pair<int, int> > v;

 dfs(grid, i, j, i, j, v);

 

 // insert the coordinates for

 // this island to set

 coordinates.insert(v);

 }

 }

 

 return coordinates.size();

}

 

// Driver code

int main()

{

 vector<vector<int> > grid = { { 1, 1, 0, 1, 1 },

 { 1, 0, 0, 0, 0 },

 { 0, 0, 0, 0, 1 },

 { 1, 1, 0, 1, 1 } };

 

 cout << "Number of distinct islands is "

 << countDistinctIslands(grid);

 

 return 0;

}  
  
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

# Python implementation of above approach

 

# 2D array for the storing the horizontal and vertical

# directions. (Up, left, down, right

dirs = [ [ 0, -1 ],

 [ -1, 0 ],

 [ 0, 1 ],

 [ 1, 0 ] ]

 

# Function to perform dfs of the input grid

def dfs(grid, x0, y0, i, j, v):

 rows = len(grid)

 cols = len(grid[0])

 

 if i < 0 or i >= rows or j < 0 or j >= cols
or grid[i][j] <= 0:

 return

 # marking the visited element as -1

 grid[i][j] *= -1

 

 # computing coordinates with x0, y0 as base

 v.append( (i - x0, j - y0) )

 

 # repeat dfs for neighbors

 for dir in dirs: 

 dfs(grid, x0, y0, i + dir[0], j + dir[1], v)

 

 

 

# Main function that returns distinct count of islands in

# a given boolean 2D matrix

def countDistinctIslands(grid):

 rows = len(grid)

 if rows == 0:

 return 0

 

 cols = len(grid[0])

 if cols == 0:

 return 0

 

 coordinates = set()

 

 for i in range(rows):

 for j in range(cols): 

 

 # If a cell is not 1

 # no need to dfs

 if grid[i][j] != 1:

 continue

 

 # to hold coordinates

 # of this island

 v = []

 dfs(grid, i, j, i, j, v)

 

 # insert the coordinates for

 # this island to set

 coordinates.add(tuple(v))

 

 return len(coordinates)

 

# Driver code

grid = [[ 1, 1, 0, 1, 1 ],

[ 1, 0, 0, 0, 0 ],

[ 0, 0, 0, 0, 1 ],

[ 1, 1, 0, 1, 1 ] ]

 

print("Number of distinct islands is", countDistinctIslands(grid))

 

# This code is contributed by ankush_953  
  
---  
  
 __

 __

 **Output:**

    
    
    Number of distinct islands is 3
    

**Time complexity:** O(rows * cols)  
 **Space complexity:** O(rows * cols)

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


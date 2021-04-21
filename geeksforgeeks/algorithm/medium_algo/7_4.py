Find the maximum cost path from the bottom-left corner to the top-right corner



Given a two dimensional grid, each cell of which contains integer cost which
represents a cost to traverse through that cell. The task is to find the
maximum cost path from the bottom-left corner to the top-right corner.

 **Note:** Use up and right moves only

 **Examples:**

    
    
    **Input :** mat[][] = {{20, -10, 0}, 
                       {1, 5, 10}, 
                       {1, 2, 3}}
    **Output :** 18
    (2, 0) ==> (2, 1) ==> (1, 1) ==> (1, 2) ==> (0, 2)  
    cost for this path is (1+2+5+10+0) = 18
    
    **Input :** mat[][] = {{1, -2, -3}, 
                       {1, 15, 10},
                       {1, -2, 3}}
    **Output :** 24
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Prerequisites:** Minimum Cost Path with Left, Right, Bottom and Up moves
allowed

 **Approach:** The idea is to maintain a separate array to store the maximum
cost for all the cells using queue. For every cell check if current cost in
reaching that cell is more than the previous cost or not. If previous cost is
minimum then update the cell with the current cost.

  

  

Below is the implementation of the above approach :  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to find maximum cost to reach

// top right corner from bottom left corner

#include <bits/stdc++.h>

using namespace std; 

 

#define ROW 3

#define COL 3 

 

// To store matrix cell coordinates 

struct Point 

{ 

 int x; 

 int y; 

}; 

 

// Check whether given cell (row, col) 

// is a valid cell or not. 

bool isValid(Point p) 

{ 

 // Return true if row number and column number 

 // is in range 

 return (p.x >=0) && (p.y <COL); 

} 

 

 

// Function to find maximum cost to reach 

// top right corner from bottom left corner

int find_max_cost(int mat[][COL]) 

{ 

 int max_val[ROW][COL]; 

 memset(max_val, 0, sizeof max_val);

 max_val[ROW-1][0] = mat[ROW-1][0]; 

 

 // Starting point 

 Point src = {ROW-1,0};

 

 // Create a queue for traversal 

 queue<Point> q; 

 

 q.push(src); // Enqueue source cell 

 

 // Do a BFS starting from source cell 

 // on the allowed direction

 while (!q.empty()) 

 { 

 Point curr = q.front();

 q.pop(); 

 

 // Find up point

 Point up = {curr.x-1, curr.y};

 

 // if adjacent cell is valid, enqueue it. 

 if (isValid(up)) 

 { 

 max_val[up.x][up.y] = max(max_val[up.x][up.y], 

 mat[up.x][up.y] + max_val[curr.x][curr.y]);

 q.push(up);

 }

 

 // Find right point 

 Point right = {curr.x, curr.y+1};

 

 if(isValid(right)) 

 { 

 max_val[right.x][right.y] = max(max_val[right.x][right.y],

 mat[right.x][right.y] + max_val[curr.x][curr.y]);

 q.push(right);

 }

 

 } 

 

 // Return the required answer

 return max_val[0][COL-1]; 

} 

 

// Driver code

int main() 

{ 

 int mat[ROW][COL] = { {20, -10, 0},

 {1, 5, 10},

 {1, 2, 3},}; 

 

 std::cout<<"Given matrix is "<<endl;

 

 for(int i = 0 ; i<ROW;++i)

 {

 for(int j =0; j<COL; ++j)

 std::cout<<mat[i][j]<<" ";

 

 std::cout<<endl;

 }

 

 std::cout<<"Maximum cost is " << find_max_cost(mat); 

 

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

// Java program to find maximum cost to reach

// top right corner from bottom left corner

import java.util.*;

class GFG

{

static int ROW = 3;

static int COL = 3;

 

// To store matrix cell coordinates 

static class Point 

{ 

 int x; 

 int y; 

 

 public Point(int x, int y) 

 {

 this.x = x;

 this.y = y;

 } 

} 

 

// Check whether given cell (row, col) 

// is a valid cell or not. 

static boolean isValid(Point p) 

{ 

 // Return true if row number and column number 

 // is in range 

 return (p.x >= 0) && (p.y < COL); 

} 

 

// Function to find maximum cost to reach 

// top right corner from bottom left corner

static int find_max_cost(int mat[][]) 

{ 

 int [][]max_val = new int[ROW][COL]; 

 max_val[ROW - 1][0] = mat[ROW - 1][0]; 

 

 // Starting point 

 Point src = new Point(ROW - 1, 0);

 

 // Create a queue for traversal 

 Queue<Point> q = new LinkedList<>(); 

 

 q.add(src); // Enqueue source cell 

 

 // Do a BFS starting from source cell 

 // on the allowed direction

 while (!q.isEmpty()) 

 { 

 Point curr = q.peek();

 q.remove(); 

 

 // Find up point

 Point up = new Point(curr.x - 1, curr.y);

 

 // if adjacent cell is valid, enqueue it. 

 if (isValid(up)) 

 { 

 max_val[up.x][up.y] = Math.max(max_val[up.x][up.y], 

 mat[up.x][up.y] + max_val[curr.x][curr.y]);

 q.add(up);

 }

 

 // Find right point 

 Point right = new Point(curr.x, curr.y + 1);

 

 if(isValid(right)) 

 { 

 max_val[right.x][right.y] = Math.max(max_val[right.x][right.y],

 mat[right.x][right.y] + max_val[curr.x][curr.y]);

 q.add(right);

 }

 } 

 

 // Return the required answer

 return max_val[0][COL - 1]; 

} 

 

// Driver code

public static void main(String[] args) 

{

 int mat[][] = {{20, -10, 0},

 {1, 5, 10},

 {1, 2, 3}}; 

 

 System.out.println("Given matrix is ");

 

 for(int i = 0 ; i < ROW; ++i)

 {

 for(int j = 0; j < COL; ++j)

 System.out.print(mat[i][j] + " ");

 

 System.out.println();

 }

 

 System.out.print("Maximum cost is " + 

 find_max_cost(mat)); 

}

}

 

// This code is contributed by PrinciRaj1992   
  
---  
  
__

__

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to find maximum cost to reach

# top right corner from bottom left corner

from collections import deque as queue

 

ROW = 3

COL = 3

 

# Check whether given cell (row, col)

# is a valid cell or not.

def isValid(p):

 

 # Return true if row number and column number

 # is in range

 return (p[0] >= 0) and (p[1] < COL)

 

# Function to find maximum cost to reach

# top right corner from bottom left corner

def find_max_cost(mat):

 max_val = [[0 for i in range(COL)] for i in
range(ROW)]

 

 max_val[ROW - 1][0] = mat[ROW - 1][0]

 

 # Starting po

 src = [ROW - 1, 0]

 

 # Create a queue for traversal

 q = queue()

 

 q.appendleft(src) # Enqueue source cell

 

 # Do a BFS starting from source cell

 # on the allowed direction

 while (len(q) > 0):

 curr = q.pop()

 

 # Find up point

 up = [curr[0] - 1, curr[1]]

 

 # if adjacent cell is valid, enqueue it.

 if (isValid(up)):

 max_val[up[0]][up[1]] =
max(max_val[up[0]][up[1]],mat[up[0]][up[1]] +
max_val[curr[0]][curr[1]])

 q.appendleft(up)

 

 

 # Find right po

 right = [curr[0], curr[1] + 1]

 

 if(isValid(right)):

 max_val[right[0]][right[1]] =
max(max_val[right[0]][right[1]],mat[right[0]][right[1]]
+ max_val[curr[0]][curr[1]])

 q.appendleft(right)

 

 

 # Return the required answer

 return max_val[0][COL - 1]

 

# Driver code

mat = [[20, -10, 0],

 [1, 5, 10],

 [1, 2, 3]]

 

print("Given matrix is ")

 

for i in range(ROW):

 for j in range(COL):

 print(mat[i][j],end=" ")

 print()

 

print("Maximum cost is ", find_max_cost(mat))

 

# This code is contributed by mohit kumar 29  
  
---  
  
 __

 __

## C#

 __

 __  
 __

 __

 __  
 __  
 __

// C# program to find maximum cost to reach

// top right corner from bottom left corner

using System;

using System.Collections.Generic;

 

class GFG

{

 

static int ROW = 3;

static int COL = 3;

 

// To store matrix cell coordinates 

public class Point 

{ 

 public int x; 

 public int y; 

 

 public Point(int x, int y) 

 {

 this.x = x;

 this.y = y;

 } 

} 

 

// Check whether given cell (row, col) 

// is a valid cell or not. 

static Boolean isValid(Point p) 

{ 

 // Return true if row number and 

 // column number is in range 

 return (p.x >= 0) && (p.y < COL); 

} 

 

// Function to find maximum cost to reach 

// top right corner from bottom left corner

static int find_max_cost(int [,]mat) 

{ 

 int [,]max_val = new int[ROW,COL]; 

 max_val[ROW - 1, 0] = mat[ROW - 1, 0]; 

 

 // Starting point 

 Point src = new Point(ROW - 1, 0);

 

 // Create a queue for traversal 

 Queue<Point> q = new Queue<Point>(); 

 

 q.Enqueue(src); // Enqueue source cell 

 

 // Do a BFS starting from source cell 

 // on the allowed direction

 while (q.Count != 0) 

 { 

 Point curr = q.Peek();

 q.Dequeue(); 

 

 // Find up point

 Point up = new Point(curr.x - 1, curr.y);

 

 // if adjacent cell is valid, enqueue it. 

 if (isValid(up)) 

 { 

 max_val[up.x, up.y] = Math.Max(max_val[up.x, up.y], 

 mat[up.x, up.y] + max_val[curr.x, curr.y]);

 q.Enqueue(up);

 }

 

 // Find right point 

 Point right = new Point(curr.x, 

 curr.y + 1);

 

 if(isValid(right)) 

 { 

 max_val[right.x, right.y] = Math.Max(max_val[right.x, right.y],

 mat[right.x, right.y] + max_val[curr.x, curr.y]);

 q.Enqueue(right);

 }

 } 

 

 // Return the required answer

 return max_val[0, COL - 1]; 

} 

 

// Driver code

public static void Main(String[] args) 

{

 int [,]mat = {{20, -10, 0},

 {1, 5, 10},

 {1, 2, 3}}; 

 

 Console.WriteLine("Given matrix is ");

 

 for(int i = 0 ; i < ROW; ++i)

 {

 for(int j = 0; j < COL; ++j)

 Console.Write(mat[i, j] + " ");

 

 Console.WriteLine();

 }

 

 Console.Write("Maximum cost is " + 

 find_max_cost(mat)); 

}

}

 

// This code is contributed by Princi Singh  
  
---  
  
 __

 __

 **Output:**

    
    
    Given matrix is 
    20 -10 0 
    1 5 10 
    1 2 3 
    Maximum cost is 18
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


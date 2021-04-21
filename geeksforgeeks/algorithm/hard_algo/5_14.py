Count number of ways to reach destination in a maze



Given a maze of 0 and -1 cells, the task is to find all the paths from (0, 0)
to (n-1, m-1), and every path should pass through at least one cell which
contains -1. From a given cell, we are allowed to move to cells (i+1, j) and
(i, j+1) only.  
This problem is a variation of the problem published here.

 **Examples:**

>  **Input:** maze[][] = {  
> {0, 0, 0, 0},  
> {0, -1, 0, 0},  
> {-1, 0, 0, 0},  
> {0, 0, 0, 0}}  
>  **Output:** 16

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** To find all the paths which go through at least one marked cell
(cell containing -1). If we find the paths that do not go through any of the
marked cells and all the possible paths from (0, 0) to (n-1, m-1) then we can
find all the paths that go through at least one of the marks cells.  
 **Number of paths that pass through at least one marked cell = (Total number
of paths – Number of paths that do not pass through any marked cell)**  
We will use the approach mentioned in this article to find the total number of
paths that do not pass through any marked cell and the total number of paths
from source to destination will be (m + n – 2)! / (n – 1)! * (m – 1)! where m
and n are the number of rows and columns.

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

#define R 4

#define C 4

 

// Function to return the count of possible paths

// in a maze[R][C] from (0, 0) to (R-1, C-1) that

// do not pass through any of the marked cells

int countPaths(int maze[][C])

{

 // If the initial cell is blocked, there is no

 // way of moving anywhere

 if (maze[0][0] == -1)

 return 0;

 

 // Initializing the leftmost column

 for (int i = 0; i < R; i++) {

 if (maze[i][0] == 0)

 maze[i][0] = 1;

 

 // If we encounter a blocked cell in leftmost

 // row, there is no way of visiting any cell

 // directly below it.

 else

 break;

 }

 

 // Similarly initialize the topmost row

 for (int i = 1; i < C; i++) {

 if (maze[0][i] == 0)

 maze[0][i] = 1;

 

 // If we encounter a blocked cell in bottommost

 // row, there is no way of visiting any cell

 // directly below it.

 else

 break;

 }

 

 // The only difference is that if a cell is -1,

 // simply ignore it else recursively compute

 // count value maze[i][j]

 for (int i = 1; i < R; i++) {

 for (int j = 1; j < C; j++) {

 // If blockage is found, ignore this cell

 if (maze[i][j] == -1)

 continue;

 

 // If we can reach maze[i][j] from maze[i-1][j]

 // then increment count.

 if (maze[i - 1][j] > 0)

 maze[i][j] = (maze[i][j] + maze[i - 1][j]);

 

 // If we can reach maze[i][j] from maze[i][j-1]

 // then increment count.

 if (maze[i][j - 1] > 0)

 maze[i][j] = (maze[i][j] + maze[i][j - 1]);

 }

 }

 

 // If the final cell is blocked, output 0, otherwise

 // the answer

 return (maze[R - 1][C - 1] > 0) ? maze[R - 1][C - 1] : 0;

}

// Function to return the count of all possible

// paths from (0, 0) to (n - 1, m - 1)

int numberOfPaths(int m, int n)

{

 // We have to calculate m+n-2 C n-1 here

 // which will be (m+n-2)! / (n-1)! (m-1)!

 int path = 1;

 for (int i = n; i < (m + n - 1); i++) {

 path *= i;

 path /= (i - n + 1);

 }

 return path;

}

 

// Function to return the total count of paths

// from (0, 0) to (n - 1, m - 1) that pass

// through at least one of the marked cells

int solve(int maze[][C])

{

 

 // Total count of paths - Total paths that do not

 // pass through any of the marked cell

 int ans = numberOfPaths(R, C) - countPaths(maze);

 

 // return answer

 return ans;

}

 

// Driver code

int main()

{

 int maze[R][C] = { { 0, 0, 0, 0 },

 { 0, -1, 0, 0 },

 { -1, 0, 0, 0 },

 { 0, 0, 0, 0 } };

 

 cout << solve(maze);

 

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

import java.io.*;

 

class GFG 

{

static int R = 4;

static int C = 4;

 

// Function to return the count of possible paths

// in a maze[R][C] from (0, 0) to (R-1, C-1) that

// do not pass through any of the marked cells

static int countPaths(int maze[][])

{

 

 // If the initial cell is blocked, 

 // there is no way of moving anywhere

 if (maze[0][0] == -1)

 return 0;

 

 // Initializing the leftmost column

 for (int i = 0; i < R; i++)

 {

 if (maze[i][0] == 0)

 maze[i][0] = 1;

 

 // If we encounter a blocked cell in leftmost

 // row, there is no way of visiting any cell

 // directly below it.

 else

 break;

 }

 

 // Similarly initialize the topmost row

 for (int i = 1; i < C; i++)

 {

 if (maze[0][i] == 0)

 maze[0][i] = 1;

 

 // If we encounter a blocked cell in bottommost

 // row, there is no way of visiting any cell

 // directly below it.

 else

 break;

 }

 

 // The only difference is that if a cell is -1,

 // simply ignore it else recursively compute

 // count value maze[i][j]

 for (int i = 1; i < R; i++) 

 {

 for (int j = 1; j < C; j++) 

 {

 

 // If blockage is found, ignore this cell

 if (maze[i][j] == -1)

 continue;

 

 // If we can reach maze[i][j] from

 // maze[i-1][j] then increment count.

 if (maze[i - 1][j] > 0)

 maze[i][j] = (maze[i][j] + 

 maze[i - 1][j]);

 

 // If we can reach maze[i][j] from 

 // maze[i][j-1] then increment count.

 if (maze[i][j - 1] > 0)

 maze[i][j] = (maze[i][j] +

 maze[i][j - 1]);

 }

 }

 

 // If the final cell is blocked, 

 // output 0, otherwise the answer

 return (maze[R - 1][C - 1] > 0) ?

 maze[R - 1][C - 1] : 0;

}

 

// Function to return the count of all possible

// paths from (0, 0) to (n - 1, m - 1)

static int numberOfPaths(int m, int n)

{

 // We have to calculate m+n-2 C n-1 here

 // which will be (m+n-2)! / (n-1)! (m-1)!

 int path = 1;

 for (int i = n; i < (m + n - 1); i++)

 {

 path *= i;

 path /= (i - n + 1);

 }

 return path;

}

 

// Function to return the total count of paths

// from (0, 0) to (n - 1, m - 1) that pass

// through at least one of the marked cells

static int solve(int maze[][])

{

 

 // Total count of paths - Total paths that do not

 // pass through any of the marked cell

 int ans = numberOfPaths(R, C) - countPaths(maze);

 

 // return answer

 return ans;

}

 

// Driver code

public static void main (String[] args) 

{

 int maze[][] = { { 0, 0, 0, 0 },

 { 0, -1, 0, 0 },

 { -1, 0, 0, 0 },

 { 0, 0, 0, 0 } };

 

 System.out.println(solve(maze));

}

}

 

// This code is contributed by anuj_67..  
  
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

R = 4

C = 4

 

# Function to return the count of 

# possible paths in a maze[R][C] 

# from (0, 0) to (R-1, C-1) that

# do not pass through any of 

# the marked cells

def countPaths(maze):

 

 # If the initial cell is blocked, 

 # there is no way of moving anywhere

 if (maze[0][0] == -1):

 return 0

 

 # Initializing the leftmost column

 for i in range(R):

 if (maze[i][0] == 0):

 maze[i][0] = 1

 

 # If we encounter a blocked cell 

 # in leftmost row, there is no way of 

 # visiting any cell directly below it.

 else:

 break

 

 # Similarly initialize the topmost row

 for i in range(1, C):

 if (maze[0][i] == 0):

 maze[0][i] = 1

 

 # If we encounter a blocked cell in 

 # bottommost row, there is no way of 

 # visiting any cell directly below it.

 else:

 break

 

 # The only difference is that if 

 # a cell is -1, simply ignore it 

 # else recursively compute 

 # count value maze[i][j]

 for i in range(1, R):

 for j in range(1, C):

 

 # If blockage is found, 

 # ignore this cell

 if (maze[i][j] == -1):

 continue

 

 # If we can reach maze[i][j] from 

 # maze[i-1][j] then increment count.

 if (maze[i - 1][j] > 0):

 maze[i][j] = (maze[i][j] +

 maze[i - 1][j])

 

 # If we can reach maze[i][j] from 

 # maze[i][j-1] then increment count.

 if (maze[i][j - 1] > 0):

 maze[i][j] = (maze[i][j] +

 maze[i][j - 1])

 

 # If the final cell is blocked, 

 # output 0, otherwise the answer

 if (maze[R - 1][C - 1] > 0):

 return maze[R - 1][C - 1]

 else:

 return 0

 

# Function to return the count of 

# all possible paths from 

# (0, 0) to (n - 1, m - 1)

def numberOfPaths(m, n):

 

 # We have to calculate m+n-2 C n-1 here

 # which will be (m+n-2)! / (n-1)! (m-1)!

 path = 1

 for i in range(n, m + n - 1):

 

 path *= i

 path //= (i - n + 1)

 

 return path

 

# Function to return the total count 

# of paths from (0, 0) to (n - 1, m - 1) 

# that pass through at least one 

# of the marked cells

def solve(maze):

 

 # Total count of paths - Total paths 

 # that do not pass through any of 

 # the marked cell

 ans = (numberOfPaths(R, C) -

 countPaths(maze))

 

 # return answer

 return ans

 

# Driver code

maze = [[ 0, 0, 0, 0 ],

 [ 0, -1, 0, 0 ],

 [ -1, 0, 0, 0 ],

 [ 0, 0, 0, 0 ]]

 

print(solve(maze))

 

# This code is contributed

# by Mohit Kumar  
  
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

// C# implementation of the approach

using System;

class GFG 

{

static int R = 4;

static int C = 4;

 

// Function to return the count of possible paths

// in a maze[R][C] from (0, 0) to (R-1, C-1) that

// do not pass through any of the marked cells

static int countPaths(int [,]maze)

{

 

 // If the initial cell is blocked, 

 // there is no way of moving anywhere

 if (maze[0, 0] == -1)

 return 0;

 

 // Initializing the leftmost column

 for (int i = 0; i < R; i++)

 {

 if (maze[i, 0] == 0)

 maze[i, 0] = 1;

 

 // If we encounter a blocked cell in leftmost

 // row, there is no way of visiting any cell

 // directly below it.

 else

 break;

 }

 

 // Similarly initialize the topmost row

 for (int i = 1; i < C; i++)

 {

 if (maze[0, i] == 0)

 maze[0, i] = 1;

 

 // If we encounter a blocked cell in 

 // bottommost row, there is no way of 

 // visiting any cell directly below it.

 else

 break;

 }

 

 // The only difference is that if a cell is -1,

 // simply ignore it else recursively compute

 // count value maze[i][j]

 for (int i = 1; i < R; i++) 

 {

 for (int j = 1; j < C; j++) 

 {

 

 // If blockage is found, ignore this cell

 if (maze[i, j] == -1)

 continue;

 

 // If we can reach maze[i][j] from

 // maze[i-1][j] then increment count.

 if (maze[i - 1, j] > 0)

 maze[i, j] = (maze[i, j] + 

 maze[i - 1, j]);

 

 // If we can reach maze[i][j] from 

 // maze[i][j-1] then increment count.

 if (maze[i, j - 1] > 0)

 maze[i, j] = (maze[i, j] +

 maze[i, j - 1]);

 }

 }

 

 // If the final cell is blocked, 

 // output 0, otherwise the answer

 return (maze[R - 1, C - 1] > 0) ?

 maze[R - 1, C - 1] : 0;

}

 

// Function to return the count of all possible

// paths from (0, 0) to (n - 1, m - 1)

static int numberOfPaths(int m, int n)

{

 // We have to calculate m+n-2 C n-1 here

 // which will be (m+n-2)! / (n-1)! (m-1)!

 int path = 1;

 for (int i = n; i < (m + n - 1); i++)

 {

 path *= i;

 path /= (i - n + 1);

 }

 return path;

}

 

// Function to return the total count of paths

// from (0, 0) to (n - 1, m - 1) that pass

// through at least one of the marked cells

static int solve(int [,]maze)

{

 

 // Total count of paths - Total paths that do not

 // pass through any of the marked cell

 int ans = numberOfPaths(R, C) - 

 countPaths(maze);

 

 // return answer

 return ans;

}

 

// Driver code

public static void Main () 

{

 int [,]maze = {{ 0, 0, 0, 0 },

 { 0, -1, 0, 0 },

 { -1, 0, 0, 0 },

 { 0, 0, 0, 0 }};

 

 Console.Write(solve(maze));

}

}

 

// This code is contributed by anuj_67..  
  
---  
  
 __

 __

 **Output:**

    
    
    16
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save


Maximum sum path in a Matrix



Given an **n*m** matrix, the task is to find the maximum sum of elements of
cells starting from the cell (0, 0) to cell (n-1, m-1).  
However, the allowed moves are right, downwards or diagonally right, i.e, from
location (i, j) next move can be **(i+1, j)** , or, **(i, j+1)** , or **(i+1,
j+1)**. Find the maximum sum of elements satisfying the allowed moves.  
 **Examples:**

    
    
    **Input:**
    mat[][] = {{100, -350, -200},
               {-100, -300, 700}}
    **Output:** 500
    **Explanation:** 
    Path followed is 100 -> -300 -> 700
    
    **Input:**
    mat[][] = {{500, 100, 230},
               {1000, 300, 100},
               {200, 1000, 200}}
    **Output:** 3000
    **Explanation:**
    Path followed is 500 -> 1000 -> 300 -> 1000 -> 200
    

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:** Dynamic programming is used to solve the above problem in a
recursive way.

  1. Allot a position at the beginning of the matrix at (0, 0).
  2. Check each next allowed position from the current position and select the path with maximum sum.
  3. Take care of the boundaries of the matrix, i.e, if the position reaches the last row or last column then the only possible choice will be right or downwards respectively.
  4. Use a map to store track of all the visiting positions and before visiting any (i, j), check whether or not the position is visited before.
  5. Update the maximum of all possible paths returned by each recursive calls made.
  6. Go till the position reaches the destination cell, i.e, (n-1.m-1).

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

#include<bits/stdc++.h>

using namespace std;

#define N 100

// No of rows and columns

int n, m;

// Declaring the matrix of maximum

// 100 rows and 100 columns

int a[N][N];

// Variable visited is used to keep

// track of all the visited positions

// Variable dp is used to store

// maximum sum till current position

vector<vector<int> > dp(N, vector<int>(N)),

 visited(N, vector<int>(N));

// For storing current sum

int current_sum = 0;

// For continuous update of

// maximum sum required

int total_sum = 0;

// Function to Input the matrix of size n*m

void inputMatrix()

{

 n = 3;

 m = 3;

 a[0][0] = 500;

 a[0][1] = 100;

 a[0][2] = 230;

 a[1][0] = 1000;

 a[1][1] = 300;

 a[1][2] = 100;

 a[2][0] = 200;

 a[2][1] = 1000;

 a[2][2] = 200;

}

// Function to calculate maximum sum of path

int maximum_sum_path(int i, int j)

{

 // Checking boundary condition

 if (i == n - 1 && j == m - 1)

 return a[i][j];

 // Checking whether or not (i, j) is visited

 if (visited[i][j])

 return dp[i][j];

 // Marking (i, j) is visited

 visited[i][j] = 1;

 // Updating the maximum sum till

 // the current position in the dp

 int& total_sum = dp[i][j];

 // Checking whether the position hasn't

 // visited the last row or the last column.

 // Making recursive call for all the possible

 // moves from the current cell and then adding the

 // maximum returned by the calls and updating it.

 if (i < n - 1 & j < m - 1) {

 int current_sum = max(maximum_sum_path(i, j + 1),

 max(

 maximum_sum_path(i + 1, j + 1),

 maximum_sum_path(i + 1, j)));

 total_sum = a[i][j] + current_sum;

 }

 // Checking whether

 // position has reached last row

 else if (i == n - 1)

 total_sum = a[i][j]

 + maximum_sum_path(i, j + 1);

 // If the position is in the last column

 else

 total_sum = a[i][j]

 + maximum_sum_path(i + 1, j);

 // Returning the updated maximum value

 return total_sum;

}

// Driver Code

int main()

{

 inputMatrix();

 // Calling the implemented function

 int maximum_sum = maximum_sum_path(0, 0);

 cout << maximum_sum;

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

class GFG{

 

static final int N = 100;

// No of rows and columns

static int n, m;

// Declaring the matrix of maximum

// 100 rows and 100 columns

static int a[][] = new int[N][N];

// Variable visited is used to keep

// track of all the visited positions

// Variable dp is used to store

// maximum sum till current position

static int dp[][] = new int[N][N];

static int visited[][] = new int[N][N];

// For storing current sum

static int current_sum = 0;

// For continuous update of

// maximum sum required

static int total_sum = 0;

// Function to Input the matrix

// of size n*m

static void inputMatrix()

{

 n = 3;

 m = 3;

 a[0][0] = 500;

 a[0][1] = 100;

 a[0][2] = 230;

 a[1][0] = 1000;

 a[1][1] = 300;

 a[1][2] = 100;

 a[2][0] = 200;

 a[2][1] = 1000;

 a[2][2] = 200;

}

// Function to calculate maximum sum of path

static int maximum_sum_path(int i, int j)

{

 

 // Checking boundary condition

 if (i == n - 1 && j == m - 1)

 return a[i][j];

 // Checking whether or not

 // (i, j) is visited

 if (visited[i][j] != 0)

 return dp[i][j];

 // Marking (i, j) is visited

 visited[i][j] = 1;

 int total_sum = 0;

 // Checking whether the position hasn't

 // visited the last row or the last column.

 // Making recursive call for all the possible

 // moves from the current cell and then adding the

 // maximum returned by the calls and updating it.

 if (i < n - 1 & j < m - 1)

 {

 int current_sum = Math.max(

 maximum_sum_path(i, j + 1),

 Math.max(

 maximum_sum_path(i + 1, j + 1),

 maximum_sum_path(i + 1, j)));

 total_sum = a[i][j] + current_sum;

 }

 // Checking whether position

 // has reached last row

 else if (i == n - 1)

 total_sum = a[i][j] +

 maximum_sum_path(i, j + 1);

 // If the position is in the last column

 else

 total_sum = a[i][j] +

 maximum_sum_path(i + 1, j);

 // Updating the maximum sum till

 // the current position in the dp

 dp[i][j] = total_sum;

 // Returning the updated maximum value

 return total_sum;

}

// Driver Code

public static void main(String[] args)

{

 inputMatrix();

 // Calling the implemented function

 int maximum_sum = maximum_sum_path(0, 0);

 System.out.println(maximum_sum);

}

}

// This code is contributed by jrishabh99  
  
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

// C# program to implement

// the above approach

using System;

class GFG{

static readonly int N = 100;

// No of rows and columns

static int n, m;

// Declaring the matrix of maximum

// 100 rows and 100 columns

static int[,]a = new int[N, N];

// Variable visited is used to keep

// track of all the visited positions

// Variable dp is used to store

// maximum sum till current position

static int [,]dp = new int[N, N];

static int [,]visited = new int[N, N];

// For storing current sum

static int current_sum = 0;

// For continuous update of

// maximum sum required

static int total_sum = 0;

// Function to Input the matrix

// of size n*m

static void inputMatrix()

{

 n = 3;

 m = 3;

 a[0, 0] = 500;

 a[0, 1] = 100;

 a[0, 2] = 230;

 a[1, 0] = 1000;

 a[1, 1] = 300;

 a[1, 2] = 100;

 a[2, 0] = 200;

 a[2, 1] = 1000;

 a[2, 2] = 200;

}

// Function to calculate maximum

// sum of path

static int maximum_sum_path(int i,

 int j)

{

 // Checking boundary condition

 if (i == n - 1 && j == m - 1)

 return a[i, j];

 // Checking whether or not

 // (i, j) is visited

 if (visited[i, j] != 0)

 return dp[i, j];

 // Marking (i, j) is visited

 visited[i, j] = 1;

 int total_sum = 0;

 // Checking whether the position

 // hasn't visited the last row

 // or the last column.

 // Making recursive call for all

 // the possible moves from the

 // current cell and then adding the

 // maximum returned by the calls

 // and updating it.

 if (i < n - 1 & j < m - 1)

 {

 int current_sum = Math.Max(maximum_sum_path(i, j + 1),

 Math.Max(maximum_sum_path(i + 1,

 j + 1),

 maximum_sum_path(i + 1, j)));

 total_sum = a[i, j] + current_sum;

 }

 // Checking whether position

 // has reached last row

 else if (i == n - 1)

 total_sum = a[i, j] +

 maximum_sum_path(i, j + 1);

 // If the position is

 // in the last column

 else

 total_sum = a[i, j] +

 maximum_sum_path(i + 1, j);

 // Updating the maximum

 // sum till the current

 // position in the dp

 dp[i, j] = total_sum;

 // Returning the updated

 // maximum value

 return total_sum;

}

// Driver Code

public static void Main(String[] args)

{

 inputMatrix();

 // Calling the implemented function

 int maximum_sum = maximum_sum_path(0, 0);

 Console.WriteLine(maximum_sum);

}

}

// This code is contributed by shikhasingrajput  
  
---  
  
 __

 __

 **Output**

    
    
    3000
    
    
    

**Time Complexity:** O(N*M)  
 **Auxiliary Space:** O(N*M)

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save


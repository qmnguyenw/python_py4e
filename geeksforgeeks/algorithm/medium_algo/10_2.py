A variation of Rat in a Maze : multiple steps or jumps allowed



A variation of rat in a maze.  
You are given an **N * N** 2-D matrix shaped maze (let’s call it M), there is
a rat in the **top-left cell** i.e. **M[0][0]** and there is an escape door in
the **bottom-right cell** i.e. **M[N-1][N-1]**. From each cell **M[i][j]** (0
≤ i ≤ N-1, 0 ≤ j ≤ N-1) the rat can go a number of steps towards its right (
for eg: to M[i][j+ s]), or a number of steps downwards ( for eg: to M[i+
s][j]), where the maximum number of steps (or maximum value of s) can be the
value in the cell **M[i][j]**. If any cell contains **0** then that is a
**dead-end**. **For eg:** In the second picture in the figure below, the rat
at **M[0][0]** can jump to a cell : **M[0][1]** , **M[0][2]** , **M[1][0]** or
**M[2][0]**.

![](https://media.geeksforgeeks.org/wp-content/uploads/problem-
pics-1-300x170.png)

You have to print a possible path **from M[0][0] to M[N-1][N-1]** in the form
of a matrix of size **N * N** such that the cells that are in the path have a
value **1** and other cells have a value **0**. For the above example one such
solution is :

![](https://media.geeksforgeeks.org/wp-
content/uploads/solution-3-1-281x300.png)

There is a **backtracking solution** for this problem in this article.

  

  

 **Here a Dynamic Programming based solution is presented.**

 **Examples:**

>  **Input:** mat[][] = {  
> {3, 0, 0, 2, 1},  
> {0, 0, 0, 0, 2},  
> {0, 1, 0, 1, 0},  
> {1, 0, 0, 1, 1},  
> {3, 0, 0, 1, 1} }  
>  **Output:**  
>  1 0 0 1 1  
> 0 0 0 0 1  
> 0 0 0 0 0  
> 0 0 0 0 1  
> 0 0 0 0 1
>
>  **Input:** mat[][] = { {0, 0}, {0, 1} }  
>  **Output:** No path exists

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:**

  * Initialize a boolean **CRF[N][N]** (can reach from) matrix with **false**. Now make **CRF[N – 1][N – 1] = true** as destination can be reached from the destination.
  * Now, starting from **maze[N – 1][N – 1]** and ending at **maze[0][0]** update all the cells in **CRF[][]** according to whether it is possible to reach any other valid cell (leading to the destination).
  * When all of the **CRF[][]** matrix has been updated, use to create a matrix which contains all **1s** at the cells in the path leading to the destination and other cells are **0s**.
  * Print this newly created matrix in the end.
  * If it is not possible to reach the destination then print **No path exists**.

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

#include <iostream>

using namespace std;

#define MAX 50

 

// Function to check whether the path exists

bool hasPath(int maze[][MAX], int sol[][MAX], 

 int N)

{

 

 for (int i = 0; i < N; i++)

 for (int j = 0; j < N; j++)

 sol[i][j] = 0;

 

 // Declaring and initializing CRF

 // (can reach from) matrix

 bool** CRF = new bool*[N];

 for (int i = 0; i < N; i++)

 CRF[i] = new bool[N];

 

 for (int i = 0; i < N; i++)

 for (int j = 0; j < N; j++)

 CRF[i][j] = false;

 CRF[N - 1][N - 1] = true;

 

 // Using the DP to fill CRF matrix 

 // in correct order

 for (int k = N - 1; k >= 0; k--) {

 for (int j = k; j >= 0; j--) {

 

 if (!(k == N - 1 && j == N - 1)) {

 

 // If it is possible to get 

 // to a valid location from 

 // cell maze[k][j]

 for (int a = 0; a <= maze[k][j]; a++) {

 if ((j + a < N && CRF[k][j + a] == true)

 || (k + a < N && CRF[k + a][j] == true)) {

 CRF[k][j] = true;

 break;

 }

 }

 

 // If it is possible to get to 

 // a valid location from cell

 // maze[j][k]

 for (int a = 0; a <= maze[j][k]; a++) {

 if ((k + a < N && CRF[j][k + a] == true)

 || (j + a < N && CRF[j + a][k] == true)) {

 CRF[j][k] = true;

 break;

 }

 }

 }

 }

 }

 

 // If CRF[0][0] is false it means we cannot reach

 // the end of the maze at all

 if (CRF[0][0] == false)

 return false;

 

 // Filling the solution matrix using CRF

 int i = 0, j = 0;

 while (!(i == N - 1 && j == N - 1)) {

 sol[i][j] = 1;

 if (maze[i][j] > 0)

 

 // Get to a valid location from 

 // the current cell

 for (int a = 1; a <= maze[i][j]; a++) {

 if ((j + a < N && CRF[i][j + a] == true)) {

 j = j + a;

 break;

 }

 else if ((i + a < N && CRF[i + a][j] == true)) {

 i = i + a;

 break;

 }

 }

 }

 sol[N - 1][N - 1] = 1;

 

 return true;

}

 

// Utility function to print the contents

// of a 2-D array

void printMatrix(int sol[][MAX], int N)

{

 for (int i = 0; i < N; i++) {

 for (int j = 0; j < N; j++)

 cout << sol[i][j] << " ";

 cout << "\n";

 }

}

 

// Driver code

int main()

{

 

 int maze[][MAX] = { { 2, 2, 1, 1, 0 },

 { 0, 0, 3, 0, 0 }, 

 { 1, 0, 0, 0, 0 }, 

 { 0, 0, 2, 0, 1 },

 { 0, 0, 3, 0, 0 } };

 int N = sizeof(maze) / sizeof(maze[0]);

 int sol[N][MAX];

 

 // If path exists

 if (hasPath(maze, sol, N))

 

 // Print the path

 printMatrix(sol, N);

 else

 cout << "No path exists";

 

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

class GFG 

{

static int MAX = 50;

 

// Function to check whether the path exists

static boolean hasPath(int maze[][], 

 int sol[][], int N)

{

 for (int i = 0; i < N; i++)

 for (int j = 0; j < N; j++)

 sol[i][j] = 0;

 

 // Declaring and initializing CRF

 // (can reach from) matrix

 boolean [][]CRF = new boolean[N][N];

 

 CRF[N - 1][N - 1] = true;

 

 // Using the DP to fill CRF matrix 

 // in correct order

 for (int k = N - 1; k >= 0; k--) 

 {

 for (int j = k; j >= 0; j--) 

 {

 

 if (!(k == N - 1 && j == N - 1))

 {

 

 // If it is possible to get 

 // to a valid location from 

 // cell maze[k][j]

 for (int a = 0; a <= maze[k][j]; a++)

 {

 if ((j + a < N && CRF[k][j + a] == true) || 

 (k + a < N && CRF[k + a][j] == true)) 

 {

 CRF[k][j] = true;

 break;

 }

 }

 

 // If it is possible to get to 

 // a valid location from cell

 // maze[j][k]

 for (int a = 0; a <= maze[j][k]; a++) 

 {

 if ((k + a < N && CRF[j][k + a] == true) ||

 (j + a < N && CRF[j + a][k] == true)) 

 {

 CRF[j][k] = true;

 break;

 }

 }

 }

 }

 }

 

 // If CRF[0][0] is false it means we cannot reach

 // the end of the maze at all

 if (CRF[0][0] == false)

 return false;

 

 // Filling the solution matrix using CRF

 int i = 0, j = 0;

 while (!(i == N - 1 && j == N - 1))

 {

 sol[i][j] = 1;

 if (maze[i][j] > 0)

 

 // Get to a valid location from 

 // the current cell

 for (int a = 1; a <= maze[i][j]; a++) 

 {

 if ((j + a < N && CRF[i][j + a] == true)) 

 {

 j = j + a;

 break;

 }

 else if ((i + a < N && CRF[i + a][j] == true)) 

 {

 i = i + a;

 break;

 }

 }

 }

 sol[N - 1][N - 1] = 1;

 

 return true;

}

 

// Utility function to print the contents

// of a 2-D array

static void printMatrix(int sol[][], int N)

{

 for (int i = 0; i < N; i++)

 {

 for (int j = 0; j < N; j++)

 System.out.print(sol[i][j] + " ");

 System.out.println();

 }

}

 

// Driver code

public static void main(String[] args) 

{

 int maze[][] = {{ 2, 2, 1, 1, 0 },

 { 0, 0, 3, 0, 0 }, 

 { 1, 0, 0, 0, 0 }, 

 { 0, 0, 2, 0, 1 },

 { 0, 0, 3, 0, 0 }};

 int N = maze.length;

 int [][]sol = new int [N][MAX];

 

 // If path exists

 if (hasPath(maze, sol, N))

 

 // Print the path

 printMatrix(sol, N);

 else

 System.out.println("No path exists");

 }

}

 

// This code is contributed by Princi Singh  
  
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

static int MAX = 50;

 

// Function to check whether the path exists

static Boolean hasPath(int [,]maze,

 int [,]sol, int N)

{

 int i, j, k;

 for (i = 0; i < N; i++)

 for (j = 0; j < N; j++)

 sol[i, j] = 0;

 

 // Declaring and initializing CRF

 // (can reach from) matrix

 Boolean [,]CRF = new Boolean[N, N];

 

 CRF[N - 1, N - 1] = true;

 

 // Using the DP to fill CRF matrix 

 // in correct order

 for (k = N - 1; k >= 0; k--) 

 {

 for (j = k; j >= 0; j--) 

 {

 if (!(k == N - 1 && j == N - 1))

 {

 

 // If it is possible to get 

 // to a valid location from 

 // cell maze[k,j]

 for (int a = 0; a <= maze[k, j]; a++)

 {

 if ((j + a < N && CRF[k, j + a] == true) || 

 (k + a < N && CRF[k + a, j] == true)) 

 {

 CRF[k, j] = true;

 break;

 }

 }

 

 // If it is possible to get to 

 // a valid location from cell

 // maze[j,k]

 for (int a = 0; a <= maze[j, k]; a++) 

 {

 if ((k + a < N && CRF[j, k + a] == true) ||

 (j + a < N && CRF[j + a, k] == true)) 

 {

 CRF[j, k] = true;

 break;

 }

 }

 }

 }

 }

 

 // If CRF[0,0] is false it means we cannot 

 // reach the end of the maze at all

 if (CRF[0, 0] == false)

 return false;

 

 // Filling the solution matrix using CRF

 i = 0; j = 0;

 while (!(i == N - 1 && j == N - 1))

 {

 sol[i, j] = 1;

 if (maze[i, j] > 0)

 

 // Get to a valid location from 

 // the current cell

 for (int a = 1; a <= maze[i, j]; a++) 

 {

 if ((j + a < N && 

 CRF[i, j + a] == true)) 

 {

 j = j + a;

 break;

 }

 else if ((i + a < N && 

 CRF[i + a, j] == true)) 

 {

 i = i + a;

 break;

 }

 }

 }

 sol[N - 1, N - 1] = 1;

 

 return true;

}

 

// Utility function to print the contents

// of a 2-D array

static void printMatrix(int [,]sol, int N)

{

 for (int i = 0; i < N; i++)

 {

 for (int j = 0; j < N; j++)

 Console.Write(sol[i, j] + " ");

 Console.WriteLine();

 }

}

 

// Driver code

public static void Main(String[] args) 

{

 int [,]maze = {{ 2, 2, 1, 1, 0 },

 { 0, 0, 3, 0, 0 }, 

 { 1, 0, 0, 0, 0 }, 

 { 0, 0, 2, 0, 1 },

 { 0, 0, 3, 0, 0 }};

 int N = maze.GetLength(0);

 int [,]sol = new int [N, MAX];

 

 // If path exists

 if (hasPath(maze, sol, N))

 

 // Print the path

 printMatrix(sol, N);

 else

 Console.WriteLine("No path exists");

 }

}

 

// This code is contributed by Rajput-Ji  
  
---  
  
 __

 __

 **Output:**

    
    
    1 1 1 0 0 
    0 0 1 0 0 
    0 0 0 0 0 
    0 0 1 0 0 
    0 0 1 0 1
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


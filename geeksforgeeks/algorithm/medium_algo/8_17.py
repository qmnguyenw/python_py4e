Number of connected components in a 2-D matrix of strings



Given a 2-D matrix **mat[][]** the task is count the number of connected
components in the matrix. A connected component is formed by all equal
elements that share some common side with at least one other element of the
same component.

 **Examples:**

    
    
    **Input:** mat[][] = {"bbba", 
                                       "baaa"}
    **Output:** 2
    The two connected components are:
    bbb       
    b
    
    AND
    
      a
    aaa
    
    **Input:** mat[][] = {"aabba", 
                                       "aabba", 
                                       "aaaca"}
    **Output:** 4
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** For every cell that hasn’t been visited before perform DFS. DFS
will cover all the connected cells (up, left, right and down) with same value.
So the answer would be the total times DFS is run.

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

#define maxRow 500

#define maxCol 500

 

bool visited[maxRow][maxCol] = { 0 };

 

// Function that return true if mat[row][col]

// is valid and hasn't been visited

bool isSafe(string M[], int row, int col, char c, 

 int n, int l)

{

 // If row and column are valid and element 

 // is matched and hasn't been visited then 

 // the cell is safe

 return (row >= 0 && row < n)

 && (col >= 0 && col < l)

 && (M[row][col] == c && !visited[row][col]);

}

 

// Function for depth first search

void DFS(string M[], int row, int col, char c, 

 int n, int l)

{

 // These arrays are used to get row and column

 // numbers of 4 neighbours of a given cell

 int rowNbr[] = { -1, 1, 0, 0 };

 int colNbr[] = { 0, 0, 1, -1 };

 

 // Mark this cell as visited

 visited[row][col] = true;

 

 // Recur for all connected neighbours

 for (int k = 0; k < 4; ++k)

 if (isSafe(M, row + rowNbr[k],

 col + colNbr[k], c, n, l))

 

 DFS(M, row + rowNbr[k], 

 col + colNbr[k], c, n, l);

}

 

// Function to return the number of

// connectewd components in the matrix

int connectedComponents(string M[], int n)

{

 int connectedComp = 0;

 int l = M[0].length();

 

 for (int i = 0; i < n; i++) {

 for (int j = 0; j < l; j++) {

 if (!visited[i][j]) {

 char c = M[i][j];

 DFS(M, i, j, c, n, l);

 connectedComp++;

 }

 }

 }

 

 return connectedComp;

}

 

// Driver code

int main()

{

 string M[] = {"aabba", "aabba", "aaaca"};

 int n = sizeof(M)/sizeof(M[0]);

 

 cout << connectedComponents(M, n);

 

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

static final int maxRow = 500;

static final int maxCol = 500;

 

static boolean visited[][] = new boolean[maxRow][maxCol];

 

// Function that return true if mat[row][col]

// is valid and hasn't been visited

static boolean isSafe(String M[], int row, int col, 

 char c, int n, int l) 

{

 // If row and column are valid and element 

 // is matched and hasn't been visited then 

 // the cell is safe

 return (row >= 0 && row < n) && 

 (col >= 0 && col < l) &&

 (M[row].charAt(col) == c &&

 !visited[row][col]);

}

 

// Function for depth first search

static void DFS(String M[], int row, int col, 

 char c, int n, int l) 

{

 // These arrays are used to get row and column

 // numbers of 4 neighbours of a given cell

 int rowNbr[] = {-1, 1, 0, 0};

 int colNbr[] = {0, 0, 1, -1};

 

 // Mark this cell as visited

 visited[row][col] = true;

 

 // Recur for all connected neighbours

 for (int k = 0; k < 4; ++k)

 {

 if (isSafe(M, row + rowNbr[k],

 col + colNbr[k], c, n, l)) 

 {

 DFS(M, row + rowNbr[k],

 col + colNbr[k], c, n, l);

 }

 }

}

 

// Function to return the number of

// connectewd components in the matrix

static int connectedComponents(String M[], int n) 

{

 int connectedComp = 0;

 int l = M[0].length();

 

 for (int i = 0; i < n; i++) 

 {

 for (int j = 0; j < l; j++) 

 {

 if (!visited[i][j])

 {

 char c = M[i].charAt(j);

 DFS(M, i, j, c, n, l);

 connectedComp++;

 }

 }

 }

 

 return connectedComp;

}

 

// Driver code

public static void main(String[] args) 

{

 String M[] = {"aabba", "aabba", "aaaca"};

 int n = M.length;

 System.out.println(connectedComponents(M, n));

}

}

 

// This code contributed by PrinciRaj1992   
  
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

import numpy as np

 

maxRow = 500

maxCol = 500

 

visited = np.zeros((maxCol, maxRow))

 

# Function that return true if mat[row][col] 

# is valid and hasn't been visited 

def isSafe(M, row, col, c, n, l) :

 

 # If row and column are valid and element 

 # is matched and hasn't been visited then 

 # the cell is safe 

 return ((row >= 0 and row < n) and

 (col >= 0 and col < l) and

 (M[row][col] == c and not

 visited[row][col])); 

 

# Function for depth first search 

def DFS(M, row, col, c, n, l) : 

 

 # These arrays are used to get row 

 # and column numbers of 4 neighbours 

 # of a given cell 

 rowNbr = [ -1, 1, 0, 0 ]; 

 colNbr = [ 0, 0, 1, -1 ]; 

 

 # Mark this cell as visited 

 visited[row][col] = True; 

 

 # Recur for all connected neighbours 

 for k in range(4) :

 if (isSafe(M, row + rowNbr[k], 

 col + colNbr[k], c, n, l)) :

 

 DFS(M, row + rowNbr[k], 

 col + colNbr[k], c, n, l); 

 

# Function to return the number of 

# connectewd components in the matrix 

def connectedComponents(M, n) :

 

 connectedComp = 0; 

 l = len(M[0]); 

 

 for i in range(n) :

 for j in range(l) :

 if (not visited[i][j]) : 

 c = M[i][j]; 

 DFS(M, i, j, c, n, l); 

 connectedComp += 1; 

 

 return connectedComp; 

 

# Driver code 

if __name__ == "__main__" :

 

 M = ["aabba", "aabba", "aaaca"]; 

 n = len(M)

 

 print(connectedComponents(M, n)); 

 

# This code is contributed by Ryuga  
  
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

 

static readonly int maxRow = 500;

static readonly int maxCol = 500;

 

static bool [,]visited = new bool[maxRow,maxCol];

 

// Function that return true if mat[row,col]

// is valid and hasn't been visited

static bool isSafe(String []M, int row, int col, 

 char c, int n, int l) 

{

 // If row and column are valid and element 

 // is matched and hasn't been visited then 

 // the cell is safe

 return (row >= 0 && row < n) && 

 (col >= 0 && col < l) &&

 (M[row][col] == c &&

 !visited[row,col]);

}

 

// Function for depth first search

static void DFS(String []M, int row, int col, 

 char c, int n, int l) 

{

 // These arrays are used to get row and column

 // numbers of 4 neighbours of a given cell

 int []rowNbr = {-1, 1, 0, 0};

 int []colNbr = {0, 0, 1, -1};

 

 // Mark this cell as visited

 visited[row,col] = true;

 

 // Recur for all connected neighbours

 for (int k = 0; k < 4; ++k)

 {

 if (isSafe(M, row + rowNbr[k],

 col + colNbr[k], c, n, l)) 

 {

 DFS(M, row + rowNbr[k],

 col + colNbr[k], c, n, l);

 }

 }

}

 

// Function to return the number of

// connectewd components in the matrix

static int connectedComponents(String []M, int n) 

{

 int connectedComp = 0;

 int l = M[0].Length;

 

 for (int i = 0; i < n; i++) 

 {

 for (int j = 0; j < l; j++) 

 {

 if (!visited[i,j])

 {

 char c = M[i][j];

 DFS(M, i, j, c, n, l);

 connectedComp++;

 }

 }

 }

 

 return connectedComp;

}

 

// Driver code

public static void Main(String[] args) 

{

 String []M = {"aabba", "aabba", "aaaca"};

 int n = M.Length;

 Console.WriteLine(connectedComponents(M, n));

}

}

 

// This code contributed by Rajput-Ji  
  
---  
  
 __

 __

 **Output:**

    
    
    4
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save


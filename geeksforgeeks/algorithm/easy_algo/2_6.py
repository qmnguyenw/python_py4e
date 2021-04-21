Return an array of anti-diagonals of given N*N square matrix



Given a square matrix of size N*N, return an array of its anti-diagonals. For
better understanding let us look at the image given below:

 **Examples:**

    
    
    **Input :**

![null](https://media.geeksforgeeks.org/wp-
content/uploads/20200410232131/drawisland-3-1.png)

    
    
     **Output :**
     1
     2  5
     3  6  9
     4  7  10  13
     8  11 14
     12 15
     16

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach 1:**  
To solve the problem mentioned above we have two major observations.

  * The first one is, some diagonals start from the zeroth row for each column and ends when either start column >= 0 or start row < N.
  * While the second observation is that the remaining diagonals start with end column for each row and ends when either start row < N or start column >= 0.

Below is the implementation of the above approach:

  

  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation to return

// an array of its anti-diagonals

// when an N*N square matrix is given

#include <iostream>

using namespace std;

// function to print the diagonals

void diagonal(int A[3][3])

{

 int N = 3;

 // For each column start row is 0

 for (int col = 0; col < N; col++) {

 int startcol = col, startrow = 0;

 while (startcol >= 0 && startrow < N) {

 cout << A[startrow][startcol] << " ";

 startcol--;

 startrow++;

 }

 cout << "\n";

 }

 // For each row start column is N-1

 for (int row = 1; row < N; row++) {

 int startrow = row, startcol = N - 1;

 while (startrow < N && startcol >= 0) {

 cout << A[startrow][startcol] << " ";

 startcol--;

 startrow++;

 }

 cout << "\n";

 }

}

// Driver code

int main()

{

 // matrix iniliasation

 int A[3][3] = { { 1, 2, 3 }, { 4, 5, 6 }, { 7, 8, 9 } };

 diagonal(A);

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

// Java implementation to return

// an array of its anti-diagonals

// when an N*N square matrix is given

class Matrix {

 // function to print the diagonals

 void diagonal(int A[][])

 {

 int N = 3;

 // For each column start row is 0

 for (int col = 0; col < N; col++) {

 int startcol = col, startrow = 0;

 while (startcol >= 0 && startrow < N) {

 System.out.print(A[startrow][startcol]

 + " ");

 startcol--;

 startrow++;

 }

 System.out.println();

 }

 // For each row start column is N-1

 for (int row = 1; row < N; row++) {

 int startrow = row, startcol = N - 1;

 while (startrow < N && startcol >= 0) {

 System.out.print(A[startrow][startcol]

 + " ");

 startcol--;

 startrow++;

 }

 System.out.println();

 }

 }

 // Driver code

 public static void main(String args[])

 {

 // matrix initialisation

 int A[][]

 = { { 1, 2, 3 }, { 4, 5, 6 }, { 7, 8, 9
} };

 Matrix m = new Matrix();

 m.diagonal(A);

 }

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

# Python3 implementation to return

# an array of its anti-diagonals

# when an N*N square matrix is given

# function to print the diagonals

def diagonal(A):

 N = 3

 # For each column start row is 0

 for col in range(N):

 startcol = col

 startrow = 0

 while(startcol >= 0 and

 startrow < N):

 print(A[startrow][startcol], end = " ")

 startcol -= 1

 startrow += 1

 print()

 # For each row start column is N-1

 for row in range(1, N):

 startrow = row

 startcol = N - 1

 while(startrow < N and

 startcol >= 0):

 print(A[startrow][startcol],

 end=" ")

 startcol -= 1

 startrow += 1

 print()

# Driver code

if __name__ == "__main__":

 # matrix iniliasation

 A = [[1, 2, 3],

 [4, 5, 6],

 [7, 8, 9]]

 diagonal(A)

# This code is contributed by AnkitRai01  
  
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

// C# implementation to return

// an array of its anti-diagonals

// when an N*N square matrix is given

using System;

class GFG {

 // Function to print the diagonals

 static void diagonal(int[, ] A)

 {

 int N = 3;

 // For each column start row is 0

 for (int col = 0; col < N; col++) {

 int startcol = col, startrow = 0;

 while (startcol >= 0 && startrow < N) {

 Console.Write(A[startrow, startcol] + " ");

 startcol--;

 startrow++;

 }

 Console.WriteLine();

 }

 // For each row start column is N-1

 for (int row = 1; row < N; row++) {

 int startrow = row, startcol = N - 1;

 while (startrow < N && startcol >= 0) {

 Console.Write(A[startrow, startcol] + " ");

 startcol--;

 startrow++;

 }

 Console.WriteLine();

 }

 }

 // Driver code

 public static void Main(string[] args)

 {

 // Matrix initialisation

 int[, ] A

 = { { 1, 2, 3 }, { 4, 5, 6 }, { 7, 8, 9 } };

 diagonal(A);

 }

}

// This code is contributed by AnkitRai01  
  
---  
  
 __

 __

## Javascript

 __

 __  
 __

 __

 __  
 __  
 __

<script>

// Javascript implementation to return

// an array of its anti-diagonals

// when an N*N square matrix is given

// Function to print the diagonals

function diagonal(A)

{

 let N = 3;

 // For each column start row is 0

 for(let col = 0; col < N; col++)

 {

 let startcol = col, startrow = 0;

 while (startcol >= 0 && startrow < N)

 {

 document.write(A[startrow][startcol] + " ");

 startcol--;

 startrow++;

 }

 document.write("</br>");

 }

 // For each row start column is N-1

 for(let row = 1; row < N; row++)

 {

 let startrow = row, startcol = N - 1;

 while (startrow < N && startcol >= 0)

 {

 document.write(A[startrow][startcol] + " ");

 startcol--;

 startrow++;

 }

 document.write("</br>");

 }

}

// Driver code

// matrix iniliasation

let A = [ [ 1, 2, 3 ], [ 4, 5, 6 ], [ 7, 8, 9 ] ];

diagonal(A);

 

// This code is contributed by suresh07

</script>  
  
---  
  
 __

 __

 **Output:**

    
    
    1 
    2 4 
    3 5 7 
    6 8 
    9

**Time Complexity:** Time complexity of the above solution is O(N*N).

 **Approach 2: Much simpler and concise ( Same time Complexity)**

In this approach, we will make the use of sum of indices of any element in a
matrix. Let indices of any element be represented by i (row) an j (column).

If we find the sum of indices of any element in a N*N matrix, we will observe
that the sum of indices for any element lies between 0 (when i = j = 0) and
2*N – 2 (when i = j = N-1).

So we will follow the following steps:

  * Declare a vector of vectors of size 2*N – 1 for holding unique sums from sum = 0 to sum = 2*N – 2.
  * Now we will loop through the vector and pushback the elements of similar sum to same row in that vector of vectors.

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program for the above approach

#include <iostream>

#include <vector>

using namespace std;

// Function to print diagonals

void diagonal(vector<vector<int> >& A)

{

 int n = A.size();

 int N = 2 * n - 1;

 vector<vector<int> > result(N);

 // Push each element in the result vector

 for (int i = 0; i < n; i++)

 for (int j = 0; j < n; j++)

 result[i + j].push_back(A[i][j]);

 

 // Print the diagonals

 for (int i = 0; i < result.size(); i++)

 {

 cout << endl;

 for (int j = 0; j < result[i].size(); j++)

 cout << result[i][j] << " ";

 }

}

// Driver Code

int main()

{

 vector<vector<int> > A = { { 1, 2, 3, 4 },

 { 5, 6, 7, 8 },

 { 9, 10, 11, 12 },

 { 13, 14, 15, 16 } };

 

 // Function Call

 diagonal(A);

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

// Java program for the above approach

import java.util.*;

import java.lang.*;

class GFG{

 

// Function to print diagonals

static void diagonal(int[][] A)

{

 int n = A.length;

 int N = 2 * n - 1;

 

 ArrayList<ArrayList<Integer>> result = new ArrayList<>();

 

 for(int i = 0; i < N; i++)

 result.add(new ArrayList<>());

 

 // Push each element in the result vector

 for(int i = 0; i < n; i++)

 for(int j = 0; j < n; j++)

 result.get(i + j).add(A[i][j]);

 

 // Print the diagonals

 for(int i = 0; i < result.size(); i++)

 {

 System.out.println();

 for(int j = 0; j < result.get(i).size(); j++)

 System.out.print(result.get(i).get(j) + " ");

 }

}

 

// Driver code

public static void main(String[] args)

{

 int[][] A = { { 1, 2, 3, 4 },

 { 5, 6, 7, 8 },

 { 9, 10, 11, 12 },

 { 13, 14, 15, 16 } };

 

 // Function Call

 diagonal(A);

}

}

// This code is contributed by offbeat  
  
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

# Python3 program for the above approach

# Function to print diagonals

def diagonal(A) :

 n = len(A)

 N = 2 * n - 1

 result = []

 

 for i in range(N) :

 result.append([])

 

 # Push each element in the result vector

 for i in range(n) :

 for j in range(n) :

 result[i + j].append(A[i][j])

 # Print the diagonals

 for i in range(len(result)) :

 

 for j in range(len(result[i])) :

 print(result[i][j] , end = " ")

 

 print()

A = [ [ 1, 2, 3, 4 ],

 [ 5, 6, 7, 8 ],

 [ 9, 10, 11, 12 ],

 [ 13, 14, 15, 16 ] ]

# Function Call

diagonal(A)

# This code is contributed by divyesh072019  
  
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

// C# program for the above approach

using System;

using System.Collections.Generic;

class GFG {

 

 // Function to print diagonals

 static void diagonal(List<List<int>> A)

 {

 

 int n = A.Count;

 int N = 2 * n - 1;

 

 List<List<int>> result = new List<List<int>>();

 

 for (int i = 0; i < N; i++)

 {

 result.Add(new List<int>());

 }

 

 // Push each element in the result vector

 for (int i = 0; i < n; i++)

 for (int j = 0; j < n; j++)

 result[i + j].Add(A[i][j]);

 

 // Print the diagonals

 for (int i = 0; i < result.Count; i++)

 {

 for (int j = 0; j < result[i].Count; j++)

 Console.Write(result[i][j] + " ");

 Console.WriteLine();

 }

 }

 

 static void Main() {

 List<List<int>> A = new List<List<int>>();

 A.Add(new List<int> {1, 2, 3, 4});

 A.Add(new List<int> {5, 6, 7, 8});

 A.Add(new List<int> {9, 10, 11, 12});

 A.Add(new List<int> {13, 14, 15, 16});

 

 // Function Call

 diagonal(A);

 }

}  
  
---  
  
 __

 __

 **Output :**

    
    
    1  
    2 5  
    3 6 9  
    4 7 10 13  
    8 11 14  
    12 15  
    16

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


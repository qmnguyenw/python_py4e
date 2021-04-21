Construct a matrix such that union of ith row and ith column contains every
element from 1 to 2N-1



Given a number **N** , the task is to construct a **square matrix** of **N *
N** where union of elements in some **i th** row with the **i th** column
contains every element in the range [1, 2*N-1]. If no such matrix exists,
print -1.

 **Note:** There can be multiple possible solutions for a particular N

 **Examples:**

>  **Input:** N = 6  
>  **Output:**  
>  6 4 2 5 3 1  
> 10 6 5 3 1 2  
> 8 11 6 1 4 3  
> 11 9 7 6 2 4  
> 9 7 10 8 6 5  
> 7 8 9 10 11 6  
>  **Explanation:**  
>  The above matrix is of 6 * 6 in which every ith row and column contains
> elements from 1 to 11, like:  
> 1st row and 1st column = {6, 4, 2, 5, 3, 1} & {6, 10, 8, 11, 9, 7} = {1, 2,
> 3, 4, 5, 6, 7, 8, 9, 10, 11}  
> 2nd row and 2nd column = {10, 6, 5, 3, 1, 2} & {4, 6, 11, 9, 7, 8} = {1, 2,
> 3, 4, 5, 6, 7, 8, 9, 10, 11}  
> 3rd row and 3rd column = {8, 11, 6, 1, 4, 3} & {2, 5, 6, 7, 10, 9} = {1, 2,
> 3, 4, 5, 6, 7, 8, 9, 10, 11}  
> 4th row and 4th column = {11, 9, 7, 6, 2, 4} & {5, 3, 1, 6, 8, 10} = {1, 2,
> 3, 4, 5, 6, 7, 8, 9, 10, 11}  
> 5th row and 5th column = {9, 7, 10, 8, 6, 5} & {3, 1, 4, 2, 6, 11} = {1, 2,
> 3, 4, 5, 6, 7, 8, 9, 10, 11}  
> 6th row and 6th column = {7, 8, 9, 10, 11, 6} & {1, 2, 3, 4, 5, 6} = {1, 2,
> 3, 4, 5, 6, 7, 8, 9, 10, 11}
>
>  **Input:** N = 6  
>  **Output:** -1  
>  **Explanation:**  
>  There is no such matrix possible in which every i’th row and i’th column
> contains every elements from 1 to 9. Hence, the answer is -1.
>
>  
>
>
>  
>

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:**  
If we observe carefully, we can see that:

  * For any odd number except 1, the square matrix is not possible to generate
  * To generate the square matrix for even order, the idea is to fill up the **upper half of the diagonal** elements of the matrix in the range of **1 to N-1** and fill all the **diagonal elements with the N** and the **lower half of the diagonal elements** can be filled in number from range **N + 1 to 2N – 1**.

Below is the algorithm fr this approach:

  1. Matrix of odd order can’t be filled as observed except for **N = 1**
  2. For Matrix of even order,
    * Firstly, fill all diagonal elements equal to N.
    * Consider the two halves of the matrix diagonally bisected, each half can be filled with N-1 elements.
    * Fill upper half with elements from **[1, N-1]** and the lower half with elements from **[N+1, 2N-1]**.
    * As it can be easily observed that there is a pattern that second row’s last element can be always 2.
    * Now, consecutive elements in the last column are at a difference of 2. Hence generalised form can be given as **A[i]=[(N-2)+2i]%(N-1)+1** , for all i from 1 to N-1
    * Simply add _N_ to all the elements of the lower half.

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation of the above approach

 

#include <bits/stdc++.h>

using namespace std;

 

int matrix[100][100];

 

// Function to find the square matrix

void printRequiredMatrix(int n)

{

 // For Matrix of order 1,

 // it will contain only 1

 if (n == 1) {

 cout << "1"

 << "\n";

 }

 

 // For Matrix of odd order,

 // it is not possible

 else if (n % 2 != 0) {

 cout << "-1"

 << "\n";

 }

 

 // For Matrix of even order

 else {

 // All diagonal elements of the

 // matrix can be N itself.

 for (int i = 0; i < n; i++) {

 matrix[i][i] = n;

 }

 int u = n - 1;

 

 // Assign values at desired

 // place in the matrix

 for (int i = 0; i < n - 1; i++) {

 

 matrix[i][u] = i + 1;

 

 for (int j = 1; j < n / 2; j++) {

 

 int a = (i + j) % (n - 1);

 int b = (i - j + n - 1) % (n - 1);

 if (a < b)

 swap(a, b);

 matrix[b][a] = i + 1;

 }

 }

 

 // Loop to add N in the lower half

 // of the matrix such that it contains

 // elements from 1 to 2*N - 1

 for (int i = 0; i < n; i++)

 for (int j = 0; j < i; j++)

 matrix[i][j] = matrix[j][i] + n;

 

 // Loop to print the matrix

 for (int i = 0; i < n; i++) {

 for (int j = 0; j < n; j++)

 cout << matrix[i][j] << " ";

 cout << "\n";

 }

 }

 cout << "\n";

}

 

// Driver Code

int main()

{

 int n = 1;

 printRequiredMatrix(n);

 

 n = 3;

 printRequiredMatrix(n);

 

 n = 6;

 printRequiredMatrix(n);

 

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

// Java implementation of the above approach

class GFG {

 

 static int matrix[][] = new int[100][100]; 

 

 // Function to find the square matrix 

 static void printRequiredMatrix(int n) 

 { 

 // For Matrix of order 1, 

 // it will contain only 1 

 if (n == 1) { 

 System.out.println("1");

 } 

 

 // For Matrix of odd order, 

 // it is not possible 

 else if (n % 2 != 0) { 

 System.out.println("-1");

 } 

 

 // For Matrix of even order 

 else { 

 // All diagonal elements of the 

 // matrix can be N itself. 

 for (int i = 0; i < n; i++) { 

 matrix[i][i] = n; 

 } 

 int u = n - 1; 

 

 // Assign values at desired 

 // place in the matrix 

 for (int i = 0; i < n - 1; i++) { 

 

 matrix[i][u] = i + 1; 

 

 for (int j = 1; j < n / 2; j++) { 

 

 int a = (i + j) % (n - 1); 

 int b = (i - j + n - 1) % (n - 1); 

 if (a < b) {

 int temp = a;

 a = b; 

 b = temp;

 }

 matrix[b][a] = i + 1; 

 } 

 } 

 

 // Loop to add N in the lower half 

 // of the matrix such that it contains 

 // elements from 1 to 2*N - 1 

 for (int i = 0; i < n; i++) 

 for (int j = 0; j < i; j++) 

 matrix[i][j] = matrix[j][i] + n; 

 

 // Loop to print the matrix 

 for (int i = 0; i < n; i++) { 

 for (int j = 0; j < n; j++) 

 System.out.print(matrix[i][j] + " "); 

 System.out.println() ;

 } 

 } 

 System.out.println();

 } 

 

 // Driver Code 

 public static void main (String[] args) 

 { 

 int n = 1; 

 printRequiredMatrix(n); 

 

 n = 3; 

 printRequiredMatrix(n); 

 

 n = 6; 

 printRequiredMatrix(n); 

 

 } 

}

 

// This code is contributed by AnkitRai01  
  
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

# Python3 implementation of the above approach

import numpy as np;

 

matrix = np.zeros((100,100)); 

 

# Function to find the square matrix 

def printRequiredMatrix(n) : 

 

 # For Matrix of order 1, 

 # it will contain only 1 

 if (n == 1) :

 print("1"); 

 

 # For Matrix of odd order, 

 # it is not possible 

 elif (n % 2 != 0) : 

 print("-1");

 

 # For Matrix of even order 

 else :

 # All diagonal elements of the 

 # matrix can be N itself. 

 for i in range(n) :

 matrix[i][i] = n; 

 

 u = n - 1; 

 

 # Assign values at desired 

 # place in the matrix 

 for i in range(n - 1) :

 

 matrix[i][u] = i + 1; 

 

 for j in range(1, n//2) :

 

 a = (i + j) % (n - 1); 

 b = (i - j + n - 1) % (n - 1); 

 if (a < b) :

 a,b = b,a

 

 matrix[b][a] = i + 1; 

 

 # Loop to add N in the lower half 

 # of the matrix such that it contains 

 # elements from 1 to 2*N - 1 

 for i in range(n) :

 for j in range(i) :

 matrix[i][j] = matrix[j][i] + n; 

 

 # Loop to print the matrix 

 for i in range(n) :

 for j in range(n) :

 print(matrix[i][j] ,end=" "); 

 print();

 

 print()

 

# Driver Code 

if __name__ == "__main__" : 

 

 n = 1; 

 printRequiredMatrix(n); 

 

 n = 3; 

 printRequiredMatrix(n); 

 

 n = 6; 

 printRequiredMatrix(n); 

 

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

// C# implementation of the above approach

using System;

 

class GFG {

 

 static int [,]matrix = new int[100, 100]; 

 

 // Function to find the square matrix 

 static void printRequiredMatrix(int n) 

 { 

 // For Matrix of order 1, 

 // it will contain only 1 

 if (n == 1) { 

 Console.WriteLine("1");

 } 

 

 // For Matrix of odd order, 

 // it is not possible 

 else if (n % 2 != 0) { 

 Console.WriteLine("-1");

 } 

 

 // For Matrix of even order 

 else

 { 

 // All diagonal elements of the 

 // matrix can be N itself. 

 for (int i = 0; i < n; i++) { 

 matrix[i, i] = n; 

 } 

 int u = n - 1; 

 

 // Assign values at desired 

 // place in the matrix 

 for (int i = 0; i < n - 1; i++) { 

 

 matrix[i, u] = i + 1; 

 

 for (int j = 1; j < n / 2; j++) { 

 

 int a = (i + j) % (n - 1); 

 int b = (i - j + n - 1) % (n - 1); 

 if (a < b) {

 int temp = a;

 a = b; 

 b = temp;

 }

 matrix[b, a] = i + 1; 

 } 

 } 

 

 // Loop to add N in the lower half 

 // of the matrix such that it contains 

 // elements from 1 to 2*N - 1 

 for (int i = 0; i < n; i++) 

 for (int j = 0; j < i; j++) 

 matrix[i, j] = matrix[j, i] + n; 

 

 // Loop to print the matrix 

 for (int i = 0; i < n; i++) { 

 for (int j = 0; j < n; j++) 

 Console.Write(matrix[i, j] + " "); 

 Console.WriteLine() ;

 } 

 } 

 Console.WriteLine();

 } 

 

 // Driver Code 

 public static void Main (String[] args) 

 { 

 int n = 1; 

 printRequiredMatrix(n); 

 

 n = 3; 

 printRequiredMatrix(n); 

 

 n = 6; 

 printRequiredMatrix(n); 

 } 

}

 

// This code is contributed by Yash_R  
  
---  
  
 __

 __

 **Output:**

    
    
    1
    
    -1
    
    6 4 2 5 3 1 
    10 6 5 3 1 2 
    8 11 6 1 4 3 
    11 9 7 6 2 4 
    9 7 10 8 6 5 
    7 8 9 10 11 6
    

**Performance Analysis:**

  *  **Time Complexity:** As in the above approach, there is two loops to iterate over the whole N*N matrix which takes O(N2) time in worst case, Hence the Time Complexity will be **O(N 2)**.
  *  **Auxiliary Space Complexity:** As in the above approach, there is no extra space used, Hence the auxiliary space complexity will be **O(1)**

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


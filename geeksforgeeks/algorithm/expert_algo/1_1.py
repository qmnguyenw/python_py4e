Check if a palindromic matrix can be formed from the given array elements



Given an array **arr[]** consisting of **N 2** integers, the task is to check
whether a matrix of dimensions **N * N** can be formed from the given array
elements, which is palindrome. If it is possible, print the palindrome matrix.

> A **palindrome matrix** is the one in which each of the rows and columns are
> palindrome.

 **Examples:**

>  **Input:** arr[] = {5, 1, 3, 4, 5, 3, 5, 4, 5}  
>  **Output:**  
>  Yes  
> 5 3 5  
> 4 1 4  
> 5 3 5
>
>  **Input:** arr[] = {3, 4, 2, 1, 5, 6, 6, 6, 9}  
>  **Output:** No
>
>  
>
>
>  
>

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** Below is some observations based on which the given problem can
be solved:

  * An important observation here is – To put a value in the first column of the first row, the exact same value needs to put in the last column of the same row to preserve the palindromic behavior of the row. Also, to make columns palindrome, the same value needs to be put in the first column and last column of the last row.
  * Therefore, in total, 4 instances of the same value are needed to put them symmetrically in the matrix.
  * Also in the case of a matrix having an odd number of rows and columns only 2 instances of the same value are needed for the middle rows and columns because the elements in the middle row and column will be symmetric to themselves.
  * So here the elements can be divided into three types:
    1. Elements having a frequency in a multiple of 4.
    2. Elements having a frequency in a multiple of 2.
    3. The element which is present only once.

Now using the Greedy Technique fill the matrix using the below steps:

  1. Use a priority queue to store the frequency of the elements in a sorted manner.
  2. If the current row is not the middle row then choose an element having a frequency of **at least 4** to place these **4** numbers at symmetrically on the four corners such that the row and column in which it is placed remain palindromic.
  3. If the current row is the middle row choose an element having a frequency of **at least 2** to place the values symmetrically.
  4. If at any step the required number of elements is not found then the palindrome matrix is not possible then print **No**. 
  5. Otherwise, print **Yes** and print the palindromic matrix formed.

Below is the implementation of the above approach:

## C++14

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program for the above approach

 

#include <bits/stdc++.h>

using namespace std;

 

// Function to fill the matrix to

// make it palindromic if possible

void fill(vector<pair<int, int> >& temp,

 priority_queue<pair<int, int> >& q,

 vector<vector<int> >& grid)

{

 // First element of priority queue

 auto it = q.top();

 q.pop();

 

 // If the frequency of element is

 // less than desired frequency

 // then not possible

 if (it.first < temp.size()) {

 cout << "No\n";

 exit(0);

 }

 

 // If possible then assign value

 // to the matrix

 for (auto c : temp) {

 grid

 = it.second;

 }

 

 // Decrease the frequency

 it.first -= temp.size();

 

 // Again push inside queue

 q.push(it);

}

 

// Function to check if palindromic

// matrix of dimension N*N can be

// formed or not

void checkPalindrome(int A[], int N)

{

 // Stores the frequency

 map<int, int> mp;

 

 // Stores in the order of frequency

 priority_queue<pair<int, int> > q;

 

 // To store the palindromic

 // matrix if exists

 vector<vector<int> >

 grid(N, vector<int>(N));

 

 for (int c = 0; c < N * N; c++) {

 

 mp[A]++;

 }

 

 // Number of rows

 

 // Assign in priority queue

 for (auto c : mp)

 q.push({ c.second, c.first });

 

 // Middle index

 int m = N / 2;

 

 // Stores the indexes to be filled

 vector<pair<int, int> > temp;

 

 for (int i = 0; i < m; i++) {

 

 for (int j = 0; j < m; j++) {

 

 // Find the opposite indexes

 // which have same value

 int revI = N - i - 1;

 int revJ = N - j - 1;

 

 temp = { { i, j },

 { revI, j },

 { i, revJ },

 { revI, revJ } };

 

 // Check if all the indexes

 // in temp can be filled

 // with same value

 fill(temp, q, grid);

 

 temp.clear();

 }

 }

 

 // If N is odd then to fill the

 // middle row and middle column

 if (N & 1) {

 

 for (int i = 0; i < m; i++) {

 

 // Fill the temp

 temp = { { i, m },

 { N - i - 1, m } };

 

 // Fill grid with temp

 fill(temp, q, grid);

 

 // Clear temp

 temp.clear();

 

 // Fill the temp

 temp = { { m, i },

 { m, N - i - 1 } };

 

 // Fill grid with temp

 fill(temp, q, grid);

 temp.clear();

 }

 

 // For the middle element

 // of middle row and column

 temp = { { m, m } };

 fill(temp, q, grid);

 }

 

 cout << "Yes" << endl;

 

 // Print the matrix

 for (int i = 0; i < N; i++) {

 

 for (int j = 0; j < N; j++) {

 

 cout << grid[i][j] << " ";

 }

 cout << endl;

 }

}

 

// Driver Code

int main()

{

 // Given array A[]

 int A[] = { 1, 1, 1, 1, 2, 3, 3, 4, 4 };

 

 int N = sizeof(A) / sizeof(A[0]);

 

 N = sqrt(N);

 

 // Function call

 checkPalindrome(A, N);

 

 return 0;

}  
  
---  
  
 __

 __

 **Output:**

    
    
    Yes
    1 4 1 
    3 2 3 
    1 4 1
    

_**Time Complexity:** O(N2)_  
 _ **Auxiliary Space:** O(N2)_

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


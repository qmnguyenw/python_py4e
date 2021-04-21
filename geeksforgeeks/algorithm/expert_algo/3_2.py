Number of submatrices with OR value 1



Given a **N*N** binary matrix, task is to find the count of rectangular sub-
matrices with OR value 1.

 **Examples:**

    
    
    **Input :** arr[][] = {{0, 0, 0},
                       {0, 0, 0},
                       {0, 0, 0}}
    **Output :** 0
    **Explanation** : All the submatrices will have an OR value 0.
    Thus, ans = 0.
    
    **Input :** arr[][] = {{0, 0, 0},
                      {0, 1, 0},
                      {0, 0, 0}}
    **Output :** 16
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

A **Simple Solution** will be to generate all the possible sub-matrices and
then check if any of the values inside them are 1. If for a sub-matrix,
atleast a single element is one, we increment the value of final answer for
one. The time complexity of above approach is O(n6).

 **Better approach** : Lets have a look at this problem in an other way. We
will now try to find the number of submatrices with all 0s. And for the final
answer, we will substract this value from the total number of submatrices.

To optimize the process, for every index of the matrix, we will try to find
the number of submatrices starting from that index having all 0s in it.

  

  

Our first step towards solving this problem is creating a matrix ‘p_arr’.

  * For each index (R, C), if arr[R][C] equals 0, then in p_arr[R][C], we will store the number of 0s to the right of the cell(R, C) along row ‘R’ before we encounter ‘1’ or end of the array plus one.
  * If arr[R][C] equals 1, the p_arr[R][C] equals zero.

For creating this matrix, we will use the following recurrence relation.

    
    
    IF arr[R][C] is 0
        p_arr[R][C] = p_arr[R][C+1] + 1
    ELSE 
        p_arr[R][C] = 0
    
    arr[][] = {{1, 0, 0, 0},
               {0, 1, 0, 1},
               {0, 1, 0, 0},
               {0, 0, 0, 0}}
    
    p_arr[][] for above will look like
              {{0, 3, 2, 1},
               {1, 0, 1, 0},
               {1, 0, 2, 1},
               {4, 3, 2, 1}}
    

Once, we have the required matrix **p_arr** , we will start processing the
matrix ‘p_arr’ column-wise. If we are processing jth column of the matrix
‘p_arr’, then for each element ‘i’ of this column, we will try to find the
number of sub-matrices starting from cell **(i, j)** with all 0s.

For this, we can use stack data structure.

 **Algorithm** :

  1. Initialize a stack ‘q’ to store the value of the elements getting pushed along with the count(Cij) of the number of elements that were pushed in the stack with a value **strictly greater** than the value of the current element. We will use pair to tie up the two data together.  
Initialize a variable to_sum with 0. At each step, this variable is updated to
store the number of submatrices with all 0s starting from the element being
pushed at that step. Thus, using ‘to_sum’, we update the count of number of
submatrices with all 0s at each step.

  2. For a column ‘j’, at any step ‘i’, we will prepare to push p_arr[i][j] in the stack. Let Qt represent the topmost element of the stack and Ct represent the number of elements previously pushed in the stack with a value greater than the top-most element of the stack. Before pushing an element ‘p_arr[i][j]’ in the stack, while the stack is not empty or topmost element is greater than the number to be pushed, keep popping the topmost element of the stack and at the same time update **to_sum** as **to_sum += (C t \+ 1) * (Qt – p_arr[i][j])**. Let Ci, jrepresent the number of elements greater than the current element that were pushed in this stack previously. We also need to keep a track of Ci, j. Thus, before popping an element, we update Ci, j as Ci, j += Ct along with to_sum.
  3. We update the number of submatrices with all zeros as count_zero_submatrices += to_sum.
  4. Finally, we push that element in the stack after pairing it with Ci, j.

Total number of sub-matrices in a N*N matrix equals:

    
    
    (N2 * (N + 1)2)/4
    

Thus, the final answer will be:

    
    
    ans = (N2 * (N + 1)2)/4 - count_zero_submatrices 
    

We create the prefix-array in O(N2) and for each column we push an element in
the stack or pop it out only once. Thus, the time complexity of this algorithm
is O(N2).

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to count number of submatrices

// with OR value 1

 

#include <iostream>

#include <stack>

#define n 3

using namespace std;

 

// Function to find required prefix-count for each row

// from right to left

void findPrefixCount(int p_arr[][n], bool arr[][n])

{

 for (int i = 0; i < n; i++)

 for (int j = n - 1; j >= 0; j--) {

 

 if (arr[i][j])

 continue;

 if (j != n - 1)

 p_arr[i][j] += p_arr[i][j + 1];

 

 p_arr[i][j] += (int)(!arr[i][j]);

 }

}

 

// Function to find the count of submatrices

// with OR value 1

int matrixOrValueOne(bool arr[][n])

{

 // Array to store prefix count of zeros from

 // right to left for boolean array

 int p_arr[n][n] = { 0 };

 

 findPrefixCount(p_arr, arr);

 

 // Variable to store the count of

 // submatrices with OR value 0

 int count_zero_submatrices = 0;

 

 // Loop to evaluate each column of

 // the prefix matrix uniquely.

 // For each index of a column we will try to

 // determine the number of sub-matrices

 // starting from that index

 // and has all 1s

 for (int j = 0; j < n; j++) {

 

 int i = n - 1;

 

 // stack to store elements and the count

 // of the numbers they popped

 

 // First part of pair will be the

 // value of inserted element.

 // Second part will be the count

 // of the number of elements pushed

 // before with a greater value

 stack<pair<int, int> > q;

 

 // Variable to store the number of submatrices

 // with all 0s

 int to_sum = 0;

 

 while (i >= 0) {

 

 int c = 0;

 

 while (q.size() != 0 and q.top().first > p_arr[i][j]) {

 

 to_sum -= (q.top().second + 1) * 

 (q.top().first - p_arr[i][j]);

 

 c += q.top().second + 1;

 

 q.pop();

 }

 

 to_sum += p_arr[i][j];

 

 count_zero_submatrices += to_sum;

 

 q.push({ p_arr[i][j], c });

 

 i--;

 }

 }

 

 // Return the final answer

 return (n * (n + 1) * n * (n + 1)) / 4

 - count_zero_submatrices;

}

 

// Driver Code

int main()

{

 bool arr[][n] = { { 0, 0, 0 },

 { 0, 1, 0 },

 { 0, 0, 0 } };

 

 cout << matrixOrValueOne(arr);

 

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

// Java program to count number of submatrices

// with OR value 1

import java.util.*;

 

class GFG

{

static int n = 3;

static class pair

{ 

 int first, second; 

 public pair(int first, int second) 

 { 

 this.first = first; 

 this.second = second; 

 } 

} 

 

// Function to find required prefix-count 

// for each row from right to left

static void findPrefixCount(int p_arr[][],

 boolean arr[][])

{

 for (int i = 0; i < n; i++)

 for (int j = n - 1; j >= 0; j--)

 {

 if (arr[i][j])

 continue;

 if (j != n - 1)

 p_arr[i][j] += p_arr[i][j + 1];

 

 p_arr[i][j] += (arr[i][j] == false ? 1 : 0);

 }

}

 

// Function to find the count of submatrices

// with OR value 1

static int matrixOrValueOne(boolean arr[][])

{

 // Array to store prefix count of zeros from

 // right to left for boolean array

 int [][]p_arr = new int[n][n];

 

 findPrefixCount(p_arr, arr);

 

 // Variable to store the count of

 // submatrices with OR value 0

 int count_zero_submatrices = 0;

 

 // Loop to evaluate each column of

 // the prefix matrix uniquely.

 // For each index of a column we will try to

 // determine the number of sub-matrices

 // starting from that index

 // and has all 1s

 for (int j = 0; j < n; j++)

 {

 int i = n - 1;

 

 // stack to store elements and the count

 // of the numbers they popped

 

 // First part of pair will be the

 // value of inserted element.

 // Second part will be the count

 // of the number of elements pushed

 // before with a greater value

 Stack<pair> q = new Stack<pair>();

 

 // Variable to store the number of submatrices

 // with all 0s

 int to_sum = 0;

 

 while (i >= 0)

 {

 int c = 0;

 

 while (q.size() != 0 && 

 q.peek().first > p_arr[i][j]) 

 {

 

 to_sum -= (q.peek().second + 1) * 

 (q.peek().first - p_arr[i][j]);

 

 c += q.peek().second + 1;

 

 q.pop();

 }

 

 to_sum += p_arr[i][j];

 

 count_zero_submatrices += to_sum;

 

 q.add(new pair(p_arr[i][j], c ));

 

 i--;

 }

 }

 

 // Return the final answer

 return (n * (n + 1) * n * (n + 1)) / 4

 - count_zero_submatrices;

}

 

// Driver Code

public static void main(String[] args) 

{

 boolean arr[][] = { { false, false, false },

 { false, true, false },

 { false, false, false } };

 

 System.out.println(matrixOrValueOne(arr));

}

}

 

// This code is contributed by PrinciRaj1992  
  
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

# Python3 program to count number

# of submatrices with OR value 1 

 

# Function to find required prefix-count 

# for each row from right to left 

def findPrefixCount(p_arr, arr): 

 

 for i in range(0, n):

 for j in range(n - 1, -1, -1): 

 

 if arr[i][j]: 

 continue

 if j != n - 1: 

 p_arr[i][j] += p_arr[i][j + 1] 

 

 p_arr[i][j] += int(not arr[i][j]) 

 

# Function to find the count 

# of submatrices with OR value 1 

def matrixOrValueOne(arr): 

 

 # Array to store prefix count of zeros 

 # from right to left for boolean array 

 p_arr = [[0 for i in range(n)] 

 for j in range(n)] 

 

 findPrefixCount(p_arr, arr) 

 

 # Variable to store the count of 

 # submatrices with OR value 0 

 count_zero_submatrices = 0

 

 # Loop to evaluate each column of 

 # the prefix matrix uniquely. 

 # For each index of a column we will try 

 # to determine the number of sub-matrices 

 # starting from that index and has all 1s 

 for j in range(0, n): 

 

 i = n - 1

 

 # stack to store elements and the 

 # count of the numbers they popped 

 

 # First part of pair will be the 

 # value of inserted element. 

 # Second part will be the count 

 # of the number of elements pushed 

 # before with a greater value 

 q = [] 

 

 # Variable to store the number 

 # of submatrices with all 0s 

 to_sum = 0

 

 while i >= 0: 

 

 c = 0

 while (len(q) != 0 and

 q[-1][0] > p_arr[i][j]): 

 

 to_sum -= ((q[-1][1] + 1) *

 (q[-1][0] - p_arr[i][j]))

 

 c += q.pop()[1] + 1

 

 to_sum += p_arr[i][j] 

 count_zero_submatrices += to_sum 

 

 q.append((p_arr[i][j], c)) 

 i -= 1

 

 # Return the final answer 

 return ((n * (n + 1) * n * (n + 1)) //

 4 - count_zero_submatrices) 

 

# Driver Code 

if __name__ == "__main__": 

 

 n = 3

 arr = [[0, 0, 0], 

 [0, 1, 0], 

 [0, 0, 0]] 

 

 print(matrixOrValueOne(arr))

 

# This code is contributed by Rituraj Jain  
  
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

// C# program to count number of submatrices

// with OR value 1

using System;

using System.Collections.Generic;

 

class GFG

{

static int n = 3;

class pair

{ 

 public int first, second; 

 public pair(int first, int second) 

 { 

 this.first = first; 

 this.second = second; 

 } 

} 

 

// Function to find required prefix-count 

// for each row from right to left

static void findPrefixCount(int [,]p_arr,

 bool [,]arr)

{

 for (int i = 0; i < n; i++)

 for (int j = n - 1; j >= 0; j--)

 {

 if (arr[i, j])

 continue;

 if (j != n - 1)

 p_arr[i, j] += p_arr[i, j + 1];

 

 p_arr[i, j] += (arr[i, j] == false ? 1 : 0);

 }

}

 

// Function to find the count of submatrices

// with OR value 1

static int matrixOrValueOne(bool [,]arr)

{

 // Array to store prefix count of zeros from

 // right to left for bool array

 int [,]p_arr = new int[n, n];

 

 findPrefixCount(p_arr, arr);

 

 // Variable to store the count of

 // submatrices with OR value 0

 int count_zero_submatrices = 0;

 

 // Loop to evaluate each column of

 // the prefix matrix uniquely.

 // For each index of a column we will try to

 // determine the number of sub-matrices

 // starting from that index

 // and has all 1s

 for (int j = 0; j < n; j++)

 {

 int i = n - 1;

 

 // stack to store elements and the count

 // of the numbers they.Popped

 

 // First part of pair will be the

 // value of inserted element.

 // Second part will be the count

 // of the number of elements.Pushed

 // before with a greater value

 Stack<pair> q = new Stack<pair>();

 

 // Variable to store the number of 

 // submatrices with all 0s

 int to_sum = 0;

 

 while (i >= 0)

 {

 int c = 0;

 

 while (q.Count != 0 && 

 q.Peek().first > p_arr[i, j]) 

 {

 

 to_sum -= (q.Peek().second + 1) * 

 (q.Peek().first - p_arr[i, j]);

 

 c += q.Peek().second + 1;

 

 q.Pop();

 }

 

 to_sum += p_arr[i, j];

 

 count_zero_submatrices += to_sum;

 

 q.Push(new pair(p_arr[i, j], c));

 

 i--;

 }

 }

 

 // Return the final answer

 return (n * (n + 1) * n * (n + 1)) / 4 - 

 count_zero_submatrices;

}

 

// Driver Code

public static void Main(String[] args) 

{

 bool [,]arr = { { false, false, false },

 { false, true, false },

 { false, false, false } };

 

 Console.WriteLine(matrixOrValueOne(arr));

}

}

 

// This code is contributed by Rajput-Ji  
  
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


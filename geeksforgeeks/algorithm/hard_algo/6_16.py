Number of submatrices with all 1s



Given a **N*N** matrix containing only 0s and 1s, the task is to count the
number of submatrices containing all 1s.

 **Examples:**

    
    
    **Input :** arr[][] = {{1, 1, 1},
                       {1, 1, 1},
                       {1, 1, 1}}
    **Output :** 36
    **Explanation** : All the possible submatrices will have only 1s.
    Since, there are 36 submatrices in total, ans = 36
    
    **Input :** {{1, 1, 1},
                       {1, 0, 1},
                       {1, 1, 1}}
    **Output :** 20
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

For simplicity, we will say a sub-matrix starts from an index (R, C), if that
particular index is its top-left corner.

A **Simple** Solution will be to generate all the possible sub-matrices and
then check if all the values inside them are 1. If for a sub-matrix, all the
elements are one, we increment the value of the final answer for one. The time
complexity of the above approach is O(n6).

 **Better Approach** : To optimize the process, for every index of the matrix,
we will try to find the number of submatrices starting from that index having
all 1s in it.

  

  

Our first step towards solving this problem is creating a matrix ‘p_arr’.

For each index (R, C), if arr[R][C] equals 1, then in p_arr[R][C], we will
store the number of 1s to the right of the cell(R, C) along row ‘R’ before we
encounter first zero or end of the array plus 1.  
If arr[R][C] equals zero, the p_arr[R][C] also equals zero.

For creating this matrix, we will use the following recurrence relation.

    
    
    IF arr[R][C] is not 0
        p_arr[R][C] = p_arr[R][C+1] + 1
    ELSE 
        p_arr[R][C] = 0
    
    arr[][] = {{1, 0, 1, 1},
               {0, 1, 0, 1},
               {1, 1, 1, 0},
               {1, 0, 1, 1}}
    p_arr[][] for above will look like
              {{1, 0, 2, 1},
               {0, 1, 0, 1},
               {3, 2, 1, 0},
               {1, 0, 2, 1}}
    

Once, we have the required matrix **p_arr** , we will proceed towards the next
step. Look at the matrix ‘p_arr’ column-wise. If we are processing jth column
of the matrix p_arr, then for each element ‘i’ of this column, we will try to
find the number of sub-matrices starting from cell **(i, j)** with all 1s.

For this, we can use stack data structure.

 **Algorithm** :

  1. Initialize a stack ‘q’ to store the value of the elements getting pushed along with the count(Cij) of the number of elements that were pushed in this stack with a value **strictly greater** than the value of the current element. We will use a pair to tie up the two data together.  
Initialize a variable ‘to_sum’ with 0. At each step, this variable is updated
to store the number of submatrices with all 1s starting from the element being
pushed at that step. Thus, using ‘to_sum’, we update the count of number of
submatrices with all 1s at each step.

  2. For a column ‘j’, at any step ‘i’, we will prepare to push p_arr[i][j] in the stack. Let Qt represent the topmost element of the stack and Ct represent the number of elements previously pushed in the stack with a value greater than the top-most element of the stack. Before pushing an element ‘p_arr[i][j]’ in the stack, while the stack is not empty or topmost element is greater than the number to be pushed, keep popping the topmost element of the stack and at the same time update **to_sum** as **to_sum += (C t \+ 1) * (Qt – p_arr[i][j])**. Let Ci, jrepresent the number of elements greater than the current element that were pushed in this stack previously. We also need to keep a track of Ci, j. Thus, before popping an element, we update Ci, j as Ci, j += Ct along with to_sum.
  3. We update the answer as ans += to_sum.
  4. Finally, we push that element in the stack after pairing it with Ci, j.

Create the prefix-array in O(n2) and for each column, we push an element in
the stack or pop it out only once. Thus, the time complexity of this algorithm
is O(n2).

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to count number of

// sub-matrices with all 1s

 

#include <iostream>

#include <stack>

 

using namespace std;

 

#define n 3

 

// Function to find required prefix-count for

// each row from right to left

void findPrefixCount(int p_arr[][n], bool arr[][n])

{

 for (int i = 0; i < n; i++) {

 for (int j = n - 1; j >= 0; j--) {

 

 if (!arr[i][j])

 continue;

 

 if (j != n - 1)

 p_arr[i][j] += p_arr[i][j + 1];

 

 p_arr[i][j] += (int)arr[i][j];

 }

 }

}

 

// Function to count the number of

// sub-matrices with all 1s

int matrixAllOne(bool arr[][n])

{

 // Array to store required prefix count of

 // 1s from right to left for boolean array

 int p_arr[n][n] = { 0 };

 

 findPrefixCount(p_arr, arr);

 

 // variable to store the final answer

 int ans = 0;

 

 /* Loop to evaluate each column of

 the prefix matrix uniquely.

 For each index of a column we will try to

 determine the number of sub-matrices

 starting from that index

 and has all 1s */

 for (int j = 0; j < n; j++) {

 

 int i = n - 1;

 

 /* Stack to store elements and the count

 of the numbers they popped

 

 First part of pair will be the

 value of inserted element.

 Second part will be the count

 of the number of elements pushed

 before with a greater value */

 stack<pair<int, int> > q;

 

 // variable to store the number of

 // submatrices with all 1s

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

 

 ans += to_sum;

 

 q.push({ p_arr[i][j], c });

 

 i--;

 }

 }

 

 return ans;

}

 

// Driver Code

int main()

{

 bool arr[][n] = { { 1, 1, 0 },

 { 1, 0, 1 },

 { 0, 1, 1 } };

 

 cout << matrixAllOne(arr);

 

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

// Java program to count number of

// sub-matrices with all 1s

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

 

// Function to find required prefix-count for

// each row from right to left

static void findPrefixCount(int p_arr[][], 

 boolean arr[][])

{

 for (int i = 0; i < n; i++)

 {

 for (int j = n - 1; j >= 0; j--) 

 {

 if (!arr[i][j])

 continue;

 

 if (j != n - 1)

 p_arr[i][j] += p_arr[i][j + 1];

 

 p_arr[i][j] += arr[i][j] == true ? 1 : 0;

 }

 }

}

 

// Function to count the number of

// sub-matrices with all 1s

static int matrixAllOne(boolean arr[][])

{

 // Array to store required prefix count of

 // 1s from right to left for boolean array

 int [][]p_arr = new int[n][n];

 

 findPrefixCount(p_arr, arr);

 

 // variable to store the final answer

 int ans = 0;

 

 /* Loop to evaluate each column of

 the prefix matrix uniquely.

 For each index of a column we will try to

 determine the number of sub-matrices

 starting from that index

 and has all 1s */

 for (int j = 0; j < n; j++) 

 {

 int i = n - 1;

 

 /* Stack to store elements and the count

 of the numbers they popped

 

 First part of pair will be the

 value of inserted element.

 Second part will be the count

 of the number of elements pushed

 before with a greater value */

 Stack<pair> q = new Stack<pair>();

 

 // variable to store the number of

 // submatrices with all 1s

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

 

 ans += to_sum;

 

 q.add(new pair(p_arr[i][j], c));

 

 i--;

 }

 }

 return ans;

}

 

// Driver Code

public static void main(String[] args)

{

 boolean arr[][] = { { true, true, false },

 { true, false, true },

 { false, true, true } };

 

 System.out.println(matrixAllOne(arr));

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

# Python3 program to count the number

# of sub-matrices with all 1s 

 

# Function to find required prefix-count 

# for each row from right to left 

def findPrefixCount(p_arr, arr): 

 

 for i in range(0, n): 

 for j in range(n - 1, -1, -1): 

 

 if not arr[i][j]: 

 continue

 

 if j != n - 1: 

 p_arr[i][j] += p_arr[i][j + 1] 

 

 p_arr[i][j] += arr[i][j] 

 

# Function to count the number of 

# sub-matrices with all 1s 

def matrixAllOne(arr): 

 

 # Array to store required prefix count of 

 # 1s from right to left for boolean array 

 p_arr = [[0 for i in range(n)] for j in
range(n)] 

 

 findPrefixCount(p_arr, arr) 

 

 # variable to store the final answer 

 ans = 0

 

 # Loop to evaluate each column of 

 # the prefix matrix uniquely. 

 # For each index of a column we will try to 

 # determine the number of sub-matrices 

 # starting from that index and has all 1s

 for j in range(0, n): 

 

 i = n - 1

 

 # Stack to store elements and the count 

 # of the numbers they popped 

 

 # First part of pair will be the 

 # value of inserted element. 

 # Second part will be the count 

 # of the number of elements pushed 

 # before with a greater value */

 q = [] 

 

 # variable to store the number of 

 # submatrices with all 1s 

 to_sum = 0

 

 while i >= 0: 

 

 c = 0

 while len(q) != 0 and q[-1][0] > p_arr[i][j]: 

 

 to_sum -= (q[-1][1] + 1) * \

 (q[-1][0] - p_arr[i][j]) 

 

 c += q[-1][1] + 1

 q.pop() 

 

 to_sum += p_arr[i][j] 

 ans += to_sum 

 

 q.append((p_arr[i][j], c)) 

 i -= 1

 

 return ans 

 

# Driver Code 

if __name__ == "__main__":

 

 arr = [[1, 1, 0], [1, 0, 1], [0, 1,
1]] 

 

 n = 3

 print(matrixAllOne(arr)) 

 

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

// C# program to count number of

// sub-matrices with all 1s

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

 

// Function to find required prefix-count for

// each row from right to left

static void findPrefixCount(int [,]p_arr, 

 Boolean [,]arr)

{

 for (int i = 0; i < n; i++)

 {

 for (int j = n - 1; j >= 0; j--) 

 {

 if (!arr[i, j])

 continue;

 

 if (j != n - 1)

 p_arr[i, j] += p_arr[i, j + 1];

 

 p_arr[i, j] += arr[i, j] == true ? 1 : 0;

 }

 }

}

 

// Function to count the number of

// sub-matrices with all 1s

static int matrixAllOne(Boolean [,]arr)

{

 // Array to store required prefix count of

 // 1s from right to left for boolean array

 int [,]p_arr = new int[n, n];

 

 findPrefixCount(p_arr, arr);

 

 // variable to store the final answer

 int ans = 0;

 

 /* Loop to evaluate each column of

 the prefix matrix uniquely.

 For each index of a column we will try to

 determine the number of sub-matrices

 starting from that index

 and has all 1s */

 for (int j = 0; j < n; j++) 

 {

 int i = n - 1;

 

 /* Stack to store elements and the count

 of the numbers they popped

 

 First part of pair will be the

 value of inserted element.

 Second part will be the count

 of the number of elements pushed

 before with a greater value */

 Stack<pair> q = new Stack<pair>();

 

 // variable to store the number of

 // submatrices with all 1s

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

 

 ans += to_sum;

 

 q.Push(new pair(p_arr[i, j], c));

 

 i--;

 }

 }

 return ans;

}

 

// Driver Code

public static void Main(String[] args)

{

 Boolean [,]arr = {{ true, true, false },

 { true, false, true },

 { false, true, true }};

 

 Console.WriteLine(matrixAllOne(arr));

}

}

 

// This code is contributed by 29AjayKumar  
  
---  
  
 __

 __

 **Output:**

    
    
    10
    

**Time Complexity** : O(N2)

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


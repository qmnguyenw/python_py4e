Find N in the given matrix that follows a pattern



Given an infinite matrix filled with the natural numbers as shown below:

    
    
    1 2 4 7 . . .
    3 5 8 . . . .
    6 9 . . . . .
    10  . . . . .
    . . . . . . .
    

Also, given an integer **N** and the task is to find the row and the column of
the integer **N** in the given matrix.

 **Examples:**

    
    
    **Input:** N = 5
    **Output:** 2 2
    5 is present in the 2nd row 
    and the 2nd column.
    
    **Input:** N = 3
    **Output:** 2 1
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** On observing the problem carefully, the row number can be
obtained by subtracting first **x** natural numbers from **N** such that they
satisfy the condition **N – (x * (x + 1)) / 2 ≥ 1** and the resultant value
will be the required row number.  
To get the corresponding column, add first **x** natural numbers to **1** such
that they satisfy the condition **1 + (y * (y + 1)) / 2 ≤ A**. Subtract this
resultant value from **N** to get the gap between the base and the given value
and again subtract the gap from **y + 1**.

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

 

// Function to return the row and

// the column of the given integer

pair<int, int> solve(int n)

{

 

 int low = 1, high = 1e4, x = n, p = 0;

 

 // Binary search for the row number

 while (low <= high) {

 int mid = (low + high) / 2;

 int sum = (mid * (mid + 1)) / 2;

 

 // Condition to get the maximum

 // x that satisfies the criteria

 if (x - sum >= 1) {

 p = mid;

 low = mid + 1;

 }

 else {

 high = mid - 1;

 }

 }

 

 int start = 1, end = 1e4, y = 1, q = 0;

 

 // Binary search for the column number

 while (start <= end) {

 int mid = (start + end) / 2;

 int sum = (mid * (mid + 1)) / 2;

 

 // Condition to get the maximum

 // y that satisfies the criteria

 if (y + sum <= n) {

 q = mid;

 start = mid + 1;

 }

 else {

 end = mid - 1;

 }

 }

 

 // Get the row and the column number

 x = x - (p * (p + 1)) / 2;

 y = y + (q * (q + 1)) / 2;

 int r = x;

 int c = q + 1 - n + y;

 

 // Return the pair

 pair<int, int> ans = { r, c };

 return ans;

}

 

// Driver code

int main()

{

 int n = 5;

 

 pair<int, int> p = solve(n);

 cout << p.first << " " << p.second;

 

 return 0;

}  
  
---  
  
 __

 __


Maximum number of strings that can be formed with given zeros and ones



Given a list of strings **arr[]** of zeros and ones only and two integer **N**
and **M** , where **N** is the number of **1’s** and **M** is the number of
**0’s**. The task is to find the maximum number of strings from the given list
of strings that can be constructured with given number of 0’s and 1’s.

 **Examples:**

>  **Input:** arr[] = {“10”, “0001”, “11100”, “1”, “0”}, M = 5, N = 3  
>  **Output:** 4  
>  **Explanation:**  
>  The 4 strings which can be formed using five 0’s and three 1’s are: “10”,
> “0001”, “1”, “0”
>
>  **Input:** arr[] = {“10”, “00”, “000” “0001”, “111001”, “1”, “0”}, M = 3, N
> = 1  
>  **Output:** 3  
>  **Explanation:**  
>  The 3 strings which can be formed using three 0’s and one 1’s are: “00”,
> “1”, “0”

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Naive Approach:** The idea is to generate all the combination of the given
list of strings and check the count of zeros and ones satisfying the given
condition. But the time complexity of this solution is exponential.

  

  

 **Time Complexity:** O( **2 N**), where **N** is the number of strings in the
list.

 **Efficient Approach:**  
An efficient solution is given by using Dynamic Programming. The idea is to
use recursion for generating all possible combinations and store the results
for Overlapping Subproblems during recursion.  
Below are the steps:

  1. The idea is to use 3D dp array( **dp[M][N][i]** ) where **N** and **M** are the number of **1’s** and **0’s** respectively and **i** is the index of the string in the list.
  2. Find the number of **1’s** and **0’s** in the current string and check if the count of the zeros and ones is less than or equals to the given count **N and M** respectively.
  3. If above condition is true, then check whether current state value is stored in the dp table or not. If yes then return this value.
  4. Else recursively move for the next iteration by including and excluding the current string as:
    
    
    // By including the current string
    x = 1 + recursive_function(M - zero, N - ones, arr, i + 1)
    
    // By excluding the current string 
    y = recursive_function(M, N, arr, i + 1)
    
    // and update the dp table as:
    dp[M][N][i] = max(x, y)
    

  5. The maximum value of the above two recursive calls will give the maximum number with **N 1’s and M 0’s** for the current state.

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

#include <bits/stdc++.h>

using namespace std;

 

// 3D dp table to store the state value

int dp[100][100][100];

 

// Function that count the combination

// of 0's and 1's from the given list

// of string

int countString(int m, int n,

 vector<string>& arr, int i)

{

 // Base Case if count of 0's or 1's

 // becomes negative

 if (m < 0 || n < 0) {

 return INT_MIN;

 }

 

 // If index reaches out of bound

 if (i >= arr.size()) {

 return 0;

 }

 

 // Return the prestored result

 if (dp[m][n][i] != -1) {

 return dp[m][n][i];

 }

 

 // Intialise count of 0's and 1's

 // to 0 for the current state

 int zero = 0, one = 0;

 

 // Calculate the number of 1's and

 // 0's in current string

 for (char c : arr[i]) {

 if (c == '0') {

 zero++;

 }

 else {

 one++;

 }

 }

 

 // Include the current string and

 // recurr for the next iteration

 int x = 1 + countString(m - zero,

 n - one,

 arr, i + 1);

 

 // Exclude the current string and

 // recurr for the next iteration

 int y = countString(m, n, arr, i + 1);

 

 // Update the maximum of the above

 // two states to the current dp state

 return dp[m][n][i] = max(x, y);

}

 

// Driver Code

int main()

{

 vector<string> arr = { "10", "0001", "1",

 "111001", "0" };

 

 // N 0's and M 1's

 int N = 3, M = 5;

 

 // Intialise dp array to -1

 memset(dp, -1, sizeof(dp));

 

 // Function call

 cout << countString(M, N, arr, 0);

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

class GFG{

 

// 3D dp table to store the state value

static int [][][]dp = new int[100][100][100];

 

// Function that count the combination

// of 0's and 1's from the given list

// of String

static int countString(int m, int n,

 String []arr, int i)

{

 // Base Case if count of 0's or 1's

 // becomes negative

 if (m < 0 || n < 0) {

 return Integer.MIN_VALUE;

 }

 

 // If index reaches out of bound

 if (i >= arr.length) {

 return 0;

 }

 

 // Return the prestored result

 if (dp[m][n][i] != -1) {

 return dp[m][n][i];

 }

 

 // Intialise count of 0's and 1's

 // to 0 for the current state

 int zero = 0, one = 0;

 

 // Calculate the number of 1's and

 // 0's in current String

 for (char c : arr[i].toCharArray()) {

 if (c == '0') {

 zero++;

 }

 else {

 one++;

 }

 }

 

 // Include the current String and

 // recurr for the next iteration

 int x = 1 + countString(m - zero,

 n - one,

 arr, i + 1);

 

 // Exclude the current String and

 // recurr for the next iteration

 int y = countString(m, n, arr, i + 1);

 

 // Update the maximum of the above

 // two states to the current dp state

 return dp[m][n][i] = Math.max(x, y);

}

 

// Driver Code

public static void main(String[] args)

{

 String []arr = { "10", "0001", "1",

 "111001", "0" };

 

 // N 0's and M 1's

 int N = 3, M = 5;

 

 // Intialise dp array to -1

 for(int i = 0;i<100;i++){

 for(int j = 0;j<100;j++){

 for(int l=0;l<100;l++)

 dp[i][j][l]=-1;

 }

 }

 

 // Function call

 System.out.print(countString(M, N, arr, 0));

}

}

 

// This code is contributed by 29AjayKumar  
  
---  
  
 __

 __

## Python 3

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 program for the above approach

import sys

 

# 3D dp table to store the state value

dp = [[[-1 for i in range(100)]for j in
range(100)] for k in range(100)]

 

# Function that count the combination

# of 0's and 1's from the given list

# of string

def countString(m, n, arr, i):

 

 # Base Case if count of 0's or 1's

 # becomes negative

 if (m < 0 or n < 0):

 return -sys.maxsize - 1

 

 # If index reaches out of bound

 if (i >= len(arr)):

 return 0

 

 # Return the prestored result

 if (dp[m][n][i] != -1):

 return dp[m][n][i]

 

 # Intialise count of 0's and 1's

 # to 0 for the current state

 zero = 0

 one = 0

 

 # Calculate the number of 1's and

 # 0's in current string

 for c in arr[i]:

 if (c == '0'):

 zero += 1

 else:

 one += 1

 

 # Include the current string and

 # recurr for the next iteration

 x = 1 + countString(m - zero, n - one, arr, i + 1)

 

 # Exclude the current string and

 # recurr for the next iteration

 y = countString(m, n, arr, i + 1)

 

 dp[m][n][i] = max(x, y)

 

 # Update the maximum of the above

 # two states to the current dp state

 return dp[m][n][i]

 

# Driver Code

if __name__ == '__main__':

 arr = ["10", "0001", "1","111001", "0"]

 

 # N 0's and M 1's

 N = 3

 M = 5

 

 # Function call

 print(countString(M, N, arr, 0))

 

# This code is contributed by Surendra_Gangwar  
  
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

 

class GFG{

 

// 3D dp table to store the state value

static int [,,]dp = new int[100, 100, 100];

 

// Function that count the combination

// of 0's and 1's from the given list

// of String

static int countString(int m, int n,

 String []arr, int i)

{

 // Base Case if count of 0's or 1's

 // becomes negative

 if (m < 0 || n < 0) {

 return int.MinValue;

 }

 

 // If index reaches out of bound

 if (i >= arr.Length) {

 return 0;

 }

 

 // Return the prestored result

 if (dp[m, n, i] != -1) {

 return dp[m, n, i];

 }

 

 // Intialise count of 0's and 1's

 // to 0 for the current state

 int zero = 0, one = 0;

 

 // Calculate the number of 1's and

 // 0's in current String

 foreach (char c in arr[i].ToCharArray()) {

 if (c == '0') {

 zero++;

 }

 else {

 one++;

 }

 }

 

 // Include the current String and

 // recurr for the next iteration

 int x = 1 + countString(m - zero,

 n - one,

 arr, i + 1);

 

 // Exclude the current String and

 // recurr for the next iteration

 int y = countString(m, n, arr, i + 1);

 

 // Update the maximum of the above

 // two states to the current dp state

 return dp[m, n, i] = Math.Max(x, y);

}

 

// Driver Code

public static void Main(String[] args)

{

 String []arr = { "10", "0001", "1",

 "111001", "0" };

 

 // N 0's and M 1's

 int N = 3, M = 5;

 

 // Intialise dp array to -1

 for(int i = 0; i < 100; i++){

 for(int j = 0; j < 100; j++){

 for(int l = 0; l < 100; l++)

 dp[i, j, l] = -1;

 }

 }

 

 // Function call

 Console.Write(countString(M, N, arr, 0));

}

}

 

// This code is contributed by Rajput-Ji  
  
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


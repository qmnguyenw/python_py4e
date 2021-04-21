Unique subsequences of length K with given sum



Given an array **arr[]** of **N** integers and two numbers **K** and **S** ,
the task is to print all the subsquence of length **K** with the sum **S**.

 **Examples:**

>  **Input:** N = 5, K = 3, S = 20, arr[] = {4, 6, 8, 2, 12}  
>  **Output:**  
>  {6, 2, 12}  
>  **Explanation:**  
>  Only one subsequence of size 3 with a sum 20 is possible i.e., {6, 2, 12}
> and sum is 6 + 2 + 12 = 20
>
>  **Input:** N = 10, K = 5, S = 25, arr[] = {2, 4, 6, 8, 10, 12, 1, 2, 5, 7}  
>  **Output:**  
>  {10, 1, 2, 5, 7}  
> {4, 8, 1, 5, 7}  
> {4, 8, 10, 1, 2}  
> {4, 6, 12, 1, 2}  
> {4, 6, 8, 2, 5}  
> {2, 10, 1, 5, 7}  
> {2, 8, 12, 1, 2}  
> {2, 6, 10, 2, 5}  
> {2, 6, 8, 2, 7}  
> {2, 4, 12, 2, 5}  
> {2, 4, 10, 2, 7}  
> {2, 4, 8, 10, 1}  
> {2, 4, 6, 12, 1}  
> {2, 4, 6, 8, 5}

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** The idea is to use Backtracking to print all the subsequence
with given sum **S**. Below are the steps:

  

  

  * Iterate for all the value of the array **arr[]** and do the following:
    1. If we include the current element in the resultant subsequence then, decrement **K** and the above value of current element to the sum **S**.
    2. Recursively iterate from next index of the element to the end of the array to find the resultant subsequence.
    3. If **K is 0** and **S is 0** then we got our one of the resultant subsequence of length **K** and sum **S** , print this subsequence and backtrack for the next resulting subsequence.
    4. If we doesn’t include the current element then, find the resultant subsequence by excluding the current element and repeating the above procedure for the rest of the element in the array.
  * Resultant array in the steps 3 will give all the possible subsequence of length **K** with given sum **S**.

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

 

// Function to find all the subsequences

// of a given length and having sum S

void comb(int* arr, int len, int r,

 int ipos, int* op, int opos,

 int sum)

{

 

 // Termination condition

 if (opos == r) {

 

 int sum2 = 0;

 for (int i = 0; i < opos; i++) {

 

 // Add value to sum

 sum2 = sum2 + op[i];

 }

 

 // Check if the resultant sum

 // equals to target sum

 if (sum == sum2) {

 

 // If true

 for (int i = 0; i < opos; i++)

 

 // Print resultant array

 cout << op[i] << ", ";

 

 cout << endl;

 }

 

 // End this recursion stack

 return;

 }

 if (ipos < len) {

 

 // Check all the combinations

 // using backtracking

 comb(arr, len, r, ipos + 1,

 op, opos, sum);

 

 op[opos] = arr[ipos];

 

 // Check all the combinations

 // using backtracking

 comb(arr, len, r, ipos + 1,

 op, opos + 1, sum);

 }

}

 

// Driver Code

int main()

{

 // Given array

 int arr[] = { 4, 6, 8, 2, 12 };

 int K = 3;

 int S = 20;

 

 int N = sizeof(arr) / sizeof(arr[0]);

 

 // To store the subsquence

 int op[N] = { 0 };

 

 // Function Call

 comb(arr, N, K, 0, op, 0, S);

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

 

class GFG{

 

// Function to find all the subsequences

// of a given length and having sum S

static void comb(int []arr, int len, int r,

 int ipos, int[] op, int opos,

 int sum)

{

 

 // Termination condition

 if (opos == r)

 {

 int sum2 = 0;

 for(int i = 0; i < opos; i++) 

 {

 

 // Add value to sum

 sum2 = sum2 + op[i];

 }

 

 // Check if the resultant sum

 // equals to target sum

 if (sum == sum2)

 {

 

 // If true

 for(int i = 0; i < opos; i++)

 

 // Print resultant array

 System.out.print(op[i] + ", ");

 

 System.out.println();

 }

 

 // End this recursion stack

 return;

 }

 if (ipos < len) 

 {

 

 // Check all the combinations

 // using backtracking

 comb(arr, len, r, ipos + 1,

 op, opos, sum);

 

 op[opos] = arr[ipos];

 

 // Check all the combinations

 // using backtracking

 comb(arr, len, r, ipos + 1,

 op, opos + 1, sum);

 }

}

 

// Driver Code

public static void main(String[] args)

{

 

 // Given array

 int arr[] = { 4, 6, 8, 2, 12 };

 int K = 3;

 int S = 20;

 

 int N = arr.length;

 

 // To store the subsquence

 int op[] = new int[N];

 

 // Function Call

 comb(arr, N, K, 0, op, 0, S);

}

}

 

// This code is contributed by amal kumar choubey  
  
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

 

# Function to find all the subsequences 

# of a given length and having sum S 

def comb(arr, Len, r, ipos, op, opos, Sum):

 

 # Termination condition

 if (opos == r):

 

 sum2 = 0

 for i in range(opos):

 

 # Add value to sum

 sum2 = sum2 + op[i]

 

 # Check if the resultant sum

 # equals to target sum

 if (Sum == sum2):

 

 # If true

 for i in range(opos):

 

 # Print resultant array

 print(op[i], end = ", ")

 

 print()

 

 # End this recursion stack

 return

 

 if (ipos < Len):

 

 # Check all the combinations

 # using backtracking

 comb(arr, Len, r, ipos + 1, 

 op, opos, Sum)

 

 op[opos] = arr[ipos]

 

 # Check all the combinations

 # using backtracking

 comb(arr, Len, r, ipos + 1, op, 

 opos + 1, Sum)

 

# Driver code

if __name__ == '__main__':

 

 # Given array

 arr = [ 4, 6, 8, 2, 12 ]

 K = 3

 S = 20

 N = len(arr)

 

 # To store the subsequence

 op = [0] * N

 

 # Function call

 comb(arr, N, K, 0, op, 0, S)

 

# This code is contributed by himanshu77  
  
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

 

// Function to find all the subsequences

// of a given length and having sum S

static void comb(int []arr, int len, int r,

 int ipos, int[] op, int opos,

 int sum)

{

 

 // Termination condition

 if (opos == r)

 {

 int sum2 = 0;

 for(int i = 0; i < opos; i++) 

 {

 

 // Add value to sum

 sum2 = sum2 + op[i];

 }

 

 // Check if the resultant sum

 // equals to target sum

 if (sum == sum2)

 {

 

 // If true

 for(int i = 0; i < opos; i++)

 

 // Print resultant array

 Console.Write(op[i] + ", ");

 Console.WriteLine();

 }

 

 // End this recursion stack

 return;

 }

 if (ipos < len) 

 {

 

 // Check all the combinations

 // using backtracking

 comb(arr, len, r, ipos + 1,

 op, opos, sum);

 

 op[opos] = arr[ipos];

 

 // Check all the combinations

 // using backtracking

 comb(arr, len, r, ipos + 1,

 op, opos + 1, sum);

 }

}

 

// Driver Code

public static void Main(String[] args)

{

 

 // Given array

 int []arr = { 4, 6, 8, 2, 12 };

 int K = 3;

 int S = 20;

 

 int N = arr.Length;

 

 // To store the subsquence

 int []op = new int[N];

 

 // Function call

 comb(arr, N, K, 0, op, 0, S);

}

}

 

// This code is contributed by amal kumar choubey  
  
---  
  
 __

 __

  
 **Output:**

    
    
    6, 2, 12, 

**Time Complexity:** _O(N*N!)_

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


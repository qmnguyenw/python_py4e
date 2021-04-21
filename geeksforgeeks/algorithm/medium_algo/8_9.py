Maximum sum possible for a sub-sequence such that no two elements appear at a
distance < K in the array



Given an array **arr[]** of **n** integers and an integer **k** , the task is
to find the maximum sum possible for a sub-sequence such that no two elements
of the sub-sequence appear at a distance **≤ k** in the original array.

 **Examples:**

>  **Input:** arr[] = {5, 3, 4, 11, 2}, k=1  
>  **Output:** 16  
> All possible sub-sequences are {5, 4, 2}, {5, 11}, {5, 2}, {3, 11}, {3, 2},
> {4, 2} and {11}  
> Out of which 5 + 11 = 16 gives the maximum sum.
>
>  **Input:** arr[] = {6, 7, 1, 3, 8, 2, 4}, k = 2  
>  **Output:** 15

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** While chosing an element at index **i** , we have two options,
either we include the current element in the sub-sequence or we don’t. Let
**dp[i]** represents the maximum sum so far on reaching element at index
**i**. We can calculate the value of **dp[i]** as follows:

  

  

>  **dp[i] = max(dp[i – (k + 1)] + arr[i], dp[i – 1])**
>
>  **dp[i – (k + 1)] + arr[i]** is the case when element at index **i** is
> included. In that situation, maximum value will be arr[i] + maximum value
> till the last included element from the array.
>
>  **dp[i – 1]** is the case when current element is not included and the
> maximum value till now will be the maximum value till the previous element.

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

 

// Function to return the maximum sum possible

int maxSum(int* arr, int k, int n)

{

 if (n == 0)

 return 0;

 if (n == 1)

 return arr[0];

 if (n == 2)

 return max(arr[0], arr[1]);

 

 // dp[i] represent the maximum sum so far

 // after reaching current position i

 int dp[n];

 

 // Initialize dp[0]

 dp[0] = arr[0];

 

 // Initialize the dp values till k since any

 // two elements included in the sub-sequence

 // must be atleast k indices apart, and thus

 // first element and second element

 // will be k indices apart

 for (int i = 1; i <= k; i++)

 dp[i] = max(arr[i], dp[i - 1]);

 

 // Fill remaining positions

 for (int i = k + 1; i < n; i++)

 dp[i] = max(arr[i], dp[i - (k + 1)] + arr[i]);

 

 // Return the maximum sum

 int max = *(std::max_element(dp, dp + n));

 return max;

}

 

// Driver code

int main()

{

 int arr[] = { 6, 7, 1, 3, 8, 2, 4 };

 int n = sizeof(arr) / sizeof(arr[0]);

 int k = 2;

 cout << maxSum(arr, k, n);

 

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

 

// Function to return the maximum sum possible

static int maxSum(int []arr, int k, int n)

{

 if (n == 0)

 return 0;

 if (n == 1)

 return arr[0];

 if (n == 2)

 return Math.max(arr[0], arr[1]);

 

 // dp[i] represent the maximum sum so far

 // after reaching current position i

 int[] dp = new int[n];

 

 // Initialize dp[0]

 dp[0] = arr[0];

 

 // Initialize the dp values till k since any

 // two elements included in the sub-sequence

 // must be atleast k indices apart, and thus

 // first element and second element

 // will be k indices apart

 for (int i = 1; i <= k; i++)

 dp[i] = Math.max(arr[i], dp[i - 1]);

 

 // Fill remaining positions

 for (int i = k + 1; i < n; i++)

 dp[i] = Math.max(arr[i], dp[i - (k + 1)] + arr[i]);

 

 // Return the maximum sum

 return maximum(dp);

}

 

static int maximum(int[] arr)

{

 int max = Integer.MIN_VALUE;

 for(int i = 0; i < arr.length; i++) 

 {

 if(arr[i] > max) 

 {

 max = arr[i];

 }

 }

 return max;

}

 

// Driver code

public static void main (String[] args)

{

 int []arr = { 6, 7, 1, 3, 8, 2, 4 };

 int n = arr.length;

 int k = 2;

 System.out.println(maxSum(arr, k, n));

}

}

 

// This code is contributed by mits  
  
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

 

# Function to return the 

# maximum sum possible 

def maxSum(arr, k, n) : 

 

 if (n == 0) :

 return 0; 

 if (n == 1) :

 return arr[0]; 

 if (n == 2) :

 return max(arr[0], arr[1]); 

 

 # dp[i] represent the maximum sum so far 

 # after reaching current position i 

 dp = [0] * n ; 

 

 # Initialize dp[0] 

 dp[0] = arr[0]; 

 

 # Initialize the dp values till k since any 

 # two elements included in the sub-sequence 

 # must be atleast k indices apart, and thus 

 # first element and second element 

 # will be k indices apart 

 for i in range(1, k + 1) : 

 dp[i] = max(arr[i], dp[i - 1]); 

 

 # Fill remaining positions 

 for i in range(k + 1, n) : 

 dp[i] = max(arr[i], 

 dp[i - (k + 1)] + arr[i]); 

 

 # Return the maximum sum 

 max_element = max(dp); 

 return max_element; 

 

# Driver code 

if __name__ == "__main__" : 

 arr = [ 6, 7, 1, 3, 8, 2, 4 ]; 

 n = len(arr); 

 k = 2; 

 

 print(maxSum(arr, k, n)); 

 

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

using System.Linq;

 

class GFG

{

 

// Function to return the maximum sum possible

static int maxSum(int []arr, int k, int n)

{

 if (n == 0)

 return 0;

 if (n == 1)

 return arr[0];

 if (n == 2)

 return Math.Max(arr[0], arr[1]);

 

 // dp[i] represent the maximum sum so far

 // after reaching current position i

 int[] dp = new int[n];

 

 // Initialize dp[0]

 dp[0] = arr[0];

 

 // Initialize the dp values till k since any

 // two elements included in the sub-sequence

 // must be atleast k indices apart, and thus

 // first element and second element

 // will be k indices apart

 for (int i = 1; i <= k; i++)

 dp[i] = Math.Max(arr[i], dp[i - 1]);

 

 // Fill remaining positions

 for (int i = k + 1; i < n; i++)

 dp[i] = Math.Max(arr[i], dp[i - (k + 1)] + arr[i]);

 

 // Return the maximum sum

 int max = dp.Max();

 return max;

}

 

// Driver code

static void Main()

{

 int []arr = { 6, 7, 1, 3, 8, 2, 4 };

 int n = arr.Length;

 int k = 2;

 Console.WriteLine(maxSum(arr, k, n));

}

}

 

// This code is contributed by mits  
  
---  
  
 __

 __

 **Output:**

    
    
    15
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


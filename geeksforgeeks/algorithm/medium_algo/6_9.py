Number of subarrays with GCD equal to 1



Given an array **arr[]** , the task is to find the number of sub-arrays with
GCD value equal to **1**.

 **Examples:**

>  **Input:** arr[] = {1, 1, 1}  
>  **Output:** 6  
> All the subarrays of the given array  
> will have GCD equal to 1.
>
>  **Input:** arr[] = {2, 2, 2}  
>  **Output:** 0

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** The key observation is that if the GCD of all the elements of
the sub-array **arr[l…r]** is known then the GCD of all the elements of the
sub-array **arr[l…r+1]** can be obtained by simply taking the GCD of the
previous sub-array with **arr[r + 1]**.  
Thus, for every index **i** , keep iterating forward and compute the GCD from
index **i** to **j** and check if its equal to **1**.

  

  

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

 

// Function to return the required count

int cntSubArr(int* arr, int n)

{

 // To store the final answer

 int ans = 0;

 

 for (int i = 0; i < n; i++) {

 

 // To store the GCD starting from

 // index 'i'

 int curr_gcd = 0;

 

 // Loop to find the gcd of each subarray

 // from arr[i] to arr[i...n-1]

 for (int j = i; j < n; j++) {

 curr_gcd = __gcd(curr_gcd, arr[j]);

 

 // Increment the count if curr_gcd = 1

 ans += (curr_gcd == 1);

 }

 }

 

 // Return the final answer

 return ans;

}

 

// Driver code

int main()

{

 int arr[] = { 1, 1, 1 };

 int n = sizeof(arr) / sizeof(int);

 

 cout << cntSubArr(arr, n);

 

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

 

// Function to return the required count

static int cntSubArr(int []arr, int n)

{

 // To store the final answer

 int ans = 0;

 

 for (int i = 0; i < n; i++) 

 {

 

 // To store the GCD starting from

 // index 'i'

 int curr_gcd = 0;

 

 // Loop to find the gcd of each subarray

 // from arr[i] to arr[i...n-1]

 for (int j = i; j < n; j++) 

 {

 curr_gcd = __gcd(curr_gcd, arr[j]);

 

 // Increment the count if curr_gcd = 1

 ans += (curr_gcd == 1) ? 1 : 0;

 }

 }

 

 // Return the final answer

 return ans;

}

 

static int __gcd(int a, int b) 

{ 

 if (b == 0) 

 return a; 

 return __gcd(b, a % b); 

}

 

// Driver code

public static void main(String []args) 

{

 int arr[] = { 1, 1, 1 };

 int n = arr.length;

 

 System.out.println(cntSubArr(arr, n));

}

}

 

// This code is contributed by Rajput-Ji  
  
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

from math import gcd

 

# Function to return the required count 

def cntSubArr(arr, n) :

 

 # To store the final answer 

 ans = 0; 

 

 for i in range(n) :

 

 # To store the GCD starting from 

 # index 'i' 

 curr_gcd = 0; 

 

 # Loop to find the gcd of each subarray 

 # from arr[i] to arr[i...n-1] 

 for j in range(i, n) :

 curr_gcd = gcd(curr_gcd, arr[j]); 

 

 # Increment the count if curr_gcd = 1 

 ans += (curr_gcd == 1);

 

 # Return the final answer 

 return ans; 

 

# Driver code 

if __name__ == "__main__" :

 

 arr = [ 1, 1, 1 ]; 

 n = len(arr); 

 

 print(cntSubArr(arr, n)); 

 

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

// C# implementation of the approach

using System;

 

class GFG 

{

 

// Function to return the required count

static int cntSubArr(int []arr, int n)

{

 // To store the final answer

 int ans = 0;

 

 for (int i = 0; i < n; i++) 

 {

 

 // To store the GCD starting from

 // index 'i'

 int curr_gcd = 0;

 

 // Loop to find the gcd of each subarray

 // from arr[i] to arr[i...n-1]

 for (int j = i; j < n; j++) 

 {

 curr_gcd = __gcd(curr_gcd, arr[j]);

 

 // Increment the count if curr_gcd = 1

 ans += (curr_gcd == 1) ? 1 : 0;

 }

 }

 

 // Return the final answer

 return ans;

}

 

static int __gcd(int a, int b) 

{ 

 if (b == 0) 

 return a; 

 return __gcd(b, a % b); 

}

 

// Driver code

public static void Main(String []args) 

{

 int []arr = { 1, 1, 1 };

 int n = arr.Length;

 

 Console.WriteLine(cntSubArr(arr, n));

}

}

 

// This code is contributed by Rajput-Ji  
  
---  
  
 __

 __

 **Output:**

    
    
    6
    

**Time Complexity:** O(N2)

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


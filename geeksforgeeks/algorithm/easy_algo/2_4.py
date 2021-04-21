Maximum LCM among all pairs (i, j) from the given Array



Given an array **arr[]** , the task is to find the maximum LCM when the
elements of the array are taken in pairs.

 **Examples:**

>  **Input:** arr[] = {17, 3, 8, 6}  
> **Output:** 136  
> **Explanation:**  
> Respective Pairs with their LCM are:  
> {8, 17} has LCM 136,  
> {3, 17} has LCM 51,  
> {6, 17} has LCM 102,  
> {3, 8} has LCM 24,  
> {3, 6} has LCM 6, and  
> {6, 8} has LCM 24.  
> Maximum LCM among these =136.  
>  **Input:** array[] = {1, 8, 12, 9}  
> **Output:** 72  
> **Explanation:**  
> 72 is the highest LCM among all the pairs of the given array.

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Naive Approach:** Use two loops to generate all possible pairs of elements
of the array and calculate LCM of them. Update the LCM whenever we get a
higher value.  
_**Time Complexity:** O(N2)_  
Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation to find the maximum

// LCM of pairs in an array

#include <bits/stdc++.h>

using namespace std;

// Function comparing all LCM pairs

int maxLcmOfPairs(int arr[], int n)

{

 // To store the highest LCM

 int maxLCM = -1;

 // To generate all pairs from array

 for (int i = 0; i < n; i++) {

 for (int j = i + 1; j < n; j++) {

 // Find LCM of the pair

 // Update the maxLCM if this is

 // greater than its existing value

 maxLCM

 = max(maxLCM, (arr[i] * arr[j])

 / __gcd(arr[i], arr[j]));

 }

 }

 // Return the highest value of LCM

 return maxLCM;

}

// Driver code

int main()

{

 int arr[] = { 17, 3, 8, 6 };

 int n = sizeof(arr) / sizeof(arr[0]);

 cout << maxLcmOfPairs(arr, n);

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

// Java implementation to find the maximum

// LCM of pairs in an array

import java.util.*;

class GFG {

 // Function comparing all LCM pairs

 static int maxLcmOfPairs(int arr[], int n)

 {

 // To store the highest LCM

 int maxLCM = -1;

 // To generate all pairs from array

 for (int i = 0; i < n; i++) {

 for (int j = i + 1; j < n; j++) {

 // Find LCM of the pair

 // Update the maxLCM if this is

 // greater than its existing value

 maxLCM = Math.max(

 maxLCM, (arr[i] * arr[j])

 / __gcd(arr[i], arr[j]));

 }

 }

 // Return the highest value of LCM

 return maxLCM;

 }

 static int __gcd(int a, int b)

 {

 return b == 0 ? a : __gcd(b, a % b);

 }

 // Driver code

 public static void main(String[] args)

 {

 int arr[] = { 17, 3, 8, 6 };

 int n = arr.length;

 System.out.print(maxLcmOfPairs(arr, n));

 }

}

// This code is contributed by sapnasingh4991  
  
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

# Python3 implementation to find the

# maximum LCM of pairs in an array

from math import gcd

# Function comparing all LCM pairs

def maxLcmOfPairs(arr, n):

 # To store the highest LCM

 maxLCM = -1

 # To generate all pairs from array

 for i in range(n):

 for j in range(i + 1, n, 1):

 # Find LCM of the pair

 # Update the maxLCM if this is

 # greater than its existing value

 maxLCM = max(maxLCM, (arr[i] * arr[j]) //

 gcd(arr[i], arr[j]))

 # Return the highest value of LCM

 return maxLCM

# Driver code

if __name__ == '__main__':

 arr = [17, 3, 8, 6]

 n = len(arr)

 print(maxLcmOfPairs(arr, n))

# This code is contributed by hupendraSingh  
  
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

// C# implementation to find the maximum

// LCM of pairs in an array

using System;

class GFG {

 // Function comparing all LCM pairs

 static int maxLcmOfPairs(int[] arr, int n)

 {

 // To store the highest LCM

 int maxLCM = -1;

 // To generate all pairs from array

 for (int i = 0; i < n; i++) {

 for (int j = i + 1; j < n; j++) {

 // Find LCM of the pair

 // Update the maxLCM if this is

 // greater than its existing value

 maxLCM = Math.Max(

 maxLCM, (arr[i] * arr[j])

 / __gcd(arr[i], arr[j]));

 }

 }

 // Return the highest value of LCM

 return maxLCM;

 }

 static int __gcd(int a, int b)

 {

 return b == 0 ? a : __gcd(b, a % b);

 }

 // Driver code

 public static void Main()

 {

 int[] arr = { 17, 3, 8, 6 };

 int n = arr.Length;

 Console.Write(maxLcmOfPairs(arr, n));

 }

}

// This code is contributed by Code_Mech  
  
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

// javascript implementation to find the maximum

// LCM of pairs in an array

 // Function comparing all LCM pairs

 function maxLcmOfPairs(arr , n)

 {

 

 // To store the highest LCM

 var maxLCM = -1;

 // To generate all pairs from array

 for (i = 0; i < n; i++)

 {

 for (j = i + 1; j < n; j++)

 {

 // Find LCM of the pair

 // Update the maxLCM if this is

 // greater than its existing value

 maxLCM = Math.max(maxLCM, (arr[i] * arr[j]) / __gcd(arr[i], arr[j]));

 }

 }

 // Return the highest value of LCM

 return maxLCM;

 }

 function __gcd(a , b) {

 return b == 0 ? a : __gcd(b, a % b);

 }

 // Driver code

 var arr = [ 17, 3, 8, 6 ];

 var n = arr.length;

 document.write(maxLcmOfPairs(arr, n));

// This code is contributed by umadevi9616

</script>  
  
---  
  
 __

 __

 **Output**

  

  

    
    
    136


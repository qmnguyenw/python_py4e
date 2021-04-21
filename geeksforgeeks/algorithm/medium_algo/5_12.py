Remove minimum elements from ends of array so that sum decreases by at least K
| O(N)



Given an array **arr[]** consisting of **N** elements, the task is to remove
minimum number of elements from the ends of the array such that the total sum
of the array decreases by at least **K**. **Note** that **K** will always be
less than or equal to the sum of all the elements of the array.

 **Examples:**

>  **Input:** arr[] = {1, 11, 5, 5}, K = 11  
>  **Output:** 2  
> After removing two elements form the left  
> end, the sum decreases by 1 + 11 = 12.  
> Thus, the answer is 2.
>
>  **Input:** arr[] = {1, 2, 3}, K = 6  
>  **Output:** 3

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** A dynamic programming based approach has already been discussed
in another post. In this article, an approach using the two-pointer technique
will be discussed. It can be observed that the task is to find the longest
sub-array with the sum of its elements at most **sum(arr) – K** where
**sum(arr)** is the sum of all the elements of the array **arr[]**.  
Let the length of such subarray be **L**. Thus, the minimum number of elements
to be removed from the array will be equal to **N – L**. To find the length of
longest such subarray, refer this article.

  

  

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

 

// Function to return the count of minimum

// elements to be removed from the ends

// of the array such that the sum of the

// array decrease by at least K

int minCount(int* arr, int n, int k)

{

 

 // To store the final answer

 int ans = 0;

 

 // Maximum possible sum required

 int sum = 0;

 for (int i = 0; i < n; i++)

 sum += arr[i];

 sum -= k;

 

 // Left point

 int l = 0;

 

 // Right pointer

 int r = 0;

 

 // Total current sum

 int tot = 0;

 

 // Two pointer loop

 while (l < n) {

 

 // If the sum fits

 if (tot <= sum) {

 

 // Update the answer

 ans = max(ans, r - l);

 if (r == n)

 break;

 

 // Update the total sum

 tot += arr[r++];

 }

 

 else {

 

 // Increment the left pointer

 tot -= arr[l++];

 }

 }

 

 return (n - ans);

}

 

// Driver code

int main()

{

 int arr[] = { 1, 11, 5, 5 };

 int n = sizeof(arr) / sizeof(int);

 int k = 11;

 

 cout << minCount(arr, n, k);

 

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

 

 // Function to return the count of minimum 

 // elements to be removed from the ends 

 // of the array such that the sum of the 

 // array decrease by at least K 

 static int minCount(int arr[], 

 int n, int k) 

 { 

 

 // To store the final answer 

 int ans = 0; 

 

 // Maximum possible sum required 

 int sum = 0; 

 for (int i = 0; i < n; i++) 

 sum += arr[i]; 

 sum -= k; 

 

 // Left point 

 int l = 0; 

 

 // Right pointer 

 int r = 0; 

 

 // Total current sum 

 int tot = 0; 

 

 // Two pointer loop 

 while (l < n) 

 { 

 

 // If the sum fits 

 if (tot <= sum)

 { 

 

 // Update the answer 

 ans = Math.max(ans, r - l); 

 if (r == n) 

 break; 

 

 // Update the total sum 

 tot += arr[r++]; 

 } 

 else

 { 

 

 // Increment the left pointer 

 tot -= arr[l++]; 

 } 

 }

 return (n - ans); 

 } 

 

 // Driver code 

 public static void main (String[] args)

 { 

 int arr[] = { 1, 11, 5, 5 }; 

 int n = arr.length; 

 int k = 11; 

 

 System.out.println(minCount(arr, n, k)); 

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

# Python3 implementation of the approach

 

# Function to return the count of minimum 

# elements to be removed from the ends 

# of the array such that the sum of the 

# array decrease by at least K 

def minCount(arr, n, k) :

 

 # To store the final answer 

 ans = 0; 

 

 # Maximum possible sum required 

 sum = 0; 

 for i in range(n) :

 sum += arr[i]; 

 sum -= k; 

 

 # Left point 

 l = 0; 

 

 # Right pointer 

 r = 0; 

 

 # Total current sum 

 tot = 0; 

 

 # Two pointer loop 

 while (l < n) :

 

 # If the sum fits 

 if (tot <= sum) :

 

 # Update the answer 

 ans = max(ans, r - l); 

 if (r == n) :

 break; 

 

 # Update the total sum 

 tot += arr[r]; 

 r += 1

 

 else :

 

 # Increment the left pointer 

 tot -= arr[l]; 

 l += 1

 

 return (n - ans); 

 

# Driver code 

if __name__ == "__main__" : 

 

 arr = [ 1, 11, 5, 5 ]; 

 n = len(arr); 

 k = 11; 

 

 print(minCount(arr, n, k)); 

 

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

 

 // Function to return the count of minimum 

 // elements to be removed from the ends 

 // of the array such that the sum of the 

 // array decrease by at least K 

 static int minCount(int []arr, 

 int n, int k) 

 { 

 

 // To store the final answer 

 int ans = 0; 

 

 // Maximum possible sum required 

 int sum = 0; 

 for (int i = 0; i < n; i++) 

 sum += arr[i]; 

 sum -= k; 

 

 // Left point 

 int l = 0; 

 

 // Right pointer 

 int r = 0; 

 

 // Total current sum 

 int tot = 0; 

 

 // Two pointer loop 

 while (l < n) 

 { 

 

 // If the sum fits 

 if (tot <= sum)

 { 

 

 // Update the answer 

 ans = Math.Max(ans, r - l); 

 if (r == n) 

 break; 

 

 // Update the total sum 

 tot += arr[r++]; 

 } 

 else

 { 

 

 // Increment the left pointer 

 tot -= arr[l++]; 

 } 

 }

 return (n - ans); 

 } 

 

 // Driver code 

 public static void Main()

 { 

 int []arr = { 1, 11, 5, 5 }; 

 int n = arr.Length; 

 int k = 11; 

 

 Console.WriteLine(minCount(arr, n, k)); 

 } 

}

 

// This code is contributed by AnkitRai01  
  
---  
  
 __

 __

 **Output:**

    
    
    2
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


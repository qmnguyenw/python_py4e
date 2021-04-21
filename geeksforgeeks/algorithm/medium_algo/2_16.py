Count of subsets having sum of min and max element less than K



Given an integer array **arr[]** and an integer **K** , the task is to find
the number of non-empty subsets S such that **min(S) + max(S) < K**.

 **Examples:**

>  **Input** : arr[] = {2, 4, 5, 7} K = 8  
>  **Output** : 4  
>  **Explanation:**  
>  The possible subsets are {2}, {2, 4}, {2, 4, 5} and {2, 5}
>
>  **Input:** : arr[] = {2, 4, 2, 5, 7} K = 10  
>  **Output:** 26

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach**

  

  

  1. Sort the input array first.
  2. Now use Two Pointer Technique to count the number of subsets.
  3. Let take two pointers left and right and set left = 0 and right = N-1.
  4. >  **if (arr[left] + arr[right] < K )**  
> Increment the left pointer by 1 and add **2 j – i** into answer, because the
> left and right values make up a potential end values of a subset. All the
> values from [i, j – 1] also make up end of subsets which will have the sum <
> K. So, we need to calculate all the possible subsets for left = i and right
> ∊ [i, j]. So, after suming up values 2 j – i + 1 \+ 2 j – i – 2 \+ … + 2 0
> of the GP, we get **2 j – i **.  
>  **if( arr[left] + arr[right] >= K )**  
> Decrement the right pointer by 1.

  5. Repeat the below process until **left <= right**.

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to print count

// of subsets S such that

// min(S) + max(S) < K

 

#include <bits/stdc++.h>

using namespace std;

 

// Function that return the

// count of subset such that

// min(S) + max(S) < K

int get_subset_count(int arr[], int K,

 int N)

{

 // Sorting the array

 sort(arr, arr + N);

 

 int left, right;

 left = 0;

 right = N - 1;

 

 // ans stores total number of subsets

 int ans = 0;

 

 while (left <= right) {

 if (arr[left] + arr[right] < K) {

 

 // add all posible subsets

 // between i and j

 ans += 1 << (right - left);

 left++;

 }

 else {

 // Decrease the sum

 right--;

 }

 }

 return ans;

}

 

// Driver code

int main()

{

 int arr[] = { 2, 4, 5, 7 };

 int K = 8;

 int N = sizeof(arr) / sizeof(arr[0]);

 cout << get_subset_count(arr, K, N);

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

// Java program to print count

// of subsets S such that

// Math.min(S) + Math.max(S) < K

import java.util.*;

 

class GFG{

 

// Function that return the

// count of subset such that

// Math.min(S) + Math.max(S) < K

static int get_subset_count(int arr[], int K,

 int N)

{

 

 // Sorting the array

 Arrays.sort(arr);

 

 int left, right;

 left = 0;

 right = N - 1;

 

 // ans stores total number

 // of subsets

 int ans = 0;

 

 while (left <= right)

 {

 if (arr[left] + arr[right] < K)

 {

 

 // Add all posible subsets

 // between i and j

 ans += 1 << (right - left);

 left++;

 }

 else

 {

 

 // Decrease the sum

 right--;

 }

 }

 return ans;

}

 

// Driver code

public static void main(String[] args)

{

 int arr[] = { 2, 4, 5, 7 };

 int K = 8;

 int N = arr.length;

 

 System.out.print(get_subset_count(arr, K, N));

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

# Python3 program to print

# count of subsets S such 

# that min(S) + max(S) < K 

 

# Function that return the

# count of subset such that

# min(S) + max(S) < K 

def get_subset_count(arr, K, N):

 

 # Sorting the array 

 arr.sort() 

 

 left = 0; 

 right = N - 1; 

 

 # ans stores total number of subsets 

 ans = 0; 

 

 while (left <= right):

 if (arr[left] + arr[right] < K):

 

 # Add all posible subsets 

 # between i and j 

 ans += 1 << (right - left); 

 left += 1; 

 else:

 

 # Decrease the sum 

 right -= 1; 

 

 return ans; 

 

# Driver code 

arr = [ 2, 4, 5, 7 ]; 

K = 8; 

 

print(get_subset_count(arr, K, 4))

 

# This code is contributed by grand_master  
  
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

// C# program to print count

// of subsets S such that

// Math.Min(S) + Math.Max(S) < K

using System;

 

class GFG{

 

// Function that return the

// count of subset such that

// Math.Min(S) + Math.Max(S) < K

static int get_subset_count(int []arr, int K,

 int N)

{

 

 // Sorting the array

 Array.Sort(arr);

 

 int left, right;

 left = 0;

 right = N - 1;

 

 // ans stores total number

 // of subsets

 int ans = 0;

 

 while (left <= right)

 {

 if (arr[left] + arr[right] < K)

 {

 

 // Add all posible subsets

 // between i and j

 ans += 1 << (right - left);

 left++;

 }

 else

 {

 

 // Decrease the sum

 right--;

 }

 }

 return ans;

}

 

// Driver code

public static void Main(String[] args)

{

 int []arr = { 2, 4, 5, 7 };

 int K = 8;

 int N = arr.Length;

 

 Console.Write(get_subset_count(arr, K, N));

}

}

 

// This code is contributed by gauravrajput1  
  
---  
  
 __

 __

 **Output:**

    
    
    4
    

**Time Complexity:** _O(N* log N)_  
 **Auxiliary Space:** _O(1)_

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


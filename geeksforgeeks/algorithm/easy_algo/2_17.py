Longest increasing sub-sequence formed by concatenating array to itself N
times



Given an array **arr[]** of size **N** , the task is to find the length of the
longest increasing subsequence in the array formed by the concatenation of the
arr[] to itself at the end N times.  
 **Examples:**  

> **Input:** arr[] = {3, 2, 1}, N = 3  
> **Output:** 3  
> **Explanation:**  
> The array formed by the concatenation –  
> {3, 2, 1, 3, 2, 1, 3, 2, 1}  
> The longest increasing subsequence that can be formed from this array is of
> length 3 which is {1, 2, 3}
>
>  **Input:** N = 3 arr[] = {3, 1, 4}  
> **Output:**  
> **Explanation:**  
> The array formed by concatenation –  
> {3, 1, 4, 3, 1, 4, 3, 1, 4}  
> The longest increasing subsequence that can be formed from this array is of
> length 3 which is {1, 3, 4}

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 ** _Naive Approach:_**  
The basic approach to solve this problem is to create the final array by
concatenating the given array to itself N times, and then finding the longest
increasing subsequence in it.  
**Time Complexity:** O(N2)  
**Auxiliary Space:** O(N2)

 **Efficient Approach:**  
According to the efficient approach, any element that is present in the
longest increasing subsequence can be present only once. It means that the
repetition of the elements N times won’t affect the subsequence, but, any
element can be chosen anytime. Therefore, it would be efficient to find the
longest increasing subset in the array of length N, which can be found by
finding all the unique elements of the array.  
Below is the algorithm for the efficient approach:  
**Algorithm:**

  

  

  * Store the unique elements of the array in a map with (element, count) as the (key, value) pair.
  * For each element in the array 
    * If the current element is not present in the map, then insert it in the map, with count 1.
    * Otherwise, increment the count of the array elements in the array.
  * Find the length of the map which will be the desired answer.

 **For Example:**

> Given Array be – {4, 4, 1}  
> Creating the map of unique elements: {(4, 2), (1, 1)}  
> Length of the Map = 2  
> Hence the required longest subsequence = 2

Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation to find the

// longest increasing subsequence

// in repeating element of array

#include <bits/stdc++.h>

using namespace std;

// Function to find the LCS

int findLCS(int arr[], int n){

 unordered_map<int, int> mp;

 

 // Loop to create frequency array

 for (int i = 0; i < n; i++) {

 mp[arr[i]]++;

 }

 return mp.size();

}

// Driver code

int main()

{

 int n = 3;

 int arr[] = {3, 2, 1};

 cout<<findLCS(arr, n);

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

// Java implementation to find the

// longest increasing subsequence

// in repeating element of array

import java.util.*;

class GFG{

// Function to find the LCS

static int findLCS(int arr[], int n)

{

 HashMap<Integer,

 Integer> mp = new HashMap<Integer,

 Integer>();

 

 // Loop to create frequency array

 for(int i = 0; i < n; i++)

 {

 if(mp.containsKey(arr[i]))

 {

 mp.put(arr[i], mp.get(arr[i]) + 1);

 }

 else

 {

 mp.put(arr[i], 1);

 }

 }

 return mp.size();

}

// Driver code

public static void main(String[] args)

{

 int n = 3;

 int arr[] = { 3, 2, 1 };

 

 System.out.print(findLCS(arr, n));

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

# Python3 implementation to find the

# longest increasing subsequence

# in repeating element of array

# Function to find the LCS

def findLCS(arr, n):

 

 mp = {}

 # Loop to create frequency array

 for i in range(n):

 if arr[i] in mp:

 mp[arr[i]] += 1

 else:

 mp[arr[i]] = 1

 

 return len(mp)

# Driver code

n = 3

arr = [ 3, 2, 1 ]

print(findLCS(arr, n))

# This code is contributed by ng24_7  
  
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

// C# implementation to find the

// longest increasing subsequence

// in repeating element of array

using System;

using System.Collections.Generic;

class GFG{

// Function to find the LCS

static int findLCS(int []arr, int n)

{

 Dictionary<int,

 int> mp = new Dictionary<int,

 int>();

 

 // Loop to create frequency array

 for(int i = 0; i < n; i++)

 {

 if(mp.ContainsKey(arr[i]))

 {

 mp[arr[i]] = mp[arr[i]] + 1;

 }

 else

 {

 mp.Add(arr[i], 1);

 }

 }

 return mp.Count;

}

// Driver code

public static void Main(String[] args)

{

 int n = 3;

 int []arr = { 3, 2, 1 };

 

 Console.Write(findLCS(arr, n));

}

}

// This code is contributed by amal kumar choubey  
  
---  
  
 __

 __

 **Performance Analysis:**

  * **Time Complexity:** As in the above approach, there only one loop which takes O(N) time in worst case, Hence the Time Complexity will be **O(N)**.
  *  **Space Complexity:** As in the above approach, there one Hash map used which can take O(N) space in worst case, Hence the space complexity will be **O(N)**

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


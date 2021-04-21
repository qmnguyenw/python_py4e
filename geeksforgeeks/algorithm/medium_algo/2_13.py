Find intersection of intervals given by two lists



Given two **2-D arrays** which represent intervals. Each 2-D array represents
a list of intervals. Each list of intervals is **disjoint** and sorted in
increasing order. Find the intersection or set of ranges that are common to
both the lists.

> Disjoint means no element is common in a list. Example: {1, 4} and {5, 6}
> are disjoint while {1, 4} and {2, 5} are not as 2, 3 and 4 are common to
> both intervals.

**Examples:**

> **Input:** arr1[][] = {{0, 4}, {5, 10}, {13, 20}, {24, 25}}  
> arr2[][] = {{1, 5}, {8, 12}, {15, 24}, {25, 26}}  
> **Output:** {{1, 4}, {5, 5}, {8, 10}, {15, 20}, {24, 24}, {25, 25}}  
>  **Explanation:**  
>  {1, 4} lies completely within range {0, 4} and {1, 5}. Hence, {1, 4} is the
> desired intersection. Similarly, {24, 24} lies completely within two
> intervals {24, 25} and {15, 24}.
>
>  **Input:** arr1[][] = {{0, 2}, {5, 10}, {12, 22}, {24, 25}}  
> arr2[][] = {{1, 4}, {9, 12}, {15, 24}, {25, 26}}  
> **Output:** {{1, 2}, {9, 10}, {12, 12}, {15, 22}, {24, 24}, {25, 25}}  
> **Explanation:**  
> {1, 2} lies completely within range {0, 2} and {1, 4}. Hence, {1, 2} is the
> desired intersection. Similarly, {12, 12} lies completely within two
> intervals {12, 22} and {9, 12}.  
>
>
>  
>
>
>  
>

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:**  
To solve the problem mentioned above, two pointer technique can be used, as
per the steps given below:

  * Maintain **two pointers** i and j to traverse the two interval lists, arr1 and arr2 respectively.
  * Now, if arr1[i] has smallest endpoint, it can only intersect with arr2[j]. Similarly, if arr2[j] has smallest endpoint, it can only intersect with arr1[i]. If intersection occurs, find the intersecting segment.
  * [l, r] will be the intersecting segment iff l <= r, where **l = max(arr1[i][0], arr2[j][0])** and **r = min(arr1[i][1], arr2[j][1])**.
  * Increment the i and j pointers accordingly to move ahead.

Below is the implementation of the approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation to find the

// intersection of the two intervals

 

#include <bits/stdc++.h>

using namespace std;

 

// Function to print intersecting intervals

void printIntervals(vector<vector<int> > arr1,

 vector<vector<int> > arr2)

{

 

 // i and j pointers for

 // arr1 and arr2 respectively

 int i = 0, j = 0;

 

 // Size of the two lists

 int n = arr1.size(), m = arr2.size();

 

 // Loop through all intervals unless

 // one of the interval gets exhausted

 while (i < n && j < m) {

 // Left bound for intersecting segment

 int l = max(arr1[i][0], arr2[j][0]);

 

 // Right bound for intersecting segment

 int r = min(arr1[i][1], arr2[j][1]);

 

 // If segment is valid print it

 if (l <= r)

 cout << "{" << l << ", "

 << r << "}\n";

 

 // If i-th interval's right

 // bound is smaller

 // increment i else

 // increment j

 if (arr1[i][1] < arr2[j][1])

 i++;

 else

 j++;

 }

}

 

// Driver code

int main()

{

 

 vector<vector<int> > arr1

 = { { 0, 4 }, { 5, 10 },

 { 13, 20 }, { 24, 25 } };

 

 vector<vector<int> > arr2

 = { { 1, 5 }, { 8, 12 },

 { 15, 24 }, { 25, 26 } };

 

 printIntervals(arr1, arr2);

 

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

// Java implementation to find

// intersecting intervals

class GFG{

 

// Function to print intersecting intervals

static void printIntervals(int arr1[][],

 int arr2[][])

{

 

 // i and j pointers for arr1 and 

 // arr2 respectively

 int i = 0, j = 0;

 

 int n = arr1.length, m = arr2.length;

 

 // Loop through all intervals unless 

 // one of the interval gets exhausted

 while (i < n && j < m) 

 {

 

 // Left bound for intersecting segment

 int l = Math.max(arr1[i][0], arr2[j][0]);

 

 // Right bound for intersecting segment

 int r = Math.min(arr1[i][1], arr2[j][1]);

 

 // If segment is valid print it

 if (l <= r) 

 System.out.println("{" + l + ", " +

 r + "}");

 

 // If i-th interval's right bound is 

 // smaller increment i else increment j

 if (arr1[i][1] < arr2[j][1])

 i++;

 else

 j++;

 }

}

 

// Driver code

public static void main(String[] args)

{

 int arr1[][] = { { 0, 4 }, { 5, 10 },

 { 13, 20 }, { 24, 25 } };

 

 int arr2[][] = { { 1, 5 }, { 8, 12 }, 

 { 15, 24 }, { 25, 26 } };

 

 printIntervals(arr1, arr2);

}

}

 

// This code is contributed by sarthak_eddy  
  
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

# Python3 implementation to find

# intersecting intervals

 

# Function to print intersecting 

# intervals

def printIntervals(arr1, arr2):

 

 # i and j pointers for arr1 

 # and arr2 respectively

 i = j = 0

 

 n = len(arr1)

 m = len(arr2)

 

 # Loop through all intervals unless one 

 # of the interval gets exhausted

 while i < n and j < m:

 

 # Left bound for intersecting segment

 l = max(arr1[i][0], arr2[j][0])

 

 # Right bound for intersecting segment

 r = min(arr1[i][1], arr2[j][1])

 

 # If segment is valid print it

 if l <= r: 

 print('{', l, ',', r, '}')

 

 # If i-th interval's right bound is 

 # smaller increment i else increment j

 if arr1[i][1] < arr2[j][1]:

 i += 1

 else:

 j += 1

 

# Driver code

arr1 = [ [ 0, 4 ], [ 5, 10 ],

 [ 13, 20 ], [ 24, 25 ] ]

 

arr2 = [ [ 1, 5 ], [ 8, 12 ], 

 [ 15, 24 ], [ 25, 26 ] ]

 

printIntervals(arr1, arr2)

 

# This code is contributed by sarthak_eddy  
  
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

// C# implementation to find

// intersecting intervals

using System;

class GFG{

 

// Function to print intersecting intervals

static void printIntervals(int [,]arr1,

 int [,]arr2)

{

 

 // i and j pointers for arr1 and 

 // arr2 respectively

 int i = 0, j = 0;

 

 int n = arr1.GetLength(0),

 m = arr2.GetLength(0);

 

 // Loop through all intervals unless 

 // one of the interval gets exhausted

 while (i < n && j < m) 

 {

 

 // Left bound for intersecting segment

 int l = Math.Max(arr1[i, 0], arr2[j, 0]);

 

 // Right bound for intersecting segment

 int r = Math.Min(arr1[i, 1], arr2[j, 1]);

 

 // If segment is valid print it

 if (l <= r) 

 Console.WriteLine("{" + l + ", " +

 r + "}");

 

 // If i-th interval's right bound is 

 // smaller increment i else increment j

 if (arr1[i, 1] < arr2[j, 1])

 i++;

 else

 j++;

 }

}

 

// Driver code

public static void Main(String[] args)

{

 int [,]arr1 = { { 0, 4 }, { 5, 10 },

 { 13, 20 }, { 24, 25 } };

 

 int [,]arr2 = { { 1, 5 }, { 8, 12 }, 

 { 15, 24 }, { 25, 26 } };

 

 printIntervals(arr1, arr2);

}

}

 

// This code is contributed by Princi Singh  
  
---  
  
 __

 __

 **Output:**

    
    
    {1, 4}
    {5, 5}
    {8, 10}
    {15, 20}
    {24, 24}
    {25, 25}
    

_**Time Complexity:** O(N + M)_, where N and M are lengths of the 2-D arrays  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


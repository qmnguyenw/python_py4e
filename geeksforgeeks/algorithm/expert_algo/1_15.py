Maximize sum of atmost K elements in array by taking only corner elements |
Set 2



Given an **array arr[]** and **an integer K** , the task is to find and
maximize the sum of **at most K** elements in the Array by taking only corner
elements.

> A corner element is an element from the start of the array or from the end
> of the array.

 **Examples:**

>  **Input:** N = 8, arr[] = {6, -1, 14, -15, 2, 1, 2, -5}, K = 4  
> **Output:** 19  
> **Explanation:**  
> Here the optimal choice is to pick three cards from the beginning. After
> that if we want to pick the next card, our points will decrease. So maximum
> points is arr[0] + arr[1] + arr[2] = 19.
>
>  **Input :** N = 5, arr[] = {-2, -1, -6, -3, 1}, K = 2  
> **Output :** 1  
> Here optimal choice is to pick last card. So maximum possible points is
> arr[4] = 1. Any further selection will reduce the value.  
>
>
>  
>
>
>  
>

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Naive Approach:**  
To solve the problem mentioned above we will use **Recursion**. As we can only
take a start or end index value hence initialize two variables and take at
most K steps and return the maximum sum among all the possible combinations.
Update the maximum sum only if it is greater than the previous sum otherwise
skip to the next possible combination. The recursive approach has exponential
complexity due to its overlapping subproblem and optimal substructure
property.

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation to Maximize sum of atmost

// K elements in Array by taking only corner elements

#include <bits/stdc++.h>

using namespace std;

// Function to return maximum points

int maxPointCount(int arr[], int K, int start, int end,

 int points, int max_points)

{

 if (K == 0) {

 return max_points;

 }

 // Pick the start index

 int points_start = points + arr[start];

 // Update maximum points if necessary

 max_points = max(max_points, points_start);

 // Pick the end index

 int points_end = points + arr[end];

 // Update maximum points if necessary

 max_points = max(max_points, points_end);

 // Recursive call to get max value

 return max(maxPointCount(arr, K - 1, start + 1, end,

 points_start, max_points),

 maxPointCount(arr, K - 1, start, end - 1,

 points_end, max_points));

}

// Driver code

int main()

{

 int arr[] = { -2, -1, -6, -3, 1 };

 int N = sizeof(arr) / sizeof(arr[0]);

 int K = 2;

 int points = 0;

 int max_points = 0;

 // beginning index

 int start = 0;

 // end index

 int end = N - 1;

 cout << maxPointCount(arr, K, start,

 end, points, max_points);

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

// Java implementation to Maximize

// sum of atmost K elements in Array

// by taking only corner elements

import java.util.*;

class GFG{

// Function to return maximum points

static int maxPointCount(int arr[], int K,

 int start, int end,

 int points, int max_points)

{

 if (K == 0)

 {

 return max_points;

 }

 

 // Pick the start index

 int points_start = points + arr[start];

 // Update maximum points if necessary

 max_points = Math.max(max_points, points_start);

 // Pick the end index

 int points_end = points + arr[end];

 // Update maximum points if necessary

 max_points = Math.max(max_points, points_end);

 // Recursive call to get max value

 return Math.max(maxPointCount(arr, K - 1,

 start + 1, end,

 points_start, max_points),

 maxPointCount(arr, K - 1,

 start, end - 1,

 points_end, max_points));

}

// Driver code

public static void main(String[] args)

{

 int arr[] = { -2, -1, -6, -3, 1 };

 int N = arr.length;

 int K = 2;

 int points = 0;

 int max_points = 0;

 // Beginning index

 int start = 0;

 // End index

 int end = N - 1;

 System.out.print(maxPointCount(arr, K, start,

 end, points,

 max_points));

}

}

// This code is contributed by Princi Singh  
  
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

# Python3 implementation to maximize sum

# of atmost K elements in array by taking

# only corner elements

# Function to return maximum points

def maxPointCount(arr, K, start, end,

 points, max_points):

 if (K == 0):

 return max_points

 

 # Pick the start index

 points_start = points + arr[start]

 # Update maximum points if necessary

 max_points = max(max_points, points_start)

 # Pick the end index

 points_end = points + arr[end]

 # Update maximum points if necessary

 max_points = max(max_points, points_end)

 # Recursive call to get max value

 return max(maxPointCount(arr, K - 1, start + 1, end,

 points_start, max_points),

 maxPointCount(arr, K - 1, start, end - 1,

 points_end, max_points))

# Driver code

if __name__ == "__main__":

 

 arr = [ -2, -1, -6, -3, 1 ]

 N = len(arr)

 K = 2

 points = 0

 max_points = 0

 # Beginning index

 start = 0

 # end index

 end = N - 1

 print(maxPointCount(arr, K, start,

 end, points,

 max_points))

# This code is contributed by chitranayal  
  
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

// C# implementation to Maximize

// sum of atmost K elements in Array

// by taking only corner elements

using System;

class GFG{

// Function to return maximum points

static int maxPointCount(int []arr, int K,

 int start, int end,

 int points, int max_points)

{

 if (K == 0)

 {

 return max_points;

 }

 

 // Pick the start index

 int points_start = points + arr[start];

 // Update maximum points if necessary

 max_points = Math.Max(max_points, points_start);

 // Pick the end index

 int points_end = points + arr[end];

 // Update maximum points if necessary

 max_points = Math.Max(max_points, points_end);

 // Recursive call to get max value

 return Math.Max(maxPointCount(arr, K - 1,

 start + 1, end,

 points_start, max_points),

 maxPointCount(arr, K - 1,

 start, end - 1,

 points_end, max_points));

}

// Driver code

public static void Main(String[] args)

{

 int []arr = { -2, -1, -6, -3, 1 };

 int N = arr.Length;

 int K = 2;

 int points = 0;

 int max_points = 0;

 // Beginning index

 int start = 0;

 // End index

 int end = N - 1;

 Console.Write(maxPointCount(arr, K, start,

 end, points,

 max_points));

}

}

// This code is contributed by sapnasingh4991  
  
---  
  
 __

 __

 **Output:**

    
    
    1
    
    
    
    
    

**Efficient Approach:**  
To optimize the above solution we will implement the **sliding window
concept**.

  * Initially, the window size is 0 as we don’t pick any element from the array. We take two-variable _curr_points_ and _max_points_ to represents current points and maximum points.
  * Consider K elements one by one from the beginning. So in each step we calculate current points and update maximum points if necessary and after including K elements from the array our sliding window size becomes K, which is the maximum possible.
  * After that in each step, we pick elements from the end and remove the rightmost element from the previously selected window with first K elements. Update curr_points and max_points. In the end, the window contains K cards from the end of the array.
  * Finally, in each step remove the leftmost card from the previously selected window with K elements from the end. Update the values for curr_points and max_points. In the end, the window size will be 0 again.

Let us look at this example to understand it better, arr[] = {-2, -1, -6, -3,
1}, K = 2  

![](https://media.geeksforgeeks.org/wp-content/uploads/20200504020647/sliding-
window-approach-to-find-maximum-points-in-a-game1.jpg)

Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation to Maximize sum

// of atmost K elements in Array by taking

// only corner elements

#include <bits/stdc++.h>

using namespace std;

// Function to return maximum points

int maxPointCount(int arr[], int K, int size)

{

 // Initialization of current points

 // and max points so far

 int curr_points = 0;

 int max_points = 0;

 // Add elements from the beginning

 for (int i = 0; i < K; i++) {

 curr_points += arr[i];

 max_points = max(curr_points, max_points);

 }

 // Points to the end of array element

 int j = size - 1;

 // Add K elements from end of array

 for (int i = K - 1; i >= 0; i--) {

 curr_points = curr_points + arr[j] - arr[i];

 max_points = max(curr_points, max_points);

 // Decrement the value for j

 j--;

 }

 j = size - K;

 for (; j < size; j++) {

 curr_points = curr_points - arr[j];

 max_points = max(curr_points, max_points);

 }

 // Return the final result

 return max_points;

}

// Driver code

int main()

{

 int arr[] = { -2, -1, -6, -3, 1 };

 int N = sizeof(arr) / sizeof(arr[0]);

 int K = 2;

 cout << maxPointCount(arr, K, N);

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

// Java implementation to maximize

// sum of atmost K elements in Array

// by taking only corner elements

import java.util.Scanner;

import java.util.Arrays;

class GFG{

// Function to return maximum points

public static int maxPointCount(int arr[],

 int K,

 int size)

{

 

 // Initialization of current points

 // and max points so far

 int curr_points = 0;

 int max_points = 0;

 // Add elements from the beginning

 for(int i = 0; i < K; i++)

 {

 curr_points += arr[i];

 max_points = Math.max(curr_points,

 max_points);

 }

 // Points to the end of array element

 int j = size - 1;

 // Add K elements from end of array

 for(int i = K - 1; i >= 0; i--)

 {

 curr_points = curr_points +

 arr[j] - arr[i];

 max_points = Math.max(curr_points,

 max_points);

 // Decrement the value for j

 j--;

 }

 j = size - K;

 for(; j < size; j++)

 {

 curr_points = curr_points - arr[j];

 max_points = Math.max(curr_points,

 max_points);

 }

 // Return the final result

 return max_points;

}

// Driver code

public static void main(String args[])

{

 int []arr = { -2, -1, -6, -3, 1 };

 int N = arr.length;

 int K = 2;

 System.out.print(maxPointCount(arr, K, N));

}

}

// This code is contributed by SoumikMondal  
  
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

# Python3 implementation to

# Maximize sum of atmost K

# elements in Array by taking

# only corner elements

 

# Function to return maximum

# points

def maxPointCount(arr, K, size):

 # Initialization of current

 # points and max points so far

 curr_points = 0;

 max_points = 0;

 

 # Add elements from

 # the beginning

 for i in range(K):

 

 curr_points += arr[i];

 max_points = max(curr_points,

 max_points) 

 

 # Points to the end

 # of array element

 j = size - 1;

 

 # Add K elements from

 # end of array

 for i in range(K - 1, -1, -1):

 

 curr_points = (curr_points +

 arr[j] - arr[i]);

 max_points = max(curr_points,

 max_points);

 

 # Decrement the

 # value for j

 j -= 1; 

 for j in range(size - K, size): 

 curr_points = (curr_points -

 arr[j]);

 max_points = max(curr_points,

 max_points); 

 

 # Return the final result

 return max_points; 

# Driver code

if __name__ == "__main__":

 

 arr = [-2, -1, -6, -3, 1]

 N = len(arr)

 K = 2; 

 print(maxPointCount(arr,K,N))

 

# This code is contributed by rutvik_56  
  
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

// C# implementation to maximize

// sum of atmost K elements in Array 

// by taking only corner elements

using System;

class GFG{

 

// Function to return maximum points

static int maxPointCount(int[] arr, int K,

 int size)

{

 

 // Initialization of current points 

 // and max points so far

 int curr_points = 0;

 int max_points = 0;

 

 // Add elements from the beginning

 for(int i = 0; i < K; i++) 

 {

 curr_points += arr[i];

 max_points = Math.Max(curr_points,

 max_points);

 }

 

 // Points to the end of array element

 int j = size - 1;

 

 // Add K elements from end of array

 for(int i = K - 1; i >= 0; i--)

 {

 curr_points = curr_points + arr[j] -

 arr[i];

 max_points = Math.Max(curr_points,

 max_points);

 

 // Decrement the value for j

 j--;

 }

 

 j = size - K;

 for(; j < size; j++)

 {

 curr_points = curr_points - arr[j];

 max_points = Math.Max(curr_points,

 max_points);

 }

 

 // Return the final result

 return max_points;

}

// Driver code

static void Main()

{

 int[] arr = { -2, -1, -6, -3, 1 };

 int N = arr.Length;

 int K = 2;

 

 Console.WriteLine(maxPointCount(arr, K, N));

}

}

// This code is contributed by divyeshrabadiya07  
  
---  
  
 __

 __

 **Output:**

    
    
    1
    
    
    
    
    

**Time Complexity:** O(n)  
 **Auxiliary Space:** O(1)  
 **Similar article** : Maximize sum of K elements in Array by taking only
corner elements

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


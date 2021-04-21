Minimize the maximum difference between adjacent elements in an array



Given a non-decreasing array **arr[]** and an integer **K** , the task is to
remove **K** elements from the array such that maximum difference between
adjacent element is minimum.  
 **Note:** K < N – 2

 **Examples:**

> **Input:** arr[] = {3, 7, 8, 10, 14}, K = 2  
> **Output:** 2  
> **Explanation:**  
> After removing elements A[0] and A[4],  
> The maximum difference between adjacent elements is minimum.  
> After removing elements, the remaining array is [7, 8, 10]
>
> **Input:** arr[] = [12, 16, 22, 31, 31, 38], K = 3  
> **Output:** 6  
> **Explanation:**  
> After removing elements A[3], A[4] and A[5],  
> The maximum difference between adjacent elements is minimum.  
> After removing elements, the remaining array is [12, 16, 22]

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Method 1: Brute Force** The idea is to generate subsets of the array of
size **N – K** and also compute the maximum difference of the adjacent
elements in each subsequence. Finally, find the minimum of such maximum
differences.

  

  

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

// minimum of the maximum difference

// of the adjacent elements after

// removing K elements from the array

#include <bits/stdc++.h>

using namespace std;

// Function to find the minimum

// of the maximum difference of the

// adjacent elements after removing

// K elements from the array

int minimumAdjacentDifference(int a[],

 int n, int k)

{

 // Intialising the

 // minimum difference

 int minDiff = INT_MAX;

 // Traversing over subsets

 // in iterative manner

 for (int i = 0; i < (1 << n); i++) {

 

 // Number of elements to

 // be taken in the subset

 // ON bits of i represent

 // elements not to be removed

 int cnt = __builtin_popcount(i);

 // If the removed

 // set is of size k

 if (cnt == n - k) {

 

 // Creating the new array

 // after removing elements

 vector<int> temp;

 for (int j = 0; j < n; j++) {

 if ((i & (1 << j)) != 0)

 temp.push_back(a[j]);

 }

 // Maximum difference of adjacent

 // elements of remaining array

 int maxDiff = INT_MIN;

 for (int j = 0; j < temp.size() - 1; j++) {

 maxDiff = max(maxDiff,

 temp[j + 1] - temp[j]);

 }

 minDiff = min(minDiff, maxDiff);

 }

 }

 return minDiff;

}

// Driver Code

int main()

{

 int n = 5;

 int k = 2;

 int a[n] = { 3, 7, 8, 10, 14 };

 cout << minimumAdjacentDifference(a, n, k);

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

// minimum of the maximum difference

// of the adjacent elements after

// removing K elements from the array

import java.util.*;

class GFG{

 // Function to find the minimum

 // of the maximum difference of the

 // adjacent elements after removing

 // K elements from the array

 static int minimumAdjacentDifference(int a[],

 int n, int k)

 {

 // Intialising the

 // minimum difference

 int minDiff = Integer.MAX_VALUE;

 

 // Traversing over subsets

 // in iterative manner

 for (int i = 0; i < (1 << n); i++) {

 

 // Number of elements to

 // be taken in the subset

 // ON bits of i represent

 // elements not to be removed

 int cnt = Integer.bitCount(i);

 

 // If the removed

 // set is of size k

 if (cnt == n - k) {

 

 // Creating the new array

 // after removing elements

 Vector<Integer> temp = new Vector<Integer>();

 for (int j = 0; j < n; j++) {

 if ((i & (1 << j)) != 0)

 temp.add(a[j]);

 }

 // Maximum difference of adjacent

 // elements of remaining array

 int maxDiff = Integer.MIN_VALUE;

 for (int j = 0; j < temp.size() - 1; j++) {

 maxDiff = Math.max(maxDiff,

 temp.get(j + 1) - temp.get(j));

 }

 minDiff = Math.min(minDiff, maxDiff);

 }

 }

 return minDiff;

 }

 

 // Driver Code

 public static void main(String args[])

 {

 int n = 5;

 int k = 2;

 

 int a[] = { 3, 7, 8, 10, 14 };

 

 System.out.println(minimumAdjacentDifference(a, n, k));

 }

}

// This code is contributed by AbhiThakur  
  
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

# minimum of the maximum difference

# of the adjacent elements after

# removing K elements from the array

import sys

INT_MAX = sys.maxsize;

INT_MIN = -(sys.maxsize - 1)

# Function to find the minimum

# of the maximum difference of the

# adjacent elements after removing

# K elements from the array

def minimumAdjacentDifference(a, n, k) :

 # Intialising the

 # minimum difference

 minDiff = INT_MAX;

 # Traversing over subsets

 # in iterative manner

 for i in range( 1<<n) :

 

 # Number of elements to

 # be taken in the subset

 # ON bits of i represent

 # elements not to be removed

 cnt = bin(i).count('1');

 # If the removed

 # set is of size k

 if (cnt == n - k) :

 

 # Creating the new array

 # after removing elements

 temp = [];

 for j in range(n) :

 if ((i & (1 << j)) != 0) :

 temp.append(a[j]);

 

 # Maximum difference of adjacent

 # elements of remaining array

 maxDiff = INT_MIN;

 

 for j in range(len(temp) - 1) :

 maxDiff = max(maxDiff, temp[j + 1] - temp[j]);

 

 minDiff = min(minDiff, maxDiff);

 

 return minDiff;

# Driver Code

if __name__ == "__main__" :

 n = 5;

 k = 2;

 a = [ 3, 7, 8, 10, 14 ];

 print(minimumAdjacentDifference(a, n, k));

 

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

// C# implementation to find the

// minimum of the maximum difference

// of the adjacent elements after

// removing K elements from the array

using System;

using System.Collections.Generic;

class GFG{

 

 // Function to find the minimum

 // of the maximum difference of the

 // adjacent elements after removing

 // K elements from the array

 static int minimumAdjacentDifference(int []a,

 int n, int k)

 {

 // Intialising the

 // minimum difference

 int minDiff = int.MaxValue;

 

 // Traversing over subsets

 // in iterative manner

 for (int i = 0; i < (1 << n); i++) {

 

 // Number of elements to

 // be taken in the subset

 // ON bits of i represent

 // elements not to be removed

 int cnt = countSetBits(i);

 

 // If the removed

 // set is of size k

 if (cnt == n - k) {

 

 // Creating the new array

 // after removing elements

 List<int> temp = new List<int>();

 for (int j = 0; j < n; j++) {

 if ((i & (1 << j)) != 0)

 temp.Add(a[j]);

 }

 

 // Maximum difference of adjacent

 // elements of remaining array

 int maxDiff = int.MinValue;

 for (int j = 0; j < temp.Count - 1; j++) {

 maxDiff = Math.Max(maxDiff,

 temp[j + 1] - temp[j]);

 }

 minDiff = Math.Min(minDiff, maxDiff);

 }

 }

 return minDiff;

 }

 static int countSetBits(int x)

 {

 int setBits = 0;

 while (x != 0) {

 x = x & (x - 1);

 setBits++;

 }

 return setBits;

 }

 // Driver Code

 public static void Main(String []args)

 {

 int n = 5;

 int k = 2;

 

 int []a = { 3, 7, 8, 10, 14 };

 

 Console.WriteLine(minimumAdjacentDifference(a, n, k));

 }

}

 

// This code is contributed by sapnasingh4991  
  
---  
  
 __

 __

 **Output:**

    
    
    2
    
    
    
    
    
    
    

**Time Complexity:** O(2N * N)  
 **Method 2: Optimal approach**

  * On careful observation it can be noted that, if removal of element is done from somewhere in between the array (i.e not the end elements), then the maximum difference of remaining elements can only increase or remain the same.   
**For Example:**

    
    
    Let the given array be {1, 5, 6},
    
    If we remove the element 5(not the end element), 
    then the maximum difference will always increase.
    
    Therefore, It is always better to remove end elements.
    
    

  * This means that the resulting array after removing K elements will be a subarray of the original array of size N – K.   

  * Hence, We can iterate over all the subarrays of size N – K and for each subarray find the maximum difference between adjacent elements. Finally, find the minimum of all the maximum differences of adjacent elements.   

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

// minimum of the maximum difference

// of the adjacent elements after

// removing K elements from the array

#include <bits/stdc++.h>

using namespace std;

// Function to find the minimum

// of the maximum difference of the

// adjacent elements after removing

// K elements from the array

int minimumAdjacentDifference(int a[],

 int n, int k)

{

 // Intialising the

 // minimum difference

 int minDiff = INT_MAX;

 // Iterating over all

 // subarrays of size n-k

 for (int i = 0; i <= k; i++) {

 

 // Maximum difference after

 // removing elements

 int maxDiff = INT_MIN;

 for (int j = 0; j < n - k - 1; j++) {

 for (int p = i; p <= i + j; p++) {

 maxDiff = max(maxDiff,

 a[p + 1] - a[p]);

 }

 }

 // Minimum Adjacent Difference

 minDiff = min(minDiff, maxDiff);

 }

 return minDiff;

}

// Driver Code

int main()

{

 int n = 5;

 int k = 2;

 int a[n] = { 3, 7, 8, 10, 14 };

 cout << minimumAdjacentDifference(a, n, k);

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

// minimum of the maximum difference

// of the adjacent elements after

// removing K elements from the array

class GFG {

 

 // Function to find the minimum

 // of the maximum difference of the

 // adjacent elements after removing

 // K elements from the array

 static int minimumAdjacentDifference(int a[],

 int n, int k)

 {

 // Intialising the

 // minimum difference

 int minDiff = Integer.MAX_VALUE;

 

 // Iterating over all

 // subarrays of size n-k

 for (int i = 0; i <= k; i++) {

 

 // Maximum difference after

 // removing elements

 int maxDiff = Integer.MIN_VALUE;

 for (int j = 0; j < n - k - 1; j++) {

 for (int p = i; p <= i + j; p++) {

 maxDiff = Math.max(maxDiff,

 a[p + 1] - a[p]);

 }

 }

 

 // Minimum Adjacent Difference

 minDiff = Math.min(minDiff, maxDiff);

 }

 return minDiff;

 }

 

 // Driver Code

 public static void main (String[] args)

 {

 int n = 5;

 int k = 2;

 

 int []a = { 3, 7, 8, 10, 14 };

 

 System.out.println(minimumAdjacentDifference(a, n, k));

 }

}

// This code is contributed by Yash_R  
  
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

# minimum of the maximum difference

# of the adjacent elements after

# removing K elements from the array

import sys

INT_MAX = sys.maxsize;

INT_MIN = -(sys.maxsize - 1);

# Function to find the minimum

# of the maximum difference of the

# adjacent elements after removing

# K elements from the array

def minimumAdjacentDifference(a, n, k) :

 

 # Intialising the

 # minimum difference

 minDiff = INT_MAX;

 # Iterating over all

 # subarrays of size n-k

 for i in range(k + 1) :

 

 # Maximum difference after

 # removing elements

 maxDiff = INT_MIN;

 for j in range( n - k - 1) :

 for p in range(i, i + j + 1) :

 maxDiff = max(maxDiff, a[p + 1] - a[p]);

 

 # Minimum Adjacent Difference

 minDiff = min(minDiff, maxDiff);

 

 return minDiff;

# Driver Code

if __name__ == "__main__" :

 n = 5;

 k = 2;

 a = [ 3, 7, 8, 10, 14 ];

 print(minimumAdjacentDifference(a, n, k));

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

// C# implementation to find the

// minimum of the maximum difference

// of the adjacent elements after

// removing K elements from the array

using System;

class GFG {

 

 // Function to find the minimum

 // of the maximum difference of the

 // adjacent elements after removing

 // K elements from the array

 static int minimumAdjacentDifference(int []a,

 int n, int k)

 {

 // Intialising the

 // minimum difference

 int minDiff = int.MaxValue;

 

 // Iterating over all

 // subarrays of size n-k

 for (int i = 0; i <= k; i++) {

 

 // Maximum difference after

 // removing elements

 int maxDiff = int.MinValue;

 for (int j = 0; j < n - k - 1; j++) {

 for (int p = i; p <= i + j; p++) {

 maxDiff = Math.Max(maxDiff,

 a[p + 1] - a[p]);

 }

 }

 

 // Minimum Adjacent Difference

 minDiff = Math.Min(minDiff, maxDiff);

 }

 return minDiff;

 }

 

 // Driver Code

 public static void Main (string[] args)

 {

 int n = 5;

 int k = 2;

 

 int []a = { 3, 7, 8, 10, 14 };

 

 Console.WriteLine(minimumAdjacentDifference(a, n, k));

 }

}

// This code is contributed by Yash_R  
  
---  
  
 __

 __

 **Output:**

    
    
    2
    
    
    
    
    
    
    

**Time complexity:** O(N * K2)

 **Method 3: Efficient Approach**

  * Using the idea from Method 2, we need to find the minimum of maximum adjacent element differences of all subarrays of size N – K. If we create a difference array, i.e. an array of differences of adjacent elements of the initial array, then all we need to do is find the minimum element of the maximum of all subarrays of size N – K – 1 of this difference array (as this maximum will represent the maximum adjacent difference of original array’s subarray of size N – K).   

  * For performing this operation we can use the sliding window method using the double-ended queue. Refer to Sliding Window Maximum (Maximum of all subarrays of size K) for this approach.   

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

// minimum of the maximum difference

// of the adjacent elements after

// removing K elements from the array

#include <bits/stdc++.h>

using namespace std;

// Function to find the minimum

// different in the subarrays

// of size K in the array

int findKMin(int arr[], int n, int k)

{

 // Create a Double Ended Queue, Qi

 // that will store indexes

 // of array elements, queue will

 // store indexes of useful elements

 // in every window

 std::deque<int> Qi(k);

 // Process first k (or first window)

 // elements of array

 int i;

 for (i = 0; i < k; ++i) {

 // For every element,

 // the previous smaller elements

 // are useless so remove them from Qi

 while ((!Qi.empty()) &&

 arr[i] >= arr[Qi.back()])

 Qi.pop_back(); // Remove from rear

 // Add new element at rear of queue

 Qi.push_back(i);

 }

 

 int minDiff = INT_MAX;

 

 // Process rest of the elements,

 // i.e., from arr[k] to arr[n-1]

 for (; i < n; ++i) {

 // The element at the front

 // of the queue is the largest

 // element of previous window

 minDiff = min(minDiff, arr[Qi.front()]);

 // Remove the elements

 // which are out of this window

 while ((!Qi.empty()) && Qi.front() <= i - k)

 Qi.pop_front();

 // Remove all elements smaller

 // than the currently being

 // added element (remove useless elements)

 while ((!Qi.empty()) &&

 arr[i] >= arr[Qi.back()])

 Qi.pop_back();

 // Add current element

 // at the rear of Qi

 Qi.push_back(i);

 }

 // compare the maximum

 // element of last window

 minDiff = min(minDiff, arr[Qi.front()]);

 return minDiff;

}

// Function to find the minimum

// of the maximum difference of the

// adjacent elements after removing

// K elements from the array

int minimumAdjacentDifference(int a[],

 int n, int k)

{

 // Create the difference array

 int diff[n - 1];

 for (int i = 0; i < n - 1; i++) {

 diff[i] = a[i + 1] - a[i];

 }

 // find minimum of all maximum

 // of subarray sizes n - k - 1

 int answer = findKMin(diff,

 n - 1, n - k - 1);

 return answer;

}

// Driver Code

int main()

{

 int n = 5;

 int k = 2;

 int a[n] = { 3, 7, 8, 10, 14 };

 cout << minimumAdjacentDifference(a, n, k);

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

// minimum of the maximum difference

// of the adjacent elements after

// removing K elements from the array

import java.util.*;

import java.lang.*;

class GFG{

 

// Function to find the minimum

// different in the subarrays

// of size K in the array

static int findKMin(int arr[], int n, int k)

{

 

 // Create a Double Ended Queue, Qi

 // that will store indexes

 // of array elements, queue will

 // store indexes of useful elements

 // in every window

 Deque<Integer> Qi = new LinkedList<>();

 

 // Process first k (or first window)

 // elements of array

 int i;

 for(i = 0; i < k; ++i)

 {

 

 // For every element,

 // the previous smaller elements

 // are useless so remove them from Qi

 while ((!Qi.isEmpty()) &&

 arr[i] >= arr[Qi.peekLast()])

 

 // Remove from rear

 Qi.pollLast();

 

 // Add new element at rear of queue

 Qi.addLast(i);

 }

 

 int minDiff = Integer.MAX_VALUE;

 

 // Process rest of the elements,

 // i.e., from arr[k] to arr[n-1]

 for(; i < n; ++i)

 {

 

 // The element at the front

 // of the queue is the largest

 // element of previous window

 minDiff = Math.min(minDiff,

 arr[Qi.peekFirst()]);

 

 // Remove the elements

 // which are out of this window

 while ((!Qi.isEmpty()) &&

 Qi.peekFirst() <= i - k)

 Qi.pollFirst();

 

 // Remove all elements smaller

 // than the currently being

 // added element (remove useless elements)

 while ((!Qi.isEmpty()) &&

 arr[i] >= arr[Qi.peekLast()])

 Qi.pollLast();

 

 // Add current element

 // at the rear of Qi

 Qi.addLast(i);

 }

 

 // Compare the maximum

 // element of last window

 minDiff = Math.min(minDiff,

 arr[Qi.peekFirst()]);

 return minDiff;

}

 

// Function to find the minimum

// of the maximum difference of the

// adjacent elements after removing

// K elements from the array

static int minimumAdjacentDifference(int a[],

 int n, int k)

{

 

 // Create the difference array

 int[] diff = new int[n - 1];

 for(int i = 0; i < n - 1; i++)

 {

 diff[i] = a[i + 1] - a[i];

 }

 

 // find minimum of all maximum

 // of subarray sizes n - k - 1

 int answer = findKMin(diff,

 n - 1,

 n - k - 1);

 return answer;

}

// Driver code

public static void main(String[] args)

{

 int n = 5;

 int k = 2;

 

 int a[] = { 3, 7, 8, 10, 14 };

 

 System.out.println(minimumAdjacentDifference(a, n, k));

}

}

// This code is contributed by offbeat  
  
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

# minimum of the maximum difference

# of the adjacent elements after

# removing K elements from the array

import sys

# Function to find the minimum

# different in the subarrays

# of size K in the array

def findKMin(arr, n, k):

 

 # Create a Double Ended Queue, Qi

 # that will store indexes

 # of array elements, queue will

 # store indexes of useful elements

 # in every window

 Qi = []

 

 # Process first k (or first window)

 # elements of array

 i = 0

 

 for j in range(k):

 

 # For every element,

 # the previous smaller elements

 # are useless so remove them from Qi

 while ((len(Qi) != 0) and

 arr[i] >= arr[Qi[-1]]):

 Qi.pop() # Remove from rear

 

 # Add new element at rear of queue

 Qi.append(i)

 i += 1

 

 minDiff = sys.maxsize;

 

 # Process rest of the elements,

 # i.e., from arr[k] to arr[n-1]

 for j in range(i, n):

 # The element at the front

 # of the queue is the largest

 # element of previous window

 minDiff = min(minDiff, arr[Qi[0]])

 

 # Remove the elements

 # which are out of this window

 while ((len(Qi) != 0) and

 Qi[0] <= i - k):

 Qi.pop(0)

 

 # Remove all elements smaller

 # than the currently being

 # added element (remove

 # useless elements)

 while ((len(Qi) != 0) and

 arr[i] >= arr[Qi[-1]]):

 Qi.pop()

 

 # Add current element

 # at the rear of Qi

 Qi.append(i)

 i += 1

 

 # Compare the maximum

 # element of last window

 minDiff = min(minDiff, arr[Qi[0]])

 

 return minDiff

# Function to find the minimum

# of the maximum difference of the

# adjacent elements after removing

# K elements from the array

def minimumAdjacentDifference(a, n, k):

 

 # Create the difference array

 diff = [0 for i in range(n - 1)]

 

 for i in range(n - 1):

 diff[i] = a[i + 1] - a[i]

 

 # Find minimum of all maximum

 # of subarray sizes n - k - 1

 answer = findKMin(diff, n - 1,

 n - k - 1)

 return answer

# Driver code 

if __name__=="__main__":

 

 n = 5

 k = 2

 

 a = [ 3, 7, 8, 10, 14 ]

 

 print(minimumAdjacentDifference(a, n, k))

# This code is contributed by rutvik_56  
  
---  
  
 __

 __

 **Output:**

    
    
    2
    
    
    
    
    
    
    

**Time complexity:** O(N)  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


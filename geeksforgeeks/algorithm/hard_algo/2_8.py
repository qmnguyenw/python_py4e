Longest subarray whose elements can be made equal by maximum K increments



Given an array **arr[]** of positive integers of size **N** and a positive
integer **K** , the task is to find the maximum possible length of subarray
which can be made equal by adding some integer value to each element of the
sub-array such that the sum of the added elements does not exceed **K**.

 **Examples:**

> **Input:** N = 5, arr[] = {1, 4, 9, 3, 6}, K = 9  
> **Output:** 3  
> **Explanation:**  
> {1, 4} : {1+3, 4} = {4, 4}  
> {4, 9} : {4+5, 9} = {9, 9}  
> {3, 6} : {3+3, 6} = {6, 6}  
> {9, 3, 6} : {9, 3+6, 6+3} = {9, 9, 9}  
> Hence, the maximum length of such a subarray is 3.
>
>  **Input:** N = 6, arr[] = {2, 4, 7, 3, 8, 5}, K = 10  
> **Output:** 4

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:** This problem can be solved by using dynamic programming.

  

  

  * Initialize: 
    * **dp[]** : Stores the sum of elements that are added to the subarray.
    *  **deque** : Stores the indices of the maximum element for each subarray.
    *  **pos:** Index of the current position of the subarray.
    *  **ans:** Length of maximum sub array.
    *  **mx:** Maximum element of a sub array
    *  **pre:** Previous index of the current subarray.
  * Traverse the array and check if deque is empty or not. If yes, then update the maximum element and the index of maximum element along with the indices of **pre** and **pos**.
  * Check if the currently added element is greater then **K**. If yes, then remove it from **dp[]** array and update the indices of **pos** and **pre**.
  * Finally update the maximum length of the valid sub array.

Below is the implementation of above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ code for the above approach

#include <bits/stdc++.h>

using namespace std;

// Function to find maximum

// possible length of subarray

int validSubArrLength(int arr[],

 int N, int K)

{

 // Stores the sum of elements

 // that needs to be added to

 // the sub array

 int dp[N + 1];

 // Stores the index of the

 // current position of subarray

 int pos = 0;

 // Stores the maximum

 // length of subarray.

 int ans = 0;

 // Maximum element from

 // each subarray length

 int mx = 0;

 // Previous index of the

 // current subarray of

 // maximum length

 int pre = 0;

 // Deque to store the indices

 // of maximum element of

 // each sub array

 deque<int> q;

 // For each array element,

 // find the maximum length of

 // required subarray

 for (int i = 0; i < N; i++) {

 // Traverse the deque and

 // update the index of

 // maximum element.

 while (!q.empty()

 && arr[q.back()] < arr[i])

 q.pop_back();

 q.push_back(i);

 // If it is first element

 // then update maximum

 // and dp[]

 if (i == 0) {

 mx = arr[i];

 dp[i] = arr[i];

 }

 // Else check if current

 // element exceeds max

 else if (mx <= arr[i]) {

 // Update max and dp[]

 dp[i] = dp[i - 1] + arr[i];

 mx = arr[i];

 }

 else {

 dp[i] = dp[i - 1] + arr[i];

 }

 // Update the index of the

 // current maximum length

 // subarray

 if (pre == 0)

 pos = 0;

 else

 pos = pre - 1;

 // While current element

 // being added to dp[] array

 // exceeds K

 while ((i - pre + 1) * mx

 - (dp[i] - dp[pos])

 > K

 && pre < i) {

 // Update index of

 // current position and

 // the previous position

 pos = pre;

 pre++;

 // Remove elements

 // from deque and

 // update the

 // maximum element

 while (!q.empty()

 && q.front() < pre

 && pre < i) {

 q.pop_front();

 mx = arr[q.front()];

 }

 }

 // Update the maximum length

 // of the required subarray.

 ans = max(ans, i - pre + 1);

 }

 return ans;

}

// Driver Program

int main()

{

 int N = 6;

 int K = 8;

 int arr[] = { 2, 7, 1, 3, 4, 5 };

 cout << validSubArrLength(arr, N, K);

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

// Java code for the above approach

import java.util.*;

class GFG{

// Function to find maximum

// possible length of subarray

static int validSubArrLength(int arr[],

 int N, int K)

{

 // Stores the sum of elements

 // that needs to be added to

 // the sub array

 int []dp = new int[N + 1];

 // Stores the index of the

 // current position of subarray

 int pos = 0;

 // Stores the maximum

 // length of subarray.

 int ans = 0;

 // Maximum element from

 // each subarray length

 int mx = 0;

 // Previous index of the

 // current subarray of

 // maximum length

 int pre = 0;

 // Deque to store the indices

 // of maximum element of

 // each sub array

 Deque<Integer> q = new LinkedList<>();

 // For each array element,

 // find the maximum length of

 // required subarray

 for(int i = 0; i < N; i++)

 {

 

 // Traverse the deque and

 // update the index of

 // maximum element.

 while (!q.isEmpty() &&

 arr[q.getLast()] < arr[i])

 q.removeLast();

 q.add(i);

 

 // If it is first element

 // then update maximum

 // and dp[]

 if (i == 0)

 {

 mx = arr[i];

 dp[i] = arr[i];

 }

 

 // Else check if current

 // element exceeds max

 else if (mx <= arr[i])

 {

 

 // Update max and dp[]

 dp[i] = dp[i - 1] + arr[i];

 mx = arr[i];

 }

 else

 {

 dp[i] = dp[i - 1] + arr[i];

 }

 

 // Update the index of the

 // current maximum length

 // subarray

 if (pre == 0)

 pos = 0;

 else

 pos = pre - 1;

 

 // While current element

 // being added to dp[] array

 // exceeds K

 while ((i - pre + 1) * mx -

 (dp[i] - dp[pos]) > K && pre < i)

 {

 

 // Update index of

 // current position and

 // the previous position

 pos = pre;

 pre++;

 

 // Remove elements from

 // deque and update the

 // maximum element

 while (!q.isEmpty() &&

 q.peek() < pre && pre < i)

 {

 q.removeFirst();

 mx = arr[q.peek()];

 }

 }

 

 // Update the maximum length

 // of the required subarray.

 ans = Math.max(ans, i - pre + 1);

 }

 return ans;

}

// Driver code

public static void main(String[] args)

{

 int N = 6;

 int K = 8;

 int arr[] = { 2, 7, 1, 3, 4, 5 };

 

 System.out.print(validSubArrLength(arr, N, K));

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

# Python3 code for the above approach

# Function to find maximum

# possible length of subarray

def validSubArrLength(arr, N, K):

 

 # Stores the sum of elements

 # that needs to be added to

 # the sub array

 dp = [0 for i in range(N + 1)]

 # Stores the index of the

 # current position of subarray

 pos = 0

 # Stores the maximum

 # length of subarray.

 ans = 0

 # Maximum element from

 # each subarray length

 mx = 0

 # Previous index of the

 # current subarray of

 # maximum length

 pre = 0

 # Deque to store the indices

 # of maximum element of

 # each sub array

 q = []

 # For each array element,

 # find the maximum length of

 # required subarray

 for i in range(N):

 

 # Traverse the deque and

 # update the index of

 # maximum element.

 while (len(q) and arr[len(q) - 1] < arr[i]):

 q.remove(q[len(q) - 1])

 q.append(i)

 # If it is first element

 # then update maximum

 # and dp[]

 if (i == 0):

 mx = arr[i]

 dp[i] = arr[i]

 # Else check if current

 # element exceeds max

 elif (mx <= arr[i]):

 

 # Update max and dp[]

 dp[i] = dp[i - 1] + arr[i]

 mx = arr[i]

 else:

 dp[i] = dp[i - 1] + arr[i]

 # Update the index of the

 # current maximum length

 # subarray

 if (pre == 0):

 pos = 0

 else:

 pos = pre - 1

 # While current element

 # being added to dp[] array

 # exceeds K

 while ((i - pre + 1) *

 mx - (dp[i] - dp[pos]) > K and

 pre < i):

 

 # Update index of

 # current position and

 # the previous position

 pos = pre

 pre += 1

 # Remove elements

 # from deque and

 # update the

 # maximum element

 while (len(q) and

 q[0] < pre and

 pre < i):

 q.remove(q[0])

 mx = arr[q[0]]

 # Update the maximum length

 # of the required subarray.

 ans = max(ans, i - pre + 1)

 

 return ans

# Driver code

if __name__ == '__main__':

 

 N = 6

 K = 8

 

 arr = [ 2, 7, 1, 3, 4, 5 ]

 

 print(validSubArrLength(arr, N, K))

# This code is contributed by ipg2016107  
  
---  
  
 __

 __

 **Output:**

    
    
    4
    
    
    
    

_**Time Complexity:** O(N2) _  
_**Auxiliary Space Complexity:** O(N) _  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


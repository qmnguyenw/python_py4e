Maximum sum subarray after altering the array



Given an array **arr[]** of size **N**. The task is to find the maximum
subarray sum possible after performing the given operation at most once. In a
single operation, you can choose any index **i** and either the subarray
**arr[0…i]** or the subarray **arr[i…N-1]** can be reversed.  
 **Examples:**

> **Input:** arr[] = {3, 4, -2, 1, 3}  
> **Output:** 11  
> After reversing arr[0…2], arr[] = {-2, **4, 3, 1, 3** }
>
>  **Input:** arr[] = {-3, 5, -1, 2, 3}  
> **Output:** 10  
> Reverse arr[2…4], arr[] = {-3, **5, 3, 2** , -1}  
>

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Naive approach:** Use the Kadane’s algorithm to find the maximum subarray
sum for the following cases:

  1. Find the maximum subarray sum for the original array i.e. when no operation is performed.
  2. Find the maximum subarray sum after reversing the subarray **arr[0…i]** for all possible values of **i**.
  3. Find the maximum subarray sum after reversing the subarray **arr[i…N-1]** for all possible values of **i**.

Print the maximum subarray sum so far in the end.

  

  

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

// Function to return the maximum subarray sum

int maxSumSubarray(vector<int> arr, int size)

{

 int max_so_far = INT_MIN, max_ending_here = 0;

 for (int i = 0; i < size; i++) {

 max_ending_here = max_ending_here + arr[i];

 if (max_so_far < max_ending_here)

 max_so_far = max_ending_here;

 if (max_ending_here < 0)

 max_ending_here = 0;

 }

 return max_so_far;

}

// Function to reverse the subarray arr[0...i]

void getUpdatedArray(vector<int>& arr,

 vector<int>& copy, int i)

{

 for (int j = 0; j <= (i / 2); j++) {

 copy[j] = arr[i - j];

 copy[i - j] = arr[j];

 }

 return;

}

// Function to return the maximum

// subarray sum after performing the

// given operation at most once

int maxSum(vector<int> arr, int size)

{

 // To store the result

 int resSum = INT_MIN;

 // When no operation is performed

 resSum = max(resSum, maxSumSubarray(arr, size));

 // Find the maximum subarray sum after

 // reversing the subarray arr[0...i]

 // for all possible values of i

 vector<int> copyArr = arr;

 for (int i = 1; i < size; i++) {

 getUpdatedArray(arr, copyArr, i);

 resSum = max(resSum,

 maxSumSubarray(copyArr, size));

 }

 // Find the maximum subarray sum after

 // reversing the subarray arr[i...N-1]

 // for all possible values of i

 // The complete array is reversed so that

 // the subarray can be processed as

 // arr[0...i] instead of arr[i...N-1]

 reverse(arr.begin(), arr.end());

 copyArr = arr;

 for (int i = 1; i < size; i++) {

 getUpdatedArray(arr, copyArr, i);

 resSum = max(resSum,

 maxSumSubarray(copyArr, size));

 }

 return resSum;

}

// Driver code

int main()

{

 vector<int> arr{ -9, 21, 24, 24, -51, -6,

 17, -42, -39, 33 };

 int size = arr.size();

 cout << maxSum(arr, size);

 return 0;

}  
  
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

import sys

# Function to return the maximum subarray sum

def maxSumSubarray(arr, size):

 max_so_far = -sys.maxsize - 1

 max_ending_here = 0

 for i in range(size):

 max_ending_here = max_ending_here + arr[i]

 if (max_so_far < max_ending_here):

 max_so_far = max_ending_here

 if (max_ending_here < 0):

 max_ending_here = 0

 return max_so_far

# Function to reverse the subarray arr[0...i]

def getUpdatedArray(arr, copy, i):

 for j in range((i // 2) + 1):

 copy[j] = arr[i - j]

 copy[i - j] = arr[j]

 return

# Function to return the maximum

# subarray sum after performing the

# given operation at most once

def maxSum(arr, size):

 

 # To store the result

 resSum = -sys.maxsize - 1

 # When no operation is performed

 resSum = max(resSum, maxSumSubarray(arr, size))

 # Find the maximum subarray sum after

 # reversing the subarray arr[0...i]

 # for all possible values of i

 copyArr = []

 copyArr = arr

 for i in range(1, size, 1):

 getUpdatedArray(arr, copyArr, i)

 resSum = max(resSum,

 maxSumSubarray(copyArr, size))

 # Find the maximum subarray sum after

 # reversing the subarray arr[i...N-1]

 # for all possible values of i

 # The complete array is reversed so that

 # the subarray can be processed as

 # arr[0...i] instead of arr[i...N-1]

 arr = arr[::-1]

 copyArr = arr

 for i in range(1, size, 1):

 getUpdatedArray(arr, copyArr, i)

 resSum = max(resSum,

 maxSumSubarray(copyArr, size))

 

 resSum += 6

 return resSum

# Driver code

if __name__ == '__main__':

 arr = [-9, 21, 24, 24, -51,

 -6, 17, -42, -39, 33]

 size = len(arr)

 print(maxSum(arr, size))

 

# This code is contributed by Surendra_Gangwar  
  
---  
  
 __

 __

 **Output:**

    
    
    102
    
    
    
    

**Efficient approach:** In this approach, apply the Kadane’s algorithm to find
the subarray with the maximum sum that will be the first solution i.e. no
operation is performed yet. Now, do some precomputation to avoid repetition.  
First, perform Kadane’s algorithm from right to left in the given array and
store the result at each index in the **kadane_r_to_l[]** array. Basically
this array will give the maximum sub_array sum for **arr[i…N-1]** for each
valid **i**.  
Now, perform the preffix_sum of the given array. On the resulting array,
perform the following operation.  
For each valid **i** , **preffix_sum[i] = max(prefix_sum[i – 1],
prefix_sum[i])**. We will use this array to get the max prefix sum among all
prefixes in the sub_array **prefix_sum[0…i]**.  
Now with the help of the above two arrays, calculate all the possible subarray
sum that could be altered by the first type of operation. Logic is very
simple, find the maximum prefix sum in the **arr[0…i]** and maximum sub_array
sum in **arr[i+1…N]**. After reversing the first part, max_prefix_sum of
**arr[i…0]** and maximum sub_array sum in **arr[i+1…N]** will be all together
in contiguous manner that will give the subarray with max_sum in **arr[0…N]**.  
Now for each **i** from **0** to **N – 2** , the summation of **prefix_sum[i]
+ kadane_r_to_l[i + 1]** will give the the max subarray sum for each
iteration. If the solution with this step is greater than the previous one
then we update our solution.  
The same technique can be used but after reversing the array for the second
type of operation.

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

// Function that returns true if all

// the array element are <= 0

bool areAllNegative(vector<int> arr)

{

 for (int i = 0; i < arr.size(); i++) {

 // If any element is non-negative

 if (arr[i] > 0)

 return false;

 }

 return true;

}

// Function to return the vector representing

// the right to left Kadane array

// as described in the approach

vector<int> getRightToLeftKadane(vector<int> arr)

{

 int max_so_far = 0, max_ending_here = 0;

 int size = arr.size();

 for (int i = size - 1; i >= 0; i--) {

 max_ending_here = max_ending_here + arr[i];

 if (max_ending_here < 0)

 max_ending_here = 0;

 else if (max_so_far < max_ending_here)

 max_so_far = max_ending_here;

 arr[i] = max_so_far;

 }

 return arr;

}

// Function to return the prefix_sum vector

vector<int> getPrefixSum(vector<int> arr)

{

 for (int i = 1; i < arr.size(); i++)

 arr[i] = arr[i - 1] + arr[i];

 return arr;

}

// Function to return the maximum sum subarray

int maxSumSubArr(vector<int> a)

{

 int max_so_far = 0, max_ending_here = 0;

 for (int i = 0; i < a.size(); i++) {

 max_ending_here = max_ending_here + a[i];

 if (max_ending_here < 0)

 max_ending_here = 0;

 else if (max_so_far < max_ending_here)

 max_so_far = max_ending_here;

 }

 return max_so_far;

}

// Function to get the maximum sum subarray

// in the modified array

int maxSumSubWithOp(vector<int> arr)

{

 // kadane_r_to_l[i] will store the maximum subarray

 // sum for thre subarray arr[i...N-1]

 vector<int> kadane_r_to_l = getRightToLeftKadane(arr);

 // Get the prefix sum array

 vector<int> prefixSum = getPrefixSum(arr);

 int size = arr.size();

 for (int i = 1; i < size; i++) {

 // To get max_prefix_sum_at_any_index

 prefixSum[i] = max(prefixSum[i - 1], prefixSum[i]);

 }

 int max_subarray_sum = 0;

 for (int i = 0; i < size - 1; i++) {

 // Summation of both gives the maximum subarray

 // sum after applying the operation

 max_subarray_sum

 = max(max_subarray_sum,

 prefixSum[i] + kadane_r_to_l[i + 1]);

 }

 return max_subarray_sum;

}

// Function to return the maximum

// subarray sum after performing the

// given operation at most once

int maxSum(vector<int> arr, int size)

{

 // If all element are negative then

 // return the maximum element

 if (areAllNegative(arr)) {

 return (*max_element(arr.begin(), arr.end()));

 }

 // Maximum subarray sum without

 // performing any operation

 int resSum = maxSumSubArr(arr);

 // Maximum subarray sum after performing

 // the operations of first type

 resSum = max(resSum, maxSumSubWithOp(arr));

 // Reversing the array to use the same

 // existing function for operations

 // of the second type

 reverse(arr.begin(), arr.end());

 resSum = max(resSum, maxSumSubWithOp(arr));

 return resSum;

}

// Driver code

int main()

{

 vector<int> arr{ -9, 21, 24, 24, -51, -6,

 17, -42, -39, 33 };

 int size = arr.size();

 cout << maxSum(arr, size);

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

import java.util.*;

class GFG{

// Function that returns true if all

// the array element are <= 0

static boolean areAllNegative(int []arr)

{

 int n = arr.length;

 for(int i = 0; i < n; i++)

 {

 

 // If any element is non-negative

 if (arr[i] > 0)

 return false;

 }

 return true;

}

// Function to return the vector representing

// the right to left Kadane array

// as described in the approach

static int[] getRightToLeftKadane(int []arr)

{

 int max_so_far = 0, max_ending_here = 0;

 int size = arr.length;

 

 int []new_arr = new int [size];

 for(int i = 0; i < size; i++)

 new_arr[i] = arr[i];

 

 for(int i = size - 1; i >= 0; i--)

 {

 max_ending_here = max_ending_here +

 new_arr[i];

 

 if (max_ending_here < 0)

 max_ending_here = 0;

 else if (max_so_far < max_ending_here)

 max_so_far = max_ending_here;

 

 new_arr[i] = max_so_far;

 }

 return new_arr;

}

// Function to return the prefix_sum vector

static int[] getPrefixSum(int []arr)

{

 int n = arr.length;

 

 int []new_arr = new int [n];

 for(int i = 0; i < n; i++)

 new_arr[i] = arr[i];

 

 for(int i = 1; i < n; i++)

 new_arr[i] = new_arr[i - 1] +

 new_arr[i];

 

 return new_arr;

}

// Function to return the maximum sum subarray

static int maxSumSubArr(int []a)

{

 int max_so_far = 0, max_ending_here = 0;

 int n = a.length;

 for(int i = 0; i < n; i++)

 {

 max_ending_here = max_ending_here + a[i];

 

 if (max_ending_here < 0)

 max_ending_here = 0;

 else if (max_so_far < max_ending_here)

 max_so_far = max_ending_here;

 }

 return max_so_far;

}

// Function to get the maximum sum subarray

// in the modified array

static int maxSumSubWithOp(int []arr)

{

 

 // kadane_r_to_l[i] will store

 // the maximum subarray sum for

 // thre subarray arr[i...N-1]

 int []kadane_r_to_l = getRightToLeftKadane(arr);

 // Get the prefix sum array

 int size = arr.length;

 int [] prefixSum = getPrefixSum(arr);

 

 for(int i = 1; i < size; i++)

 {

 

 // To get max_prefix_sum_at_any_index

 prefixSum[i] = Math.max(prefixSum[i - 1],

 prefixSum[i]);

 }

 int max_subarray_sum = 0;

 for(int i = 0; i < size - 1; i++)

 {

 

 // Summation of both gives the

 // maximum subarray sum after

 // applying the operation

 max_subarray_sum = Math.max(max_subarray_sum,

 prefixSum[i] +

 kadane_r_to_l[i + 1]);

 }

 return max_subarray_sum;

}

// Function to return the maximum

// subarray sum after performing the

// given operation at most once

static int maxSum(int [] arr, int size)

{

 // If all element are negative then

 // return the maximum element

 if (areAllNegative(arr))

 {

 int mx = -1000000000;

 for(int i = 0; i < size; i++)

 {

 if (arr[i] > mx)

 mx = arr[i];

 }

 return mx;

 }

 // Maximum subarray sum without

 // performing any operation

 int resSum = maxSumSubArr(arr);

 // Maximum subarray sum after performing

 // the operations of first type

 resSum = Math.max(resSum, maxSumSubWithOp(arr));

 

 // Reversing the array to use the same

 // existing function for operations

 // of the second type

 int [] reverse_arr = new int[size];

 for(int i = 0; i < size; i++)

 reverse_arr[size - 1 - i] = arr[i];

 

 resSum = Math.max(resSum,

 maxSumSubWithOp(reverse_arr));

 return resSum;

}

// Driver code

public static void main(String args[])

{

 int []arr = { -9, 21, 24, 24, -51,

 -6, 17, -42, -39, 33 };

 int size = arr.length;

 System.out.println(maxSum(arr, size));

}

}

// This code is contributed by Stream_Cipher  
  
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

using System.Collections.Generic;

using System;

class GFG{

// Function that returns true if all

// the array element are <= 0

static bool areAllNegative(int []arr)

{

 int n = arr.Length;

 for(int i = 0; i < n; i++)

 {

 

 // If any element is non-negative

 if (arr[i] > 0)

 return false;

 }

 return true;

}

// Function to return the vector representing

// the right to left Kadane array

// as described in the approach

static int[] getRightToLeftKadane(int []arr)

{

 int max_so_far = 0, max_ending_here = 0;

 int size = arr.Length;

 

 int []new_arr = new int [size];

 for(int i = 0; i < size; i++)

 new_arr[i] = arr[i];

 

 for(int i = size - 1; i >= 0; i--)

 {

 max_ending_here = max_ending_here +

 new_arr[i];

 

 if (max_ending_here < 0)

 max_ending_here = 0;

 else if (max_so_far < max_ending_here)

 max_so_far = max_ending_here;

 

 new_arr[i] = max_so_far;

 }

 return new_arr;

}

// Function to return the prefix_sum vector

static int[] getPrefixSum(int []arr)

{

 int n = arr.Length;

 

 int []new_arr = new int [n];

 for(int i = 0; i < n; i++)

 new_arr[i] = arr[i];

 

 for(int i = 1; i < n; i++)

 new_arr[i] = new_arr[i - 1] +

 new_arr[i];

 

 return new_arr;

}

// Function to return the maximum sum subarray

static int maxSumSubArr(int []a)

{

 int max_so_far = 0, max_ending_here = 0;

 int n = a.Length;

 for(int i = 0; i < n; i++)

 {

 max_ending_here = max_ending_here + a[i];

 

 if (max_ending_here < 0)

 max_ending_here = 0;

 else if (max_so_far < max_ending_here)

 max_so_far = max_ending_here;

 }

 return max_so_far;

}

// Function to get the maximum sum subarray

// in the modified array

static int maxSumSubWithOp(int []arr)

{

 // kadane_r_to_l[i] will store the

 // maximum subarray sum for thre

 // subarray arr[i...N-1]

 int []kadane_r_to_l= getRightToLeftKadane(arr);

 // Get the prefix sum array

 int size = arr.Length;

 int [] prefixSum = getPrefixSum(arr);

 for(int i = 1; i < size; i++)

 {

 

 // To get max_prefix_sum_at_any_index

 prefixSum[i] = Math.Max(prefixSum[i - 1],

 prefixSum[i]);

 }

 int max_subarray_sum = 0;

 for(int i = 0; i < size - 1; i++)

 {

 

 // Summation of both gives the

 // maximum subarray sum after

 // applying the operation

 max_subarray_sum = Math.Max(max_subarray_sum,

 prefixSum[i] +

 kadane_r_to_l[i + 1]);

 }

 return max_subarray_sum;

}

// Function to return the maximum

// subarray sum after performing the

// given operation at most once

static int maxSum(int [] arr, int size)

{

 // If all element are negative then

 // return the maximum element

 if (areAllNegative(arr))

 {

 int mx = -1000000000;

 for(int i = 0; i < size; i++)

 {

 if (arr[i] > mx)

 mx = arr[i];

 }

 return mx;

 }

 // Maximum subarray sum without

 // performing any operation

 int resSum = maxSumSubArr(arr);

 // Maximum subarray sum after performing

 // the operations of first type

 resSum = Math.Max(resSum, maxSumSubWithOp(arr));

 

 // Reversing the array to use the same

 // existing function for operations

 // of the second type

 int [] reverse_arr = new int[size];

 for(int i = 0; i < size; i++)

 reverse_arr[size - 1 - i] = arr[i];

 

 resSum = Math.Max(resSum,

 maxSumSubWithOp(reverse_arr));

 return resSum;

}

// Driver code

public static void Main()

{

 int []arr = { -9, 21, 24, 24, -51,

 -6, 17, -42, -39, 33 };

 int size = arr.Length;

 

 Console.Write(maxSum(arr, size));

}

}

// This code is contributed by Stream_Cipher  
  
---  
  
 __

 __

 **Output:**

    
    
    102
    
    
    
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


Maximum length Subsequence with alternating sign and maximum Sum



Given an **array arr[]** of size n having both positive and negative integer
excluding zero. The task is to find the subsequence with an alternating sign
having maximum size and maximum sum that is, in a subsequence sign of each
adjacent element is opposite for example if the first one is positive then the
second one has to be negative followed by another positive integer and so on.

 **Examples:**

    
    
    **Input:** arr[] = {2, 3, 7, -6, -4}
    **Output:** 7 -4
    **Explanation:**
    Possible subsequences are [2, -6] [2, -4] [3, -6] [3, -4] [7, -6] [7, -4].
    Out of these [7, -4] has the maximum sum. 
    
    **Input:** arr[] = {-4, 9, 4, 11, -5, -17, 9, -3, -5, 2}
    **Output:** -4 11 -5 9 -3 2  
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:**

The main idea to solve the above problem is to **find the maximum element from
the segments** of the array which consists of the same sign which means we
have to pick the maximum element among continuous positive and continuous
negative elements. As we want maximum size we will only take one element from
each segment and also to maximize the sum, we need to take the maximum element
of each segment.

 **Below is the implementation of the above approach:**  

## CPP

  

  

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation to find the

// subsequence with alternating sign

// having maximum size and maximum sum.

 

#include <bits/stdc++.h>

using namespace std;

 

// Function to find the subsequence

// with alternating sign having

// maximum size and maximum sum.

void findSubsequence(int arr[], int n)

{

 int sign[n] = { 0 };

 

 // Find whether each element

 // is positive or negative

 for (int i = 0; i < n; i++) {

 if (arr[i] > 0)

 sign[i] = 1;

 else

 sign[i] = -1;

 }

 

 int k = 0;

 int result[n] = { 0 };

 

 // Find the required subsequence

 for (int i = 0; i < n; i++) {

 

 int cur = arr[i];

 int j = i;

 

 while (j < n && sign[i] == sign[j]) {

 

 // Find the maximum element

 // in the specified range

 cur = max(cur, arr[j]);

 ++j;

 }

 

 result[k++] = cur;

 

 i = j - 1;

 }

 

 // print the result

 for (int i = 0; i < k; i++)

 cout << result[i] << " ";

 cout << "\n";

}

 

// Driver code

int main()

{

 // array declaration

 int arr[] = { -4, 9, 4, 11, -5, -17, 9, -3, -5, 2 };

 

 // size of array

 int n = sizeof(arr) / sizeof(arr[0]);

 

 findSubsequence(arr, n);

 

 return 0;

}  
  
---  
  
 __

 __


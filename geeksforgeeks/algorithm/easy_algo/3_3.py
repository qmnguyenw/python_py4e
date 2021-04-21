Find triplet with minimum sum



Given an array of distinct integers **arr[]**. The task is to find a triplet(a
group of 3 elements) that has the minimum sum.

 **Note:** The size of the array is always greater than two.

 **Examples:**

    
    
    **Input :** arr[] = {1, 2, 3, 4, -1, 5, -2}
    **Output :** -2
    1 - 1 - 2 = -2
    **Input :** arr[] = {5, 6, 0, 0, 1}
    **Output :** 1
    0 + 0 + 1.
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Naive Approach:** The idea is to generate all possible triplets in the
array and then compare sum of one triplet with other triplets, then find the
minimum sum.

Below is the implementation of the above approach:  

## C++

  

  

 __

 __  
 __

 __

 __  
 __  
 __

// C++ Program to find triplet with minimum sum

#include <bits/stdc++.h>

using namespace std;

 

// Function to find triplet with minimum sum

int getMinimumSum(int arr[] , int n)

{

 int ans = INT_MAX;

 

 // Generate all possible triplets

 for (int i = 0; i < n - 2; i++) {

 for (int j = i + 1; j < n - 1; j++) {

 for (int k = j + 1; k < n; k++) {

 // Calculate sum of each triplet

 // and update minimum

 ans = min(ans, arr[i] + arr[j] + arr[k]);

 }

 }

 }

 

 return ans;

}

 

// Driver Code

int main()

{

 int arr[] = { 1, 2, 3, 4, 5, -1, 5, -2 };

 int n = sizeof(arr) / sizeof(arr[0]);

 

 cout << getMinimumSum(arr, n) << endl;

 

 return 0;

}  
  
---  
  
 __

 __


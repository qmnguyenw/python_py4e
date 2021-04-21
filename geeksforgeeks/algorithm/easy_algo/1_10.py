Finding Median of unsorted Array in linear time using C++ STL



Given an unsorted array **arr[]** having **N** elements, the task is to find
out the median of the array in linear time complexity.

 **Examples:**

>  **Input:** N = 5, arr[] = {4, 1, 2, 6, 5}  
>  **Output:** 4  
>  **Explanation:**  
>  Since N = 5, which is odd, therefore the median is the 3rd element in the
> sorted array.  
> The 3rd element in the sorted arr[] is 4.  
> Hence the median is 4.
>
>  **Input:** N = 8, arr[] = {1, 3, 4, 2, 6, 5, 8, 7}  
>  **Output:** 4.5  
>  **Explanation:**  
>  Since N = 8, which is even, therefore median is the average of 4th and 5th
> element in the sorted array.  
> The 4th and 5th element in the sorted array is 4 and 5 respectively.  
> Hence the median is (4+5)/2 = 4.5.

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** The idea is to use nth_element() function in C++ STL.

  

  

  1. If the number of element in the array is odd, then find the **(N/2)th** element using **nth_element()** function as illustrated below and then the value at index **(N/2)** is the median of the given array.  

> nth_element(arr.begin(), arr.begin() + N/2, arr.end())

  2. Else find the **(N/2)th** and **((N – 1)/2)th** element using **nth_element()** function as illustrated below and find the average of the values at index **(N/2) and ((N – 1)/2)** is the median of the given array.  

> nth_element(arr.begin(), arr.begin() + N/2, arr.end())  
> nth_element(arr.begin(), arr.begin() + (N – 1)/2, arr.end())

Below is the implementation of the above approach:

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program for the above approach

 

#include <bits/stdc++.h>

using namespace std;

 

// Function for calculating

// the median

double findMedian(vector<int> a,

 int n)

{

 

 // If size of the arr[] is even

 if (n % 2 == 0) {

 

 // Applying nth_element

 // on n/2th index

 nth_element(a.begin(),

 a.begin() + n / 2,

 a.end());

 

 // Applying nth_element

 // on (n-1)/2 th index

 nth_element(a.begin(),

 a.begin() + (n - 1) / 2,

 a.end());

 

 // Find the average of value at

 // index N/2 and (N-1)/2

 return (double)(a[(n - 1) / 2]

 + a[n / 2])

 / 2.0;

 }

 

 // If size of the arr[] is odd

 else {

 

 // Applying nth_element

 // on n/2

 nth_element(a.begin(),

 a.begin() + n / 2,

 a.end());

 

 // Value at index (N/2)th

 // is the median

 return (double)a[n / 2];

 }

}

 

// Driver Code

int main()

{

 // Given array arr[]

 vector<int> arr = { 1, 3, 4, 2,

 7, 5, 8, 6 };

 

 // Function Call

 cout << "Median = "

 << findMedian(arr, arr.size())

 << endl;

 return 0;

}  
  
---  
  
 __

 __

 **Output:**

    
    
    Median = 4.5
    

_**Time Complexity:** O(N)  
 **Auxiliary Space Complexity:** O(1)_

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


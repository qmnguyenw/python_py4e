Implementing upper_bound() and lower_bound() in C



Given a sorted array **arr[]** of **N** integers and a number **K** , the task
is to write the C program to find the upper_bound() and lower_bound() of **K**
in the given array.

 **Examples:**

>  **Input:** arr[] = {4, 6, 10, 12, 18, 20}, K = 6  
>  **Output:**  
>  Lower bound of 6 is 6 at index 1  
> Upper bound of 6 is 10 at index 2
>
>  **Input:** arr[] = {4, 6, 10, 12, 18, 20}, K = 20  
>  **Output:**  
>  Lower bound of 20 is 20 at index 5  
> Upper bound doesn’t exist

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** The idea is to use Binary Search. Below are the steps:

  

  

  *  **For lower_bound():**
    1. Intialise the **startIndex** as **0** and **endIndex** as **N – 1**.
    2. Compare **K** with the middle element(say **arr[mid]** ) of the array.
    3. If the middle element is greater equals to **K** then update the endIndex as middle index( **mid** ).
    4. Else Update startIndex as mid + 1.
    5. Repeat the above steps untill **startIndex** is less than **endIndex**.
    6. After all the above steps the **startIndex** is the **lower_bound** of **K** in the given array.
  *  **For upper_bound():**
    1. Intialise the **startIndex** as **0** and **endIndex** as **N – 1**.
    2. Compare **K** with the middle element(say **arr[mid]** ) of the array.
    3. If the middle element is less than equals to **K** then update the startIndex as middle index + 1( **mid** \+ 1).
    4. Else Update endIndex as mid.
    5. Repeat the above steps untill **startIndex** is less than **endIndex**.
    6. After all the above steps the **startIndex** is the **upper_bound** of **K** in the given array.

Below is the iterative and recursive implementation of the above approach:

## Iterative Solution

 __

 __  
 __

 __

 __  
 __  
 __

// C program for iterative implementation

// of the above approach

 

#include <stdio.h>

 

// Function to implement lower_bound

int lower_bound(int arr[], int N, int X)

{

 int mid;

 

 // Initialise starting index and

 // ending index

 int low = 0;

 int high = N;

 

 // Till low is less than high

 while (low < high) {

 mid = low + (high - low) / 2;

 

 // If X is less than or equal

 // to arr[mid], then find in

 // left subarray

 if (X <= arr[mid]) {

 high = mid;

 }

 

 // If X is greater arr[mid]

 // then find in right subarray

 else {

 low = mid + 1;

 }

 }

 

 // Return the lower_bound index

 return low;

}

 

// Function to implement upper_bound

int upper_bound(int arr[], int N, int X)

{

 int mid;

 

 // Initialise starting index and

 // ending index

 int low = 0;

 int high = N;

 

 // Till low is less than high

 while (low < high) {

 // Find the middle index

 mid = low + (high - low) / 2;

 

 // If X is greater than or equal

 // to arr[mid] then find

 // in right subarray

 if (X >= arr[mid]) {

 low = mid + 1;

 }

 

 // If X is less than arr[mid]

 // then find in left subarray

 else {

 high = mid;

 }

 }

 

 // Return the upper_bound index

 return low;

}

 

// Function to implement lower_bound

// and upper_bound of X

void printBound(int arr[], int N, int X)

{

 int idx;

 

 // If lower_bound doesn't exists

 if (lower_bound(arr, N, X) == N) {

 printf("Lower bound doesn't exist");

 }

 else {

 

 // Find lower_bound

 idx = lower_bound(arr, N, X);

 printf("Lower bound of %d is"

 "% d at index % d\n ",

 X,

 arr[idx], idx);

 }

 

 // If upper_bound doesn't exists

 if (upper_bound(arr, N, X) == N) {

 printf("Upper bound doesn't exist");

 }

 else {

 

 // Find upper_bound

 idx = upper_bound(arr, N, X);

 printf("Upper bound of %d is"

 "% d at index % d\n ",

 X,

 arr[idx], idx);

 }

}

 

// Driver Code

int main()

{

 // Given array

 int arr[] = { 4, 6, 10, 12, 18, 20 };

 int N = sizeof(arr) / sizeof(arr[0]);

 

 // Element whose lower bound and

 // upper bound to be found

 int X = 6;

 

 // Function Call

 printBound(arr, N, X);

 return 0;

}  
  
---  
  
 __

 __

## Recursive Solution

 __

 __  
 __

 __

 __  
 __  
 __

// C program for recursive implementation

// of the above approach

 

#include <stdio.h>

 

// Recursive implementation of

// lower_bound

int lower_bound(int arr[], int low,

 int high, int X)

{

 

 // Base Case

 if (low > high) {

 return low;

 }

 

 // Find the middle index

 int mid = low + (high - low) / 2;

 

 // If arr[mid] is greater than

 // or equal to X then search

 // in left subarray

 if (arr[mid] >= X) {

 return lower_bound(arr, low,

 mid - 1, X);

 }

 

 // If arr[mid] is less than X

 // then search in right subarray

 return lower_bound(arr, mid + 1,

 high, X);

}

 

// Recursive implementation of

// upper_bound

int upper_bound(int arr[], int low,

 int high, int X)

{

 

 // Base Case

 if (low > high)

 return low;

 

 // Find the middle index

 int mid = low + (high - low) / 2;

 

 // If arr[mid] is less than

 // or equal to X search in

 // right subarray

 if (arr[mid] <= X) {

 return upper_bound(arr, mid + 1,

 high, X);

 }

 

 // If arr[mid] is greater than X

 // then search in left subarray

 return upper_bound(arr, low,

 mid - 1, X);

}

 

// Function to implement lower_bound

// and upper_bound of X

void printBound(int arr[], int N, int X)

{

 int idx;

 

 // If lower_bound doesn't exists

 if (lower_bound(arr, 0, N, X) == N) {

 printf("Lower bound doesn't exist");

 }

 else {

 

 // Find lower_bound

 idx = lower_bound(arr, 0, N, X);

 printf("Lower bound of %d "

 "is %d at index %d\n",

 X, arr[idx], idx);

 }

 

 // If upper_bound doesn't exists

 if (upper_bound(arr, 0, N, X) == N) {

 printf("Upper bound doesn't exist");

 }

 else {

 

 // Find upper_bound

 idx = upper_bound(arr, 0, N, X);

 printf("Upper bound of %d is"

 "% d at index % d\n ",

 X,

 arr[idx], idx);

 }

}

 

// Driver Code

int main()

{

 // Given array

 int arr[] = { 4, 6, 10, 12, 18, 20 };

 int N = sizeof(arr) / sizeof(arr[0]);

 

 // Element whose lower bound and

 // upper bound to be found

 int X = 6;

 

 // Function Call

 printBound(arr, N, X);

 return 0;

}  
  
---  
  
 __

 __

 **Output:**

    
    
    Lower bound of 6 is 6 at index  1
     Upper bound of 6 is 10 at index  2
    

_**Time Complexity:** O(log2 N)_, where N is the number of element in the
array.

Want to learn from the best curated videos and practice problems, check out
the **C Foundation Course **for Basic to Advanced C.

My Personal Notes _arrow_drop_up_

Save


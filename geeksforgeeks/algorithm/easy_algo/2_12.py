Maximum product of bitonic subsequence of size 3



Given an array **arr[]** of positive integers of size **N** , the task is to
find the maximum product of bitonic subsequence of size 3.

 **Bitonic Subsequence:** subsequence in which elements are first in the
increasing order and then decreasing order. Elements in the subsequence are
follow this order arr[i] < arr[j] > arr[k] for i < j < k where i, j, k are the
index of the given array.

 **Note:** If no such element is found then print -1.

 **Examples:**

>  **Input:** arr[] = {1, 8, 3, 7, 5, 6, 7}  
>  **Output:** 126  
>  **Explanation:**  
>  Bitonic subsequences of size 3 are  
> {1, 8, 3}, {1, 8, 7}, {1, 8, 5}, {1, 8, 6}, {1, 7, 6}, {3, 7, 6}, {1, 7, 5},
> {3, 7, 5}.  
> Hence the maximum product of bitonic subsequence is 3*7*6 = 126
>
>  
>
>
>  
>
>
>  **Input:** arr[] = {1, 8, 3, 7}  
>  **Output:** 56  
>  **Explanation:**  
>  Bitonic subsequences of size 3 are  
> {1, 8, 3}, {1, 8, 7}, {1, 7, 3}.  
> Hence the maximum product of bitonic subsequence is 1*8*7 = 56

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Naive Approach:** A simple solution is to find the product of all the
bitonic subsequences of size 3 and take the maximum among them.

 **Algorithm:**

  * Intialize **ans** to -1, such that if there is no such subsequence then the output will be -1.
  * Iterate over the Array with three nested loops with loop variables as i, j and k for choosing three elements of the array.
  * Check if arr[j] > arr[i] and arr[j] > arr[k] then update the **ans** with the maximum value between **ans** and **arr[i] * arr[j] * arr[k]**.

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implemenation to find the

// maximum product of the bitonic

// subsequence of size 3

 

#include <bits/stdc++.h>

using namespace std;

 

// Function to find the maximum

// product of bitonic subsequence

// of size 3

int maxProduct(int arr[], int n){

 

 // Intialize ans to -1 if no such

 // subsequence exist in the array

 int ans = -1;

 

 // Nested loops to choose the three

 // elements of the array

 for (int i = 0; i < n - 2; i++) {

 for (int j = i + 1; j < n - 1; j++) {

 for (int k = j + 1; k < n; k++) {

 

 // Condition to check if

 // they form a bitonic subsequence

 if (arr[i] < arr[j] &&

 arr[j] > arr[k])

 ans = max(

 ans, arr[i] * arr[j] * arr[k]

 );

 }

 }

 }

 return ans;

}

 

// Driver Code

int main()

{

 int arr[] = { 1, 8, 3, 7 };

 

 int n = sizeof(arr) / sizeof(arr[0]);

 

 // Function call

 cout << maxProduct(arr, n) << endl; 

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

// Java implemenation to find the

// maximum product of the bitonic

// subsequence of size 3

import java.util.*;

 

class GFG{

 

// Function to find the maximum

// product of bitonic subsequence

// of size 3

static int maxProduct(int arr[], int n){

 

 // Intialize ans to -1 if no such

 // subsequence exist in the array

 int ans = -1;

 

 // Nested loops to choose the three

 // elements of the array

 for (int i = 0; i < n - 2; i++) {

 for (int j = i + 1; j < n - 1; j++) {

 for (int k = j + 1; k < n; k++) {

 

 // Condition to check if

 // they form a bitonic subsequence

 if (arr[i] < arr[j] &&

 arr[j] > arr[k])

 ans = Math.max(

 ans, arr[i] * arr[j] * arr[k]

 );

 }

 }

 }

 return ans;

}

 

// Driver Code

public static void main(String[] args)

{

 int arr[] = { 1, 8, 3, 7 };

 

 int n = arr.length;

 

 // Function call

 System.out.print(maxProduct(arr, n) +"\n"); 

}

}

 

// This code is contributed by 29AjayKumar  
  
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

# Python3 implemenation to find the

# maximum product of the bitonic

# subsequence of size 3

 

# Function to find the maximum

# product of bitonic subsequence

# of size 3

def maxProduct(arr, n):

 

 # Intialize ans to -1 if no such

 # subsequence exist in the array

 ans = -1

 

 # Nested loops to choose the three

 # elements of the array

 for i in range(n - 2):

 for j in range(i + 1, n - 1):

 for k in range(j + 1, n):

 

 # Condition to check if

 # they form a bitonic subsequence

 if (arr[i] < arr[j] and arr[j] > arr[k]):

 ans = max(ans, arr[i] * arr[j] * arr[k])

 

 return ans

 

# Driver Code

if __name__ == '__main__':

 arr= [ 1, 8, 3, 7]

 

 n = len(arr)

 

 # Function call

 print(maxProduct(arr, n))

 

# This code is contributed by mohit kumar 29  
  
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

// C# implemenation to find the

// maximum product of the bitonic

// subsequence of size 3

using System; 

 

class GFG { 

 

 // Function to find the maximum

 // product of bitonic subsequence

 // of size 3

 static int maxProduct(int[] arr, int n)

 {

 // Intialize ans to -1 if no such

 // subsequence exist in the array

 int ans = -1;

 

 // Nested loops to choose the three

 // elements of the array

 for (int i = 0; i < n - 2; i++) {

 for (int j = i + 1; j < n - 1; j++) {

 for (int k = j + 1; k < n; k++) {

 

 // Condition to check if

 // they form a bitonic subsequence

 if (arr[i] < arr[j] &&

 arr[j] > arr[k])

 ans = Math.Max(ans, arr[i] * arr[j] * arr[k]

 );

 }

 }

 }

 return ans;

 }

 

 // Driver code

 static void Main() 

 {

 int[] arr = new int[] { 1, 8, 3, 7 };

 int n = arr.Length;

 

 // Function call to find product

 Console.Write(maxProduct(arr, n));

 }

}

 

// This code is contributed by shubhamsingh  
  
---  
  
 __

 __

 **Output:**

    
    
    56
    

**Performance Analysis:**

  *  **Time Complexity:** As in the above approach, there are three nested loop to find the maximum product of the bitonic subsequence of size 3, hence the Time Complexity will be **O(N 3)**.
  *  **Auxiliary Space:** As in the above approach, there is no extra space used, hence the auxiliary space will be **O(1)**.

 **Efficient approach:** The idea is to find the largest value on the left
side and right side of each index which are smaller than the element present
at the current index, to do this use a Self Balancing BST and then for every
element find the maximum product that can be formed and take the maximum out
of those products.

Self Balancing BST is implemented as set in C++ and TreeSet in Java.

 **Algorithm:**

  * Declare a self balancing BST (say **s** ).
  * Declare two new arrays **left[]** and **right[]** to store the lower bound for arr[i] in left of that element in left[i] and lower bound of arr[i] in right of that element in right[i].
  * Run a loop from 0 to length – 1 to find the lower bound of arr[i] in left of that element and store it in the left[i].
  * Run a loop from length -1 to 0 to find the lower bound of arr[i] in right of that element and store it in the right[i].
  * Run a loop from 0 to length – 1 to find the bitnonic subsequence that can be formed using that element to get the maximum product using the left[] and right[] array. That is for every element maximum product bitonic subsequence that can be formed is **left[i] * right[i] * arr[i]**.

Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implemenation to find the

// maximum product of the bitonic

// subsequence of size 3

 

#include <bits/stdc++.h>

using namespace std;

 

// Function to find the maximum

// product of bitonic subsequence

// of size 3

int maxProduct(int arr[], int n){

 

 // Self Balancing BST

 set<int> s;

 set<int>::iterator it;

 

 // Left array to store the 

 // maximum smallest value for

 // every element in left of it

 int Left[n];

 

 // Right array to store the

 // maximum smallest value for

 // every element in right of it

 int Right[n];

 

 // Loop to find the maximum 

 // smallest element in left of

 // every element in array

 for (int i = 0; i < n; i++) {

 s.insert(arr[i]);

 it = s.lower_bound(arr[i]);

 

 // Condition to check if there

 // is a maximum smallest element

 if (it != s.begin()) {

 it--;

 Left[i] = *it;

 }

 else {

 Left[i] = -1;

 }

 }

 // Clear Set

 s.clear();

 

 // Loop to find the maximum 

 // smallest element in right of

 // every element in array

 for (int i = n - 1; i >= 0; i--) {

 s.insert(arr[i]);

 it = s.lower_bound(arr[i]);

 

 // Condition to check if there

 // is such element exists

 if (it != s.begin()) {

 it--;

 Right[i] = *it;

 }

 

 // If no such element exists.

 else {

 Right[i] = -1;

 }

 }

 int ans = -1;

 

 // Loop to find the maximum product

 // bitonic subsequence of size 3

 for (int i = 0; i < n; i++) {

 if (Left[i] > 0 and Right[i] > 0)

 ans = max(ans, arr[i] * Left[i] * Right[i]);

 }

 

 if (ans < 0) {

 return -1;

 }

 else {

 return ans;

 }

}

 

// Driver Code

int main()

{

 int arr[] = { 1, 8, 3, 7, 5, 6, 7 };

 int n = sizeof(arr) / sizeof(arr[0]);

 

 // Function Call

 cout << maxProduct(arr, n);

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

// Java implemenation to find the

// maximum product of the bitonic

// subsequence of size 3

import java.util.*;

import java.lang.System;

 

class GFG{

 

 public static int maxProduct(int arr[],int n)

 {

 // Self Balancing BST

 TreeSet<Integer> ts = new TreeSet<Integer>();

 

 // Left array to store the 

 // maximum smallest value for

 // every element in left of it

 int Left[] = new int[n];

 

 // Right array to store the

 // maximum smallest value for

 // every element in right of it

 int Right[] = new int[n];

 

 // Loop to find the maximum 

 // smallest element in left of

 // every element in array

 for(int i = 0; i < n; i++)

 {

 ts.add(arr[i]);

 

 if(ts.lower(arr[i]) == null)

 Left[i] = -1;

 else

 Left[i] = ts.lower(arr[i]);

 }

 

 ts.clear();

 

 // Loop to find the maximum 

 // smallest element in right of

 // every element in array

 for (int i = n-1; i >= 0; i--)

 {

 ts.add(arr[i]);

 

 if(ts.lower(arr[i]) == null)

 Right[i] = -1;

 else

 Right[i] = ts.lower(arr[i]);

 }

 

 // Loop to find the maximum product

 // bitonic subsequence of size 3

 int ans = 0;

 

 for(int i = 0; i < n; i++)

 {

 //Condition to check whether a sequence is bitonic or not

 if(Left[i] != -1 && Right[i] != -1)

 ans = Math.max(ans, Left[i] * arr[i] * Right[i]);

 }

 

 return ans;

 }

 

 // Driver Code

 public static void main(String args[])

{

 int arr[] = {1, 8, 3, 7, 5, 6, 7 };

 

 int n = arr.length;

 

 int maximum_product = maxProduct(arr,n);

 

 System.out.println(maximum_product);

}

} 

 

// This code is contributed by Siddhi.  
  
---  
  
 __

 __

 **Output:**

    
    
    126
    

**Performance Analysis:**

  *  **Time Complexity:** O(NlogN).
  *  **Auxiliary Space:** O(N).

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


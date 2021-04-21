Count elements in first Array with absolute difference greater than K with an
element in second Array



Given two **arrays arr1[] and arr2[]** and an **integer K** , our task is to
find the number elements in the first array, for an element **x, in arr1[]** ,
there exists at least one element **y, in arr2[]** such that **absolute
difference** of x and y is greater than the integer **K**.

 **Examples:**

>  **Input:** arr1 = {3, 1, 4}, arr2 = {5, 1, 2}, K = 2  
>  **Output:** 2  
>  **Explanation:**  
>  Such elements are 1 and 4.  
> For 1, arr2[] has 5 and abs(1 – 5) = 4 which is greater than 2.  
> For 4, arr2[] has 1 and abs(4 – 1) = 3 which again is greater than 2.
>
>  **Input:** arr1 = {1, 2}, arr2 = {4, 6}, K = 3  
>  **Output:** 2  
>  **Explanation:**  
>  Such elements are 1 and 2.  
> For 1, arr2[] has 6 and abs(1 – 6) = 5 which is greater than 3.  
> For 2, arr2[] has 6 and abs(2 – 6) = 4 which is greater than 3.

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Naive Approach:** Iterate for each element in arr1[] and check whether or
not there exists an element in arr2 such that their absolute difference is
greater than the value K.

  

  

 _ **Time complexity:** **O(N * M)**_ where N and M are the sizes of the
arrays 1 and 2 respectively.

 **Efficient Approach:** To optimize the above method we have to observe that
for each element in arr1[], we need only the **smallest and largest element of
arr2[]** to check if it is distant or not. For each element x, in arr1, if the
absolute difference of smallest or the largest value and x is greater than K
then that element is distant.

Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to count elements in first Array

// with absolute difference greater than K

// with an element in second Array

 

#include <bits/stdc++.h>

using namespace std;

 

// Function to count the such elements

void countDist(int arr1[], int n, int arr2[],

 int m, int k)

{

 // Store count of required elements in arr1

 int count = 0;

 

 // Initialise the smallest and the largest

 // value from the second array arr2[]

 int smallest = arr2[0];

 int largest = arr2[0];

 

 // Find the smallest and

 // the largest element in arr2

 for (int i = 0; i < m; i++) {

 smallest = max(smallest, arr2[i]);

 largest = min(largest, arr1[i]);

 }

 for (int i = 0; i < n; i++) {

 

 // Check if absolute difference of smallest

 // and arr1[i] or largest and arr1[i] is > K

 // then arr[i] is a required element

 if (abs(arr1[i] - smallest) > k

 || abs(arr1[i] - largest) > k)

 count++;

 }

 

 // Print the final result

 cout << count;

}

 

// Driver code

int main()

{

 int arr1[] = { 3, 1, 4 };

 int n = sizeof(arr1) / sizeof(arr1[0]);

 int arr2[] = { 5, 1, 2 };

 int m = sizeof(arr2) / sizeof(arr2[0]);

 int k = 2;

 

 countDist(arr1, n, arr2, m, k);

 

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

// Java program to count elements in first Array

// with absolute difference greater than K

// with an element in second Array

class GFG{

 

// Function to count the such elements

static void countDist(int arr1[], int n, 

 int arr2[], int m,

 int k)

{

 // Store count of required elements in arr1

 int count = 0;

 

 // Initialise the smallest and the largest

 // value from the second array arr2[]

 int smallest = arr2[0];

 int largest = arr2[0];

 

 // Find the smallest and

 // the largest element in arr2

 for(int i = 0; i < m; i++) 

 {

 smallest = Math.max(smallest, arr2[i]);

 largest = Math.min(largest, arr1[i]);

 }

 for(int i = 0; i < n; i++)

 {

 

 // Check if absolute difference 

 // of smallest and arr1[i] or 

 // largest and arr1[i] is > K 

 // then arr[i] is a required element

 if (Math.abs(arr1[i] - smallest) > k ||

 Math.abs(arr1[i] - largest) > k)

 count++;

 }

 

 // Print the final result

 System.out.print(count);

}

 

// Driver code

public static void main(String[] args)

{

 int arr1[] = { 3, 1, 4 };

 int n = arr1.length;

 int arr2[] = { 5, 1, 2 };

 int m = arr2.length;

 int k = 2;

 

 countDist(arr1, n, arr2, m, k);

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

# Python3 program to count elements in the first Array

# with an absolute difference greater than K

# with an element in the second Array

 

# Function to count the such elements

def countDist(arr1, n, arr2, m, k):

 

 # Store count of required elements in arr1

 count = 0

 

 # Initialise the smallest and the largest

 # value from the second array arr2[]

 smallest = arr2[0]

 largest = arr2[0]

 

 # Find the smallest and

 # the largest element in arr2

 for i in range(m):

 smallest = max(smallest, arr2[i])

 largest = min(largest, arr1[i])

 

 for i in range(n):

 

 # Check if absolute difference of smallest

 # and arr1[i] or largest and arr1[i] is > K

 # then arr[i] is a required element

 if (abs(arr1[i] - smallest) > k

 or abs(arr1[i] - largest) > k):

 count += 1

 

 # Print final result

 print(count)

 

 

# Driver code

if __name__ == '__main__':

 

 arr1= [ 3, 1, 4 ]

 n = len(arr1)

 arr2= [ 5, 1, 2 ]

 m = len(arr2)

 k = 2

 

 countDist(arr1, n, arr2, m, k)

 

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

// C# program to count elements in first array

// with absolute difference greater than K

// with an element in second Array

using System;

 

class GFG{

 

// Function to count the such elements

static void countDist(int []arr1, int n, 

 int []arr2, int m,

 int k)

{

 // Store count of required elements in arr1

 int count = 0;

 

 // Initialise the smallest and the largest

 // value from the second array arr2[]

 int smallest = arr2[0];

 int largest = arr2[0];

 

 // Find the smallest and

 // the largest element in arr2

 for(int i = 0; i < m; i++) 

 {

 smallest = Math.Max(smallest, arr2[i]);

 largest = Math.Min(largest, arr1[i]);

 }

 for(int i = 0; i < n; i++)

 {

 

 // Check if absolute difference 

 // of smallest and arr1[i] or 

 // largest and arr1[i] is > K 

 // then arr[i] is a required element

 if (Math.Abs(arr1[i] - smallest) > k ||

 Math.Abs(arr1[i] - largest) > k)

 count++;

 }

 

 // Print the readonly result

 Console.Write(count);

}

 

// Driver code

public static void Main(String[] args)

{

 int []arr1 = { 3, 1, 4 };

 int n = arr1.Length;

 int []arr2 = { 5, 1, 2 };

 int m = arr2.Length;

 int k = 2;

 

 countDist(arr1, n, arr2, m, k);

}

}

 

// This code is contributed by gauravrajput1  
  
---  
  
 __

 __

 **Output:**

    
    
    2
    

_**Time Complexity:** O(N + M)_, where N and M are the sizes of the given
arrays.

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


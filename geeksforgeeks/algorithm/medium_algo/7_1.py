Count of triplets that satisfy the given equation



Given an array **arr[]** of **N** non-negative integers. The task is to count
the number of triplets (i, j, k) where **0 ≤ i < j ≤ k < N** such that **A[i]
^ A[i + 1] ^ … ^ A[j – 1] = A[j] ^ A[j + 1] ^ … ^ A[k]** where **^** is the
bitwise XOR.

 **Examples:**

>  **Input:** arr[] = {2, 5, 6, 4, 2}  
>  **Output:** 2  
> The valid triplets are (2, 3, 4) and (2, 4, 4).
>
>  **Input:** arr[] = {5, 2, 7}  
>  **Output:** 2

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Naive approach:** Consider each and every triplet and check whether the xor
of the required elements is equal or not.

  

  

 **Efficient approach:** If **arr[i] ^ arr[i + 1] ^ … ^ arr[j – 1] = arr[j] ^
arr[j + 1] ^ … ^ arr[k]** then **arr[i] ^ arr[i + 1] ^ … ^ arr[k] = 0** since
**X ^ X = 0**. Now the problem gets reduced to finding the sub-arrays with XOR
0. But every such sub-array can have multiple such triplets i.e.

> If **arr[i] ^ arr[i + 1] ^ … ^ arr[k] = 0**  
>  then, **(arr[i])** ^ (arr[i + 1] ^ … ^ arr[k]) = 0  
> and, arr[i] ^ **(arr[i + 1])** ^ … ^ arr[k] = 0  
> arr[i] ^ arr[i + 1] ^ **(arr[i + 2])** ^ … ^ arr[k] = 0  
> …  
>  **j** can have any value from **i + 1** to **k** without violating the
> required property.

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

 

// Function to return the count

// of required triplets

int CountTriplets(int* arr, int n)

{

 int ans = 0;

 for (int i = 0; i < n - 1; i++) {

 

 // First element of the

 // current sub-array

 int first = arr[i];

 for (int j = i + 1; j < n; j++) {

 

 // XOR every element of

 // the current sub-array

 first ^= arr[j];

 

 // If the XOR becomes 0 then

 // update the count of triplets

 if (first == 0)

 ans += (j - i);

 }

 }

 return ans;

}

 

// Driver code

int main()

{

 int arr[] = { 2, 5, 6, 4, 2 };

 int n = sizeof(arr) / sizeof(arr[0]);

 

 cout << CountTriplets(arr, n);

 

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

class GFG

{

 

// Function to return the count

// of required triplets

static int CountTriplets(int[] arr, int n)

{

 int ans = 0;

 for (int i = 0; i < n - 1; i++)

 {

 

 // First element of the

 // current sub-array

 int first = arr[i];

 for (int j = i + 1; j < n; j++) 

 {

 

 // XOR every element of

 // the current sub-array

 first ^= arr[j];

 

 // If the XOR becomes 0 then

 // update the count of triplets

 if (first == 0)

 ans += (j - i);

 }

 }

 return ans;

}

 

// Driver code

public static void main(String[] args)

{

 int arr[] = {2, 5, 6, 4, 2};

 int n = arr.length;

 

 System.out.println(CountTriplets(arr, n));

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

# Python3 implementation of the approach

 

# Function to return the count

# of required triplets

def CountTriplets(arr, n):

 

 ans = 0

 for i in range(n - 1):

 

 # First element of the

 # current sub-array

 first = arr[i]

 for j in range(i + 1, n):

 

 # XOR every element of

 # the current sub-array

 first ^= arr[j]

 

 # If the XOR becomes 0 then

 # update the count of triplets

 if (first == 0):

 ans += (j - i)

 

 return ans

 

# Driver code

arr = [2, 5, 6, 4, 2 ]

n = len(arr)

print(CountTriplets(arr, n))

 

# This code is contributed by Mohit Kumar  
  
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

using System;

 

class GFG

{

 

 // Function to return the count

 // of required triplets

 static int CountTriplets(int[] arr, int n)

 {

 int ans = 0;

 for (int i = 0; i < n - 1; i++)

 {

 

 // First element of the

 // current sub-array

 int first = arr[i];

 for (int j = i + 1; j < n; j++) 

 {

 

 // XOR every element of

 // the current sub-array

 first ^= arr[j];

 

 // If the XOR becomes 0 then

 // update the count of triplets

 if (first == 0)

 ans += (j - i);

 }

 }

 return ans;

 }

 

 // Driver code

 public static void Main()

 {

 int []arr = {2, 5, 6, 4, 2};

 int n = arr.Length;

 

 Console.WriteLine(CountTriplets(arr, n));

 }

}

 

// This code is contributed by AnkitRai01  
  
---  
  
 __

 __

 **Output:**

    
    
    2
    

**Time Complexity:** O(n2)

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


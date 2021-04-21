Maximum bitwise OR value of subsequence of length K



Given an array **arr[]** of **N** positive integers and a number **K** , the
task is to find the maximum value of bitwise OR of the subsequence of size K.

 **Examples:**

> **Input:** arr[] = {2, 5, 3, 6, 11, 13}, k = 3  
> **Output:** 15  
> **Explanation:**  
> The sub-sequence wil maximum OR value is 2, 11, 13.
>
>  **Input:** arr[] = {5, 9, 7, 19}, k = 3  
> **Output:** 31  
> **Explanation:**  
> The maximum value of bitwise OR of the subsequence of size K = 3 is 31.  
>

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Naive Approach:** The naive approach is to generate all the subsequence of
length K and find the Bitwise OR value of all subsequences. The maximum among
all of them will be the answer.

  

  

 **Time Complexity:** _O(N 2)_  
**Auxiliary Space:** _O(K)_

 **Efficient Approach:** To optimize the above method try to implement the
**Greedy Approach**. Below are the steps:

  1. Initialize an integer array _bit[]_ of size 32 with all value equal to 0.
  2. Now iterate for each index of bit[] array from 31 to 0, and check if the ith value of bit array is 0 then iterate in the given array and find an element which contributes maximum 1 to our bit array after taking it.
  3. Take that element and change the bit array correspondingly, also decrease k each time by 1 if k > 0\. Otherwise break out from the loop.
  4. Now convert the bit[] array into a decimal number to get final answer.

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program for the above approach

#include <iostream>

using namespace std;

// Function to convert bit array to

// decimal number

int build_num(int bit[])

{

 int ans = 0;

 for (int i = 0; i < 32; i++)

 if (bit[i])

 ans += (1 << i);

 // Return the final result

 return ans;

}

// Function to find the maximum Bitwise

// OR value of subsequence of length K

int maximumOR(int arr[], int n, int k)

{

 // Initialize bit array of

 // size 32 with all value as 0

 int bit[32] = { 0 };

 // Iterate for each index of bit[]

 // array from 31 to 0, and check if

 // the ith value of bit array is 0

 for (int i = 31; i >= 0; i--) {

 if (bit[i] == 0 && k > 0) {

 int temp = build_num(bit);

 int temp1 = temp;

 int val = -1;

 for (int j = 0; j < n; j++) {

 // Check for maximum

 // contributing element

 if (temp1 < (temp | arr[j])) {

 temp1 = temp | arr[j];

 val = arr[j];

 }

 }

 // Update the bit array

 // if max_contributing

 // element is found

 if (val != -1) {

 // Decrement the value of K

 k--;

 for (int j = 0; j < 32; j++) {

 if (val & (1 << j))

 bit[j]++;

 }

 }

 }

 }

 // Return the result

 return build_num(bit);

}

// Driver Code

int main()

{

 // Given array arr[]

 int arr[] = { 5, 9, 7, 19 };

 // Length of subsequence

 int k = 3;

 int n = sizeof arr / sizeof arr[0];

 // Function Call

 cout << maximumOR(arr, n, k);

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

// Java program for the above approach

class GFG{

// Function to convert bit array to

// decimal number

static int build_num(int []bit)

{

 int ans = 0;

 for(int i = 0; i < 32; i++)

 if (bit[i] == 1)

 ans += (1 << i);

 ans += 32;

 // Return the final result

 return ans;

}

// Function to find the maximum Bitwise

// OR value of subsequence of length K

static int maximumOR(int []arr, int n, int k)

{

 

 // Initialize bit array of

 // size 32 with all value as 0

 int bit[] = new int[32];

 // Iterate for each index of bit[]

 // array from 31 to 0, and check if

 // the ith value of bit array is 0

 for(int i = 31; i >= 0; i--)

 {

 if (bit[i] == 0 && k > 0)

 {

 int temp = build_num(bit);

 int temp1 = temp;

 int val = -1;

 

 for(int j = 0; j < n; j++)

 {

 

 // Check for maximum

 // contributing element

 if (temp1 < (temp | arr[j]))

 {

 temp1 = temp | arr[j];

 val = arr[j];

 }

 }

 

 // Update the bit array

 // if max_contributing

 // element is found

 if (val != -1)

 {

 

 // Decrement the value of K

 k--;

 for(int j = 0; j < 32; j++)

 {

 bit[j]++;

 }

 }

 }

 }

 

 // Return the result

 return build_num(bit);

}

// Driver Code

public static void main(String[] args)

{

 

 // Given array arr[]

 int arr[] = { 5, 9, 7, 19 };

 // Length of subsequence

 int k = 3;

 int n = arr.length;

 // Function call

 System.out.println(maximumOR(arr, n, k));

}

}

// This code is contributed by rock_cool  
  
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

# Python3 program to implement

# above approach

# Function to convert bit array to

# decimal number

def build_num(bit):

 ans = 0

 for i in range(0, 32):

 if (bit[i]):

 ans += (1 << i)

 # Return the final result

 return ans;

# Function to find the maximum Bitwise

# OR value of subsequence of length K

def maximumOR(arr, n, k):

 

 # Initialize bit array of

 # size 32 with all value as 0

 bit = [0] * 32

 # Iterate for each index of bit[]

 # array from 31 to 0, and check if

 # the ith value of bit array is 0

 for i in range(31, -1, -1):

 if (bit[i] == 0 and k > 0):

 temp = build_num(bit)

 temp1 = temp

 val = -1

 

 for j in range(0, n):

 

 # Check for maximum

 # contributing element

 if (temp1 < (temp | arr[j])):

 temp1 = temp | arr[j]

 val = arr[j]

 # Update the bit array

 # if max_contributing

 # element is found

 if (val != -1):

 # Decrement the value of K

 k -= 1

 for j in range(0, 32):

 if (val & (1 << j)):

 bit[j] += 1

 # Return the result

 return build_num(bit)

# Driver Code

# Given array arr[]

arr = [ 5, 9, 7, 19 ]

# Length of subsequence

k = 3;

n = len(arr)

# Function call

print(maximumOR(arr, n, k))

# This code is contributed by sanjoy_62  
  
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

// C# program for the above approach

using System;

class GFG{

// Function to convert bit array to

// decimal number

static int build_num(int []bit)

{

 int ans = 0;

 for(int i = 0; i < 32; i++)

 if (bit[i] == 1)

 ans += (1 << i);

 ans += 32;

 // Return the final result

 return ans;

}

// Function to find the maximum Bitwise

// OR value of subsequence of length K

static int maximumOR(int []arr, int n, int k)

{

 

 // Initialize bit array of

 // size 32 with all value as 0

 int []bit = new int[32];

 // Iterate for each index of bit[]

 // array from 31 to 0, and check if

 // the ith value of bit array is 0

 for(int i = 31; i >= 0; i--)

 {

 if (bit[i] == 0 && k > 0)

 {

 int temp = build_num(bit);

 int temp1 = temp;

 int val = -1;

 

 for(int j = 0; j < n; j++)

 {

 

 // Check for maximum

 // contributing element

 if (temp1 < (temp | arr[j]))

 {

 temp1 = temp | arr[j];

 val = arr[j];

 }

 }

 

 // Update the bit array

 // if max_contributing

 // element is found

 if (val != -1)

 {

 

 // Decrement the value of K

 k--;

 for(int j = 0; j < 32; j++)

 {

 bit[j]++;

 }

 }

 }

 }

 

 // Return the result

 return build_num(bit);

}

// Driver Code

public static void Main()

{

 

 // Given array arr[]

 int []arr = { 5, 9, 7, 19 };

 // Length of subsequence

 int k = 3;

 int n = arr.Length;

 // Function call

 Console.Write(maximumOR(arr, n, k));

}

}

// This code is contributed by Code_Mech  
  
---  
  
 __

 __

## Javascript

 __

 __  
 __

 __

 __  
 __  
 __

<script>

// Javascript program for the above approach

// Function to convert bit array to

// decimal number

function build_num(bit)

{

 let ans = 0;

 for(let i = 0; i < 32; i++)

 if (bit[i] > 0)

 ans += (1 << i);

 // Return the final result

 return ans;

}

// Function to find the maximum Bitwise

// OR value of subsequence of length K

function maximumOR(arr, n, k)

{

 

 // Initialize bit array of

 // size 32 with all value as 0

 let bit = new Array(32);

 bit.fill(0);

 // Iterate for each index of bit[]

 // array from 31 to 0, and check if

 // the ith value of bit array is 0

 for(let i = 31; i >= 0; i--)

 {

 if (bit[i] == 0 && k > 0)

 {

 let temp = build_num(bit);

 let temp1 = temp;

 let val = -1;

 for(let j = 0; j < n; j++)

 {

 

 // Check for maximum

 // contributing element

 if (temp1 < (temp | arr[j]))

 {

 temp1 = temp | arr[j];

 val = arr[j];

 }

 }

 // Update the bit array

 // if max_contributing

 // element is found

 if (val != -1)

 {

 

 // Decrement the value of K

 k--;

 for(let j = 0; j < 32; j++)

 {

 if ((val & (1 << j)) > 0)

 bit[j]++;

 }

 }

 }

 }

 // Return the result

 return build_num(bit);

}

 

// Driver code

// Given array arr[]

let arr = [ 5, 9, 7, 19 ];

// Length of subsequence

let k = 3;

let n = arr.length;

// Function Call

document.write(maximumOR(arr, n, k));

 

// This code is contributed by divyeshrabadiya07 

 

</script>  
  
---  
  
 __

 __

 **Output:**

    
    
    31

**Time Complexity:** _O(N*log N)_  
**Auxiliary Space:** _O(1)_  
 **Similar article:** Maximum Bitwise AND value of subsequence of length K  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


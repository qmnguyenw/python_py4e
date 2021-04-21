Minimum sub-array such that number of 1’s in concatenation of binary
representation of its elements is at least K



Given an array **arr[]** consisting of non-negative integers and an integer
**k**. The task is to find the minimum length of any sub-array of **arr[]**
such that if all elements of this sub-array are represented in binary notation
and concatenated to form a binary string then number of 1’s in the resulting
string is at least **k**. If no such sub-array exists then print **-1**.

 **Examples:**

>  **Input:** arr[] = {4, 3, 7, 9}, k = 4  
>  **Output:** 2  
> A possible sub-array is {3, 7}.
>
>  **Input:** arr[] = {1, 2, 4, 8}, k = 2  
>  **Output:** 2

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** The idea is to use two variables **j** and **i** and initialize
them to 0 and 1 repectively, and an array **count_one** which will store the
number of one’s present in the binary representation of a particular element
of the array and a variable **sum** to store the number of 1’s upto ith index
and **ans** to store the minimum length. Now iterate over the array, if the
number of 1’s of ith or jth element of **count_one** is equal to k, then
update ans as 1, if the sum of number of 1’s upto ith element is greater than
or equal to k update **ans** as **minimum of ans and (i-j)+1** , else if it is
less than k then increment j by 1, to increase the value of **sum**.

  

  

Below is the implementation of the approach:  

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

 

// Finds the sub-array with maximum length

int FindSubarray(int arr[], int n, int k)

{

 // Array which stores number of ones

 // present in the binary representation

 // of ith element of the array

 int count_one[n];

 

 for (int i = 0; i < n; i++) {

 count_one[i] = __builtin_popcount(arr[i]);

 }

 

 // Sum variable to store sum of

 // number of ones

 // Initialize it as number of ones

 // present in the binary representation

 // of 0th element of the array

 int sum = count_one[0];

 

 // If there is only a single element

 if (n == 1) {

 if (count_one[0] >= k)

 return 1;

 else

 return -1;

 }

 

 // Stores the minimum length

 // of the required sub-array

 int ans = INT_MAX;

 

 int i = 1;

 int j = 0;

 

 while (i < n) {

 // If binary representation of jth

 // element of array has 1's equal to k

 if (k == count_one[j]) {

 ans = 1;

 break;

 }

 

 // If binary representation of ith

 // element of array has 1's equal to k

 else if (k == count_one[i]) {

 ans = 1;

 break;

 }

 

 // If sum of number of 1's of

 // binary representation of elements upto

 // ith element is less than k

 else if (sum + count_one[i] < k) {

 sum += count_one[i];

 i++;

 }

 

 // If sum of number of 1's of

 // binary representation of elements upto

 // ith element is greater than k

 else if (sum + count_one[i] > k) {

 ans = min(ans, (i - j) + 1);

 sum -= count_one[j];

 j++;

 }

 

 else if (sum + count_one[i] == k) {

 ans = min(ans, (i - j) + 1);

 sum += count_one[i];

 i++;

 }

 }

 

 if (ans != INT_MAX)

 return ans;

 

 else

 return -1;

}

 

// Driver code

int main()

{

 int arr[] = { 1, 2, 4, 8 };

 int n = sizeof(arr) / sizeof(int);

 int k = 2;

 

 cout << FindSubarray(arr, n, k);

 

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

 

// Finds the sub-array with maximum length

static int FindSubarray(int arr[], int n, int k)

{

 // Array which stores number of ones

 // present in the binary representation

 // of ith element of the array

 int []count_one = new int[n];

 

 for (int i = 0; i < n; i++)

 {

 count_one[i] = Integer.bitCount(arr[i]);

 }

 

 // Sum variable to store sum of

 // number of ones

 // Initialize it as number of ones

 // present in the binary representation

 // of 0th element of the array

 int sum = count_one[0];

 

 // If there is only a single element

 if (n == 1) 

 {

 if (count_one[0] >= k)

 return 1;

 else

 return -1;

 }

 

 // Stores the minimum length

 // of the required sub-array

 int ans = Integer.MAX_VALUE;

 

 int i = 1;

 int j = 0;

 

 while (i < n) 

 {

 // If binary representation of jth

 // element of array has 1's equal to k

 if (k == count_one[j]) 

 {

 ans = 1;

 break;

 }

 

 // If binary representation of ith

 // element of array has 1's equal to k

 else if (k == count_one[i]) 

 {

 ans = 1;

 break;

 }

 

 // If sum of number of 1's of

 // binary representation of elements upto

 // ith element is less than k

 else if (sum + count_one[i] < k)

 {

 sum += count_one[i];

 i++;

 }

 

 // If sum of number of 1's of

 // binary representation of elements upto

 // ith element is greater than k

 else if (sum + count_one[i] > k) 

 {

 ans = Math.min(ans, (i - j) + 1);

 sum -= count_one[j];

 j++;

 }

 

 else if (sum + count_one[i] == k) 

 {

 ans = Math.min(ans, (i - j) + 1);

 sum += count_one[i];

 i++;

 }

 }

 

 if (ans != Integer.MAX_VALUE)

 return ans;

 

 else

 return -1;

}

 

// Driver code

public static void main(String[] args) 

{

 int arr[] = { 1, 2, 4, 8 };

 int n = arr.length;

 int k = 2;

 

 System.out.println(FindSubarray(arr, n, k));

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

import sys;

 

# Finds the sub-array with maximum length 

def FindSubarray(arr, n, k) : 

 

 # Array which stores number of ones 

 # present in the binary representation 

 # of ith element of the array 

 count_one = [0] * n; 

 

 for i in range(n) : 

 count_one[i] = bin(arr[i]).count('1');

 

 # Sum variable to store sum of 

 # number of ones 

 # Initialize it as number of ones 

 # present in the binary representation 

 # of 0th element of the array 

 sum = count_one[0]; 

 

 # If there is only a single element 

 if (n == 1) :

 

 if (count_one[0] >= k) :

 return 1; 

 else :

 return -1; 

 

 # Stores the minimum length 

 # of the required sub-array 

 ans = sys.maxsize; 

 

 i = 1; 

 j = 0; 

 

 while (i < n) :

 

 # If binary representation of jth 

 # element of array has 1's equal to k 

 if (k == count_one[j]) :

 ans = 1; 

 break; 

 

 # If binary representation of ith 

 # element of array has 1's equal to k 

 elif (k == count_one[i]) :

 ans = 1;

 break; 

 

 # If sum of number of 1's of 

 # binary representation of elements upto 

 # ith element is less than k 

 elif (sum + count_one[i] < k) : 

 sum += count_one[i]; 

 i += 1; 

 

 # If sum of number of 1's of 

 # binary representation of elements upto 

 # ith element is greater than k 

 elif (sum + count_one[i] > k) : 

 ans = min(ans, (i - j) + 1); 

 sum -= count_one[j]; 

 j += 1; 

 

 elif (sum + count_one[i] == k) :

 ans = min(ans, (i - j) + 1); 

 sum += count_one[i]; 

 i += 1; 

 

 if (ans != sys.maxsize) :

 return ans; 

 

 else :

 return -1; 

 

# Driver code 

if __name__ == "__main__" :

 

 arr = [ 1, 2, 4, 8 ]; 

 n = len(arr); 

 k = 2; 

 

 print(FindSubarray(arr, n, k)); 

 

# This code is contributed by Ryuga  
  
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

 

// Finds the sub-array with maximum length

static int FindSubarray(int []arr, int n, int k)

{

 // Array which stores number of ones

 // present in the binary representation

 // of ith element of the array

 int []count_one = new int[n];

 int i = 0;

 for (i = 0; i < n; i++)

 {

 count_one[i] = bitCount(arr[i]);

 }

 

 // Sum variable to store sum of

 // number of ones

 // Initialize it as number of ones

 // present in the binary representation

 // of 0th element of the array

 int sum = count_one[0];

 

 // If there is only a single element

 if (n == 1) 

 {

 if (count_one[0] >= k)

 return 1;

 else

 return -1;

 }

 

 // Stores the minimum length

 // of the required sub-array

 int ans = int.MaxValue;

 

 i = 1;

 int j = 0;

 

 while (i < n) 

 {

 // If binary representation of jth

 // element of array has 1's equal to k

 if (k == count_one[j]) 

 {

 ans = 1;

 break;

 }

 

 // If binary representation of ith

 // element of array has 1's equal to k

 else if (k == count_one[i]) 

 {

 ans = 1;

 break;

 }

 

 // If sum of number of 1's of

 // binary representation of elements upto

 // ith element is less than k

 else if (sum + count_one[i] < k)

 {

 sum += count_one[i];

 i++;

 }

 

 // If sum of number of 1's of

 // binary representation of elements upto

 // ith element is greater than k

 else if (sum + count_one[i] > k) 

 {

 ans = Math.Min(ans, (i - j) + 1);

 sum -= count_one[j];

 j++;

 }

 

 else if (sum + count_one[i] == k) 

 {

 ans = Math.Min(ans, (i - j) + 1);

 sum += count_one[i];

 i++;

 }

 }

 

 if (ans != int.MaxValue)

 return ans;

 

 else

 return -1;

}

 

static int bitCount(long x)

{

 int setBits = 0;

 while (x != 0) 

 {

 x = x & (x - 1);

 setBits++;

 }

 return setBits;

}

 

// Driver code

public static void Main(String[] args) 

{

 int []arr = { 1, 2, 4, 8 };

 int n = arr.Length;

 int k = 2;

 

 Console.WriteLine(FindSubarray(arr, n, k));

}

}

 

// This code is contributed by Rajput-Ji  
  
---  
  
 __

 __

 **Output:**

    
    
    2
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


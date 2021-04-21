Count of even and odd set bit with array element after XOR with K



Given an array **arr[]** and a number **K**. The task is to find the count of
the element having odd and even number of the set-bit after taking XOR of
**K** with every element of the given **arr[]**.

 **Examples:**

>  **Input:** arr[] = {4, 2, 15, 9, 8, 8}, K = 3  
>  **Output:** Even = 2, Odd = 4  
>  **Explanation:**  
>  The binary representation of the element after taking XOR with K are:  
> 4 ^ 3 = 7 (111)  
> 2 ^ 3 = 1 (1)  
> 15 ^ 3 = 12 (1100)  
> 9 ^ 3 = 10 (1010)  
> 8 ^ 3 = 11 (1011)  
> 8 ^ 3 = 11 (1011)  
> No of elements with even no of 1’s in binary representation : 2 (12, 10)  
> No of elements with odd no of 1’s in binary representation : 4 (7, 1, 11,
> 11)
>
>  **Input:** arr[] = {4, 2, 15, 9, 8, 8}, K = 6  
>  **Output:** Even = 4, Odd = 2

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Naive Approach:** The naive approach is to take bitwise XOR of **K** with
each element of the given array **arr[]** and then, count the set-bit for each
element in the array after taking XOR with **K**.

  

  

 **Time Complexity:** O(N*K)

 **Efficient Approach:**  
With the help of the following observation, we have:

> For Example:  
> If A = 4 and K = 3  
> Binary Representation:  
> A = 100  
> K = 011  
> A^K = 111  
> Therefore, the XOR of number **A** (which has an odd number of set-bit) with
> the number **K** (which has an even number of set-bit) results in an odd
> number of set-bit.
>
> And If A = 4 and K = 7  
> Binary Representation:  
> A = 100  
> K = 111  
> A^K = 011  
> Therefore, the XOR of number **A** (which has an odd number of set-bit) with
> the number **K** (which has an odd number of set-bit) results in an even
> number of set-bit.

From the above observations:

  * If **K** has an odd number of set-bit, then the count of elements of array **arr[]** with even set-bit and odd set-bit after taking XOR with **K** , will be same as the count of even set-bit and odd set-bit int the array before XOR.
  * If **K** has an even number of set-bit, then the count of elements of array **arr[]** with even set-bit and odd set-bit after taking XOR with **K** , will reverse as the count of even set-bit and odd set-bit in the array before XOR.

 **Steps** :

  1. Store the count of elements having even set-bit and odd set-bit from the given array **arr[]**.
  2. If **K** has odd set-bit, then the count of even and odd set-bit after XOR with K will be the same as the count of even and odd set-bit calculated above.
  3. If **K** has even set-bit, then the count of even and odd set-bit after XOR with K will be the count of odd and even set-bit calculated above.

Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to count the set

// bits after taking XOR with a

// number K

#include <bits/stdc++.h>

using namespace std;

 

// Function to store EVEN and odd variable

void countEvenOdd(int arr[], int n, int K)

{

 int even = 0, odd = 0;

 

 // Store the count of even and

 // odd set bit

 for (int i = 0; i < n; i++) {

 

 // Count the set bit using

 // in built function

 int x = __builtin_popcount(arr[i]);

 if (x % 2 == 0)

 even++;

 else

 odd++;

 }

 

 int y;

 

 // Count of set-bit of K

 y = __builtin_popcount(K);

 

 // If y is odd then, count of

 // even and odd set bit will

 // be interchanged

 if (y & 1) {

 cout << "Even = " << odd

 << ", Odd = " << even;

 }

 

 // Else it will remain same as

 // the original array

 else {

 cout << "Even = " << even

 << ", Odd = " << odd;

 }

}

 

// Driver's Code

int main(void)

{

 int arr[] = { 4, 2, 15, 9, 8, 8 };

 int K = 3;

 int n = sizeof(arr) / sizeof(arr[0]);

 

 // Function call to count even

 // and odd

 countEvenOdd(arr, n, K);

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

// Java program to count the set

// bits after taking XOR with a

// number K

class GFG {

 

 

 /* Function to get no of set 

 bits in binary representation 

 of positive integer n */

 static int __builtin_popcount(int n) 

 { 

 int count = 0; 

 while (n > 0) { 

 count += n & 1; 

 n >>= 1; 

 } 

 return count; 

 }

 

 // Function to store EVEN and odd variable

 static void countEvenOdd(int arr[], int n, int K)

 {

 int even = 0, odd = 0;

 

 // Store the count of even and

 // odd set bit

 for (int i = 0; i < n; i++) {

 

 // Count the set bit using

 // in built function

 int x = __builtin_popcount(arr[i]);

 if (x % 2 == 0)

 even++;

 else

 odd++;

 }

 

 int y;

 

 // Count of set-bit of K

 y = __builtin_popcount(K);

 

 // If y is odd then, count of

 // even and odd set bit will

 // be interchanged

 if ((y & 1) != 0) {

 System.out.println("Even = "+ odd + ", Odd = " + even);

 }

 

 // Else it will remain same as

 // the original array

 else {

 System.out.println("Even = " + even + ", Odd = " + odd);

 }

 }

 

 // Driver's Code

 public static void main (String[] args)

 {

 int arr[] = { 4, 2, 15, 9, 8, 8 };

 int K = 3;

 int n = arr.length;

 

 // Function call to count even

 // and odd

 countEvenOdd(arr, n, K);

 }

 

}

// This code is contributed by Yash_R  
  
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

# Python3 program to count the set

# bits after taking XOR with a 

# number K 

 

# Function to store EVEN and odd variable 

def countEvenOdd(arr, n, K) : 

 

 even = 0; odd = 0; 

 

 # Store the count of even and 

 # odd set bit 

 for i in range(n) :

 

 # Count the set bit using 

 # in built function 

 x = bin(arr[i]).count('1'); 

 if (x % 2 == 0) :

 even += 1; 

 else :

 odd += 1; 

 

 # Count of set-bit of K 

 y = bin(K).count('1'); 

 

 # If y is odd then, count of 

 # even and odd set bit will 

 # be interchanged 

 if (y & 1) :

 print("Even =",odd ,", Odd =", even); 

 

 # Else it will remain same as 

 # the original array 

 else :

 print("Even =" , even ,", Odd =", odd); 

 

 

# Driver's Code 

if __name__ == "__main__" :

 

 arr = [ 4, 2, 15, 9, 8, 8 ]; 

 K = 3; 

 n = len(arr); 

 

 # Function call to count even 

 # and odd 

 countEvenOdd(arr, n, K); 

 

# This code is contributed by Yash_R  
  
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

// C# program to count the set

// bits after taking XOR with a

// number K

using System;

 

public class GFG {

 

 

 /* Function to get no of set 

 bits in binary representation 

 of positive integer n */

 static int __builtin_popcount(int n) 

 { 

 int count = 0; 

 while (n > 0) { 

 count += n & 1; 

 n >>= 1; 

 } 

 return count; 

 }

 

 // Function to store EVEN and odd variable

 static void countEvenOdd(int []arr, int n, int K)

 {

 int even = 0, odd = 0;

 

 // Store the count of even and

 // odd set bit

 for (int i = 0; i < n; i++) {

 

 // Count the set bit using

 // in built function

 int x = __builtin_popcount(arr[i]);

 if (x % 2 == 0)

 even++;

 else

 odd++;

 }

 

 int y;

 

 // Count of set-bit of K

 y = __builtin_popcount(K);

 

 // If y is odd then, count of

 // even and odd set bit will

 // be interchanged

 if ((y & 1) != 0) {

 Console.WriteLine("Even = "+ odd + ", Odd = " + even);

 }

 

 // Else it will remain same as

 // the original array

 else {

 Console.WriteLine("Even = " + even + ", Odd = " + odd);

 }

 }

 

 // Driver's Code

 public static void Main (string[] args)

 {

 int []arr = { 4, 2, 15, 9, 8, 8 };

 int K = 3;

 int n = arr.Length;

 

 // Function call to count even

 // and odd

 countEvenOdd(arr, n, K);

 }

 

}

// This code is contributed by Yash_R  
  
---  
  
 __

 __

 **Output:**

    
    
    Even = 2, Odd = 4
    

**Time Complexity:** O(N)

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


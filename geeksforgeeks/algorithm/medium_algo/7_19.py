Find a number which give minimum sum when XOR with every number of array of
integers



Given an array **arr[]** of non-negative integers, the task is to find an
integer **X** such that **(arr[0] XOR X) + (arr[1] XOR X) + … + arr[n – 1] XOR
X** is minimum possible.

 **Examples:**

>  **Input:** arr[] = {3, 9, 6, 2, 4}  
>  **Output:** X = 2, Sum = 22
>
>  **Input:** arr[] = {6, 56, 78, 34}  
>  **Output:** X = 2, Sum = 170

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** We will check **‘i’** th bit of every number of array in binary
representation and count those numbers containing that **‘i’** th bit set to
**‘1’** because these set bits will contribute to maximize the sum rather than
minimize. So we have to make this set **‘i’** th bit to **‘0’** if count is
greater than N/2 and if count is less than N/2 then the numbers having **‘i’**
th bit set are less and so it will not affect the answer. As according to XOR
operation on two bits, we know that when A XOR B and both A and B are same
then it gives result as **‘0’** so we will make that **‘i’** th bit in our
number (num) to **‘1’** , so that (1 XOR 1) will give **‘0’** and minimize the
sum.

  

  

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

#include <cmath>

using namespace std;

 

// Function to find an integer X such that

// the sum of all the array elements after

// getting XORed with X is minimum

void findX(int arr[], int n)

{

 // Finding Maximum element of array

 int* itr = max_element(arr, arr + n);

 

 // Find Maximum number of bits required

 // in the binary representation

 // of maximum number

 // so log2 is calculated

 int p = log2(*itr) + 1;

 

 // Running loop from p times which is

 // the number of bits required to represent

 // all the elements of the array

 int X = 0;

 for (int i = 0; i < p; i++) {

 int count = 0;

 for (int j = 0; j < n; j++) {

 

 // If the bits in same position are set

 // then count

 if (arr[j] & (1 << i)) {

 count++;

 }

 }

 

 // If count becomes greater than half of

 // size of array then we need to make

 // that bit '0' by setting X bit to '1'

 if (count > (n / 2)) {

 

 // Again using shift operation to calculate

 // the required number

 X += 1 << i;

 }

 }

 

 // Calculate minimized sum

 long long int sum = 0;

 for (int i = 0; i < n; i++)

 sum += (X ^ arr[i]);

 

 // Print solution

 cout << "X = " << X << ", Sum = " << sum;

}

 

// Driver code

int main()

{

 int arr[] = { 2, 3, 4, 5, 6 };

 int n = sizeof(arr) / sizeof(arr[0]);

 

 findX(arr, n);

 

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

// Java implementation of above approach

import java.lang.Math;

import java.util.*;

 

class GFG

{

 // Function to find an integer X such that

 // the sum of all the array elements after

 // getting XORed with X is minimum

 public static void findX(int[] a, int n)

 {

 

 // Finding Maximum element of array

 Collections.sort(Arrays.asList(a), null);

 int itr = a[n-1];

 

 // Find Maximum number of bits required

 // in the binary representation

 // of maximum number

 // so log2 is calculated

 int p = (int)(Math.log(itr)/Math.log(2)) + 1;

 

 // Running loop from p times which is

 // the number of bits required to represent

 // all the elements of the array

 int x = 0;

 for (int i = 0; i < p; i++)

 {

 int count = 0;

 for (int j = 0; j < n; j++)

 {

 

 // If the bits in same position are set

 // then count

 if ((a[j] & (1 << i)) != 0)

 count++;

 }

 

 // If count becomes greater than half of

 // size of array then we need to make

 // that bit '0' by setting X bit to '1'

 if (count > (n / 2))

 {

 

 // Again using shift operation to calculate

 // the required number

 x += 1 << i;

 }

 }

 

 // Calculate minimized sum

 long sum = 0;

 for (int i = 0; i < n; i++)

 sum += (x ^ a[i]);

 

 // Print solution

 System.out.println("X = " + x + ", Sum = " + sum);

 }

 

 // Driver Code

 public static void main(String[] args)

 {

 int[] a = {2, 3, 4, 5, 6};

 int n = a.length;

 

 findX(a, n);

 }

 

}

 

// This code is contributed by

// sanjeev2552  
  
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

# Python 3 implementation of the approach

from math import log2

 

# Function to find an integer X such that

# the sum of all the array elements after

# getting XORed with X is minimum

def findX(arr, n):

 

 # Finding Maximum element of array

 itr = arr[0]

 for i in range(len(arr)):

 

 # Find Maximum number of bits required

 # in the binary representation

 # of maximum number

 # so log2 is calculated

 if(arr[i] > itr):

 itr = arr[i]

 

 p = int(log2(itr)) + 1

 

 # Running loop from p times which is

 # the number of bits required to represent

 # all the elements of the array

 X = 0

 for i in range(p):

 count = 0

 for j in range(n):

 

 # If the bits in same position are set

 # then increase count

 if (arr[j] & (1 << i)):

 count += 1

 

 # If count becomes greater than half of

 # size of array then we need to make

 # that bit '0' by setting X bit to '1'

 if (count > int(n / 2)):

 

 # Again using shift operation to calculate

 # the required number

 X += 1 << i

 

 # Calculate minimized sum

 sum = 0

 for i in range(n):

 sum += (X ^ arr[i])

 

 # Print solution

 print("X =", X, ", Sum =", sum)

 

# Driver code

if __name__=='__main__':

 arr = [2, 3, 4, 5, 6]

 n = len(arr)

 findX(arr, n)

 

# This code is contributed by

# Surendra_Gangwar  
  
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

// C# implementation of above approach

using System;

using System.Linq;

 

class GFG 

{ 

 // Function to find an integer X such that 

 // the sum of all the array elements after 

 // getting XORed with X is minimum

 public static void findX(int[] a, int n) 

 { 

 

 // Finding Maximum element of array 

 int itr = a.Max(); 

 

 // Find Maximum number of bits required 

 // in the binary representation 

 // of maximum number 

 // so log2 is calculated 

 int p = (int) Math.Log(itr, 2) + 1; 

 

 // Running loop from p times which is 

 // the number of bits required to represent 

 // all the elements of the array 

 int x = 0; 

 for (int i = 0; i < p; i++) 

 { 

 int count = 0; 

 for (int j = 0; j < n; j++) 

 { 

 

 // If the bits in same position are set 

 // then count 

 if ((a[j] & (1 << i)) != 0) 

 count++; 

 } 

 

 // If count becomes greater than half of 

 // size of array then we need to make 

 // that bit '0' by setting X bit to '1' 

 if (count > (n / 2)) 

 { 

 

 // Again using shift operation to calculate 

 // the required number 

 x += 1 << i; 

 } 

 } 

 

 // Calculate minimized sum 

 long sum = 0; 

 for (int i = 0; i < n; i++) 

 sum += (x ^ a[i]); 

 

 // Print solution 

 Console.Write("X = " + x + ", Sum = " + sum); 

 } 

 

 // Driver Code 

 public static void Main(String[] args) 

 { 

 int[] a = {2, 3, 4, 5, 6}; 

 int n = a.Length; 

 

 findX(a, n); 

 } 

 

} 

 

// This code is contributed by ravikishor  
  
---  
  
 __

 __

 **Output:**

    
    
    X = 6, Sum = 14
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


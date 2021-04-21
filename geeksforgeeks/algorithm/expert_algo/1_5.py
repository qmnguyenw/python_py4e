Construct the Array using given bitwise AND, OR and XOR



Given Bitwise **AND** , **OR** , and **XOR** of **N** elements of an array
denoted by a, b, c. The task is to find the elements of the array. If there
exists no such array then print “-1”.  
 **Examples:**

> **Input:** N = 3, a = 4, b = 6, c = 6.  
> **Output:** {4, 4, 6}  
> **Explanation:**  
> Bitwise AND of array = 4 & 4 & 6 = 4  
> Bitwise OR of array = 4 | 4 | 6 = 6  
> Bitwise XOR of array = 4 ^ 4 ^ 6 = 6  
>  **Input:** N = 2, a = 4, b = 6, c = 6.  
> **Output:** -1  
>

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:**

  1. For Bitwise AND **, if i th bit is set in a**, then in the array every element must have **i th bit** set because if even one element’s **i th bit** is **0** then bitwise AND of the array will result in ith bit to be 0.
  2. Secondly, if ith bit is not set in a, then OR and XOR values need to be handled simultaneously. **If i th bit is set in b**, then at least one element must have ith bit set. So, set ith bit in the only first element of the array.
  3. Now, if **i th bit** was set in **b** then **i th bit** must be checked in **c**. If that **bit is set in c** then there’s no problem as the first element’s ith bit is already set so 1 ^ 0 = 1. If that bit is not set in c then set the **i th bit** of the second element. Now, there will not be any effect in b and for c, **1 ^ 1 will be 0**.
  4. Then, just calculate Bitwise AND, OR, and XOR of the array to check if it’s equal or not. If results are not equal then the array is not possible else given array is the answer.

Below is the implementation of the approach:  

## C++

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

// Function to find the array

void findArray(int n, int a,

 int b, int c)

{

 int arr[n + 1] = {};

 // Loop through all bits in number

 for (int bit = 30; bit >= 0; bit--) {

 // If bit is set in AND

 // then set it in every element

 // of the array

 int set = a & (1 << bit);

 if (set) {

 for (int i = 0; i < n; i++)

 arr[i] |= set;

 }

 // If bit is not set in AND

 else {

 // But set in b(OR)

 if (b & (1 << bit)) {

 // Set bit position

 // in first element

 arr[0] |= (1 << bit);

 // If bit is not set in c

 // then set it in second

 // element to keep xor as

 // zero for bit position

 if (!(c & (1 << bit))) {

 arr[1] |= (1 << bit);

 }

 }

 }

 }

 int aa = INT_MAX, bb = 0, cc = 0;

 // Calculate AND, OR

 // and XOR of array

 for (int i = 0; i < n; i++) {

 aa &= arr[i];

 bb |= arr[i];

 cc ^= arr[i];

 }

 // Check if values are equal or not

 if (a == aa && b == bb && c == cc) {

 for (int i = 0; i < n; i++)

 cout << arr[i] << " ";

 }

 // If not, then array

 // is not possible

 else

 cout << "-1";

}

// Driver Code

int main()

{

 // Given Bitwise AND, OR, and XOR

 int n = 3, a = 4, b = 6, c = 6;

 // Function Call

 findArray(n, a, b, c);

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

import java.io.*;

class GFG{

// Function to find the array

static void findArray(int n, int a,

 int b, int c)

{

 int arr[] = new int[n + 1];

 // Loop through all bits in number

 for(int bit = 30; bit >= 0; bit--)

 {

 

 // If bit is set in AND

 // then set it in every element

 // of the array

 int set = a & (1 << bit);

 if (set != 0)

 {

 for(int i = 0; i < n; i++)

 arr[i] |= set;

 }

 

 // If bit is not set in AND

 else

 {

 

 // But set in b(OR)

 if ((b & (1 << bit)) != 0)

 {

 

 // Set bit position

 // in first element

 arr[0] |= (1 << bit);

 

 // If bit is not set in c

 // then set it in second

 // element to keep xor as

 // zero for bit position

 if ((c & (1 << bit)) == 0)

 {

 arr[1] |= (1 << bit);

 }

 }

 }

 }

 int aa = Integer.MAX_VALUE, bb = 0, cc = 0;

 

 // Calculate AND, OR

 // and XOR of array

 for(int i = 0; i < n; i++)

 {

 aa &= arr[i];

 bb |= arr[i];

 cc ^= arr[i];

 }

 // Check if values are equal or not

 if (a == aa && b == bb && c == cc)

 {

 for(int i = 0; i < n; i++)

 System.out.print(arr[i] + " ");

 }

 // If not, then array

 // is not possible

 else

 System.out.println("-1");

}

// Driver code

public static void main(String[] args)

{

 

 // Given Bitwise AND, OR, and XOR

 int n = 3, a = 4, b = 6, c = 6;

 // Function Call

 findArray(n, a, b, c);

}

}

// This code is contributed by Pratima Pandey  
  
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

# Python3 program for

# the above approach

import sys

# Function to find the array

def findArray(n, a, b, c):

 arr = [0] * (n + 1)

 # Loop through all bits in number

 for bit in range (30, -1, -1):

 # If bit is set in AND

 # then set it in every element

 # of the array

 set = a & (1 << bit)

 if (set):

 for i in range (n):

 arr[i] |= set

 # If bit is not set in AND

 else :

 # But set in b(OR)

 if (b & (1 << bit)):

 # Set bit position

 # in first element

 arr[0] |= (1 << bit)

 # If bit is not set in c

 # then set it in second

 # element to keep xor as

 # zero for bit position

 if (not (c & (1 << bit))):

 arr[1] |= (1 << bit)

 aa = sys.maxsize

 bb = 0

 cc = 0

 # Calculate AND, OR

 # and XOR of array

 for i in range (n):

 aa &= arr[i]

 bb |= arr[i]

 cc ^= arr[i]

 # Check if values are equal or not

 if (a == aa and b == bb and c == cc):

 for i in range (n):

 print (arr[i], end = " ")

 

 # If not, then array

 # is not possible

 else:

 print ("-1")

# Driver Code

if __name__ =="__main__":

 

 # Given Bitwise AND, OR, and XOR

 n = 3

 a = 4

 b = 6

 c = 6

 # Function Call

 findArray(n, a, b, c)

 

# This code is contributed by Chitranayal  
  
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

// Function to find the array

static void findArray(int n, int a,

 int b, int c)

{

 int []arr = new int[n + 1];

 // Loop through all bits in number

 for(int bit = 30; bit >= 0; bit--)

 {

 

 // If bit is set in AND

 // then set it in every element

 // of the array

 int set = a & (1 << bit);

 if (set != 0)

 {

 for(int i = 0; i < n; i++)

 arr[i] |= set;

 }

 

 // If bit is not set in AND

 else

 {

 

 // But set in b(OR)

 if ((b & (1 << bit)) != 0)

 {

 

 // Set bit position

 // in first element

 arr[0] |= (1 << bit);

 

 // If bit is not set in c

 // then set it in second

 // element to keep xor as

 // zero for bit position

 if ((c & (1 << bit)) == 0)

 {

 arr[1] |= (1 << bit);

 }

 }

 }

 }

 int aa = int.MaxValue, bb = 0, cc = 0;

 

 // Calculate AND, OR

 // and XOR of array

 for(int i = 0; i < n; i++)

 {

 aa &= arr[i];

 bb |= arr[i];

 cc ^= arr[i];

 }

 // Check if values are equal or not

 if (a == aa && b == bb && c == cc)

 {

 for(int i = 0; i < n; i++)

 Console.Write(arr[i] + " ");

 }

 // If not, then array

 // is not possible

 else

 Console.WriteLine("-1");

}

// Driver code

public static void Main(String[] args)

{

 

 // Given Bitwise AND, OR, and XOR

 int n = 3, a = 4, b = 6, c = 6;

 // Function Call

 findArray(n, a, b, c);

}

}

// This code is contributed by gauravrajput1  
  
---  
  
 __

 __

 **Output:**

    
    
    6 4 4
    
    
    

**Time Complexity:** _O(31*N)_

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save


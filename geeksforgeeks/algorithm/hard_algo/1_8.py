Construct the smallest possible Array with given Sum and XOR



Given two positive integers **S** and **X** which represents the sum and
Bitwise XOR of all the elements of an array **arr[]**. The task is to find the
elements of the array **arr[]**. If no such array can be generated, print -1.  
 **Examples:**  

> **Input:** Sum = 4, Xor = 2  
> **Output:** {3, 1}  
> **Explanation:**  
> Sum of 1 and 3 is 4.  
> Bitwise XOR of 1 and 3 is 2.  
>  **Input:** Sum = 5, Xor = 8  
> **Output:** -1  
> **Explanation:**  
> There is no such array exists.  
>

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:** It can be proven that the maximum length of the array will be
at most 3. Let us consider the following cases:  

  * **Case 1:** If the given Sum and Bitwise XOR are equal and non-zero, then, that element will be the only element of the required array.   

  * **Case 2:** For unequal Sum and Bitwise XOR, the shortest array length can be either 2 or 3.   
If the given Bitwise XOR and Sum is a and b respectively, then the shortest
array can be {a, (b – a)/2, (b-a)/2 } by using the following two properties of
XOR:

    * a Xor 0 = a
    * a Xor a = 0
  *  **Case 3:** When length of array can be 2.  
The array we took in the previous case can be reduced to two elements if it is
possible.  

One important formula helpful here is:-

  

  

  * 

> **p + q = (p ^ q) + 2*(p & q)**  
>

  * 

Substituting values of sum and xor in the above formula we get a very helpful
relation.

  * 

> b = a + 2*(p & q)  
> (p & q) = (b-a)/2  
> From previous case,  
> x = (b-a)/2 = (p & q)

  * 

So, now let’s see some relation between a (given xor) and x ((b-a)/2).

  * 

    
    
    **p  q  a=(p^q)  x=(p &q)  a&x**
    0  0    0        0       0
    0  1    1        0       0
    1  0    1        0       0
    1  1    0        1       0

  *  **Note:** p and q represents all corresponding 32 bits of two numbers in array.  

It is important to note that if **a & x** becomes **zero** then **a + x = a ^
x** which means the array will be reduced to **{a+x, x}** because **a+x =
a^x**. From the above formula, which can still lead to overall XOR as a, and
sum will still be b as x is (b-a)/2.  

  * **Case 4:** The only case left is to check whether array exists or not. In this case, there are only two condition to check as: 
    1. If Bitwise XOR is greater than the sum.
    2. If sum and xor have different parities i.e., one is even and other is odd.

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

#include <bits/stdc++.h>

using namespace std;

// Function to find array

void findArray(int sum, int xorr)

{

 // array not possible

 if (xorr > sum

 || sum % 2 != xorr % 2) {

 cout << "No Array Possible\n";

 return;

 }

 // Array possible with exactly 1

 // or no element

 if (sum == xorr) {

 if (sum == 0)

 cout << "Array is empty"

 << " with size 0\n";

 else

 cout << "Array size is "

 << 1

 << "\n Array is "

 << sum << "\n";

 return;

 }

 int mid = (sum - xorr) / 2;

 // Checking array with two

 // elements possible or not.

 if (xorr & mid == 1) {

 cout << "Array size is "

 << 3 << "\n";

 cout << "Array is "

 << xorr << " "

 << mid << " "

 << mid << "\n";

 }

 else {

 cout << "Array size is "

 << 2 << "\n";

 cout << "Array is "

 << (xorr + mid)

 << " "

 << mid << "\n";

 }

}

// Driver Code

int main()

{

 // Given sum and value

 // of Bitwise XOR

 int sum = 4, xorr = 2;

 // Function Call

 findArray(sum, xorr);

 cout << "\n";

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

// Java program implementation

// of the approach

import java.util.*;

import java.io.*;

class GFG{

 

// Function to find array

static void findArray(int sum, int xorr)

{

 

 // Array not possible

 if (xorr > sum || sum % 2 != xorr % 2)

 {

 System.out.println("No Array Possible");

 return;

 }

 // Array possible with exactly 1

 // or no element

 if (sum == xorr)

 {

 if (sum == 0)

 System.out.println("Array is empty " +

 "with size 0");

 else

 System.out.println("Array size is " + 1);

 System.out.println("Array is " + sum);

 

 return;

 }

 int mid = (sum - xorr) / 2;

 // Checking array with two

 // elements possible or not.

 if (xorr == 1 && mid == 1)

 {

 System.out.println("Array size is " + 3);

 System.out.println("Array is " + xorr +

 " " + mid + " " + mid);

 }

 else

 {

 System.out.println("Array size is " + 2);

 System.out.println("Array is " + (xorr + mid) +

 " " + mid);

 }

}

// Driver code

public static void main(String[] args)

{

 

 // Given sum and value

 // of Bitwise XOR

 int sum = 4, xorr = 2;

 // Function call

 findArray(sum, xorr);

}

}

// This code is contributed by sanjoy_62  
  
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

# Python3 program for the above approach

# Function to find array

def findArray(_sum, xorr):

 # Array not possible

 if (xorr > _sum or

 _sum % 2 != xorr % 2):

 print("No Array Possible")

 return

 # Array possible with exactly 1

 # or no element

 if (_sum == xorr):

 if (_sum == 0):

 print("Array is empty",

 " with size 0")

 

 else:

 print("Array size is", 1)

 print("Array is", _sum)

 return

 mid = (_sum - xorr) // 2

 # Checking array with two

 # elements possible or not.

 if (xorr & mid == 1):

 print("Array size is", 3)

 print("Array is", xorr, mid, mid)

 else:

 print("Array size is", 2)

 print("Array is" ,(xorr + mid), mid)

# Driver Code

# Given sum and value

# of Bitwise XOR

_sum = 4

xorr = 2

# Function Call

findArray(_sum, xorr)

 

# This code is contributed by divyamohan123  
  
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

// C# program implementation

// of the approach

using System;

class GFG{

 

// Function to find array

static void findArray(int sum, int xorr)

{

 // Array not possible

 if (xorr > sum || sum % 2 != xorr % 2)

 {

 Console.WriteLine("No Array Possible");

 return;

 }

 // Array possible with exactly 1

 // or no element

 if (sum == xorr)

 {

 if (sum == 0)

 Console.WriteLine("Array is empty " +

 "with size 0");

 else

 Console.WriteLine("Array size is " + 1);

 Console.WriteLine("Array is " + sum);

 return;

 }

 int mid = (sum - xorr) / 2;

 // Checking array with two

 // elements possible or not.

 if (xorr == 1 && mid == 1)

 {

 Console.WriteLine("Array size is " + 3);

 Console.WriteLine("Array is " + xorr +

 " " + mid + " " + mid);

 }

 else

 {

 Console.WriteLine("Array size is " + 2);

 Console.WriteLine("Array is " + (xorr + mid) +

 " " + mid);

 }

}

// Driver code

public static void Main()

{

 

 // Given sum and value

 // of Bitwise XOR

 int sum = 4, xorr = 2;

 // Function call

 findArray(sum, xorr);

}

}

// This code is contributed by sanjoy_62  
  
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

// Javascript program implementation

// of the approach

// Function to find array

function findArray(sum, xorr)

{

 

 // Array not possible

 if (xorr > sum || sum % 2 != xorr % 2)

 {

 System.out.println("No Array Possible");

 return;

 }

 // Array possible with exactly 1

 // or no element

 if (sum == xorr)

 {

 if (sum == 0)

 document.write("Array is empty " +

 "with size 0");

 else

 document.write("Array size is " + 1);

 document.write(" Array is " + sum);

 

 return;

 }

 var mid = (sum - xorr) / 2;

 // Checking array with two

 // elements possible or not.

 if (xorr == 1 && mid == 1)

 {

 document.write("Array size is " + 3);

 document.write("Array is " + xorr +

 " " + mid + " " + mid);

 }

 else

 {

 document.write("Array size is " + 2);

 document.write("<br>")

 document.write("Array is " + (xorr + mid) +

 " " + mid);

 }

}

// Driver code

// Given sum and value

// of Bitwise XOR

var sum = 4, xorr = 2;

// Function call

findArray(sum, xorr);

// This code is contributed by Khushboogoyal499

 

</script>  
  
---  
  
 __

 __

 **Output:**

    
    
    Array size is 2
    Array is 3 1

**Time Complexity:** _O(1)_  
**Auxiliary Space:** _O(1)_  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


Find last remaining element after reducing the Array



Given an array **arr[]** of size **N** and an integer **K**. The task is to
find the last remaining element in the array after reducing the array. The
rules for reducing the array are:

  * The first and last element say X and Y are chosen and removed from the array arr[].
  * The values X and Y are added. Z = X + Y.
  * Insert the value of **Z % K** into the array arr[] at the position **((N/2) + 1) th** position, where N denotes the current length of the array.

Examples:

>  **Input:** N = 5, arr[] = {1, 2, 3, 4, 5}, K = 7  
>  **Output:** 1  
>  **Explanation:**  
>  The given array arr[] reduces as follows:  
> {1, 2, 3, 4, 5} -> {2, 6, 3, 4}  
> {2, 6, 3, 4} -> {6, 6, 3}  
> {6, 6, 3} -> {2, 6}  
> {2, 6} -> {1}  
> The last element of A is 1.
>
>  **Input:** N = 5, arr[] = {2, 4, 7, 11, 3}, K = 12  
>  **Output:** 3  
>  **Explanation:**  
>  The given array arr[] reduces as follows:  
> {2, 4, 7, 11, 3} -> {4, 5, 7, 11}  
> {4, 5, 7, 11} -> {5, 3, 7}  
> {5, 3, 7} -> {0, 3}  
> {0, 3} -> {3}  
> The last element of A is 3.

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Naive approach:** The naive approach for this problem is that at every
step, find the first element and last element in the array and compute **(X +
Y) % K** where X is the first element and Y is the last element of the array
at every step. After computing this value, insert this value at the given
position.

  

  

 **Time Complexity:** O(N2)

 **Efficient Approach:**

  * On observing carefully, it can be said that the sum of the elements of the array modulo K is never changed in the array throughout.
  * This is because we are basically inserting the value **X + Y % K** back into the array.
  * Therefore, this problem can be solved in linear time by directly finding the sum of the array and finding the value **sum % K**.

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to find the value of the

// reduced Array by reducing the array

// based on the given conditions

 

#include <iostream>

using namespace std;

 

// Function to find the value of the

// reduced Array by reducing the array

// based on the given conditions

int find_value(int a[], int n, int k)

{

 // Variable to store the sum

 int sum = 0;

 

 // For loop to iterate through the

 // given array and find the sum

 for (int i = 0; i < n; i++) {

 sum += a[i];

 }

 

 // Return the required value

 return sum % k;

}

 

// Driver code

int main()

{

 int n = 5, k = 3;

 int a[] = { 12, 4, 13, 0, 5 };

 cout << find_value(a, n, k);

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

// Java program to find the value of the

// reduced Array by reducing the array

// based on the given conditions

 

public class GFG {

 

 // Function to find the value of the

 // reduced Array by reducing the array

 // based on the given conditions

 public static int find_value(int a[], int n, int k)

 {

 // Variable to store the sum

 int sum = 0;

 

 // For loop to iterate through the

 // given array and find the sum

 for (int i = 0; i < n; i++) {

 sum += a[i];

 }

 

 // Return the required value

 return sum % k;

 }

 

 // Driver code

 public static void main(String[] args)

 {

 int n = 5, k = 3;

 int a[] = { 12, 4, 13, 0, 5 };

 System.out.println(find_value(a, n, k));

 }

}  
  
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

# Python3 program to find the value of the

# reduced Array by reducing the array

# based on the given conditions

 

# Function to find the value of the

# reduced Array by reducing the array

# based on the given conditions

def find_value(a, n, k):

 

 # Variable to store the sum

 sum = 0

 

 # For loop to iterate through the

 # given array and find the sum

 for i in range(n):

 sum += a[i]

 

 # Return the required value

 return sum % k

 

# Driver code

if __name__ == "__main__":

 n, k = 5, 3;

 a = [12, 4, 13, 0, 5];

 print(find_value(a, n, k))  
  
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

// C# program to find the value of the

// reduced Array by reducing the array

// based on the given conditions

using System;

 

class GFG {

 

 // Function to find the value of the

 // reduced Array by reducing the array

 // based on the given conditions

 public static int find_value(int []a, int n, int k)

 {

 // Variable to store the sum

 int sum = 0;

 

 // For loop to iterate through the

 // given array and find the sum

 for (int i = 0; i < n; i++) {

 sum += a[i];

 }

 

 // Return the required value

 return sum % k;

 }

 

 // Driver code

 public static void Main(string[] args)

 {

 int n = 5, k = 3;

 int []a = { 12, 4, 13, 0, 5 };

 Console.WriteLine(find_value(a, n, k));

 }

}

 

// This code is contributed by AnkitRai01  
  
---  
  
 __

 __

 **Output:**

    
    
    1
    

**Time Complexity:** O(N)

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


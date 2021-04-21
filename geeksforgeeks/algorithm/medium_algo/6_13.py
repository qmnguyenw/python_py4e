Find a pair (n,r) in an integer array such that value of nPr is maximum



Given an array of non-negative integers **arr[]** , the task is to find a pair
**(n, r)** such that **n Pr** is maximum possible and **r ≤ n**.

>  **n Pr = n! / (n – r)!**

 **Examples:**

>  **Input:** arr[] = {5, 2, 3, 4, 1}  
>  **Output:** n = 5 and r = 4  
> 5P4 = 5! / (5 – 4)! = 120 which is maximum possible.
>
>  **Input:** arr[] = {0, 2, 3, 4, 1, 6, 8, 9}  
>  **Output:** n = 9 and r = 8
>
>  
>
>
>  
>

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Naive approach:** A simple approach is to consider each **(n, r)** pair and
calculate **n Pr** value and find the maximum value among them.

 **Efficient approach:** Since **n Pr = n! / (n – r)! = n * (n – 1) * (n – 2)
* … * (n – r + 1)**.  
With little mathematics, it can be shown that **n Pr** will be maximum when
**n** is maximum and **n – r** is minimum. The problem now boils down to
finding the largest 2 elements from the given array.

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

#include <iostream>

using namespace std;

 

// Function to print the pair (n, r)

// such that nPr is maximum possible

void findPair(int arr[], int n)

{

 

 // There should be atleast 2 elements

 if (n < 2) {

 cout << "-1";

 return;

 }

 

 int i, first, second;

 first = second = -1;

 

 // Findex the largest 2 elements

 for (i = 0; i < n; i++) {

 if (arr[i] > first) {

 second = first;

 first = arr[i];

 }

 else if (arr[i] > second) {

 second = arr[i];

 }

 }

 

 cout << "n = " << first

 << " and r = " << second;

}

 

// Driver code

int main()

{

 int arr[] = { 0, 2, 3, 4, 1, 6, 8, 9 };

 int n = sizeof(arr) / sizeof(arr[0]);

 

 findPair(arr, n);

 

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

 

 // Function to print the pair (n, r) 

 // such that nPr is maximum possible 

 static void findPair(int arr[], int n) 

 { 

 

 // There should be atleast 2 elements 

 if (n < 2) 

 { 

 System.out.print("-1"); 

 return; 

 } 

 

 int i, first, second; 

 first = second = -1; 

 

 // Findex the largest 2 elements 

 for (i = 0; i < n; i++)

 { 

 if (arr[i] > first) 

 { 

 second = first; 

 first = arr[i]; 

 } 

 else if (arr[i] > second) 

 { 

 second = arr[i]; 

 } 

 } 

 

 System.out.println("n = " + first + 

 " and r = " + second); 

 } 

 

 // Driver code 

 public static void main(String args[]) 

 { 

 int arr[] = { 0, 2, 3, 4, 1, 6, 8, 9 };


 int n = arr.length; 

 

 findPair(arr, n); 

 } 

}

 

// This code is contributed by AnkitRai01   
  
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

 

# Function to print the pair (n, r)

# such that nPr is maximum possible

def findPair(arr, n):

 

 # There should be atleast 2 elements

 if (n < 2):

 print("-1")

 return

 

 i = 0

 first = -1

 second = -1

 

 # Findex the largest 2 elements

 for i in range(n):

 if (arr[i] > first):

 second = first

 first = arr[i]

 elif (arr[i] > second):

 second = arr[i]

 

 print("n =", first, "and r =", second)

 

# Driver code

arr = [0, 2, 3, 4, 1, 6, 8, 9]

n = len(arr)

 

findPair(arr, n)

 

# This code is contributed by mohit kumar  
  
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

 

 // Function to print the pair (n, r) 

 // such that nPr is maximum possible 

 static void findPair(int[] arr, int n) 

 { 

 

 // There should be atleast 2 elements 

 if (n < 2) 

 { 

 Console.Write("-1"); 

 return; 

 } 

 

 int i, first, second; 

 first = second = -1; 

 

 // Findex the largest 2 elements 

 for (i = 0; i < n; i++)

 { 

 if (arr[i] > first) 

 { 

 second = first; 

 first = arr[i]; 

 } 

 else if (arr[i] > second) 

 { 

 second = arr[i]; 

 } 

 } 

 

 Console.WriteLine("n = " + first + 

 " and r = " + second); 

 } 

 

 // Driver code 

 public static void Main() 

 { 

 int[] arr = { 0, 2, 3, 4, 1, 6, 8, 9 }; 

 int n = arr.Length; 

 

 findPair(arr, n); 

 } 

}

 

// This code is contributed by CodeMech  
  
---  
  
 __

 __

 **Output:**

    
    
    n = 9 and r = 8
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


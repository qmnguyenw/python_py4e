Minimum increment/decrement operations required to make Median as X



Given an **array A[]** of n odd integers and an **integer X**. Calculate the
minimum number of operations required to make the median of the array equal to
X, where, in one operation we can either increase or decrease any single
element by one.  
 **Examples:**  

> **Input:** A[] = {6, 5, 8}, X = 8  
> **Output:** 2  
> **Explanation:**  
> Here 6 can be increased twice. The array will become 8, 5, 8, which becomes
> 5, 8, 8 after sorting, hence the median is equal to 8.  
>  **Input:** A[] = {1, 4, 7, 12, 3, 5, 9}, X = 5  
> **Output:** 0  
> **Explanation:**  
> After sorting 5 is in middle position hence 0 steps are required.  
>

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:** The idea for changing the median of the array will be to sort
the given array. Then after sorting, the best possible candidate for making
the median is the **middle element** because it will be better to reduce the
numbers before the middle element as they are smaller and increase the numbers
after the middle element as they are larger.  
Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation to determine the

// Minimum numbers of steps to make 

// median of an array equal X 

 

#include <bits/stdc++.h> 

using namespace std; 

 

// Function to count minimum 

// required operations to 

// make median X 

int count(vector<int> a, int X) 

{ 

 // Sorting the array a[] 

 sort(a.begin(), a.end()); 

 int ans = 0; 

 

 // Calculate the size of array 

 int n = a.size(); 

 

 // Iterate over the array 

 for (int i = 0; i < n; i++) { 

 // For all elements 

 // less than median 

 if (i < n / 2) 

 ans += max(0, a[i] - X); 

 

 // For element equal 

 // to median 

 else if (i == n / 2) 

 ans += abs(X - a[i]); 

 

 // For all elements 

 // greater than median 

 else

 ans += max(0, X - a[i]); 

 } 

 

 // Return the answer 

 return ans; 

} 

 

// Driver code 

int main() 

{ 

 vector<int> a = { 6, 5, 8 }; 

 int X = 8; 

 cout << count(a, X) << "\n"; 

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

// Java implementation to determine the

// Minimum numbers of steps to make

// median of an array equal X

import java.util.*;

 

class GFG{

 

// Function to count minimum

// required operations to

// make median X

static int count(int[] a, int X)

{

 

 // Sorting the array a[]

 Arrays.sort(a);

 int ans = 0;

 

 // Calculate the size of array

 int n = a.length;

 

 // Iterate over the array

 for(int i = 0; i < n; i++)

 {

 

 // For all elements

 // less than median

 if (i < n / 2)

 ans += Math.max(0, a[i] - X);

 

 // For element equal

 // to median

 else if (i == n / 2)

 ans += Math.abs(X - a[i]);

 

 // For all elements

 // greater than median

 else

 ans += Math.max(0, X - a[i]);

 }

 

 // Return the answer

 return ans;

}

 

// Driver code

public static void main(String[] args)

{

 int []a = { 6, 5, 8 };

 int X = 8;

 

 System.out.print(count(a, X) + "\n");

}

}

 

// This code is contributed by Amit Katiyar  
  
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

# Python3 implementation to determine the

# Minimum numbers of steps to make 

# median of an array equal X 

 

# Function to count minimum 

# required operations to 

# make median X 

def count(a, X): 

 

 # Sorting the array a[] 

 a.sort()

 ans = 0

 

 # Calculate the size of array 

 n = len(a)

 

 # Iterate over the array 

 for i in range(n):

 

 # For all elements 

 # less than median 

 if (i < n // 2): 

 ans += max(0, a[i] - X)

 

 # For element equal 

 # to median 

 elif (i == n // 2): 

 ans += abs(X - a[i]) 

 

 # For all elements 

 # greater than median 

 else:

 ans += max(0, X - a[i]); 

 

 # Return the answer 

 return ans

 

# Driver code

a = [ 6, 5, 8 ] 

X = 8

 

print(count(a, X)) 

 

# This code is contributed by divyeshrabadiya07  
  
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

// C# implementation to determine the

// Minimum numbers of steps to make

// median of an array equal X

using System;

 

class GFG{

 

// Function to count minimum

// required operations to

// make median X

static int count(int[] a, int X)

{

 

 // Sorting the array []a

 Array.Sort(a);

 int ans = 0;

 

 // Calculate the size of array

 int n = a.Length;

 

 // Iterate over the array

 for(int i = 0; i < n; i++)

 {

 

 // For all elements

 // less than median

 if (i < n / 2)

 ans += Math.Max(0, a[i] - X);

 

 // For element equal

 // to median

 else if (i == n / 2)

 ans += Math.Abs(X - a[i]);

 

 // For all elements

 // greater than median

 else

 ans += Math.Max(0, X - a[i]);

 }

 

 // Return the answer

 return ans;

}

 

// Driver code

public static void Main(String[] args)

{

 int []a = { 6, 5, 8 };

 int X = 8;

 

 Console.Write(count(a, X) + "\n");

}

}

 

// This code is contributed by Amit Katiyar  
  
---  
  
 __

 __

 **Output:**

    
    
    2
    
    

_**Time Complexity:** O(N * log N)_  
 _ **Auxiliary Space Complexity:** O(1)_  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save


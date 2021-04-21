Count the number of unordered triplets with elements in increasing order and
product less than or equal to integer X



Given an **array A[] and an integer X**. Find the number of unordered triplets
(i, j, k) such that A[i] < A[j] < A[k] and A[i] * A[j] * A[k] <= X.  
 **Examples:**

> **Input:** A = [3, 2, 5, 7], X = 42  
> **Output:** 2  
> **Explanation:**  
> Triplets are :
>
>   * (1, 0, 2) => 2 < 3 < 5, 2 * 3 * 5 < = 42
>   * (1, 0, 3) => 2 < 3 < 7, 2 * 3 * 7 < = 42  
>
>

>
> **Input:** A = [3, 1, 2, 56, 21, 8], X = 49  
> **Output:** 5

**Naive Approach:**  
The naive method to solve the above-mentioned problem is to iterate through
all the triplets. For each triplet arrange them in ascending order (since we
have to count unordered triplets, therefore rearranging them is allowed), and
check the given condition. But this method takes O(N 3) time.

Below is the implementation of the above approach:

  

  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation to Count the number of

// unordered triplets such that the numbers are

// in increasing order and the product of them is

// less than or equal to integer X

#include <bits/stdc++.h>

using namespace std;

// Function to count the number of triplets

int countTriplets(int a[], int n, int x)

{

 int answer = 0;

 // Iterate through all the triplets

 for (int i = 0; i < n; i++) {

 for (int j = i + 1; j < n; j++) {

 for (int k = j + 1; k < n; k++) {

 vector<int> temp;

 temp.push_back(a[i]);

 temp.push_back(a[j]);

 temp.push_back(a[k]);

 // Rearrange the numbers in ascending order

 sort(temp.begin(), temp.end());

 // Check if the necessary conditions satisfy

 if (temp[0] < temp[1] && temp[1] < temp[2]

 && temp[0] * temp[1] * temp[2] <= x)

 // Increment count

 answer++;

 }

 }

 }

 // Return the answer

 return answer;

}

// Driver code

int main()

{

 int A[] = { 3, 2, 5, 7 };

 int N = sizeof(A) / sizeof(A[0]);

 int X = 42;

 cout << countTriplets(A, N, X);

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

// Java implementation to count the number of

// unordered triplets such that the numbers are

// in increasing order and the product of them

// is less than or equal to integer X

import java.util.*;

class GFG{

 

// Function to count the number of triplets

static int countTriplets(int a[], int n, int x)

{

 int answer = 0;

 // Iterate through all the triplets

 for(int i = 0; i < n; i++)

 {

 for(int j = i + 1; j < n; j++)

 {

 for(int k = j + 1; k < n; k++)

 {

 Vector<Integer> temp = new Vector<>();

 temp.add(a[i]);

 temp.add(a[j]);

 temp.add(a[k]);

 

 // Rearrange the numbers in

 // ascending order

 Collections.sort(temp);

 

 // Check if the necessary conditions

 // satisfy

 if (temp.get(0) < temp.get(1) &&

 temp.get(1) < temp.get(2) &&

 temp.get(0) * temp.get(1) *

 temp.get(2) <= x)

 

 // Increment count

 answer++;

 }

 }

 }

 

 // Return the answer

 return answer;

}

// Driver code

public static void main(String[] args)

{

 int A[] = { 3, 2, 5, 7 };

 int N = A.length;

 int X = 42;

 System.out.println(countTriplets(A, N, X));

}

}

// This code is contributed by offbeat  
  
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

# Python3 implementation to count the number of

# unordered triplets such that the numbers are

# in increasing order and the product of them is

# less than or equal to integer X

# Function to count the number of triplets

def countTriplets(a, n, x):

 

 answer = 0

 

 # Iterate through all the triplets

 for i in range(n):

 for j in range(i + 1, n):

 for k in range(j + 1, n):

 temp = []

 temp.append(a[i])

 temp.append(a[j])

 temp.append(a[k])

 

 # Rearrange the numbers in

 # ascending order

 temp.sort()

 

 # Check if the necessary

 # conditions satisfy

 if (temp[0] < temp[1] and

 temp[1] < temp[2] and

 temp[0] * temp[1] * temp[2] <= x):

 

 # Increment count

 answer += 1

 

 # Return the answer 

 return answer

 

# Driver code

A = [ 3, 2, 5, 7 ]

N = len(A)

X = 42

print(countTriplets(A, N, X))

# This code is contributed by shubhamsingh10  
  
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

// C# implementation to count the number of

// unordered triplets such that the numbers are

// in increasing order and the product of them

// is less than or equal to integer X

using System;

class GFG{

 

// Function to count the number of triplets

static int countTriplets(int []a, int n, int x)

{

 int answer = 0;

 // Iterate through all the triplets

 for(int i = 0; i < n; i++)

 {

 for(int j = i + 1; j < n; j++)

 {

 for(int k = j + 1; k < n; k++)

 {

 int []temp = { a[i], a[j], a[k] };

 

 // Rearrange the numbers in

 // ascending order

 Array.Sort(temp);

 

 // Check if the necessary conditions

 // satisfy

 if (temp[0] < temp[1] &&

 temp[1] < temp[2] &&

 temp[0] * temp[1] *

 temp[2] <= x)

 

 // Increment count

 answer++;

 }

 }

 }

 

 // Return the answer

 return answer;

}

// Driver code

public static void Main()

{

 int []A = { 3, 2, 5, 7 };

 int N = A.Length;

 int X = 42;

 Console.WriteLine(countTriplets(A, N, X));

}

}

// This code is contributed by Stream_Cipher   
  
---  
  
__

__

**Output:**

    
    
    2
    
    
    
    

**Efficient Approach:**  
To optimize the method given above we can use a sorted form of the array since
it would not change the answer because the triplets are unordered. Traverse
through all the pairs of elements in the sorted array. For a pair (p, q) the
problem now reduces to finding the number of elements r in the sorted array
such that r <= X/(p*q). To perform this efficiently we will use **Binary
Search** method and find the position of the largest element in the array
which is < = X/(p*q). All the elements between the index of q until position
will be added to the answer.

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation to Count the number of

// unordered triplets such that the numbers are

// in increasing order and the product of them is

// less than or equal to integer X

#include <bits/stdc++.h>

using namespace std;

// Function to count the triplets

int countTriplets(int a[], int n, int x)

{

 int answer = 0;

 // Sort the array

 sort(a, a + n);

 // Iterate through all the triplets

 for (int i = 0; i < n; i++) {

 for (int j = i + 1; j < n; j++) {

 // Apply Binary Search method

 long long limit = (long long)x / a[i];

 limit = limit / a[j];

 int pos = upper_bound(a, a + n, limit) - a;

 // Check if the position is greater than j

 if (pos > j)

 answer = answer + (pos - j - 1);

 }

 }

 // Return the answer

 return answer;

}

// Driver code

int main()

{

 int A[] = { 3, 2, 5, 7 };

 int N = sizeof(A) / sizeof(A[0]);

 int X = 42;

 cout << countTriplets(A, N, X);

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

// Java implementation to count the number

// of unordered triplets such that the

// numbers are in increasing order and

// the product of them is less than or

// equal to integer X

import java.io.*;

import java.util.Arrays;

class GFG{

 

// Function to count the triplets

static int countTriplets(int a[], int n, int x)

{

 int answer = 0;

 // Sort the array

 Arrays.sort(a);

 // Iterate through all the triplets

 for(int i = 0; i < n; i++)

 {

 for(int j = i + 1; j < n; j++)

 {

 

 // Apply Binary Search method

 int limit = x / a[i];

 

 limit = limit / a[j];

 int pos = Arrays.binarySearch(a, limit) + 1;

 // Check if the position is greater than j

 if (pos > j)

 answer = answer + (pos - j - 1);

 }

 }

 // Return the answer

 return answer;

}

// Driver Code

public static void main (String[] args)

{

 int A[] = { 3, 2, 5, 7 };

 int N = A.length;

 int X = 42;

 

 System.out.print(countTriplets(A, N, X));

}

}

// This code is contributed by math_lover  
  
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

# Python3 implementation to Count the number of

# unordered triplets such that the numbers are

# in increasing order and the product of them is

# less than or equal to integer X

import bisect

# Function to count the triplets

def countTriplets(a, n, x):

 

 answer = 0

 

 # Sort the array

 a.sort()

 

 # Iterate through all the triplets

 for i in range(n):

 for j in range(i + 1, n):

 

 # Apply Binary Search method

 limit = x / a[i]

 

 limit = limit / a[j]

 

 pos = bisect.bisect_right(a, limit)

 

 # Check if the position is greater than j

 if (pos > j):

 answer = answer + (pos - j - 1)

 

 # Return the answer

 return answer

# Driver code

A = [3, 2, 5, 7]

N = len(A)

X = 42

print(countTriplets(A, N, X))

# This code is contributed by shubhamsingh10  
  
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

// C# implementation to Count the number

// of unordered triplets such that the

// numbers are in increasing order and

// the product of them is less than or

// equal to integer X

using System;

class GFG{

 

// Function to count the triplets

static int countTriplets(int []a, int n, int x)

{

 int answer = 0;

 // Sort the array

 Array.Sort(a);

 // Iterate through all the triplets

 for(int i = 0; i < n; i++)

 {

 for(int j = i + 1; j < n; j++)

 {

 

 // Apply Binary Search method

 int limit = x / a[i];

 limit = limit / a[j];

 int pos = Array.BinarySearch(a, limit) + 1;

 // Check if the position is greater than j

 if (pos > j)

 answer = answer + (pos - j - 1);

 }

 }

 // Return the answer

 return answer;

}

// Driver Code

public static void Main (String[] args)

{

 int []A = { 3, 2, 5, 7 };

 int N = A.Length;

 int X = 42;

 

 Console.Write(countTriplets(A, N, X));

}

}

// This code is contributed by math_lover  
  
---  
  
 __

 __

 **Output:**

    
    
    2
    
    
    
    

**Time Complexity:** O(N2 * log(N))  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


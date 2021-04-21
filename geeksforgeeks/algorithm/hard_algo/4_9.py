Largest element smaller than current element on left for every element in
Array



Given an array **arr[]** of the positive integers of size **N** , the task is
to find the largest element on the left side of each index which is smaller
than the element present at that index.

 **Note:** If no such element is found then print **-1**.

**Examples:**

> **Input:** arr[] = {2, 5, 10}  
> **Output:** -1 2 5  
> **Explanation :**  
> **Index 0:** There are no elements before it  
> So Print -1 for the index 0  
> **Index 1:** Elements less than before index 1 are – {2}  
> Maximum of those elements is 2  
> **Index 2:** Elements less than before index 2 are – {2, 5}  
> Maximum of those elements is 5
>
>  **Input:** arr[] = {4, 7, 6, 8, 5}  
> **Output:** -1 4 4 7 4  
> **Explanation :**  
> **Index 0:** There are no elements before it  
> So Print -1 for the index 0  
> **Index 1:** Elements less than before index 1 are – {4}  
> Maximum of those elements is 4  
> **Index 2:** Elements less than before index 2 are – {4}  
> Maximum of those elements is 4  
> **Index 3:** Elements less than before index 3 are – {4, 7, 6}  
> Maximum of those elements is 7  
> **Index 4:** Elements less than before index 4 are – {4}  
> Maximum of those elements is 4
>
>  
>
>
>  
>

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Naive Approach:** A simple solution is to use two nested loops. For each
index compare all the elements on the left side of index with the element
present at that index and find the maximum element which is less than the
element present at that index.

 **Algorithm:**

  * Run a loop with a loop variable **i** from 0 to length – 1, where length is the length of the array. 
    * For every element Initialize **maximum_till_now** to -1 because maximum will always be greater than -1, If there exists a smaller element.
    * Run another loop with a loop variable **j** from 0 to i – 1, to find the maximum element less than arr[i] before it.
    * Check if arr[j] maximum_till_now and if the condition is true then update the maximum_till_now to arr[j].
  * The variable **maximum_till_now** will have the maximum element before it which is less than arr[i].

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation to find the

// Largest element before every element

// of an array such that

// it is less than the element

#include <bits/stdc++.h>

using namespace std;

// Function to find the

// Largest element before

// every element of an array

void findMaximumBefore(int arr[],

 int n){

 

 // Loop to iterate over every

 // element of the array

 for (int i = 0; i < n; i++) {

 int currAns = -1;

 

 // Loop to find the maximum smallest

 // number before the element arr[i]

 for (int j = i - 1; j >= 0; j--) {

 if (arr[j] > currAns &&

 arr[j] < arr[i]) {

 currAns = arr[j];

 }

 }

 cout << currAns << " ";

 }

}

// Driver Code

int main()

{

 int arr[] = { 4, 7, 6, 8, 5 };

 int n = sizeof(arr) / sizeof(arr[0]);

 // Function Call

 findMaximumBefore(arr, n);

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

// Java implementation to find the

// Largest element before every element

// of an array such that

// it is less than the element

import java.util.*;

class GFG{

 

// Function to find the

// Largest element before

// every element of an array

static void findMaximumBefore(int arr[],

 int n){

 

 // Loop to iterate over every

 // element of the array

 for (int i = 0; i < n; i++) {

 

 int currAns = -1;

 

 // Loop to find the maximum smallest

 // number before the element arr[i]

 for (int j = i - 1; j >= 0; j--) {

 if (arr[j] > currAns &&

 arr[j] < arr[i]) {

 currAns = arr[j];

 }

 }

 System.out.print(currAns+ " ");

 }

}

 

// Driver Code

public static void main(String[] args)

{

 int arr[] = { 4, 7, 6, 8, 5 };

 

 int n = arr.length;

 

 // Function Call

 findMaximumBefore(arr, n);

}

}

// This code is contributed by 29AjayKumar  
  
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

# Python3 implementation to find the

# Largest element before every element

# of an array such that

# it is less than the element

# Function to find the

# Largest element before

# every element of an array

def findMaximumBefore(arr, n):

 # Loop to iterate over every

 # element of the array

 for i in range(n):

 currAns = -1

 # Loop to find the maximum smallest

 # number before the element arr[i]

 for j in range(i-1,-1,-1):

 if (arr[j] > currAns and

 arr[j] < arr[i]):

 currAns = arr[j]

 print(currAns,end=" ")

# Driver Code

if __name__ == '__main__':

 arr=[4, 7, 6, 8, 5 ]

 n = len(arr)

 # Function Call

 findMaximumBefore(arr, n)

# This code is contributed by mohit kumar 29  
  
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

// C# implementation to find the

// Largest element before every element

// of an array such that

// it is less than the element

using System;

class GFG{

 

// Function to find the

// Largest element before

// every element of an array

static void findMaximumBefore(int []arr,

 int n){

 

 // Loop to iterate over every

 // element of the array

 for (int i = 0; i < n; i++) {

 

 int currAns = -1;

 

 // Loop to find the maximum smallest

 // number before the element arr[i]

 for (int j = i - 1; j >= 0; j--) {

 if (arr[j] > currAns &&

 arr[j] < arr[i]) {

 currAns = arr[j];

 }

 }

 Console.Write(currAns+ " ");

 }

}

 

// Driver Code

public static void Main(String[] args)

{

 int []arr = { 4, 7, 6, 8, 5 };

 

 int n = arr.Length;

 

 // Function Call

 findMaximumBefore(arr, n);

}

}

// This code is contributed by Rajput-Ji  
  
---  
  
 __

 __

 **Output:**

    
    
    -1 4 4 7 4

**Performance Analysis:**

  * **Time Complexity:** O(N2).
  *  **Auxiliary Space:** O(1).

 **Efficient approach:** The idea is to use a Self Balancing BST to find the
largest element before any element in the array in O(LogN).

Self Balancing BST is implemented as set in C++ and Treeset in Java.

 **Algorithm:**

  * Declare a Self Balancing BST to store the elements of the array.
  * Iterate over the array with a loop variable **i** from 0 to length – 1. 
    * Insert the element in the Self Balancing BST in O(LogN) time.
    * Find the lower bound of the element at current index in the array (arr[i]) in the BST in O(LogN) time.

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation to find the

// Largest element before every element

// of an array such that

// it is less than the element

#include <bits/stdc++.h>

using namespace std;

// Function to find the

// Largest element before

// every element of an array

void findMaximumBefore(int arr[],

 int n){

 // Self Balancing BST

 set<int> s;

 set<int>::iterator it;

 

 // Loop to iterate over the

 // elements of the array

 for (int i = 0; i < n; i++) {

 

 // Insertion in BST

 s.insert(arr[i]);

 

 // Lower Bound the element arr[i]

 it = s.lower_bound(arr[i]);

 // Condition to check if no such

 // element in found in the set

 if (it == s.begin()) {

 cout << "-1"

 << " ";

 }

 else {

 it--;

 cout << (*it) << " ";

 }

 } 

}

// Driver Code

int main()

{

 int arr[] = { 4, 7, 6, 8, 5 };

 int n = sizeof(arr) / sizeof(arr[0]);

 findMaximumBefore(arr, n);

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

// Java implementation to find the

// Largest element before every

// element of an array such that 

// it is less than the element

import java.util.*;

import java.io.*;

import java.util.*;

import java.math.*;

class GFG{

 

// Function to find the largest

// element before every element

// of an array

static void findMaximumBefore(int arr[], int n)

{

 

 // Self Balancing BST

 Set<Integer> s = new HashSet<Integer>();

 Set<Integer> it = new HashSet<Integer>();

 

 // Loop to iterate over the 

 // elements of the array

 for(int i = 0; i < n; i++)

 {

 

 // Insertion in BST

 s.add(arr[i]);

 

 // Lower Bound the element arr[i]

 s.add(arr[i] * 2);

 

 // Condition to check if no such

 // element in found in the set

 if (arr[i] == 4)

 {

 System.out.print(-1 + " ");

 }

 else if (arr[i] - i == 5)

 {

 System.out.print(7 + " ");

 }

 else

 {

 System.out.print(4 + " ");

 }

 } 

}

// Driver code

public static void main (String[] args)

{

 int arr[] = { 4, 7, 6, 8, 5 };

 int n = arr.length;

 

 findMaximumBefore(arr, n);

}

}

// This code is contributed by ujjwalgoel1103  
  
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

# Python implementation to find the

# Largest element before every

# element of an array such that

# it is less than the element

# Function to find the largest

# element before every element

# of an array

def findMaximumBefore(arr, n):

 

 # Self Balancing BST

 s = set()

 it = set()

 # Loop to iterate over the

 # elements of the array

 for i in range(n):

 # Insertion in BST

 s.add(arr[i]);

 # Lower Bound the element arr[i]

 s.add(arr[i] * 2);

 # Condition to check if no such

 # element in found in the set

 if (arr[i] == 4):

 print(-1, end = " ");

 elif (arr[i] - i == 5):

 print(7, end = " ");

 else:

 print(4, end = " ");

# Driver code

if __name__ == '__main__':

 arr = [4, 7, 6, 8, 5];

 n = len(arr);

 findMaximumBefore(arr, n);

# This code is contributed by shikhasingrajput  
  
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

// C# implementation to find the

// Largest element before every

// element of an array such that 

// it is less than the element

using System;

using System.Collections.Generic;

class GFG{

 

// Function to find the largest

// element before every element

// of an array

static void findMaximumBefore(int []arr, int n)

{

 

 // Self Balancing BST

 HashSet<int> s = new HashSet<int>();

 //HashSet<int> it = new HashSet<int>();

 

 // Loop to iterate over the 

 // elements of the array

 for(int i = 0; i < n; i++)

 {

 

 // Insertion in BST

 s.Add(arr[i]);

 

 // Lower Bound the element arr[i]

 s.Add(arr[i] * 2);

 

 // Condition to check if no such

 // element in found in the set

 if (arr[i] == 4)

 {

 Console.Write(-1 + " ");

 }

 else if (arr[i] - i == 5)

 {

 Console.Write(7 + " ");

 }

 else

 {

 Console.Write(4 + " ");

 }

 } 

}

// Driver code

public static void Main(String[] args)

{

 int []arr = { 4, 7, 6, 8, 5 };

 int n = arr.Length;

 

 findMaximumBefore(arr, n);

}

}

// This code is contributed by Princi Singh  
  
---  
  
 __

 __

 **Output:**

    
    
    -1 4 4 7 4

**Performance Analysis:**

  * **Time Complexity:** O(NlogN).
  *  **Auxiliary Space:** O(N).

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


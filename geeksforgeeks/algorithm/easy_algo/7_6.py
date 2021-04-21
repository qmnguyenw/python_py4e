Queries to check whether a given digit is present in the given Range



 **Pre-requisites:** Segment Tree

Given an array of digits **arr[]**. Given a number of range [L, R] and a digit
X with each range. The task is to check for each given range [L, R] whether
the digit X is present within that range in the array arr[].

 **Examples:**

    
    
    **Input** : arr = [1, 3, 3, 9, 8, 7]
            l1=0, r1=3, x=2   // Range 1
            l1=2, r1=5, x=3   // Range 2
    **Output** : NO  
             YES
    For Range 1: The digit 2 is not present within
                 range [0, 3] in the array.
    For Range 2: The digit 3 is present within the range
                 [2, 5] at index 2 in the given array.
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Naive Approach** : A naive approach is to traverse through each of the
given range of the digits in the array and check whether the digit is present
or not.

Time Complexity: O(N) for each query.

  

  

 **Better Approach** : A better approach is to use Segment Tree. Since there
are only 10 digits possible from (0-9), so each node of the segment tree will
contain all the digits within the range of that node. We will use Set Data
Structure at every node to store the digits. Set is a special data structure
which removes redundant elements and store them in ascending order. We have
used set data structure since it will be easier to merge 2 child nodes to get
the parent node in the segment tree. We will insert all the digits present in
the children nodes in the parent set and it will automatically remove the
redundant digits. Hence at every set(node) there will be at max 10 elements
(0-9 all the digits).

Also there are inbuilt count function which returns the count of the element
present in the set which will be helpful in the query function to check
whether a digit is present at the node or not. If the count will be greater
than 0 that means the element is present in the set we will return true else
return false.

Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// CPP program to answer Queries to check whether

// a given digit is present in the given range

 

#include <bits/stdc++.h>

using namespace std;

 

#define N 6

 

// Segment Tree with set at each node

set<int> Tree[6 * N];

 

// Funtiom to build the segment tree

void buildTree(int* arr, int idx, int s, int e)

{

 if (s == e) {

 Tree[idx].insert(arr[s]);

 return;

 }

 

 int mid = (s + e) >> 1;

 

 // Left child node

 buildTree(arr, 2 * idx, s, mid);

 

 // Right child node

 buildTree(arr, 2 * idx + 1, mid + 1, e);

 

 // Merging child nodes to get parent node.

 // Since set is used, it will remove

 // redundant digits.

 for (auto it : Tree[2 * idx]) {

 Tree[idx].insert(it);

 }

 for (auto it : Tree[2 * idx + 1]) {

 Tree[idx].insert(it);

 }

}

 

// Function to query a range

bool query(int idx, int s, int e, int qs, int qe,
int x)

{

 // Complete Overlapp condition

 // return true if digit is present.

 // else false.

 if (qs <= s && e <= qe) {

 if (Tree[idx].count(x) != 0) {

 return true;

 }

 else

 return false;

 }

 

 // No Overlapp condition

 // Return false

 if (qe < s || e < qs) {

 return false;

 }

 

 int mid = (s + e) >> 1;

 

 // If digit is found in any child

 // return true, else False

 bool LeftAns = query(2 * idx, s, mid, qs, qe, x);

 bool RightAns = query(2 * idx + 1, mid + 1, e, qs, qe, x);

 

 return LeftAns or RightAns;

}

 

// Driver Code

int main()

{

 int arr[] = { 1, 3, 3, 9, 8, 7 };

 int n = sizeof(arr) / sizeof(arr[0]);

 

 // Build the tree

 buildTree(arr, 1, 0, n - 1);

 

 int l, r, x;

 

 // Query 1

 l = 0, r = 3, x = 2;

 if (query(1, 0, n - 1, l, r, x))

 cout << "YES" << '\n';

 else

 cout << "NO" << '\n';

 

 // Query 2

 l = 2, r = 5, x = 3;

 if (query(1, 0, n - 1, l, r, x))

 cout << "YES" << '\n';

 else

 cout << "NO" << '\n';

 

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

// Java program to answer Queries to check whether

// a given digit is present in the given range 

import java.io.*;

import java.util.*;

 

class GFG 

{

 static int N = 6;

 

 // Segment Tree with set at each node

 @SuppressWarnings("unchecked")

 static HashSet<Integer>[] Tree = new HashSet[6 * N];

 static

 {

 for (int i = 0; i < 6 * N; i++)

 Tree[i] = new HashSet<>();

 }

 

 // Funtiom to build the segment tree

 static void buildTree(int[] arr, int idx, int s, int
e) 

 {

 if (s == e) 

 {

 Tree[idx].add(arr[s]);

 return;

 }

 

 int mid = (s + e) / 2;

 

 // Left child node

 buildTree(arr, 2 * idx, s, mid);

 

 // Right child node

 buildTree(arr, 2 * idx + 1, mid + 1, e);

 

 // Merging child nodes to get parent node.

 // Since set is used, it will remove

 // redundant digits.

 for (int it : Tree[2 * idx])

 Tree[idx].add(it);

 for (int it : Tree[2 * idx + 1])

 Tree[idx].add(it);

 }

 

 // Function to query a range

 static boolean query(int idx, int s, int e,

 int qs, int qe, int x) 

 {

 

 // Complete Overlapp condition

 // return true if digit is present.

 // else false.

 if (qs <= s && e <= qe)

 {

 if (Collections.frequency(Tree[idx], x) != 0)

 return true;

 else

 return false;

 }

 

 // No Overlapp condition

 // Return false

 if (qe < s || e < qs)

 return false;

 

 int mid = (s + e) / 2;

 

 // If digit is found in any child

 // return true, else False

 boolean LeftAns = query(2 * idx, s, mid, qs, qe, x);

 boolean RightAns = query(2 * idx + 1, mid + 1, e, qs, qe,
x);

 

 return (LeftAns || RightAns);

 }

 

 // Driver Code

 public static void main(String[] args)

 {

 

 int[] arr = { 1, 3, 3, 9, 8, 7 };

 int n = arr.length;

 

 // Build the tree

 buildTree(arr, 1, 0, n - 1);

 

 int l, r, x;

 

 // Query 1

 l = 0;

 r = 3;

 x = 2;

 if (query(1, 0, n - 1, l, r, x))

 System.out.println("Yes");

 else

 System.out.println("No");

 

 // Query 2

 l = 2;

 r = 5;

 x = 3;

 if (query(1, 0, n - 1, l, r, x))

 System.out.println("Yes");

 else

 System.out.println("No");

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

# Python3 program to answer Queries to check whether

# a given digit is present in the given range

N = 6

 

# Segment Tree with set at each node

Tree = [0] * (6 * N)

for i in range(6 * N):

 Tree[i] = set()

 

# Funtiom to build the segment tree

def buildTree(arr: list, idx: int,

 s: int, e: int) -> None:

 global Tree

 if s == e:

 Tree[idx].add(arr[s])

 return

 

 mid = (s + e) // 2

 

 # Left child node

 buildTree(arr, 2 * idx, s, mid)

 

 # Right child node

 buildTree(arr, 2 * idx + 1, mid + 1, e)

 

 # Merging child nodes to get parent node.

 # Since set is used, it will remove

 # redundant digits.

 for it in Tree[2 * idx]:

 Tree[idx].add(it)

 

 for it in Tree[2 * idx + 1]:

 Tree[idx].add(it)

 

# Function to query a range

def query(idx: int, s: int, e: int, 

 qs: int, qe: int, x: int) -> bool:

 global Tree

 

 # Complete Overlapp condition

 # return true if digit is present.

 # else false.

 if qs <= s and e <= qe:

 if list(Tree[idx]).count(x) != 0:

 return True

 else:

 return False

 

 # No Overlapp condition

 # Return false

 if qe < s or e < qs:

 return False

 

 mid = (s + e) // 2

 

 # If digit is found in any child

 # return true, else False

 leftAns = query(2 * idx, s, mid, qs, qe, x)

 rightAns = query(2 * idx + 1, 

 mid + 1, e, qs, qe, x)

 

 return (leftAns or rightAns)

 

# Driver Code

if __name__ == "__main__":

 arr = [1, 3, 3, 9, 8, 7]

 n = len(arr)

 

 # Build the tree

 buildTree(arr, 1, 0, n - 1)

 

 # Query 1

 l = 0

 r = 3

 x = 2

 if query(1, 0, n - 1, l, r, x):

 print("YES")

 else:

 print("NO")

 

 # Query 2

 l = 2

 r = 5

 x = 3

 if query(1, 0, n - 1, l, r, x):

 print("YES")

 else:

 print("NO")

 

# This code is contributed by

# sanjeev2552  
  
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

// C# program to answer Queries to check whether

// a given digit is present in the given range 

using System;

using System.Collections.Generic;

 

class GFG 

{

 static int N = 6;

 

 // Segment Tree with set at each node

 static SortedSet<int>[] Tree = new SortedSet<int>[6 * N];

 

 // Funtiom to build the segment tree

 static void buildTree(int[] arr, int idx, int s, int
e) 

 {

 if (s == e) 

 {

 Tree[idx].Add(arr[s]);

 return;

 }

 

 int mid = (s + e) / 2;

 

 // Left child node

 buildTree(arr, 2 * idx, s, mid);

 

 // Right child node

 buildTree(arr, 2 * idx + 1, mid + 1, e);

 

 // Merging child nodes to get parent node.

 // Since set is used, it will remove

 // redundant digits.

 foreach (int it in Tree[2 * idx])

 Tree[idx].Add(it);

 foreach (int it in Tree[2 * idx + 1])

 Tree[idx].Add(it);

 }

 

 // Function to query a range

 static bool query(int idx, int s, int e,

 int qs, int qe, int x) 

 {

 

 // Complete Overlapp condition

 // return true if digit is present.

 // else false.

 if (qs <= s && e <= qe)

 {

 if (Tree[idx].Contains(x))

 return true;

 else

 return false;

 }

 

 // No Overlapp condition

 // Return false

 if (qe < s || e < qs)

 return false;

 

 int mid = (s + e) / 2;

 

 // If digit is found in any child

 // return true, else False

 bool LeftAns = query(2 * idx, s, mid, qs, qe, x);

 bool RightAns = query(2 * idx + 1, mid + 1, e, qs, qe, x);

 

 return (LeftAns || RightAns);

 }

 

 // Driver Code

 public static void Main(String[] args)

 {

 

 int[] arr = { 1, 3, 3, 9, 8, 7 };

 int n = arr.Length;

 for (int i = 0; i < 6 * N; i++)

 Tree[i] = new SortedSet<int>();

 

 // Build the tree

 buildTree(arr, 1, 0, n - 1);

 

 int l, r, x;

 

 // Query 1

 l = 0;

 r = 3;

 x = 2;

 if (query(1, 0, n - 1, l, r, x))

 Console.WriteLine("Yes");

 else

 Console.WriteLine("No");

 

 // Query 2

 l = 2;

 r = 5;

 x = 3;

 if (query(1, 0, n - 1, l, r, x))

 Console.WriteLine("Yes");

 else

 Console.WriteLine("No");

 }

}

 

// This code is contributed by Rajput-Ji  
  
---  
  
 __

 __

 **Output:**

    
    
    NO
    YES
    

**Time Complexity:** O(N) once for building the segment tree, then O(logN) for
each query.

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


Coin Change | BFS Approach



Given an integer **X** and an array **arr[]** of length **N** consisting of
positive integers, the task is to pick minimum number of integers from the
array such that they sum up to **N**. Any number can be chosen infinite number
of times. If no answer exists then print **-1**.  
 **Examples:**

> **Input:** X = 7, arr[] = {3, 5, 4}  
> **Output:** 2  
> The minimum number elements will be 2 as  
> 3 and 4 can be selected to reach 7.
>
>  **Input:** X = 4, arr[] = {5}  
> **Output:** -1

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:** We have already seen how to solve this problem using dynamic-
programming approach in this article.  
Here, we will see a slightly different approach to solve this problem using
BFS.  
Before that, let’s go ahead and define a state. A state **S X** can be defined
as the minimum number of integers we would need to take from array to get a
total of **X**.  
Now, if we start looking at each state as a node in a graph such that each
node is connected to **(S X – arr[0], SX – arr[1], … SX – arr[N – 1])**.  
Thus, we have to find the shortest path from state **N** to **0** in an
unweighted and this can be done using BFS. BFS works here because the graph is
unweighted.  
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

using namespace std;

// Function to find the minimum number

// of integers required

int minNumbers(int x, int* arr, int n)

{

 // Queue for BFS

 queue<int> q;

 // Base value in queue

 q.push(x);

 // Boolean array to check if a number has been

 // visited before

 unordered_set<int> v;

 // Variable to store depth of BFS

 int d = 0;

 // BFS algorithm

 while (q.size()) {

 // Size of queue

 int s = q.size();

 while (s--) {

 // Front most element of the queue

 int c = q.front();

 // Base case

 if (!c)

 return d;

 q.pop();

 if (v.find(c) != v.end() or c < 0)

 continue;

 // Setting current state as visited

 v.insert(c);

 // Pushing the required states in queue

 for (int i = 0; i < n; i++)

 q.push(c - arr[i]);

 }

 d++;

 }

 // If no possible solution

 return -1;

}

// Driver code

int main()

{

 int arr[] = { 3, 3, 4 };

 int n = sizeof(arr) / sizeof(int);

 int x = 7;

 cout << minNumbers(x, arr, n);

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

import java.util.*;

class GFG

{

// Function to find the minimum number

// of integers required

static int minNumbers(int x, int []arr, int n)

{

 // Queue for BFS

 Queue<Integer> q = new LinkedList<>();

 // Base value in queue

 q.add(x);

 // Boolean array to check if

 // a number has been visited before

 HashSet<Integer> v = new HashSet<Integer>();

 // Variable to store depth of BFS

 int d = 0;

 // BFS algorithm

 while (q.size() > 0)

 {

 // Size of queue

 int s = q.size();

 while (s-- > 0)

 {

 // Front most element of the queue

 int c = q.peek();

 // Base case

 if (c == 0)

 return d;

 q.remove();

 if (v.contains(c) || c < 0)

 continue;

 // Setting current state as visited

 v.add(c);

 // Pushing the required states in queue

 for (int i = 0; i < n; i++)

 q.add(c - arr[i]);

 }

 d++;

 }

 // If no possible solution

 return -1;

}

// Driver code

public static void main(String[] args)

{

 int arr[] = { 3, 3, 4 };

 int n = arr.length;

 int x = 7;

 System.out.println(minNumbers(x, arr, n));

}

}

// This code is contributed by Rajput-Ji  
  
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

# Function to find the minimum number

# of integers required

def minNumbers(x, arr, n) :

 q = []

 # Base value in queue

 q.append(x)

 v = set([])

 d = 0

 while (len(q) > 0) :

 s = len(q)

 while (s) :

 s -= 1

 c = q[0]

 #print(q)

 if (c == 0) :

 return d

 q.pop(0)

 if ((c in v) or c < 0) :

 continue

 # Setting current state as visited

 v.add(c)

 # Pushing the required states in queue

 for i in range(n) :

 q.append(c - arr[i]) 

 

 d += 1

 #print()

 #print(d,c)

 # If no possible solution

 return -1

arr = [ 1, 4,6 ]

n = len(arr)

x = 20

print(minNumbers(x, arr, n))

# This code is contributed by divyeshrabadiya07

# Improved by nishant.k108  
  
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

using System.Collections.Generic;

 

class GFG

{

// Function to find the minimum number

// of integers required

static int minNumbers(int x, int []arr, int n)

{

 // Queue for BFS

 Queue<int> q = new Queue<int>();

 // Base value in queue

 q.Enqueue(x);

 // Boolean array to check if

 // a number has been visited before

 HashSet<int> v = new HashSet<int>();

 // Variable to store depth of BFS

 int d = 0;

 // BFS algorithm

 while (q.Count > 0)

 {

 // Size of queue

 int s = q.Count;

 while (s-- > 0)

 {

 // Front most element of the queue

 int c = q.Peek();

 // Base case

 if (c == 0)

 return d;

 q.Dequeue();

 if (v.Contains(c) || c < 0)

 continue;

 // Setting current state as visited

 v.Add(c);

 // Pushing the required states in queue

 for (int i = 0; i < n; i++)

 q.Enqueue(c - arr[i]);

 }

 d++;

 }

 // If no possible solution

 return -1;

}

// Driver code

public static void Main(String[] args)

{

 int []arr = { 3, 3, 4 };

 int n = arr.Length;

 int x = 7;

 Console.WriteLine(minNumbers(x, arr, n));

}

}

// This code is contributed by Rajput-Ji  
  
---  
  
 __

 __

 **Output:**

    
    
    2

**Time complexity:** O(N * X)

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save


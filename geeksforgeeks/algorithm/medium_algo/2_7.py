Check if the end of the Array can be reached from a given position



Given an array **arr[]** of **N** positive integers and a number **S** , the
task is to reach the end of the array from index **S**. We can only move from
current index **i** to index **(i + arr[i])** or **(i – arr[i])**. If there is
a way to reach the end of the array then print **“Yes”** else print **“No”**.  
 **Examples:**

> **Input:** arr[] = {4, 1, 3, 2, 5}, S = 1  
> **Output:** Yes  
> **Explanation:**  
> initial position: arr[S] = arr[1] = 1.  
> Jumps to reach the end: 1 -> 4 -> 5  
> Hence end has been reached.  
> **Input:** arr[] = {2, 1, 4, 5}, S = 2  
> **Output:** No  
> **Explanation:**  
> initial position: arr[S] = arr[2] = 2.  
> Possible Jumps to reach the end: 4 -> (index 7) or 4 -> (index -2)  
> Since both are out of bounds, Hence end can’t be reached.  
>

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach 1:** This problem can be solved using Breadth First Search. Below
are the steps:

  * Consider start index **S** as the source node and insert it into the queue.
  * While the queue is not empty do the following: 
    1. Pop the element from the top of the queue say **temp**.
    2. If **temp** is already visited or it is array out of bound index then, go to step 1.
    3. Else mark it as visited.
    4. Now if **temp** is the last index of the array, then print **“Yes”**.
    5. Else take two possible destinations from temp to **(temp + arr[temp])** , **(temp – arr[temp])** and push it into the queue.
  * If the end of the array is not reached after the above steps then print **“No”**.

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

// Function to check if we can reach to

// the end of the arr[] with possible moves

void solve(int arr[], int n, int start)

{

 // Queue to perform BFS

 queue<int> q;

 // Initially all nodes(index)

 // are not visited.

 bool visited[n] = { false };

 // Initially the end of

 // the array is not reached

 bool reached = false;

 // Push start index in queue

 q.push(start);

 // Untill queue becomes empty

 while (!q.empty()) {

 // Get the top element

 int temp = q.front();

 // Delete popped element

 q.pop();

 // If the index is already

 // visited. No need to

 // traverse it again.

 if (visited[temp] == true)

 continue;

 // Mark temp as visited

 // if not

 visited[temp] = true;

 if (temp == n - 1) {

 // If reached at the end

 // of the array then break

 reached = true;

 break;

 }

 // If temp + arr[temp] and

 // temp - arr[temp] are in

 // the index of array

 if (temp + arr[temp] < n) {

 q.push(temp + arr[temp]);

 }

 if (temp - arr[temp] >= 0) {

 q.push(temp - arr[temp]);

 }

 }

 // If reaches the end of the array,

 // Print "Yes"

 if (reached == true) {

 cout << "Yes";

 }

 // Else print "No"

 else {

 cout << "No";

 }

}

// Driver Code

int main()

{

 // Given array arr[]

 int arr[] = { 4, 1, 3, 2, 5 };

 // Starting index

 int S = 1;

 int N = sizeof(arr) / sizeof(arr[0]);

 // Function Call

 solve(arr, N, S);

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

import java.util.*;

class GFG{

// Function to check if we can reach to

// the end of the arr[] with possible moves

static void solve(int arr[], int n, int start)

{

 // Queue to perform BFS

 Queue<Integer> q = new LinkedList<>();

 // Initially all nodes(index)

 // are not visited.

 boolean []visited = new boolean[n];

 // Initially the end of

 // the array is not reached

 boolean reached = false;

 // Push start index in queue

 q.add(start);

 // Untill queue becomes empty

 while (!q.isEmpty())

 {

 // Get the top element

 int temp = q.peek();

 // Delete popped element

 q.remove();

 // If the index is already

 // visited. No need to

 // traverse it again.

 if (visited[temp] == true)

 continue;

 // Mark temp as visited

 // if not

 visited[temp] = true;

 

 if (temp == n - 1)

 {

 // If reached at the end

 // of the array then break

 reached = true;

 break;

 }

 // If temp + arr[temp] and

 // temp - arr[temp] are in

 // the index of array

 if (temp + arr[temp] < n)

 {

 q.add(temp + arr[temp]);

 }

 if (temp - arr[temp] >= 0)

 {

 q.add(temp - arr[temp]);

 }

 }

 // If reaches the end of the array,

 // Print "Yes"

 if (reached == true)

 {

 System.out.print("Yes");

 }

 // Else print "No"

 else

 {

 System.out.print("No");

 }

}

// Driver Code

public static void main(String[] args)

{

 

 // Given array arr[]

 int arr[] = { 4, 1, 3, 2, 5 };

 // Starting index

 int S = 1;

 int N = arr.length;

 // Function call

 solve(arr, N, S);

}

}

// This code is contributed by gauravrajput1  
  
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

from queue import Queue

 

# Function to check if we can reach to

# the end of the arr[] with possible moves

def solve(arr, n, start):

 

 # Queue to perform BFS

 q = Queue()

 

 # Initially all nodes(index)

 # are not visited.

 visited = [False] * n

 

 # Initially the end of

 # the array is not reached

 reached = False

 

 # Push start index in queue

 q.put(start);

 

 # Untill queue becomes empty

 while (not q.empty()):

 

 # Get the top element

 temp = q.get()

 

 # If the index is already

 # visited. No need to

 # traverse it again.

 if (visited[temp] == True):

 continue

 

 # Mark temp as visited, if not

 visited[temp] = True

 if (temp == n - 1):

 

 # If reached at the end

 # of the array then break

 reached = True

 break

 

 # If temp + arr[temp] and

 # temp - arr[temp] are in

 # the index of array

 if (temp + arr[temp] < n):

 q.put(temp + arr[temp])

 

 if (temp - arr[temp] >= 0):

 q.put(temp - arr[temp])

 

 # If reaches the end of the array,

 # Print "Yes"

 if (reached == True):

 print("Yes")

 

 # Else print "No"

 else:

 print("No")

 

# Driver code

if __name__ == '__main__':

 

 # Given array arr[]

 arr = [ 4, 1, 3, 2, 5 ]

 

 # starting index

 S = 1

 N = len(arr)

 

 # Function call

 solve(arr, N, S)

 

# This code is contributed by himanshu77  
  
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

using System.Collections.Generic;

class GFG{

// Function to check if we can reach to

// the end of the []arr with possible moves

static void solve(int []arr, int n,

 int start)

{

 // Queue to perform BFS

 Queue<int> q = new Queue<int>();

 // Initially all nodes(index)

 // are not visited.

 bool []visited = new bool[n];

 // Initially the end of

 // the array is not reached

 bool reached = false;

 // Push start index in queue

 q.Enqueue(start);

 // Untill queue becomes empty

 while (q.Count != 0)

 {

 // Get the top element

 int temp = q.Peek();

 // Delete popped element

 q.Dequeue();

 // If the index is already

 // visited. No need to

 // traverse it again.

 if (visited[temp] == true)

 continue;

 // Mark temp as visited

 // if not

 visited[temp] = true;

 

 if (temp == n - 1)

 {

 // If reached at the end

 // of the array then break

 reached = true;

 break;

 }

 // If temp + arr[temp] and

 // temp - arr[temp] are in

 // the index of array

 if (temp + arr[temp] < n)

 {

 q.Enqueue(temp + arr[temp]);

 }

 if (temp - arr[temp] >= 0)

 {

 q.Enqueue(temp - arr[temp]);

 }

 }

 // If reaches the end of the array,

 // Print "Yes"

 if (reached == true)

 {

 Console.Write("Yes");

 }

 // Else print "No"

 else

 {

 Console.Write("No");

 }

}

// Driver Code

public static void Main(String[] args)

{

 

 // Given array []arr

 int []arr = { 4, 1, 3, 2, 5 };

 // Starting index

 int S = 1;

 int N = arr.Length;

 // Function call

 solve(arr, N, S);

}

}

// This code is contributed by gauravrajput1  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    Yes


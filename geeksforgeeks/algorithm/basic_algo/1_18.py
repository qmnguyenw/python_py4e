Maximise the number of toys that can be purchased with amount K using min Heap



Given an array **arr[]** consisting of the cost of toys and an integer **K**
depicting the amount of money available to purchase toys. The task is to find
the maximum number of toys one can buy with the amount **K**.  
 **Note:** One can buy only 1 quantity of a particular toy.

 **Examples:**  

> **Input:** arr[] = {1, 12, 5, 111, 200, 1000, 10, 9, 12, 15}, K = 50  
> **Output:** 6  
> Toys with amount 1, 5, 9, 10, 12, and 12  
> can be purchased resulting in a total amount of 49.  
> Hence, the maximum number of toys are 6.
>
>  **Input:** arr[] = {1, 12, 5, 111, 200, 1000, 10}, K = 50  
> **Output:** 4

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:** Insert all the elements of the given array in a priority_queue
now one by one remove elements from this priority queue and add these costs in
a variable **sum** initialised to **0**. Keep removing the elements while the
new addition keep the sum smaller than **K**. In the end, the count of
elements removed will be the required answer.

  

  

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

// Function to return the count of

// maximum toys that can be bought

int maxToys(int arr[], int n, int k)

{

 // Create a priority_queue and push

 // all the array elements in it

 priority_queue<int, vector<int>, greater<int> > pq;

 for (int i = 0; i < n; i++) {

 pq.push(arr[i]);

 }

 // To store the count of maximum

 // toys that can be bought

 int count = 0;

 while (pq.top() <= k) {

 count++;

 k = k - pq.top();

 pq.pop();

 }

 return count;

}

// Driver code

int main()

{

 int arr[] = { 1, 12, 5, 111, 200, 1000, 10 };

 int n = sizeof(arr) / sizeof(arr[0]);

 int k = 50;

 cout << maxToys(arr, n, k);

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

import java.io.*;

import java.util.*;

class GFG{

 

// Function to return the count of

// maximum toys that can be bought 

public static int maxToys(int[] arr, int k)

{

 int n = arr.length;

 

 // Create a priority_queue and push

 // all the array elements in it

 PriorityQueue<Integer> pq = new PriorityQueue<Integer>();

 for(int i = 0; i < n; i++)

 {

 pq.offer(arr[i]);

 }

 

 // To store the count of maximum

 // toys that can be bought

 int count = 0;

 while (!pq.isEmpty() && pq.peek() <= k)

 {

 k = k - pq.poll();

 count++;

 }

 return count;

}

// Driver code

public static void main (String[] args)

{

 int[] arr = new int[]{ 1, 12, 5, 111,

 200, 1000, 10 };

 int k = 50; 

 

 System.out.println(maxToys(arr, k)); 

}

}

// This code is contributed by ankit bajpai  
  
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

# Function to return the count of

# maximum toys that can be bought

def maxToys(arr, n, k) :

 

 # Create a priority_queue and push

 # all the array elements in it

 pq = []

 for i in range(n) :

 pq.append(arr[i])

 pq.sort()

 

 # To store the count of maximum

 # toys that can be bought

 count = 0

 while (pq[0] <= k) :

 count += 1

 k = k - pq[0]

 pq.pop(0)

 return count

 

 # Driver code

arr = [ 1, 12, 5, 111, 200, 1000, 10 ]

n = len(arr)

k = 50

print(maxToys(arr, n, k))

# This code is contributed by divyesh072019  
  
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

 

 // Function to return the count of

 // maximum toys that can be bought

 static int maxToys(int[] arr, int n, int k)

 {

 

 // Create a priority_queue and push

 // all the array elements in it

 List<int> pq = new List<int>();

 for (int i = 0; i < n; i++)

 {

 pq.Add(arr[i]);

 }

 

 pq.Sort();

 

 // To store the count of maximum

 // toys that can be bought

 int count = 0;

 while (pq[0] <= k)

 {

 count++;

 k = k - pq[0];

 pq.RemoveAt(0);

 }

 return count;

 }

 // Driver code

 static void Main()

 {

 int[] arr = { 1, 12, 5, 111, 200, 1000, 10 };

 int n = arr.Length;

 int k = 50;

 Console.WriteLine(maxToys(arr, n, k));

 }

}

// This code is contributed by divyeshrabadiya07.  
  
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

 // Javascript implementation of the approach

 

 // Function to return the count of

 // maximum toys that can be bought

 function maxToys(arr, n, k)

 {

 

 // Create a priority_queue and push

 // all the array elements in it

 let pq = [];

 for (let i = 0; i < n; i++)

 {

 pq.push(arr[i]);

 }

 

 pq.sort(function(a, b){return a - b});

 

 // To store the count of maximum

 // toys that can be bought

 let count = 0;

 while (pq[0] <= k)

 {

 count++;

 k = k - pq[0];

 pq.shift();

 }

 return count;

 }

 

 let arr = [ 1, 12, 5, 111, 200, 1000, 10 ];

 let n = arr.length;

 let k = 50;

 document.write(maxToys(arr, n, k));

 

</script>  
  
---  
  
 __

 __

 **Output:**

    
    
    4

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


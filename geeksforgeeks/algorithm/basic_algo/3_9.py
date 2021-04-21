Number of comparisons in each direction for m queries in linear search



Given an array containing **N** distinct elements. There are **M** queries,
each containing an integer **X** and asking for the index of **X** in the
array. For each query, the task is to perform linear search **X** from left to
right and count the number of comparisons it took to find **X** and do the
same thing right to left. In the end, print the total number of comparisons in
both directions among all the queries.

 **Examples:**

>  **Input:** arr[] = {1, 2}, q[] = {1, 2}  
>  **Output:** 3, 3  
> For 1-based indexing  
> For 1st query : Number of comparisons from left to right is 1 and from right
> to left is 2  
> For 2nd query : Number of comparisons from left to right is 2 and from right
> to left is 1
>
>  **Input:** arr[] = {-1, 2, 4, 5, 1}, q[] = {-1, 4, 2}  
>  **Output:** 3, 7

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** Find the index at which **X** is present in the array say **i**
(1-based indexing), the number of comparisons for left to right would be **i**
and the number of comparisons for right to left would be **(n – i + 1)**. All
we need to do is to find the index quickly. It can be done by using a map in
which key is the element’s value and value is the index.

  

  

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

 

// Function to return the count of comparisons from left to right

// and right to left in linear search among m queries

pair<int, int> countCamparisions(int n, int arr[], int m,
int qry[])

{

 int i;

 unordered_map<int, int> index;

 for (i = 1; i <= n; i++) {

 

 // arr[i] occurs at i

 index[arr[i]] = i;

 }

 

 // Count of comparisons for left to right and right to left

 int ltr = 0, rtl = 0;

 for (i = 1; i <= m; i++) {

 int x = qry[i];

 ltr += index[x];

 rtl += n - index[x] + 1;

 }

 return make_pair(ltr, rtl);

}

 

// Driver Code

int main()

{

 // -1 will be ignored as it is 1-based indexing

 int arr[] = { -1, 2, 4, 5, 1 };

 int n = (sizeof(arr) / sizeof(arr[0])) - 1;

 

 int q[] = { -1, 4, 2 };

 int m = (sizeof(q) / sizeof(q[0])) - 1;

 

 pair<int, int> res = countCamparisions(n, arr, m, q);

 cout << res.first << " " << res.second;

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

import java.util.HashMap;

import java.util.Map;

 

class GFG

{

 

// Function to return the count of 

// comparisons from left to right 

// and right to left in linear 

// search among m queries 

static Pair<Integer, Integer> countCamparisions(int n, 

 int arr[], int m, int qry[]) 

{ 

 int i; 

 HashMap<Integer,Integer> index = new HashMap<>(); 

 for (i = 1; i <= n; i++) 

 { 

 

 // arr[i] occurs at i 

 index.put(arr[i], i); 

 } 

 

 // Count of comparisons for left

 // to right and right to left 

 int ltr = 0, rtl = 0; 

 for (i = 1; i <= m; i++)

 { 

 int x = qry[i]; 

 ltr += index.get(x); 

 rtl += n - index.get(x) + 1; 

 } 

 

 Pair<Integer, Integer> ans = new Pair<>(ltr, rtl);

 return ans; 

}

 

 // Driver Code 

 public static void main(String []args)

 {

 

 // -1 will be ignored as it is 1-based indexing 

 int arr[] = { -1, 2, 4, 5, 1 }; 

 int n = arr.length - 1; 

 

 int q[] = { -1, 4, 2 }; 

 int m = q.length - 1; 

 

 Pair<Integer, Integer> res = countCamparisions(n, arr, m, q); 

 System.out.println(res.first + " " + res.second);

 }

}

 

class Pair<A, B> 

{

 A first;

 B second;

 

 public Pair(A first, B second)

 {

 this.first = first;

 this.second = second;

 }

}

 

// This code is contributed by Rituraj Jain   
  
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

# Python 3 implementation of the

# above approach

 

# Function to return the count of 

# comparisons from left to right 

# and right to left in linear search

# among m queries 

def countCamparisions(n, arr, m, qry) :

 

 index = {}

 for i in range(1, n + 1) :

 

 # arr[i] occurs at i 

 index[arr[i]] = i

 

 # Count of comparisons for left to 

 # right and right to left 

 ltr, rtl = 0, 0

 for i in range(1, m + 1) :

 x = qry[i]

 ltr += index[x] 

 rtl += n - index[x] + 1

 

 return (ltr, rtl) 

 

# Driver Code

if __name__ == "__main__" :

 

 # -1 will be ignored as it 

 # is 1-based indexing 

 arr = [ -1, 2, 4, 5, 1 ] 

 n = len(arr) - 1

 

 q = [ -1, 4, 2 ] 

 m = len(q) - 1

 

 res = countCamparisions(n, arr, m, q) 

 print(res[0], res[1]) 

 

# This code is contributed by Ryuga  
  
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

// comparisons from left to right 

// and right to left in linear 

// search among m queries 

static Pair<int, 

 int> countCamparisions(int n, int []arr, 

 int m, int []qry) 

{ 

 int i; 

 Dictionary<int,

 int> index = new Dictionary<int,

 int>(); 

 for (i = 1; i <= n; i++) 

 { 

 

 // arr[i] occurs at i 

 index.Add(arr[i], i); 

 } 

 

 // Count of comparisons for left

 // to right and right to left 

 int ltr = 0, rtl = 0; 

 for (i = 1; i <= m; i++)

 { 

 int x = qry[i]; 

 ltr += index[x]; 

 rtl += n - index[x] + 1; 

 } 

 

 Pair<int, 

 int> ans = new Pair<int, 

 int>(ltr, rtl);

 return ans; 

}

 

// Driver Code 

public static void Main(String []args)

{

 

 // -1 will be ignored as 

 // it is 1-based indexing 

 int []arr = { -1, 2, 4, 5, 1 }; 

 int n = arr.Length - 1; 

 

 int []q = { -1, 4, 2 }; 

 int m = q.Length - 1; 

 

 Pair<int, int> res = countCamparisions(n, arr, m, q); 

 Console.WriteLine(res.first + " " + res.second);

}

}

 

class Pair<A, B> 

{

 public A first;

 public B second;

 

 public Pair(A first, B second)

 {

 this.first = first;

 this.second = second;

 }

}

 

// This code is contributed by 29AjayKumar  
  
---  
  
 __

 __

 **Output:**

    
    
    3 7
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


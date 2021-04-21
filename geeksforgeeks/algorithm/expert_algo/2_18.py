Queries for number of distinct elements from a given index till last index in
an array



Given a array ‘a[]’ of size n and number of queries q. Each query can be
represented by a integer m. Your task is to print the number of distinct
integers from index m to n i.e till last element of the array.

 **Examples:**

>  **Input:** arr[] = {1, 2, 3, 1, 2, 3, 4, 5}, q[] = {1, 4, 6, 8}  
>  **Output:** 5 5 3 1  
> In query 1, number of distinct integers  
> in a[0…7] is 5 (1, 2, 3, 4, 5)  
> In query 2, number of distinct integers  
> in a[3…7] is 5 (1, 2, 3, 4, 5)  
> In query 3, number of distinct integers  
> in a[5…7] is 3 (3, 4, 5)  
> In query 4, number of distinct integers  
> in a[7…7] is 1 (5)

 **Approach:**

  

  

  * Take an array **check[]** which will check if the current element is earlier visited or not. If already visited mark it as **1** otherwise **0**.
  * Take an array **idx[]** which will store the number of distinct elements from current index till last index.
  * Loop from last, if current element has not been visited, mark its check as **1** , store current counter in **idx** and increment it otherwise simply store current counter in **idx**.

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

#define MAX 100001

 

// Function to perform queries to find

// number of distinct elements from

// a given index till last index in an array

void find_distinct(int a[], int n, int q, int queries[])

{

 int check[MAX] = { 0 };

 int idx[MAX];

 int cnt = 1;

 for (int i = n - 1; i >= 0; i--) {

 // Check if current element

 // already visited or not

 if (check[a[i]] == 0) {

 

 // If not visited store current counter

 // and incremet it and mark check as 1

 idx[i] = cnt;

 check[a[i]] = 1;

 cnt++;

 }

 else {

 

 // Otherwise if visited simply

 // store current counter

 idx[i] = cnt - 1;

 }

 }

 

 // Perform queries

 for (int i = 0; i < q; i++) {

 int m = queries[i];

 cout << idx[m] << " ";

 }

}

 

// Driver code

int main()

{

 int a[] = { 1, 2, 3, 1, 2, 3, 4, 5 };

 int n = sizeof(a) / sizeof(int);

 int queries[] = { 0, 3, 5, 7 };

 int q = sizeof(queries) / sizeof(int);

 find_distinct(a, n, q, queries);

 

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

 

static int MAX =100001; 

 

// Function to perform queries to find 

// number of distinct elements from 

// a given index till last index in an array 

static void find_distinct(int a[], int n, int q, int
queries[]) 

{ 

 int []check = new int[MAX]; 

 int []idx = new int[MAX]; 

 int cnt = 1; 

 for (int i = n - 1; i >= 0; i--) 

 { 

 // Check if current element 

 // already visited or not 

 if (check[a[i]] == 0) 

 { 

 

 // If not visited store current counter 

 // and incremet it and mark check as 1 

 idx[i] = cnt; 

 check[a[i]] = 1; 

 cnt++; 

 } 

 else

 { 

 

 // Otherwise if visited simply 

 // store current counter 

 idx[i] = cnt - 1; 

 } 

 } 

 

 // Perform queries 

 for (int i = 0; i < q; i++)

 { 

 int m = queries[i]; 

 System.out.print(idx[m] + " "); 

 } 

} 

 

// Driver code 

public static void main(String[] args) 

{

 int a[] = { 1, 2, 3, 1, 2, 3, 4, 5 }; 

 int n = a.length; 

 int queries[] = { 0, 3, 5, 7 }; 

 int q = queries.length; 

 find_distinct(a, n, q, queries);

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

# Python implementation of the approach

MAX = 100001;

 

# Function to perform queries to find

# number of distinct elements from

# a given index till last index in an array

def find_distinct(a, n, q, queries):

 check = [0] * MAX;

 idx = [0] * MAX;

 cnt = 1;

 for i in range(n - 1, -1, -1):

 

 # Check if current element

 # already visited or not

 if (check[a[i]] == 0):

 

 # If not visited store current counter

 # and incremet it and mark check as 1

 idx[i] = cnt;

 check[a[i]] = 1;

 cnt += 1;

 else:

 

 # Otherwise if visited simply

 # store current counter

 idx[i] = cnt - 1;

 

 # Perform queries

 for i in range(0, q):

 m = queries[i];

 print(idx[m], end = " ");

 

# Driver code

a = [ 1, 2, 3, 1, 2, 3, 4, 5 ];

n = len(a);

queries = [ 0, 3, 5, 7 ];

q = len(queries);

find_distinct(a, n, q, queries);

 

# This code is contributed by 29AjayKumar  
  
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

 

static int MAX =100001; 

 

// Function to perform queries to find 

// number of distinct elements from 

// a given index till last index in an array 

static void find_distinct(int []a, int n, int q, int
[]queries) 

{ 

 int []check = new int[MAX]; 

 int []idx = new int[MAX]; 

 int cnt = 1; 

 for (int i = n - 1; i >= 0; i--) 

 { 

 // Check if current element 

 // already visited or not 

 if (check[a[i]] == 0) 

 { 

 

 // If not visited store current counter 

 // and incremet it and mark check as 1 

 idx[i] = cnt; 

 check[a[i]] = 1; 

 cnt++; 

 } 

 else

 { 

 

 // Otherwise if visited simply 

 // store current counter 

 idx[i] = cnt - 1; 

 } 

 } 

 

 // Perform queries 

 for (int i = 0; i < q; i++)

 { 

 int m = queries[i]; 

 Console.Write(idx[m] + " "); 

 } 

} 

 

// Driver code 

public static void Main(String[] args) 

{

 int []a = { 1, 2, 3, 1, 2, 3, 4, 5 }; 

 int n = a.Length; 

 int []queries = { 0, 3, 5, 7 }; 

 int q = queries.Length; 

 find_distinct(a, n, q, queries);

}

}

 

/* This code is contributed by PrinciRaj1992 */  
  
---  
  
 __

 __

 **Output:**

    
    
    5 5 3 1
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


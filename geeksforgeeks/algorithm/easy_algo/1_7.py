XOR of a subarray (range of elements) | Set 2



Given an array integer **arr[]** of size **N** and **Q** queries. Each query
is of the form **(L, R)** , where **L** and **R** are indices of the array.
The task is to find XOR value of the subarray **arr[L…R]**.  
 **Examples:**

>  **Input:** arr[] = {2, 5, 1, 6, 1, 2, 5} query[] = {{1, 4}}  
>  **Output:** 3  
> The XOR value of arr[1…4] is 3.
>
>  **Input:** arr[] = {2, 5, 1, 6, 1, 2, 5} query[] = {{0, 6}}  
>  **Output:** 6  
> The XOR value of arr[0…6] is 6.

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **O(N) auxiliary space approach:** Please refer this article for the O(N)
auxiliary space approach.

 **Approach:** Here we will discuss a constant space solution, but we will
modify the input array.

  

  

  1. Update the input array from index **1** to **N – 1** , such that **arr[i]** store the XOR from **arr[0]** to **arr[i]**.  

> arr[i] = XOR(arr[0], arr[1], .., arr[i])

  2. To process a query from **L** to **R** just return **arr[L-1] ^ arr[R]**.

> arr[L-1] = arr[0] ^ arr[1] ^ arr[2]…. ^ arr[L-1]  
> arr[R] = arr[0] ^ arr[1]……arr[L-1] ^ arr[L] ^ arr[L+1]…… ^ arr[R]  
> arr[L-1] ^ arr[R] = arr[L] ^ arr[L+1]…. ^ arr[R]
>
> where ^ denotes XOR

 **For example:**

> Consider the example: arr[] = { 3, 2, 4, 5, 1, 1, 5, 3 }, query[] = {{1, 4
> }, { 3, 7}}  
> After taking XOR of consecutive elements, arr[] = {3, 1, 5, 0, 1, 0, 5, 6}  
> For first query {1, 4} ans = arr[0] ^ arr[4] = 3 ^ 1 = 2  
> For second query {3, 7} ans = arr[2] ^ arr[7] = 5 ^ 6 = 3

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to find XOR

// in a range from L to R

 

#include <bits/stdc++.h>

using namespace std;

 

// Function to find XOR

// in a range from L to R

void find_Xor(int arr[],

 pair<int, int> querry[],

 int N, int Q)

{

 // Compute xor from arr[0] to arr[i]

 for (int i = 1; i < N; i++) {

 arr[i] = arr[i] ^ arr[i - 1];

 }

 

 int ans = 0;

 

 // process every query

 // in constant time

 for (int i = 0; i < Q; i++) {

 

 // if L==0

 if (querry[i].first == 0)

 ans = arr[querry[i].second];

 else

 ans = arr[querry[i].first - 1]

 ^ arr[querry[i].second];

 

 cout << ans << endl;

 }

}

 

// Driver Code

int main()

{

 int arr[] = { 3, 2, 4, 5,

 1, 1, 5, 3 };

 int N = 8;

 int Q = 2;

 pair<int, int> query[Q]

 = { { 1, 4 },

 { 3, 7 } };

 

 // query[]

 find_Xor(arr, query, N, Q);

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

// Java program to find XOR

// in a range from L to R

class GFG{

 

static class pair

{ 

 int first, second; 

 public pair(int first, int second) 

 { 

 this.first = first; 

 this.second = second; 

 } 

} 

 

// Function to find XOR

// in a range from L to R

static void find_Xor(int arr[],

 pair querry[],

 int N, int Q)

{

 

 // Compute xor from arr[0] to arr[i]

 for(int i = 1; i < N; i++)

 {

 arr[i] = arr[i] ^ arr[i - 1];

 }

 

 int ans = 0;

 

 // Process every query

 // in constant time

 for(int i = 0; i < Q; i++)

 {

 

 // If L==0

 if (querry[i].first == 0)

 ans = arr[querry[i].second];

 else

 ans = arr[querry[i].first - 1] ^

 arr[querry[i].second];

 

 System.out.print(ans + "\n");

 }

}

 

// Driver Code

public static void main(String[] args)

{

 int arr[] = { 3, 2, 4, 5,

 1, 1, 5, 3 };

 int N = 8;

 int Q = 2;

 

 pair query[] = { new pair(1, 4),

 new pair(3, 7) };

 

 // query[]

 find_Xor(arr, query, N, Q);

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

# Python3 program to find XOR

# in a range from L to R

 

# Function to find XOR 

# in a range from L to R 

def find_Xor(arr, query, N, Q):

 

 # Compute xor from arr[0] to arr[i]

 for i in range(1, N):

 arr[i] = arr[i] ^ arr[i - 1]

 

 ans = 0

 

 # Process every query 

 # in constant time 

 for i in range(Q):

 

 # If L == 0

 if query[i][0] == 0:

 ans = arr[query[i][1]]

 else:

 ans = (arr[query[i][0] - 1] ^ 

 arr[query[i][1]])

 print(ans)

 

# Driver code

def main():

 

 arr = [ 3, 2, 4, 5, 1, 1, 5, 3 ]

 N = 8

 Q = 2

 

 # query[]

 query = [ [ 1, 4 ],

 [ 3, 7 ] ]

 

 find_Xor(arr, query, N, Q)

 

main()

 

# This code is contributed by Stuti Pathak  
  
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

// C# program to find XOR

// in a range from L to R

using System;

 

class GFG{ 

class pair

{ 

 public int first, second; 

 public pair(int first, int second) 

 { 

 this.first = first; 

 this.second = second; 

 } 

} 

 

// Function to find XOR

// in a range from L to R

static void find_Xor(int []arr,

 pair []querry,

 int N, int Q)

{

 

 // Compute xor from arr[0] to arr[i]

 for(int i = 1; i < N; i++)

 {

 arr[i] = arr[i] ^ arr[i - 1];

 }

 

 int ans = 0;

 

 // Process every query

 // in constant time

 for(int i = 0; i < Q; i++)

 {

 

 // If L==0

 if (querry[i].first == 0)

 ans = arr[querry[i].second];

 else

 ans = arr[querry[i].first - 1] ^

 arr[querry[i].second];

 

 Console.Write(ans + "\n");

 }

}

 

// Driver Code

public static void Main(String[] args)

{

 int []arr = { 3, 2, 4, 5,

 1, 1, 5, 3 };

 int N = 8;

 int Q = 2;

 

 pair []query = { new pair(1, 4),

 new pair(3, 7) };

 

 // query[]

 find_Xor(arr, query, N, Q);

}

}

 

// This code is contributed by 29AjayKumar  
  
---  
  
 __

 __

 **Output:**

    
    
    2
    3
    

_**Time Complexity:** O (N + Q)_  
 _ **Auxiliary Space:** O (1)_

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


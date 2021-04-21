Schedule elevator to reduce the total time taken



Given an integer **k** and an array **arr[]** representing the destination
floors for **N** people waiting currently at the ground floor and **k** is the
capacity of the elevator i.e. maximum number of people it can hold at the same
time. It takes 1 unit time for the elevator to reach any consecutive floor
from the current floor. The task is to schedule the elevator in a way to
minimize the total time taken to get all the people to their destination floor
and then return back to the ground floor.

 **Examples:**

>  **Input:** arr[] = {2, 3, 4}, k = 2  
>  **Output:** 12  
> Second and the third persons (destination floors 3 and 4) shall go in the
> first turn taking 8 (4 + 4) unit time. The only person left will take 2 unit
> time to get to the destination  
> And then the elevator will take another 2 unit time to get back to the
> ground floor.  
> Total time taken = 8 + 2 + 2 = 12
>
>  **Input:** arr[] = {5, 5, 4}, k = 3  
>  **Output:** 10  
> Every person can get on the elevator at the same time  
> Time required will be 10 (5 + 5).

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** Sort the given array in decreasing order of destination. Create
groups of K (starting from the highest floor), the cost for each group will be
**2 * (max(Elements in current group))**. The summation across all groups will
be the answer.

  

  

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

 

// Function to return the minimum time taken

// by the elevator when operating optimally

int minTime(int n, int k, int a[])

{

 // Sort in descending order

 sort(a, a + n, greater<int>());

 int minTime = 0;

 

 // Iterate through the groups

 for (int i = 0; i < n; i += k)

 

 // Update the time taken for each group

 minTime += (2 * a[i]);

 

 // Return the total time taken

 return minTime;

}

 

// Driver code

int main()

{

 int k = 2;

 int arr[] = { 2, 3, 4 };

 int n = sizeof(arr) / sizeof(arr[0]);

 cout << minTime(n, k, arr);

 

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

 

// Function to return the minimum time taken

// by the elevator when operating optimally

static int minTime(int n, int k, int a[])

{

 // Sort in descending order

 int temp;

 for(int i = 0; i < n; i++)

 { 

 for(int j = i + 1; j < n; j++)

 {

 if(a[i] < a[j])

 {

 temp = a[i];

 a[i] = a[j];

 a[j] = temp;

 }

 }

 }

 

 

 int minTime = 0;

 

 // Iterate through the groups

 for (int i = 0; i < n; i += k)

 

 // Update the time taken for each group

 minTime += (2 * a[i]);

 

 // Return the total time taken

 return minTime;

}

 

// Driver code

public static void main(String args[])

{

 int k = 2;

 int arr[] = { 2, 3, 4 };

 int n = arr.length;

 System.out.println(minTime(n, k, arr));

}

}

 

// This code is contributed by

// Surendra_Gangwar  
  
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

 

# Function to return the minimum time taken 

# by the elevator when operating optimally 

def minTime(n, k, a) :

 

 # Sort in descending order 

 a.sort(reverse = True); 

 

 minTime = 0; 

 

 # Iterate through the groups 

 for i in range(0, n, k) :

 

 # Update the time taken for 

 # each group 

 minTime += (2 * a[i]); 

 

 # Return the total time taken 

 return minTime; 

 

# Driver code 

if __name__ == "__main__" :

 

 k = 2; 

 arr = [ 2, 3, 4 ]; 

 n = len(arr) ;

 print(minTime(n, k, arr)); 

 

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

 

class GFG 

{ 

 

// Function to return the minimum time taken 

// by the elevator when operating optimally 

static int minTime(int n, int k, int []a) 

{ 

 // Sort in descending order 

 int temp; 

 for(int i = 0; i < n; i++) 

 { 

 for(int j = i + 1; j < n; j++) 

 { 

 if(a[i] < a[j]) 

 { 

 temp = a[i]; 

 a[i] = a[j]; 

 a[j] = temp; 

 } 

 } 

 } 

 

 

 int minTime = 0; 

 

 // Iterate through the groups 

 for (int i = 0; i < n; i += k) 

 

 // Update the time taken for each group 

 minTime += (2 * a[i]); 

 

 // Return the total time taken 

 return minTime; 

} 

 

// Driver code 

public static void Main(String []args) 

{ 

 int k = 2; 

 int []arr = { 2, 3, 4 }; 

 int n = arr.Length; 

 Console.Write(minTime(n, k, arr)); 

} 

} 

 

// This code is contributed by Arnab Kundu  
  
---  
  
 __

 __

 **Output:**

    
    
    12
    

**Time Complexity:** O(N * log(N))

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


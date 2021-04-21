Make all the array elements odd with minimum operations of given type



Given an array **arr[]** consisting of even integers. At each move, you can
select any even number **X** from the array and divide all the occurrences of
**X** by **2**. The task is to find the minimum number of moves needed so that
all the elements in the array become odd.

 **Examples:**

>  **Input:** arr[] = {40, 6, 40, 20}  
>  **Output:** 4  
> Move 1: Select 40 and divide all the occurrences  
> of 40 by 2 to get {20, 6, 20, 20}  
> Move 2: Select 20 and divide all the occurrences  
> of 20 by 2 to get {10, 6, 10, 10}  
> Move 3: Select 10 and divide all the occurrences  
> of 10 by 2 to get {5, 6, 5, 5}.  
> Move 4: Select 6 and divide it by 2 to get {5, 3, 5, 5}.
>
>  **Input:** arr[] = {2, 4, 16, 8}  
>  **Output:** 4

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** This problem can be solved using greedy approach. At every
move, take the **largest remaining even number** in the array and divide it by
2. The largest is taken because there is a chance that it can become equal to
some other element in the array after it is divided by 2 which minimizes the
total operations.

  

  

Below is the implementation of the above approach:  

## CPP

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

// minimum operations required

int minOperations(int arr[], int n)

{

 

 // Insert all the elements in a set

 set<int> s;

 for (int i = 0; i < n; i++) {

 s.insert(arr[i]);

 }

 

 // To store the number of moves

 int moves = 0;

 

 // While the set is not empty

 while (s.empty() == 0) {

 

 // The last element of the set

 int z = *(s.rbegin());

 

 // If the number is even

 if (z % 2 == 0) {

 moves++;

 s.insert(z / 2);

 }

 

 // Remove the element from the set

 s.erase(z);

 }

 

 return moves;

}

 

// Driver code

int main()

{

 int arr[] = { 40, 6, 40, 20 };

 int n = sizeof(arr) / sizeof(int);

 

 cout << minOperations(arr, n);

 

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

 

class GFG 

{

 // Function to return the count of

 // minimum operations required

 static int minOperations(int arr[], int n)

 {

 

 // Insert all the elements in a set

 TreeSet<Integer> s = new TreeSet<Integer>(); 

 for (int i = 0; i < n; i++)

 {

 s.add(arr[i]);

 }

 

 // To store the number of moves

 int moves = 0;

 

 // While the set is not empty

 while (s.size() != 0)

 {

 

 // The last element of the set

 Integer z = s.last();

 

 // If the number is even

 if (z % 2 == 0) 

 {

 moves++;

 s.add(z / 2);

 }

 

 // Remove the element from the set

 s.remove(z);

 }

 

 return moves;

 }

 

 // Driver code

 public static void main (String[] args)

 {

 int arr[] = { 40, 6, 40, 20 };

 int n = arr.length;

 

 System.out.println(minOperations(arr, n));

 

 }

}

 

// This code is contributed by ApurvaRaj  
  
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

from collections import OrderedDict as mpp

 

# Function to return the count of

# minimum operations required

def minOperations(arr, n):

 

 # Insert all the elements in a set

 s = mpp()

 for i in range(n):

 s[arr[i]] = 1

 

 # To store the number of moves

 moves = 0

 

 # While the set is not empty

 while (len(s) > 0):

 

 # The last element of the set

 z = sorted(list(s.keys()))[-1]

 

 # If the number is even

 if (z % 2 == 0):

 moves += 1

 s[z / 2] = 1

 

 # Remove the element from the set

 del s[z]

 

 return moves

 

# Driver code

 

arr = [40, 6, 40, 20]

n = len(arr)

 

print(minOperations(arr, n))

 

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

// C# implementation of the approach

using System;

using System.Collections.Generic;

 

class GFG 

{ 

 // Function to return the count of 

 // minimum operations required 

 static int minOperations(int []arr, int n) 

 { 

 

 // Insert all the elements in a set 

 SortedSet<int> s = new SortedSet<int>(); 

 for (int i = 0; i < n; i++) 

 { 

 s.Add(arr[i]); 

 } 

 

 // To store the number of moves 

 int moves = 0; 

 

 // While the set is not empty 

 while (s.Count != 0) 

 { 

 

 // The last element of the set 

 int z = s.Max; 

 

 // If the number is even 

 if (z % 2 == 0) 

 { 

 moves++; 

 s.Add(z / 2); 

 } 

 

 // Remove the element from the set 

 s.Remove(z); 

 } 

 

 return moves; 

 } 

 

 // Driver code 

 public static void Main(String[] args) 

 { 

 int []arr = { 40, 6, 40, 20 }; 

 int n = arr.Length; 

 

 Console.WriteLine(minOperations(arr, n)); 

 } 

} 

 

// This code is contributed by 29AjayKumar  
  
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


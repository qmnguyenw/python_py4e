Maximize count of corresponding same elements in given permutations using
cyclic rotations



Given two permutations **P1** and **P2** of numbers from **1 to N** , the task
is to find the maximum count of corresponding same elements in the given
permutations by performing a cyclic left or right shift on **P1**.  
**Examples:**

> **Input:** P1 = [5 4 3 2 1], P2 = [1 2 3 4 5]  
> **Output:** 1  
> **Explanation:**  
> We have a matching pair at index 2 for element 3.  
>  **Input:** P1 = [1 3 5 2 4 6], P2 = [1 5 2 4 3 6]  
> **Output:** 3  
> **Explanation:**  
> Cyclic shift of second permutation towards right would give 6 1 5 2 4 3, and
> we get a match of 5, 2, 4. Hence, the answer is 3 matching pairs.  
>

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Naive Approach:** The naive approach is to check for every possible shift
in both the left and right direction count the number of matching pairs by
looping through all the permutations formed.  
_**Time Complexity:** O(N2) _  
_**Auxiliary Space:** O(1)_  
 **Efficient Approach:** The above naive approach can be optimized. The idea
is for every element to **store the smaller distance** between positions of
this element from the left and right sides in separate arrays. Hence, the
solution to the problem will be calculated as the **maximum frequency** of an
element from the two separated arrays. Below are the steps:

  1. Store the position of all the elements of the permutation **P2** in an array(say **store[]** ).
  2. For each element in the permutation **P1** , do the following: 
    * Find the difference(say **diff** ) between the position of the current element in **P2** with the position in **P1**.
    * If diff is less than 0 then update diff to **(N – diff)**.
    * Store the frequency of current difference diff in a map.
  3. After the above steps, the maximum frequency stored in the map is the maximum number of equal elements after rotation on **P1**.

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

// Function to maximize the matching

// pairs between two permutation

// using left and right rotation

int maximumMatchingPairs(int perm1[],

 int perm2[],

 int n)

{

 // Left array store distance of element

 // from left side and right array store

 // distance of element from right side

 int left[n], right[n];

 // Map to store index of elements

 map<int, int> mp1, mp2;

 for (int i = 0; i < n; i++) {

 mp1[perm1[i]] = i;

 }

 for (int j = 0; j < n; j++) {

 mp2[perm2[j]] = j;

 }

 for (int i = 0; i < n; i++) {

 // idx1 is index of element

 // in first permutation

 // idx2 is index of element

 // in second permutation

 int idx2 = mp2[perm1[i]];

 int idx1 = i;

 if (idx1 == idx2) {

 // If element if present on same

 // index on both permutations then

 // distance is zero

 left[i] = 0;

 right[i] = 0;

 }

 else if (idx1 < idx2) {

 // Calculate distance from left

 // and right side

 left[i] = (n - (idx2 - idx1));

 right[i] = (idx2 - idx1);

 }

 else {

 // Calculate distance from left

 // and right side

 left[i] = (idx1 - idx2);

 right[i] = (n - (idx1 - idx2));

 }

 }

 // Maps to store frequencies of elements

 // present in left and right arrays

 map<int, int> freq1, freq2;

 for (int i = 0; i < n; i++) {

 freq1[left[i]]++;

 freq2[right[i]]++;

 }

 int ans = 0;

 for (int i = 0; i < n; i++) {

 // Find maximum frequency

 ans = max(ans, max(freq1[left[i]],

 freq2[right[i]]));

 }

 // Return the result

 return ans;

}

// Driver Code

int main()

{

 // Given permutations P1 and P2

 int P1[] = { 5, 4, 3, 2, 1 };

 int P2[] = { 1, 2, 3, 4, 5 };

 int n = sizeof(P1) / sizeof(P1[0]);

 // Function Call

 cout << maximumMatchingPairs(P1, P2, n);

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

// Java program for

// the above approach

import java.util.*;

class GFG{

// Function to maximize the matching

// pairs between two permutation

// using left and right rotation

static int maximumMatchingPairs(int perm1[],

 int perm2[],

 int n)

{

 // Left array store distance of element

 // from left side and right array store

 // distance of element from right side

 int []left = new int[n];

 int []right = new int[n];

 // Map to store index of elements

 HashMap<Integer,

 Integer> mp1 = new HashMap<>();

 HashMap<Integer,

 Integer> mp2 = new HashMap<>();

 

 for (int i = 0; i < n; i++)

 {

 mp1.put(perm1[i], i);

 }

 for (int j = 0; j < n; j++)

 {

 mp2.put(perm2[j], j);

 }

 for (int i = 0; i < n; i++)

 {

 // idx1 is index of element

 // in first permutation

 // idx2 is index of element

 // in second permutation

 int idx2 = mp2.get(perm1[i]);

 int idx1 = i;

 if (idx1 == idx2)

 {

 // If element if present on same

 // index on both permutations then

 // distance is zero

 left[i] = 0;

 right[i] = 0;

 }

 else if (idx1 < idx2)

 {

 // Calculate distance from left

 // and right side

 left[i] = (n - (idx2 - idx1));

 right[i] = (idx2 - idx1);

 }

 else

 {

 // Calculate distance from left

 // and right side

 left[i] = (idx1 - idx2);

 right[i] = (n - (idx1 - idx2));

 }

 }

 // Maps to store frequencies of elements

 // present in left and right arrays

 HashMap<Integer,

 Integer> freq1 = new HashMap<>();

 HashMap<Integer,

 Integer> freq2 = new HashMap<>();

 

 for (int i = 0; i < n; i++)

 {

 if(freq1.containsKey(left[i]))

 freq1.put(left[i],

 freq1.get(left[i]) + 1);

 else

 freq1.put(left[i], 1);

 if(freq2.containsKey(right[i]))

 freq2.put(right[i],

 freq2.get(right[i]) + 1);

 else

 freq2.put(right[i], 1);

 }

 int ans = 0;

 for (int i = 0; i < n; i++)

 {

 // Find maximum frequency

 ans = Math.max(ans,

 Math.max(freq1.get(left[i]),

 freq2.get(right[i])));

 }

 // Return the result

 return ans;

}

// Driver Code

public static void main(String[] args)

{

 // Given permutations P1 and P2

 int P1[] = {5, 4, 3, 2, 1};

 int P2[] = {1, 2, 3, 4, 5};

 int n = P1.length;

 // Function Call

 System.out.print(maximumMatchingPairs(P1, P2, n));

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

from collections import defaultdict

# Function to maximize the matching

# pairs between two permutation

# using left and right rotation

def maximumMatchingPairs(perm1, perm2, n):

 # Left array store distance of element

 # from left side and right array store

 # distance of element from right side

 left = [0] * n

 right = [0] * n

 # Map to store index of elements

 mp1 = {}

 mp2 = {}

 for i in range (n):

 mp1[perm1[i]] = i

 

 for j in range (n):

 mp2[perm2[j]] = j

 

 for i in range (n):

 # idx1 is index of element

 # in first permutation

 # idx2 is index of element

 # in second permutation

 idx2 = mp2[perm1[i]]

 idx1 = i

 if (idx1 == idx2):

 # If element if present on same

 # index on both permutations then

 # distance is zero

 left[i] = 0

 right[i] = 0

 

 elif (idx1 < idx2):

 # Calculate distance from left

 # and right side

 left[i] = (n - (idx2 - idx1))

 right[i] = (idx2 - idx1)

 

 else :

 # Calculate distance from left

 # and right side

 left[i] = (idx1 - idx2)

 right[i] = (n - (idx1 - idx2))

 # Maps to store frequencies of elements

 # present in left and right arrays

 freq1 = defaultdict (int)

 freq2 = defaultdict (int)

 for i in range (n):

 freq1[left[i]] += 1

 freq2[right[i]] += 1

 ans = 0

 for i in range( n):

 # Find maximum frequency

 ans = max(ans, max(freq1[left[i]],

 freq2[right[i]]))

 # Return the result

 return ans

# Driver Code

if __name__ == "__main__":

 

 # Given permutations P1 and P2

 P1 = [ 5, 4, 3, 2, 1 ]

 P2 = [ 1, 2, 3, 4, 5 ]

 n = len(P1)

 # Function Call

 print(maximumMatchingPairs(P1, P2, n))

# This code is contributed by chitranayal  
  
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

// C# program for

// the above approach

using System;

using System.Collections.Generic;

class GFG{

 

// Function to maximize the matching

// pairs between two permutation

// using left and right rotation

static int maximumMatchingPairs(int []perm1,

 int []perm2,

 int n)

{

 // Left array store distance of element

 // from left side and right array store

 // distance of element from right side

 int []left = new int[n];

 int []right = new int[n];

 

 // Map to store index of elements

 Dictionary<int,

 int> mp1=new Dictionary<int,

 int>();

 Dictionary<int,

 int> mp2=new Dictionary<int,

 int>();

 

 for (int i = 0; i < n; i++)

 {

 mp1[perm1[i]] = i;

 }

 for (int j = 0; j < n; j++)

 {

 mp2[perm2[j]] = j;

 }

 

 for (int i = 0; i < n; i++)

 {

 // idx1 is index of element

 // in first permutation

 // idx2 is index of element

 // in second permutation

 int idx2 = mp2[perm1[i]];

 int idx1 = i;

 

 if (idx1 == idx2)

 {

 // If element if present on same

 // index on both permutations then

 // distance is zero

 left[i] = 0;

 right[i] = 0;

 }

 else if (idx1 < idx2)

 {

 // Calculate distance from left

 // and right side

 left[i] = (n - (idx2 - idx1));

 right[i] = (idx2 - idx1);

 }

 else

 {

 // Calculate distance from left

 // and right side

 left[i] = (idx1 - idx2);

 right[i] = (n - (idx1 - idx2));

 }

 }

 

 // Maps to store frequencies of elements

 // present in left and right arrays

 Dictionary<int,

 int> freq1=new Dictionary <int,

 int>();

 Dictionary<int,

 int> freq2=new Dictionary <int,

 int>();

 

 for (int i = 0; i < n; i++)

 {

 if(freq1.ContainsKey(left[i]))

 freq1[left[i]]++;

 else

 freq1[left[i]] = 1;

 

 if(freq2.ContainsKey(right[i]))

 freq2[right[i]]++;

 else

 freq2[right[i]] = 1;

 }

 

 int ans = 0;

 

 for (int i = 0; i < n; i++)

 {

 // Find maximum frequency

 ans = Math.Max(ans,

 Math.Max(freq1[left[i]],

 freq2[right[i]]));

 }

 

 // Return the result

 return ans;

}

 

// Driver Code

public static void Main(string[] args)

{

 // Given permutations P1 and P2

 int []P1 = {5, 4, 3, 2, 1};

 int []P2 = {1, 2, 3, 4, 5};

 int n = P1.Length;

 

 // Function Call

 Console.Write(maximumMatchingPairs(P1, P2, n));

}

}

// This code is contributed by Rutvik_56  
  
---  
  
 __

 __

 **Output:**

    
    
    1
    
    
    
    

_**Time Complexity:** O(N) _  
_**Auxiliary Space:** O(N)_

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save


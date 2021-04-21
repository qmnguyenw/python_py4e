Maximum Length Chain of Pairs | Set-2



Given an array of pairs of numbers of size **N**. In every pair, the first
number is always smaller than the second number. A pair (c, d) can follow
another pair (a, b) if b < c. The chain of pairs can be formed in this
fashion. The task is to find the length of the longest chain which can be
formed from a given set of pairs.

 **Examples:**

> **Input:** N = 5, arr={{5, 24}, {39, 60}, {15, 28}, {27, 40}, {50, 90} }  
> **Output:** 3  
> The longest chain that can be formed is of length 3, and the chain is {{5,
> 24}, {27, 40}, {50, 90}}.
>
>  **Input :** N = 2, arr={{5, 10}, {1, 11}}  
> **Output :** 1

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:** A dynamic programming approach for the problem has been
discussed here.  
Idea is to solve the problem using the greedy approach which is the same as
Activity Selection Problem.

  

  

  * Sort all pairs in increasing order of second number of each pair.
  * Select first no as the first pair of chain and set a variable s(say) with the second value of the first pair.
  * Iterate from the second pair to last pair of the array and if the value of the first element of the current pair is greater then previously selected pair then select the current pair and update the value of maximum length and variable s.
  * Return the value of Max length of chain.

Below is the implementation of the above approach.

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation of the above approach

#include <bits/stdc++.h>

using namespace std;

// Structure for storing pairs

// of first and second values.

struct val {

 int first;

 int second;

};

// Comparator function which can compare

// the second element of structure used to

// sort pairs in increasing order of second value.

bool comparator(struct val p1, struct val p2)

{

 return (p1.second < p2.second);

}

// Function for finding max length chain

int maxChainLen(struct val p[], int n)

{

 // Initialize length l = 1

 int l = 1;

 // Sort all pair in increasing order

 // according to second no of pair

 sort(p, p + n, comparator);

 // Pick up the first pair and assign the

 // value of second element fo pair to a

 // temporary variable s

 int s = p[0].second;

 // Iterate from second pair (index of

 // the second pair is 1) to the last pair

 for (int i = 1; i < n; i++) {

 // If first of current pair is greater

 // than previously selected pair then

 // select current pair and update

 // value of l and s

 if (p[i].first > s) {

 l++;

 s = p[i].second;

 }

 }

 // Return maximum length

 return l;

}

// Driver Code

int main()

{

 // Declaration of array of structure

 val p[] = { { 5, 24 }, { 39, 60 },

 { 15, 28 }, { 27, 40 }, { 50, 90 } };

 int n = sizeof(p) / sizeof(p[0]);

 // Fucntion call

 cout << maxChainLen(p, n) << endl;

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

// Java implementation of the above approach

import java.util.*;

// Structure for storing pairs

// of first and second values.

class GFG{

 

// Class for storing pairs

// of first and second values.

static class Pair

{

 int first;

 int second;

 

 Pair(int first, int second)

 {

 this.first = first;

 this.second = second;

 }

};

 

// Function for finding max length chain

static int maxChainLen(Pair p[], int n)

{

 

 // Initialize length l = 1

 int l = 1;

 // Sort all pair in increasing order

 // according to second no of pair

 Arrays.sort(p, new Comparator<Pair>()

 {

 public int compare(Pair a, Pair b)

 {

 return a.second - b.second;

 }

 });

 // Pick up the first pair and assign the

 // value of second element fo pair to a

 // temporary variable s

 int s = p[0].second;

 // Iterate from second pair (index of

 // the second pair is 1) to the last pair

 for(int i = 1; i < n; i++)

 {

 

 // If first of current pair is greater

 // than previously selected pair then

 // select current pair and update

 // value of l and s

 if (p[i].first > s)

 {

 l++;

 s = p[i].second;

 }

 }

 

 // Return maximum length

 return l;

}

// Driver Code

public static void main(String args[])

{

 

 // Declaration of array of structure

 Pair p[] = new Pair[5];

 p[0] = new Pair(5, 24);

 p[1] = new Pair(39, 60);

 p[2] = new Pair(15, 28);

 p[3] = new Pair(27, 40);

 p[4] = new Pair(50, 90);

 

 int n = p.length;

 

 // Fucntion call

 System.out.println(maxChainLen(p, n));

}

}

// This code is contributed by adityapande88  
  
---  
  
 __

 __

 **Output:**

    
    
    3

**Time complexity :** O(N*log(N))  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


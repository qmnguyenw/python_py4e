Longest Increasing Subsequence using Longest Common Subsequence Algorithm



Given an array **arr[]** of **N** integers, the task is to find and print the
Longest Increasing Subsequence.  
 **Examples:**  

> **Input:** arr[] = {12, 34, 1, 5, 40, 80}  
> **Output:** 4  
> {12, 34, 40, 80} and {1, 5, 40, 80} are the  
> longest increasing subsequences.  
>  **Input:** arr[] = {10, 22, 9, 33, 21, 50, 41, 60, 80}  
> **Output:** 6  
>

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

Prerequisite: LCS, LIS  
 **Approach:** The longest increasing subsequence of any sequence is the
subsequence of the sorted sequence of itself. It can be solved using a Dynamic
Programming approach. The approach is the same as the classical LCS problem
but instead of the second sequence, given sequence is taken again in its
sorted form.  
 **Note:** Array should have distinct elements otherwise it might give wrong
result. For example in {1, 1, 1} we know the longest increasing subsequence(a1
< a2 < … ak) is of length 1, but if we try out this example in LIS using LCS
method we would get 3 (because it finds the longest common subsequence).  
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

// Function to return the size of the

// longest increasing subsequence

int LISusingLCS(vector<int>& seq)

{

 int n = seq.size();

 // Create an 2D array of integer

 // for tabulation

 vector<vector<int> > L(n + 1, vector<int>(n + 1));

 // Take the second sequence as the sorted

 // sequence of the given sequence

 vector<int> sortedseq(seq);

 sort(sortedseq.begin(), sortedseq.end());

 // Classical Dynamic Programming algorithm

 // for Longest Common Subsequence

 for (int i = 0; i <= n; i++) {

 for (int j = 0; j <= n; j++) {

 if (i == 0 || j == 0)

 L[i][j] = 0;

 else if (seq[i - 1] == sortedseq[j - 1])

 L[i][j] = L[i - 1][j - 1] + 1;

 else

 L[i][j] = max(L[i - 1][j], L[i][j - 1]);

 }

 }

 // Return the ans

 return L[n][n];

}

// Driver code

int main()

{

 vector<int> sequence{ 12, 34, 1, 5, 40, 80 };

 cout << LISusingLCS(sequence) << endl;

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

//Java implementation of above approach

import java.util.*;

class GFG

{

 

// Function to return the size of the

// longest increasing subsequence

static int LISusingLCS(Vector<Integer> seq)

{

 int n = seq.size();

 // Create an 2D array of integer

 // for tabulation

 int L[][] = new int [n + 1][n + 1];

 // Take the second sequence as the sorted

 // sequence of the given sequence

 Vector<Integer> sortedseq = new Vector<Integer>(seq);

 Collections.sort(sortedseq);

 // Classical Dynamic Programming algorithm

 // for Longest Common Subsequence

 for (int i = 0; i <= n; i++)

 {

 for (int j = 0; j <= n; j++)

 {

 if (i == 0 || j == 0)

 L[i][j] = 0;

 else if (seq.get(i - 1) == sortedseq.get(j - 1))

 L[i][j] = L[i - 1][j - 1] + 1;

 else

 L[i][j] = Math.max(L[i - 1][j],

 L[i][j - 1]);

 }

 }

 // Return the ans

 return L[n][n];

}

// Driver code

public static void main(String args[])

{

 Vector<Integer> sequence = new Vector<Integer>();

 sequence.add(12);

 sequence.add(34);

 sequence.add(1);

 sequence.add(5);

 sequence.add(40);

 sequence.add(80);

 System.out.println(LISusingLCS(sequence));

}

}

// This code is contributed by Arnab Kundu  
  
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

# Function to return the size of the

# longest increasing subsequence

def LISusingLCS(seq):

 n = len(seq)

 # Create an 2D array of integer

 # for tabulation

 L = [[0 for i in range(n + 1)]

 for i in range(n + 1)]

 

 # Take the second sequence as the sorted

 # sequence of the given sequence

 sortedseq = sorted(seq)

 # Classical Dynamic Programming algorithm

 # for Longest Common Subsequence

 for i in range(n + 1):

 for j in range(n + 1):

 if (i == 0 or j == 0):

 L[i][j] = 0

 elif (seq[i - 1] == sortedseq[j - 1]):

 L[i][j] = L[i - 1][j - 1] + 1

 else:

 L[i][j] = max(L[i - 1][j],

 L[i][j - 1])

 # Return the ans

 return L[n][n]

# Driver code

sequence = [12, 34, 1, 5, 40, 80]

print(LISusingLCS(sequence))

# This code is contributed by mohit kumar  
  
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

// C# implementation of above approach

using System;

using System.Collections.Generic;

class GFG

{

 

// Function to return the size of the

// longest increasing subsequence

static int LISusingLCS(List<int> seq)

{

 int n = seq.Count;

 // Create an 2D array of integer

 // for tabulation

 int [,]L = new int [n + 1, n + 1];

 // Take the second sequence as the sorted

 // sequence of the given sequence

 List<int> sortedseq = new List<int>(seq);

 sortedseq.Sort();

 // Classical Dynamic Programming algorithm

 // for longest Common Subsequence

 for (int i = 0; i <= n; i++)

 {

 for (int j = 0; j <= n; j++)

 {

 if (i == 0 || j == 0)

 L[i, j] = 0;

 else if (seq[i - 1] == sortedseq[j - 1])

 L[i, j] = L[i - 1, j - 1] + 1;

 else

 L[i,j] = Math.Max(L[i - 1, j],

 L[i, j - 1]);

 }

 }

 // Return the ans

 return L[n, n];

}

// Driver code

public static void Main(String []args)

{

 List<int> sequence = new List<int>();

 sequence.Add(12);

 sequence.Add(34);

 sequence.Add(1);

 sequence.Add(5);

 sequence.Add(40);

 sequence.Add(80);

 Console.WriteLine(LISusingLCS(sequence));

}

}

// This code is contributed by 29AjayKumar  
  
---  
  
 __

 __

 **Output:**

    
    
    4
    
    

**Time Complexity:** O(n2) where n is the length of the sequence.  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save


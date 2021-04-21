Queries for number of distinct integers in Suffix



Given an array of **N** elements and **Q** queries, where each query contains
an integer **K**. For each query, the task is to find the number of distinct
integers in the suffix from **K th** element to **N th** element.

 **Examples:**

    
    
    **Input :**
    N=5, Q=3
    arr[] = {2, 4, 6, 10, 2}
    1
    3
    2
    **Output :**
    4
    3
    4
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:**  
The problem can be solved by precomputing the solution for all index from
**N-1** to **0**. The idea is to use an unordered_set in C++ as set does not
allows duplicate elements.

Traverse the array from end and add the current element into a set and the
answer for the current index would be the size of the set. So, store the size
of set at current index in an auxiliary array say suffixCount.

Below is the implementation of the above approach:  

## C++

  

  

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to find distinct

// elements in suffix

 

#include <bits/stdc++.h>

using namespace std;

 

// Function to answer queries for distinct

// count in Suffix

void printQueries(int n, int a[], int q, int qry[])

{

 // Set to keep the distinct elements

 unordered_set<int> occ;

 

 int suffixCount[n + 1];

 

 // Precompute the answer for each suffix

 for (int i = n - 1; i >= 0; i--) {

 occ.insert(a[i]);

 suffixCount[i + 1] = occ.size();

 }

 

 // Print the precomputed answers

 for (int i = 0; i < q; i++)

 cout << suffixCount[qry[i]] << endl;

}

 

// Driver Code

int main()

{

 int n = 5, q = 3;

 int a[n] = { 2, 4, 6, 10, 2 };

 int qry[q] = { 1, 3, 2 };

 

 printQueries(n, a, q, qry);

 

 return 0;

}  
  
---  
  
 __

 __


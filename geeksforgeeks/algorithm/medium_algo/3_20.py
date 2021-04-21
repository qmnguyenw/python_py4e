Minimum concatenation required to get strictly LIS for the given array



Given an **array A[]** of size n where there are only unique elements in the
array. We have to find the minimum concatenation required for sequence A to
get strictly Longest Increasing Subsequence. For array A[] we follow 1 based
indexing.

 **Examples:**

>  **Input:** A = {1, 3, 2}  
> **Output:** 2  
> **Explanation:**  
> We can concatenate A two times as [1, 3, 2, 1, 3, 2] and then output for
> index 1, 3, 5 which gives sub-sequence as 1->2->3.  
>  **Input:** A = {2, 1, 4, 3, 5}  
> **Output:** 3  
> **Explanation:**  
> The given array has to be concatenated 3 times to generate the Longest
> Increasing Subsequence.

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:**  
To solve the problem mentioned above the very first observation is that a
strictly increasing sub-sequence will always have its length equal to the
number of unique elements present in sequence A[]. Hence, we have to figure
out a way to keep the maximum consecutive numbers in order are together. We
can achieve this by taking as many strictly consecutive numbers in a sequence
before opting for concatenation and handle others in the next concatenation.

  * Form pairs of elements and its index and store them in sorted order as per value. Initialize a variable to count the required concatenation operations.
  * Run a loop from index 2 to n and if index of pair[i-1] > pair[i] then increment the variable by 1 which was counting the required concatenation operations, otherwise continue the process.

Below is the implementation of the above approach:

  

  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// CPP implementation to Find the minimum

// concatenation required to get strictly

// Longest Increasing Subsequence for the

// given array

#include <bits/stdc++.h>

using namespace std;

int increasingSubseq(int a[], int n)

{

 // Ordered map containing pairs

 // of value and index.

 map<int, int> mp;

 for (int i = 0; i < n; i++) {

 // Form pairs of value at index i

 // and it's index that is i.

 mp.insert(make_pair(a[i], i));

 }

 // Variable to insert the minimum

 // concatenations that are needed

 int ans = 1;

 // Iterator pointing to the

 // second pair in the map

 auto itr = ++mp.begin();

 // Iterator pointing to the

 // first pair in the map

 for (auto it = mp.begin(); it != mp.end(); ++it) {

 // Check if itr tends to end of map

 if (itr != mp.end()) {

 // Check if index2 is not greater than index1

 // then we have to perform a concatenation.

 if (itr->second <= it->second)

 ans += 1;

 ++itr;

 }

 }

 // Return the final answer

 cout << ans << endl;

}

// Driver code

int main()

{

 int a[] = { 2, 1, 4, 3, 5 };

 int n = sizeof(a) / sizeof(a[0]);

 increasingSubseq(a, n);

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

/*package whatever //do not write package name here */

import java.util.*;

import java.io.*;

class GFG {

 private static void increasingSubseq(int a[], int n)

 {

 // Ordered map containing pairs

 // of value and index.

 TreeMap<Integer, Integer> mp

 = new TreeMap<Integer, Integer>();

 for (int i = 0; i < n; i++) {

 // Form pairs of value at index i

 // and it's index that is i.

 mp.put(a[i], i);

 }

 // Variable to insert the minimum

 // concatenations that are needed

 int ans = 1;

 // Iterator pointing to the

 // first entry in the map

 Map.Entry<Integer, Integer> itr

 = mp.pollFirstEntry();

 for (Map.Entry<Integer, Integer> it :

 mp.entrySet())

 {

 // Check if index2 is not greater than index1

 // then we have to perform a concatenation.

 if (itr.getValue() >= it.getValue())

 ans++;

 itr = it;

 }

 System.out.println(ans);

 }

 // Driver Code

 public static void main(String[] args)

 {

 int a[] = { 2, 1, 4, 3, 5 };

 int n = a.length;

 increasingSubseq(a, n);

 }

}  
  
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

# Python 3 implementation to

# Find the minimum concatenation

# required to get strictly Longest

# Increasing Subsequence for the

# given array

def increasingSubseq(a, n):

 

 # Ordered map containing pairs

 # of value and index.

 mp = {}

 for i in range(n):

 # Form pairs of value at

 # index i and it's index

 # that is i.

 mp[a[i]] = i

 # Variable to insert the

 # minimum concatenations

 # that are needed

 ans = 1

 # Iterator pointing to the

 # second pair in the map

 itr = 1

 li= list(mp.values())

 # Iterator pointing to the

 # first pair in the map

 for key, value in mp.items():

 

 # Check if itr tends to

 # end of map

 if (itr < len(mp)):

 

 # Check if index2 is not

 # greater than index1

 # then we have to perform

 # a concatenation.

 if (li[itr] <= key):

 ans += 1

 

 itr+=1

 # Return the final

 # answer

 

 print(ans)

# Driver code

if __name__ == '__main__':

 

 a = [2, 1, 4, 3, 5]

 n = len(a)

 increasingSubseq(a, n)

# This code is contributed by bgangwar59  
  
---  
  
 __

 __

 **Output**

    
    
    3
    
    

**Time complexity:** O(N * log N)

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


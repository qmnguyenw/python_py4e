Minimum concatenation required to get strictly LIS for array with repetitive
elements | Set-2



Given an **array A[]** of size n where there can be repetitive elements in the
array. We have to find the minimum concatenation required for sequence A to
get strictly The Longest Increasing Subsequence. For array A[] we follow 1
based indexing.

 **Examples:**

>  **Input:** A = {2, 1, 2, 4, 3, 5}  
> **Output:** 2  
> **Explanation:**  
> We can concatenate A two times as [2, 1, 2, 4, 3, 5, 2, 1, 2, 4, 3, 5] and
> then output for index 2, 3, 5, 10, 12 which gives sub-sequence as 1 -> 2 ->
> 3 -> 4 -> 5.
>
>  **Input:** A = {1, 3, 2, 1, 2}  
> **Output:** 2  
> **Explanation:**  
> We can concatenate A two times as [1, 3, 2, 1, 2, 1, 3, 2, 1, 2] and then
> output for index 1, 3, 7 which gives sub-sequence as 1 -> 2 -> 3\.

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:**  
To solve the problem mentioned above the very first observation is that a
strictly increasing sub-sequence will always have its length equal to the
number of unique elements present in sequence A[]. Hence, the maximum length
of the subsequence is equal to the count of the distinct elements. To solve
the problem follow the steps given below:

  

  

  * Initialize a variable let’s say _ans_ to 1 and partition the sequence in two halves the left subsequence and the right one. Initialize the leftSeq to NULL and copy the original sequence in the rightSeq.
  * Traverse in the right subsequence to **find the minimum element** , represented by variable _CurrElement_ and store its index.
  * Now **update the left and right subsequence** , where the leftSeq is updated with the given sequence up to the index which stores the minimum element in the right subsequence. And the rightSeq to given sequence from the minimum index value until the end.
  * Traverse the array to get the next minimum element and update the value for CurrElement. If no such minimum value is there in rightSeq then it has to be in leftSeq. Find the index of that element in the left subsequence and store its index.
  * Now **again update the value for left and right subsequence** where leftSeq = given sequence up to kth index and rightSeq = given sequence from kth index to end. Repeat the process until the array limit is reached.
  * Increment the value for **ans** by 1 and stop when CurrElement is equal to the highest element.

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation to Find the minimum

// concatenation required to get strictly

// Longest Increasing Subsequence for the

// given array with repetitive elements

#include <bits/stdc++.h>

using namespace std;

int LIS(int arr[], int n)

{

 // ordered map containing value and

 // a vector containing index of

 // it's occurrences

 map<int, vector<int> > m;

 // Mapping index with their values

 // in ordered map

 for (int i = 0; i < n; i++)

 m[arr[i]].push_back(i);

 // k refers to present minimum index

 int k = n;

 // Stores the number of concatenation

 // required

 int ans = 0;

 // Iterate over map m

 for (auto it = m.begin(); it != m.end();

 it++) {

 // it.second refers to the vector

 // containing all corresponding

 // indexes

 // it.second.back refers to the

 // last element of corresponding vector

 if (it->second.back() < k) {

 k = it->second[0];

 ans += 1;

 }

 else

 // find the index of next minimum

 // element in the sequence

 k = *lower_bound(it->second.begin(),

 it->second.end(), k);

 }

 // Return the final answer

 cout << ans << endl;

}

// Driver program

int main()

{

 int arr[] = { 1, 3, 2, 1, 2 };

 int n = sizeof(arr) / sizeof(arr[0]);

 LIS(arr, n);

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

// Java implementation to Find the minimum

// concatenation required to get strictly

// Longest Increasing Subsequence for the

// given array with repetitive elements

import java.io.*;

import java.util.*;

class GFG{

static void LIS(int arr[], int n)

{

 

 // ordered map containing value and

 // a vector containing index of

 // it's occurrences

 TreeMap<Integer,

 List<Integer>> m = new TreeMap<Integer,

 List<Integer>>();

 

 // Mapping index with their values

 // in ordered map

 for(int i = 0; i < n; i++)

 {

 List<Integer> indexes;

 

 if (m.containsKey(arr[i]))

 {

 indexes = m.get(arr[i]);

 }

 else

 {

 indexes = new ArrayList<Integer>();

 }

 indexes.add(i);

 m.put(arr[i], indexes);

 }

 

 // k refers to present minimum index

 int k = n;

 // Stores the number of concatenation

 // required

 int ans = 0;

 // Iterate over map m

 for(Map.Entry<Integer,

 List<Integer>> it : m.entrySet())

 {

 

 // List containing all corresponding

 // indexes

 List<Integer> indexes = it.getValue();

 if (indexes.get(indexes.size() - 1) < k)

 {

 k = indexes.get(0);

 ans++;

 }

 else

 

 // Find the index of next minimum

 // element in the sequence

 k = lower_bound(indexes, k);

 }

 

 // Return the final answer

 System.out.println(ans);

}

static int lower_bound(List<Integer> indexes,

 int k)

{

 int low = 0, high = indexes.size() - 1;

 while (low < high)

 {

 int mid = (low + high) / 2;

 if (indexes.get(mid) < k)

 low = mid + 1;

 else

 high = mid;

 }

 return indexes.get(low);

}

// Driver code

public static void main(String[] args)

{

 int arr[] = { 1, 3, 2, 1, 2 };

 int n = arr.length;

 LIS(arr, n);

}

}

// This code is contributed by jithin  
  
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

# Python3 implementation to

# Find the minimum concatenation

# required to get strictly Longest

# Increasing Subsequence for the

# given array with repetitive elements

from bisect import bisect_left

def LIS(arr, n):

 

 # ordered map containing

 # value and a vector containing

 # index of it's occurrences

 # <int, vector<int> > m;

 m = {}

 # Mapping index with their

 # values in ordered map

 for i in range(n):

 m[arr[i]] = m.get(arr[i], [])

 m[arr[i]].append(i)

 # k refers to present

 # minimum index

 k = n

 # Stores the number of

 # concatenation required

 ans = 1

 # Iterate over map m

 for key, value in m.items():

 

 # it.second refers to the

 # vector containing all

 # corresponding indexes

 # it.second.back refers

 # to the last element of

 # corresponding vector

 if (value[len(value) - 1] < k):

 k = value[0]

 ans += 1

 else:

 

 # find the index of next

 # minimum element in the

 # sequence

 k = bisect_left(value, k)

 # Return the final

 # answer

 print(ans)

# Driver code

if __name__ == '__main__':

 

 arr = [1, 3, 2, 1, 2]

 n = len(arr)

 LIS(arr, n)

# This code is contributed by bgangwar59  
  
---  
  
 __

 __

 **Output:**

    
    
    2
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

**Time complexity:** O(n * log n)

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


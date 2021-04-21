Number of times the given string occurs in the array in the range [l, r]



Given an array of strings **arr[]** and two integers **l** and **r** , the
task is to find the number of times the given string **str** occurs in the
array in the range **[l, r]** (1-based indexing). **Note** that the strings
contain only lowercase letters.

 **Examples:**

>  **Input:** arr[] = {“abc”, “def”, “abc”}, L = 1, R = 2, str = “abc”  
>  **Output:** 1
>
>  **Input:** arr[] = {“abc”, “def”, “abc”}, L = 1, R = 3, str = “ghf”  
>  **Output:** 0

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** The idea is to use an unordered_map to store the indices in
which the ith string of array occurs. If the given string is not present in
the map then answer is zero otherwise perform binary search on the indices of
the given string present in the map, and find the number of occurrences of the
string in the range [L, R].

  

  

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

 

// Function to return the number of occurrences of

int NumOccurrences(string arr[], int n, string str, int L, int
R)

{

 // To store the indices of strings in the array

 unordered_map<string, vector<int> > M;

 for (int i = 0; i < n; i++) {

 string temp = arr[i];

 auto it = M.find(temp);

 

 // If current string doesn't

 // have an entry in the map

 // then create the entry

 if (it == M.end()) {

 vector<int> A;

 A.push_back(i + 1);

 M.insert(make_pair(temp, A));

 }

 else {

 it->second.push_back(i + 1);

 }

 }

 

 auto it = M.find(str);

 

 // If the given string is not

 // present in the array

 if (it == M.end())

 return 0;

 

 // If the given string is present

 // in the array

 vector<int> A = it->second;

 int y = upper_bound(A.begin(), A.end(), R) - A.begin();

 int x = upper_bound(A.begin(), A.end(), L - 1) - A.begin();

 

 return (y - x);

}

 

// Driver code

int main()

{

 string arr[] = { "abc", "abcabc", "abc" };

 int n = sizeof(arr) / sizeof(string);

 int L = 1;

 int R = 3;

 string str = "abc";

 

 cout << NumOccurrences(arr, n, str, L, R);

 

 return 0;

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

# Python implementation of the approach

from bisect import bisect_right as upper_bound

from collections import defaultdict

 

# Function to return the number of occurrences of

def numOccurences(arr: list, n: int, string: str, L: int,
R: int) -> int:

 

 # To store the indices of strings in the array

 M = defaultdict(lambda: list)

 for i in range(n):

 temp = arr[i]

 

 # If current string doesn't

 # have an entry in the map

 # then create the entry

 if temp not in M:

 A = []

 A.append(i + 1)

 M[temp] = A

 else:

 M[temp].append(i + 1)

 

 # If the given string is not

 # present in the array

 if string not in M:

 return 0

 

 # If the given string is present

 # in the array

 A = M[string]

 y = upper_bound(A, R)

 x = upper_bound(A, L - 1)

 

 return (y - x)

 

# Driver Code

if __name__ == "__main__":

 arr = ["abc", "abcabc", "abc"]

 n = len(arr)

 L = 1

 R = 3

 string = "abc"

 

 print(numOccurences(arr, n, string, L, R))

 

# This code is contributed by

# sanjeev2552  
  
---  
  
 __

 __

 **Output:**

    
    
    2
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


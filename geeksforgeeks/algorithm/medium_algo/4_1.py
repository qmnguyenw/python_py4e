Minimum number of Water to Land conversion to make two islands connected in a
Grid



Given a 2D grid **arr[][]** of **‘W’** and **‘L’** where **‘W’** denotes water
and **‘L’** denotes land, the task is to find the minimum number of water
components **‘W’** that must be changed to land component **‘L’** so that two
islands becomes connected.

> An **island** is the set of connected **‘L’** s.

**Note:** There can be only two disjoint islands.

 **Examples:**

> **Input:** arr[][] = {{‘W’, ‘L’}, {‘L’, ‘W’}};  
> **Output:** 1  
> **Explanation:**  
> For the given set of islands if we change arr[1][1] to ‘W’ then, set of all
> island are connected.  
> Therefore, the minimum number of ‘W’ must be changed to ‘L’ is 1.
>
>  
>
>
>  
>
>
>  **Input:** arr[][] = {{‘W’, ‘L’, ‘W’}, {‘W’, ‘W’, ‘W’}, {‘W’, ‘W’, ‘L’}}  
> **Output:** 2

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:** This problem can be solved using Floodfill algorithm. Below are
the steps:

  1. Use Floodfill algorithm for the first set of the connected islands and make all the islands as visited and store the coordinates in a hash (say **hash1** ).
  2. Use Floodfill algorithm for the second set of the connected islands and make all the islands as visited and store the coordinates in a second hash(say **hash2** ).
  3. The minimum difference between coordinates stored in both the hash is the required result.

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

// Determine the distance between two

// coordinates

int dist(pair<int, int>& p1,

 pair<int, int>& p2)

{

 return abs(p1.first - p2.first)

 + abs(p2.second - p1.second) - 1;

}

// Function to implement floodfill algorithm

void floodfill(set<pair<int, int> >& hash,

 int i, int j,

 vector<vector<char> >& A)

{

 // Base Case

 if (i < 0 || i >= A.size() || j < 0

 || j >= A[0].size() || A[i][j] != 'L') {

 return;

 }

 // Mark the current node visited

 A[i][j] = 'V';

 // Store the coordinates of in the

 // hash set

 hash.insert(make_pair(i, j));

 // Recursively iterate for the next

 // four directions

 floodfill(hash, i - 1, j, A);

 floodfill(hash, i + 1, j, A);

 floodfill(hash, i, j - 1, A);

 floodfill(hash, i, j + 1, A);

}

// Funtion to find the minimum 'W' to flipped

void findMinimumW(vector<vector<char> >& A)

{

 // Base Case

 if (A.size() == 0)

 return;

 // Two sets to store the coordinates of

 // connected island

 set<pair<int, int> > hash1, hash2;

 // Traversing the given grid[][]

 for (int i = 0; i < A.size(); i++) {

 for (int j = 0; j < A[0].size(); j++) {

 // If an island is found

 if (A[i][j] == 'L') {

 // Floodfill Algorithm for

 // the first island

 if (hash1.empty()) {

 floodfill(hash1, i, j, A);

 }

 // Floodfill Algorithm for

 // the second island

 if (hash2.empty()

 && !hash1.count({ i, j })) {

 floodfill(hash2, i, j, A);

 }

 }

 }

 }

 // To store the minimum count of 'W'

 int ans = INT_MAX;

 // Traverse both pairs of hashes

 for (auto i : hash1) {

 for (auto j : hash2) {

 ans = min(ans, dist(i, j));

 }

 }

 // Print the final answer

 cout << ans << endl;

}

// Driver Code

int main()

{

 // Given grid of land and water

 vector<vector<char> > arr;

 arr = { { 'W', 'L' }, { 'L', 'W' } };

 // Function Call

 findMinimumW(arr);

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

# Python3 program for the above approach

import sys

# Determine the distance between two

# coordinates

def dist(p1, p2):

 

 return (abs(p1[0] - p2[0]) +

 abs(p2[1] - p1[1]) - 1)

# Function to implement floodfill algorithm

def floodfill(hash, i, j, A):

 

 # Base Case

 if (i < 0 or i >= len(A) or j < 0 or

 j >= len(A[0]) or A[i][j] != 'L'):

 return hash, A

 

 # Mark the current node visited

 A[i][j] = 'V'

 

 # Store the coordinates of in the

 # hash set

 hash.add((i, j))

 

 # Recursively iterate for the next

 # four directions

 hash, A = floodfill(hash, i - 1, j, A)

 hash, A = floodfill(hash, i + 1, j, A)

 hash, A = floodfill(hash, i, j - 1, A)

 hash, A = floodfill(hash, i, j + 1, A)

 return hash, A

# Funtion to find the minimum 'W' to flipped

def findMinimumW(A):

 

 # Base Case

 if (len(A) == 0):

 return set(), A

 

 # Two sets to store the coordinates of

 # connected island

 hash1 = set()

 hash2 = set()

 

 # Traversing the given grid[][]

 for i in range(len(A)):

 for j in range(len(A[0])):

 

 # If an island is found

 if (A[i][j] == 'L'):

 

 # Floodfill Algorithm for

 # the first island

 if (len(hash1) == 0):

 hash1, A = floodfill(hash1, i, j, A)

 

 # Floodfill Algorithm for

 # the second island

 if (len(hash2) == 0 and

 (i, j) not in hash1):

 hash2, A = floodfill(hash2, i, j, A)

 

 # To store the minimum count of 'W'

 ans = sys.maxsize

 

 # Traverse both pairs of hashes

 for i in hash1:

 for j in hash2:

 ans = min(ans, dist(i, j))

 

 # Print the final answer

 print(ans)

 

# Driver Code

if __name__=='__main__':

 

 # Given grid of land and water

 arr = []

 arr = [ [ 'W', 'L' ], [ 'L', 'W' ] ]

 

 # Function Call

 findMinimumW(arr)

# This code is contributed by pratham76  
  
---  
  
 __

 __

 **Output:**

    
    
    1

_**Time Complexity:** O(N2) _  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


Divide N segments into two non-empty groups such that given condition is
satisfied



Given **N** segments (or ranges) represented by two non-negative integers
**L** and **R**. Divide these segments into two non-empty groups such that
there are no two segments from different groups that share a common point. If
if it is possible to do so, assign each segment a number from the set **{1,
2}** otherwise print **Not Possible**.

 **Examples:**

>  **Input:** arr[][] = {{5, 5}, {2, 3}, {3, 4}}  
>  **Output:** 2 1 1  
> Since 2nd and 3rd segment have one point common i.e. 3, they should be
> contained in same group.
>
>  **Input:** arr[][] = {{3, 5}, {2, 3}, {1, 4}}  
>  **Output:** Not Possible  
> All segments should be contained in the same group since every pair has a
> common point with each other. Since the other group is empty, answer is not
> possbile.

 **Prerequisites** : Merge Overlapping Intervals

  

  

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** Using the concept of merging overlapping intervals, we can
assign the same group to all those segments that are overlapping and
alternatively changing the group number.  
To merge overlapping segments, sort all the segments with respect to their
right indexes keeping in order of the original indexes of the segments. Then,
iterate over the segments and check if the previous segment is overlapping
with the current segment. If it does then merge it making it one segment and
if it doesn’t create a new one.  
At last, check if one of the group is empty of not. If one of them is empty,
answer is not possible, otherwise print all the assigned values of segments.

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// CPP Program to divide N segments into

// two non empty groups such that given

// condition is satisfied

#include <bits/stdc++.h>

using namespace std;

 

// Structure to hold the elements of

// a segment

struct segment {

 

 // left index

 int l;

 

 // right index

 int r;

 

 // index of the segment

 int idx;

};

 

// Comparator function to sort the segments

// according to the right indexes

bool comp(const segment& a, const segment& b)

{

 if (a.r == b.r)

 return a.idx < b.idx;

 return a.r < b.r;

}

 

// Function to print the answer if it exists

// using the concept of merge overlapping segments

void printAnswer(vector<pair<int, int> > v, int n)

{

 segment seg[n];

 

 // Assigning values from the vector v

 for (int i = 0; i < n; i++) {

 seg[i].l = v[i].first;

 seg[i].r = v[i].second;

 seg[i].idx = i;

 }

 

 // Sort the array of segments

 // according to right indexes

 sort(seg, seg + n, comp);

 

 // Resultant array

 int res[n];

 memset(res, 0, sizeof(res));

 

 // Let's denote first group with 0 and second

 // group with 1

 // Current segment

 int prev = 0;

 

 // Assigning group 1 to first segment

 res[seg[prev].idx] = 0;

 for (int i = 1; i < n; i++) {

 

 // If the current segment overlaps

 // with the previous segment, merge it

 if (seg[i].l <= seg[prev].r) {

 

 // Assigning same group value

 res[seg[i].idx] = res[seg[prev].idx];

 seg[prev].r = max(seg[prev].r, seg[i].r);

 }

 else {

 

 // Change group number and create

 // new segment

 res[seg[i].idx] = res[seg[prev].idx] ^ 1;

 ++prev;

 seg[prev] = seg[i];

 }

 }

 

 // Check if one of the groups is empty or not

 int one = 0, two = 0;

 for (int i = 0; i < n; i++) {

 if (!res[i])

 one++;

 else

 two++;

 }

 

 // If both groups are non-empty

 if (one && two) {

 for (int i = 0; i < n; i++)

 cout << res[i] + 1 << " ";

 cout << endl;

 }

 else

 cout << "Not Possible" << endl;

}

 

// Driver Code

int main()

{

 vector<pair<int, int> > v = { { 1, 2 }, { 3, 4 }, { 5, 6 } };

 int n = v.size();

 printAnswer(v, n);

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

# Python3 Program to divide N segments

# into two non empty groups such that 

# given condition is satisfied 

 

# Structure to hold the elements of 

# a segment 

class segment: 

 

 def __init__(self):

 self.l = None # left index

 self.r = None # right index

 self.idx = None # index of the segment

 

# Function to print the answer if

# it exists using the concept of

# merge overlapping segments 

def printAnswer(v, n): 

 

 seg = [segment() for i in range(n)] 

 

 # Assigning values from the vector v 

 for i in range(0, n): 

 seg[i].l = v[i][0] 

 seg[i].r = v[i][1] 

 seg[i].idx = i 

 

 # Sort the array of segments 

 # according to right indexes 

 seg.sort(key = lambda x: (x.r, x.idx))

 

 # Resultant array 

 res = [0] * (n) 

 

 # Let's denote first group with 0 and

 # second group with 1 Current segment 

 prev = 0

 

 # Assigning group 1 to first segment 

 res[seg[prev].idx] = 0

 for i in range(1, n): 

 

 # If the current segment overlaps 

 # with the previous segment, merge it 

 if seg[i].l <= seg[prev].r: 

 

 # Assigning same group value 

 res[seg[i].idx] = res[seg[prev].idx] 

 seg[prev].r = max(seg[prev].r, seg[i].r) 

 

 else:

 

 # Change group number and create 

 # new segment 

 res[seg[i].idx] = res[seg[prev].idx] ^ 1

 prev += 1

 seg[prev] = seg[i] 

 

 # Check if one of the groups is 

 # empty or not 

 one, two = 0, 0

 for i in range(0, n): 

 if not res[i]:

 one += 1

 else:

 two += 1

 

 # If both groups are non-empty 

 if one and two: 

 for i in range(0, n): 

 print(res[i] + 1, end = " ") 

 print() 

 

 else:

 print("Not Possible") 

 

# Driver Code 

if __name__ == "__main__":

 

 v = [[1, 2], [3, 4], [5, 6]] 

 n = len(v) 

 printAnswer(v, n) 

 

# This code is contributed 

# by Rituraj Jain  
  
---  
  
 __

 __

 **Output:**

    
    
    1 2 1
    

**Time Complexity:** O(n * log n), where n is the number of segments

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


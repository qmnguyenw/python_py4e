Find least non-overlapping number from a given set of intervals



Given an array **interval** of pairs of integers representing the starting and
ending points of the interval of size **N**. The task is to find the smallest
non-negative integer which is a non-overlapping number from the given set of
intervals.  
**Input constraints:**

![1 \\le N \\le 10^{5}0 \\le interval\[i\] \\le 10^{9}
](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-63c5f1c7656d15ac8c95137c80fd216e_l3.png)  

**Examples:**

> **Input:** interval = {{0, 4}, {6, 8}, {2, 3}, {9, 18}}  
> **Output:** 5  
> **Explanation:**  
> The smallest non-negative integer which is non-overlapping to all set of the
> intervals is 5.  
>  **Input:** interval = {{0, 14}, {86, 108}, {22, 30}, {5, 17}}  
> **Output:** 18
>
>  
>
>
>  
>

**Naive Approach:**

  * Create a visited array of size **MAX** , and for every interval mark all value true from **start** to **end**.
  * Finally, iterate from **1** to **MAX** and find the smallest value which is not visited.

However, this approach will not work if the interval co-ordinates are up to 10
9.

_**Time Complexity:** O (N 2)_  
_**Auxiliary Space:** O (MAX)_

**Efficient Approach:**

  

  

  1. Instead of iterating from start to end just create a visited array and for each range, mark **vis[start] = 1** and **vis[end+1] = -1**.
  2. Take the prefix sum of the array.
  3. Then iterate over the array to find the first integer with value **0**.

Here is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to find the

// least non-overlapping number

// from a given set intervals

#include <bits/stdc++.h>

using namespace std;

const int MAX = 1e5 + 5;

// function to find the smallest

// non-overlapping number

void find_missing(

 vector<pair<int, int> > interval)

{

 // create a visited array

 vector<int> vis(MAX);

 for (int i = 0; i < interval.size(); ++i) {

 int start = interval[i].first;

 int end = interval[i].second;

 vis[start]++;

 vis[end + 1]--;

 }

 // find the first missing value

 for (int i = 1; i < MAX; i++) {

 vis[i] += vis[i - 1];

 if (!vis[i]) {

 cout << i << endl;

 return;

 }

 }

}

// Driver function

int main()

{

 vector<pair<int, int> > interval

 = { { 0, 14 }, { 86, 108 },

 { 22, 30 }, { 5, 17 } };

 find_missing(interval);

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

// Java program to find the

// least non-overlapping number

// from a given set intervals

class GFG{

 

static int MAX = (int) (1e5 + 5);

static class pair

{

 int first, second;

 public pair(int first, int second) 

 {

 this.first = first;

 this.second = second;

 } 

}

// function to find the smallest

// non-overlapping number

static void find_missing(

 pair[] interval)

{

 // create a visited array

 int [] vis = new int[MAX];

 for (int i = 0; i < interval.length; ++i)

 {

 int start = interval[i].first;

 int end = interval[i].second;

 vis[start]++;

 vis[end + 1]--;

 }

 // find the first missing value

 for (int i = 1; i < MAX; i++) {

 vis[i] += vis[i - 1];

 if (vis[i]==0) {

 System.out.print(i +"\n");

 return;

 }

 }

}

// Driver function

public static void main(String[] args)

{

 pair []interval = {new pair( 0, 14 ),

 new pair( 86, 108 ),

 new pair( 22, 30 ),

 new pair( 5, 17 )};

 find_missing(interval);

}

}

// This code is contributed by Rohit_ranjan  
  
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

# Python3 program to find the

# least non-overlapping number

# from a given set intervals

MAX = int(1e5 + 5)

# Function to find the smallest

# non-overlapping number

def find_missing(interval):

 

 # Create a visited array

 vis = [0] * (MAX)

 for i in range(len(interval)):

 start = interval[i][0]

 end = interval[i][1]

 vis[start] += 1

 vis[end + 1] -= 1

 # Find the first missing value

 for i in range(1, MAX):

 vis[i] += vis[i - 1]

 

 if (vis[i] == 0):

 print(i)

 return

# Driver code

interval = [ [ 0, 14 ], [ 86, 108 ],

 [ 22, 30 ], [ 5, 17 ] ]

 

find_missing(interval)

# This code is contributed by divyeshrabadiya07  
  
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

// C# program to find the

// least non-overlapping number

// from a given set intervals

using System;

class GFG{

static int MAX = (int)(1e5 + 5);

class pair

{

 public int first, second;

 public pair(int first, int second)

 {

 this.first = first;

 this.second = second;

 }

}

// Function to find the smallest

// non-overlapping number

static void find_missing(pair[] interval)

{

 

 // Create a visited array

 int [] vis = new int[MAX];

 for(int i = 0; i < interval.Length; ++i)

 {

 int start = interval[i].first;

 int end = interval[i].second;

 

 vis[start]++;

 vis[end + 1]--;

 }

 // Find the first missing value

 for(int i = 1; i < MAX; i++)

 {

 vis[i] += vis[i - 1];

 if (vis[i] == 0)

 {

 Console.Write(i + "\n");

 return;

 }

 }

}

// Driver code

public static void Main(String[] args)

{

 pair []interval = { new pair(0, 14),

 new pair(86, 108),

 new pair(22, 30),

 new pair(5, 17) };

 

 find_missing(interval);

}

}

// This code is contributed by Amit Katiyar  
  
---  
  
 __

 __

 **Output:**

    
    
    18

_**Time Complexity:** O (N)_  
_**Auxiliary Space:** O (MAX)_  
However, this approach will also not work if the interval co-ordinates are up
to 10 9.

 **Efficient Approach:**

  1. Sort the range by their start-coordinate and for each next range.
  2. Check if the starting point is greater than the maximum end-coordinate encountered so far, then a missing number can be found, and it will be **previous_max + 1**.

>  **Illustration:**  
> Consider the following example:  
> interval[][] = { { 0, 14 }, { 86, 108 }, { 22, 30 }, { 5, 17 } };  
> After sorting, interval[][] = { { 0, 14 }, { 5, 17 }, { 22, 30 }, { 86, 108
> }};  
> Initial mx = 0 and after considering first interval mx = max(0, 15) = 15  
> Since mx = 15 and 15 > 5 so after considering second interval mx = max(15,
> 18) = 18  
> now 18 < 22 so 18 is least non-overlapping number.  
>

Here is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to find the

// least non-overlapping number

// from a given set intervals

#include <bits/stdc++.h>

using namespace std;

// function to find the smallest

// non-overlapping number

void find_missing(

 vector<pair<int, int> > interval)

{

 // Sort the intervals based on their

 // starting value

 sort(interval.begin(), interval.end());

 int mx = 0;

 for (int i = 0; i < (int)interval.size(); ++i) {

 // check if any missing vaue exist

 if (interval[i].first > mx) {

 cout << mx;

 return;

 }

 else

 mx = max(mx, interval[i].second + 1);

 }

 // finally print the missing value

 cout << mx;

}

// Driver function

int main()

{

 vector<pair<int, int> > interval

 = { { 0, 14 }, { 86, 108 },

 { 22, 30 }, { 5, 17 } };

 find_missing(interval);

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

// Java program to find the

// least non-overlapping number

// from a given set intervals

import java.util.*;

import java.io.*;

class GFG{

 

static class Pair implements Comparable<Pair>

{

 int start,end;

 Pair(int s, int e)

 {

 start = s;

 end = e;

 }

 

 public int compareTo(Pair p)

 {

 return this.start - p.start;

 }

}

// Function to find the smallest

// non-overlapping number

static void findMissing(ArrayList<Pair> interval)

{

 

 // Sort the intervals based on their

 // starting value

 Collections.sort(interval);

 int mx = 0;

 for(int i = 0; i < interval.size(); ++i)

 {

 

 // Check if any missing vaue exist

 if (interval.get(i).start > mx)

 {

 System.out.println(mx);

 return;

 }

 else

 mx = Math.max(mx, interval.get(i).end + 1);

 }

 

 // Finally print the missing value

 System.out.println(mx);

}

// Driver code

public static void main(String []args)

{

 ArrayList<Pair> interval = new ArrayList<>();

 interval.add(new Pair(0, 14));

 interval.add(new Pair(86, 108));

 interval.add(new Pair(22, 30));

 interval.add(new Pair(5, 17));

 

 findMissing(interval);

}

}

// This code is contributed by Ganeshchowdharysadanala  
  
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

# Python3 program to find the

# least non-overlapping number

# from a given set intervals

# function to find the smallest

# non-overlapping number

def find_missing(interval):

 # Sort the intervals based 

 # on their starting value

 interval.sort()

 mx = 0

 for i in range (len(interval)):

 # Check if any missing

 # vaue exist

 if (interval[i][0] > mx):

 print (mx)

 return

 

 else:

 mx = max(mx,

 interval[i][1] + 1)

 # Finally print the missing value

 print (mx)

# Driver code

if __name__ == "__main__":

 interval = [[0, 14], [86, 108],

 [22, 30], [5, 17]]

 find_missing(interval);

 

# This code is contributed by Chitranayal  
  
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

// C# program to find the

// least non-overlapping number

// from a given set intervals

using System;

using System.Collections.Generic;

class GFG{

 

class Pair : IComparable<Pair>

{

 public int start,end;

 public Pair(int s, int e)

 {

 start = s;

 end = e;

 }

 

 public int CompareTo(Pair p)

 {

 return this.start - p.start;

 }

}

// Function to find the smallest

// non-overlapping number

static void findMissing(List<Pair> interval)

{

 

 // Sort the intervals based on their

 // starting value

 interval.Sort();

 int mx = 0;

 for(int i = 0; i < interval.Count; ++i)

 {

 

 // Check if any missing vaue exist

 if (interval[i].start > mx)

 {

 Console.WriteLine(mx);

 return;

 }

 else

 mx = Math.Max(mx, interval[i].end + 1);

 }

 

 // Finally print the missing value

 Console.WriteLine(mx);

}

// Driver code

public static void Main(String []args)

{

 List<Pair> interval = new List<Pair>();

 interval.Add(new Pair(0, 14));

 interval.Add(new Pair(86, 108));

 interval.Add(new Pair(22, 30));

 interval.Add(new Pair(5, 17));

 

 findMissing(interval);

}

}

// This code is contributed by shikhasingrajput  
  
---  
  
 __

 __

 **Output:**

    
    
    18

 _ **Time Complexity:** O (N * logN)_  
_**Auxiliary Space:** O (1)_

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


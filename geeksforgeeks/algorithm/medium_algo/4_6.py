Find number of segments covering each point in an given array



Given segments and some points, for each point find the number of segments
covering that point.

>  _A segment_ _ **(l, r)**_ _covers a point_ _ **x**_ _if and only if_ _ **l
> < = x < = r**_ _._

 **Examples:**

> **Input:** Segments = {{0, 3}, {1, 3}, {3, 8}},  
> Points = {-1, 3, 8}.  
>  **Output :** {0, 3, 1}  
>  **Explanation :**  
>
>
>
> ![seg](https://espresso.codeforces.com/f76b3fe547bff6be5b14de76c8b78ba3efecc744.png)
>
>  
>
>
>  
>
>
>   * No segments passing through point -1
>   * All the segments passing through point 3
>   * Segment 3rd passing through point 8
>

>
>  **Input:** Segments = {{1, 3}, {2, 4}, {5, 7}},  
> Points = {0, 2, 5}.  
>  **Output:** {0, 2, 1}  
>  **Explanation :**  
>
>
>
> ![seg2](https://espresso.codeforces.com/6e9332c303e1bc5d6cf34c2d6c5e2a19c9417289.png)
>
>   * No segments passing through point 0
>   * 1st and 2nd segment passing through point 2
>   * Segment 3rd passing through point 5
>

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.  

**Approach:**

  * We can do this by using logic similar to prefix sum. 
  * Let’s represent a segment with (l, r). Form a vector of pairs, for each segment push two pairs in vector with values (l, +1) ans (r + 1, -1). 
  * Sort the points in ascending order, but we also need it’s position so mapped it with it’s position. 
  * Sort the segment vector in descending order because we iterate on it from back. 
  * Make a variable count of segments, which is initially zero. 
  * Then, we will iterate on the point and pop the pair from the segment vector until it’s first value is less than equal to current point and add it’s second value to the count. 
  * Finally, Store the values of count in an array to his respective position and print the array. 

Below is the implementation of the above approach.

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to find the number of

// segments covering each points

#include<bits/stdc++.h>

using namespace std;

// Function to print an array

void PrintArray(int n,int arr[])

{

 for(int i = 0; i < n; i++)

 {

 cout<<arr[i]<<" ";

 }

}

// Funtion prints number of segments

// covering by each points

void NumberOfSegments(vector<pair<int,int> >segments,

 vector<int>points, int s, int p)

{

 vector< pair<int, int> >pts, seg;

 

 // Pushing points and index in

 // vector as a pairs

 for(int i = 0; i < p; i++)

 {

 pts.push_back({points[i], i});;

 }

 

 for(int i = 0; i < s; i++)

 {

 // (l,+1)

 seg.push_back({segments[i].first, 1});

 // (r+1,-1)

 seg.push_back({segments[i].second+1, -1});

 }

 

 // Sort the vectors

 sort(seg.begin(), seg.end(),

 greater<pair<int,int>>());

 sort(pts.begin(),pts.end());

 

 int count = 0;

 int ans[p];

 

 for(int i = 0; i < p; i++)

 {

 int x = pts[i].first;

 

 while(!seg.empty() &&

 seg.back().first <= x)

 {

 count+= seg.back().second;

 seg.pop_back();

 }

 ans[pts[i].second] = count;

 }

 

 // Print the answer

 PrintArray(p, ans);

 

}

//Driver code

int main()

{

 // Initializing vector of pairs

 vector<pair<int,int>>seg;

 

 // Push segments

 seg.push_back({0, 3});

 seg.push_back({1, 3});

 seg.push_back({3, 8});

 

 // Given points

 vector<int>point{-1, 3, 7};

 

 int s = seg.size();

 int p = point.size();

 

 NumberOfSegments(seg, point, s, p);

 

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

// Java program to find the number of

// segments covering each points

import java.util.*;

import java.lang.*;

class GFG{

 

// Function to print an array

static void PrintArray(int n,int arr[])

{

 for(int i = 0; i < n; i++)

 {

 System.out.print(arr[i] + " ");

 }

}

// Funtion prints number of segments

// covering by each points

static void NumberOfSegments(ArrayList<int[]> segments,

 int[] points, int s, int p)

{

 ArrayList<int[]> pts = new ArrayList<>(),

 seg = new ArrayList<>();

 

 // Pushing points and index in

 // vector as a pairs

 for(int i = 0; i < p; i++)

 {

 pts.add(new int[]{points[i], i});

 }

 

 for(int i = 0; i < s; i++)

 {

 // (l,+1)

 seg.add(new int[]{segments.get(i)[0], 1});

 

 // (r+1,-1)

 seg.add(new int[]{segments.get(i)[1] + 1, -1});

 }

 

 // Sort the vectors

 Collections.sort(seg, (a, b) -> b[0] - a[0]);

 Collections.sort(pts, (a, b) -> a[0] - b[0]);

 

 int count = 0;

 int[] ans = new int[p];

 

 for(int i = 0; i < p; i++)

 {

 int x = pts.get(i)[0];

 

 while (seg.size() != 0 &&

 seg.get(seg.size() - 1)[0] <= x)

 {

 count += seg.get(seg.size() - 1)[1];

 seg.remove(seg.size() - 1);

 }

 ans[pts.get(i)[1]] = count;

 }

 

 // Print the answer

 PrintArray(p, ans);

}

// Driver code

public static void main(String[] args)

{

 

 // Initializing vector of pairs

 ArrayList<int[]>seg = new ArrayList<>();

 

 // Push segments

 seg.add(new int[]{0, 3});

 seg.add(new int[]{1, 3});

 seg.add(new int[]{3, 8});

 

 // Given points

 int[] point = {-1, 3, 7};

 

 int s = seg.size();

 int p = point.length;

 

 NumberOfSegments(seg, point, s, p);

}

}

// This code is contributed by offbeat  
  
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

# Python3 program to find the number

# of segments covering each point

# Function to print an array

def PrintArray(n, arr):

 

 for i in range(n):

 print(arr[i], end = " ")

# Funtion prints number of segments

# covering by each points

def NumberOfSegments(segments, points, s, p):

 

 pts = []

 seg = []

 

 # Pushing points and index in

 # vector as a pairs

 for i in range(p):

 pts.append([points[i], i])

 for i in range(s):

 

 # (l, +1)

 seg.append([segments[i][0], 1])

 

 # (r+1, -1)

 seg.append([segments[i][1] + 1, -1])

 # Sort the vectors

 seg.sort(reverse = True)

 pts.sort(reverse = False)

 

 count = 0

 ans = [0 for i in range(p)]

 for i in range(p):

 x = pts[i][0]

 while(len(seg) != 0 and

 seg[len(seg) - 1][0] <= x):

 

 count += seg[len(seg) - 1][1]

 seg.remove(seg[len(seg) - 1])

 

 ans[pts[i][1]] = count

 

 # Print the answer

 PrintArray(p, ans)

# Driver code

if __name__ == '__main__':

 

 # Initializing vector of pairs

 seg = []

 # Push segments

 seg.append([ 0, 3 ])

 seg.append([ 1, 3 ])

 seg.append([ 3, 8 ])

 

 # Given points

 point = [ -1, 3, 7 ]

 

 s = len(seg)

 p = len(point)

 

 NumberOfSegments(seg, point, s, p)

# This code is contributed by Bhupendra_Singh  
  
---  
  
 __

 __

 **Output:**

    
    
    0 3 1

**Time Complexity: O(s + p)**  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


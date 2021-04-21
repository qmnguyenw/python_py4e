Find the number of points that have atleast 1 point above, below, left or
right of it



Given **N** points in 2 dimensional plane. A point is said to be above another
point if the X coordinates of both points are same and the Y coordinate of the
first point is greater than the Y coordinate of the second point. Similarly,
we define below, left and right. The task is to count the number of points
that have atleast one point above, below, left or right of it.

 **Examples:**

>  **Input:** arr[] = {{0, 0}, {0, 1}, {1, 0}, {0, -1}, {-1, 0}}  
>  **Output:** 1  
> The only point which satisfies the condition is the point (0, 0).
>
>  **Input:** arr[] = {{0, 0}, {1, 0}, {0, -2}, {5, 0}}  
>  **Output:** 0

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** For every **X** coordinate, find 2 values, the minimum and
maximum **Y** coordinate among all points that have this **X** coordinate. Do
the same thing for every **Y** coordinate. Now, for a point to satisfy the
constraints, its **Y** coordinate must lie in between the 2 calculated values
for that **X** coordinate. Check the same thing for its **X** coordinate.

  

  

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

#define MX 2001

#define OFF 1000

 

// Represents a point in 2-D space

struct point {

 int x, y;

};

 

// Function to return the count of

// required points

int countPoints(int n, struct point points[])

{

 int minx[MX];

 int miny[MX];

 

 // Initialize minimum values to infinity

 fill(minx, minx + MX, INT_MAX);

 fill(miny, miny + MX, INT_MAX);

 

 // Initialize maximum values to zero

 int maxx[MX] = { 0 };

 int maxy[MX] = { 0 };

 int x, y;

 for (int i = 0; i < n; i++) {

 

 // Add offset to deal with negative 

 // values

 points[i].x += OFF;

 points[i].y += OFF;

 x = points[i].x;

 y = points[i].y;

 

 // Update the minimum and maximum

 // values

 minx[y] = min(minx[y], x);

 maxx[y] = max(maxx[y], x);

 miny[x] = min(miny[x], y);

 maxy[x] = max(maxy[x], y);

 }

 

 int count = 0;

 for (int i = 0; i < n; i++) {

 x = points[i].x;

 y = points[i].y;

 

 // Check if condition is satisfied 

 // for X coordinate

 if (x > minx[y] && x < maxx[y])

 

 // Check if condition is satisfied

 // for Y coordinate

 if (y > miny[x] && y < maxy[x])

 count++;

 }

 return count;

}

 

// Driver code

int main()

{

 struct point points[] = { { 0, 0 },

 { 0, 1 },

 { 1, 0 },

 { 0, -1 },

 { -1, 0 } };

 int n = sizeof(points) / sizeof(points[0]);

 cout << countPoints(n, points);

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

// Java implementation of the approach

import java.util.*;

 

class GFG 

{

static int MX = 2001;

static int OFF = 1000;

 

// Represents a point in 2-D space

static class point 

{

 int x, y;

 

 public point(int x, int y) 

 {

 this.x = x;

 this.y = y;

 }

 

};

 

// Function to return the count of

// required points

static int countPoints(int n, point points[])

{

 int []minx = new int[MX];

 int []miny = new int[MX];

 

 // Initialize minimum values to infinity

 for (int i = 0; i < n; i++)

 {

 minx[i]=Integer.MAX_VALUE;

 miny[i]=Integer.MAX_VALUE;

 }

 

 // Initialize maximum values to zero

 int []maxx = new int[MX];

 int []maxy = new int[MX];

 

 int x, y;

 for (int i = 0; i < n; i++)

 {

 

 // Add offset to deal with negative 

 // values

 points[i].x += OFF;

 points[i].y += OFF;

 x = points[i].x;

 y = points[i].y;

 

 // Update the minimum and maximum

 // values

 minx[y] = Math.min(minx[y], x);

 maxx[y] = Math.max(maxx[y], x);

 miny[x] = Math.min(miny[x], y);

 maxy[x] = Math.max(maxy[x], y);

 }

 

 int count = 0;

 for (int i = 0; i < n; i++) 

 {

 x = points[i].x;

 y = points[i].y;

 

 // Check if condition is satisfied 

 // for X coordinate

 if (x > minx[y] && x < maxx[y])

 

 // Check if condition is satisfied

 // for Y coordinate

 if (y > miny[x] && y < maxy[x])

 count++;

 }

 return count;

}

 

// Driver code

public static void main(String[] args)

{

 point points[] = {new point(0, 0),

 new point(0, 1),

 new point(1, 0),

 new point(0, -1),

 new point(-1, 0)};

 int n = points.length;

 System.out.println(countPoints(n, points));

}

} 

 

// This code is contributed by PrinciRaj1992  
  
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

from sys import maxsize as INT_MAX

 

MX = 2001

OFF = 1000

 

# Represents a point in 2-D space

class point:

 def __init__(self, x, y):

 self.x = x

 self.y = y

 

# Function to return the count of

# required points

def countPoints(n: int, points: list) -> int:

 

 # Initialize minimum values to infinity

 minx = [INT_MAX] * MX

 miny = [INT_MAX] * MX

 

 # Initialize maximum values to zero

 maxx = [0] * MX

 maxy = [0] * MX

 x, y = 0, 0

 for i in range(n):

 

 # Add offset to deal with negative

 # values

 points[i].x += OFF

 points[i].y += OFF

 x = points[i].x

 y = points[i].y

 

 # Update the minimum and maximum

 # values

 minx[y] = min(minx[y], x)

 maxx[y] = max(maxx[y], x)

 miny[x] = min(miny[x], y)

 maxy[x] = max(maxy[x], y)

 

 count = 0

 for i in range(n):

 x = points[i].x

 y = points[i].y

 

 # Check if condition is satisfied

 # for X coordinate

 if (x > minx[y] and x < maxx[y]):

 

 # Check if condition is satisfied

 # for Y coordinate

 if (y > miny[x] and y < maxy[x]):

 count += 1

 

 return count

 

# Driver Code

if __name__ == "__main__":

 

 points = [point(0, 0),

 point(0, 1),

 point(1, 0),

 point(0, -1),

 point(-1, 0)]

 n = len(points)

 

 print(countPoints(n, points))

 

# This code is contributed by

# sanjeev2552  
  
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

// C# implementation of the approach

using System;

using System.Collections.Generic;

 

class GFG 

{

static int MX = 2001;

static int OFF = 1000;

 

// Represents a point in 2-D space

public class point 

{

 public int x, y;

 

 public point(int x, int y) 

 {

 this.x = x;

 this.y = y;

 }

};

 

// Function to return the count of

// required points

static int countPoints(int n, point []points)

{

 int []minx = new int[MX];

 int []miny = new int[MX];

 

 // Initialize minimum values to infinity

 for (int i = 0; i < n; i++)

 {

 minx[i]=int.MaxValue;

 miny[i]=int.MaxValue;

 }

 

 // Initialize maximum values to zero

 int []maxx = new int[MX];

 int []maxy = new int[MX];

 

 int x, y;

 for (int i = 0; i < n; i++)

 {

 

 // Add offset to deal with negative 

 // values

 points[i].x += OFF;

 points[i].y += OFF;

 x = points[i].x;

 y = points[i].y;

 

 // Update the minimum and maximum

 // values

 minx[y] = Math.Min(minx[y], x);

 maxx[y] = Math.Max(maxx[y], x);

 miny[x] = Math.Min(miny[x], y);

 maxy[x] = Math.Max(maxy[x], y);

 }

 

 int count = 0;

 for (int i = 0; i < n; i++) 

 {

 x = points[i].x;

 y = points[i].y;

 

 // Check if condition is satisfied 

 // for X coordinate

 if (x > minx[y] && x < maxx[y])

 

 // Check if condition is satisfied

 // for Y coordinate

 if (y > miny[x] && y < maxy[x])

 count++;

 }

 return count;

}

 

// Driver code

public static void Main(String[] args)

{

 point []points = {new point(0, 0),

 new point(0, 1),

 new point(1, 0),

 new point(0, -1),

 new point(-1, 0)};

 int n = points.Length;

 Console.WriteLine(countPoints(n, points));

}

}

 

// This code is contributed by 29AjayKumar  
  
---  
  
 __

 __

 **Output:**

    
    
    1
    

**Time Complexity:** O(N)

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


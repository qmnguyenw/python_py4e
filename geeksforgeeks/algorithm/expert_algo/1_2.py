Maximum distance between two points in coordinate plane using Rotating
Caliper’s Method



 **Prerequisites:** Graham Scan’s Convex Hull, Orientation.  
Given a set of **N** points in a coordinates plane, the task is to find the
maximum distance between any two points in the given set of planes.

 **Examples:**

> **Input:** n = 4, Points: (0, 3), (3, 0), (0, 0), (1, 1)  
> **Output:** Maximum Distance = 4.24264  
> **Explanation:**  
> Points having maximum distance between them are (0, 3) and (3, 0)
>
> **Input:** n = 5, Points: (4, 0), (0, 2), (-1, -7), (1, 10), (2, -3)  
> **Output:** Maximum Distance = 17.11724  
> **Explanation:**  
> Points having maximum distance between them are (-1, 7) and (1, 10)

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Naive Approach:** The naive idea is to try every possible pair of points
from the given set and calculate the distances between each of them and print
the maximum distance among all the pairs.

  

  

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

#include<bits/stdc++.h>

using namespace std;

// Function calculates distance

// between two points

long dist(pair<long, long> p1,

 pair<long, long> p2)

{

 long x0 = p1.first - p2.first;

 long y0 = p1.second - p2.second;

 return x0 * x0 + y0 * y0;

}

// Function to find the maximum

// distance between any two points

double maxDist(pair<long, long> p[], int n)

{

 double Max = 0;

 // Iterate over all possible pairs

 for(int i = 0; i < n; i++)

 {

 for(int j = i + 1; j < n; j++)

 {

 

 // Update max

 Max = max(Max, (double)dist(p[i],

 p[j]));

 }

 }

 // Return actual distance

 return sqrt(Max);

}

// Driver code 

int main()

{

 

 // Number of points

 int n = 5;

 pair<long, long> p[n];

 // Given points

 p[0].first = 4, p[0].second = 0;

 p[1].first = 0, p[1].second = 2;

 p[2].first = -1, p[2].second = -7;

 p[3].first = 1, p[3].second = 10;

 p[4].first = 2, p[4].second = -3;

 // Function call

 cout << fixed << setprecision(14)

 << maxDist(p, n) <<endl;

 return 0;

}

// This code is contributed by divyeshrabadiya07  
  
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

import java.awt.*;

import java.util.ArrayList;

public class Main {

 // Function calculates distance

 // between two points

 static long dist(Point p1, Point p2)

 {

 long x0 = p1.x - p2.x;

 long y0 = p1.y - p2.y;

 return x0 * x0 + y0 * y0;

 }

 // Function to find the maximum

 // distance between any two points

 static double maxDist(Point p[])

 {

 int n = p.length;

 double max = 0;

 // Iterate over all possible pairs

 for (int i = 0; i < n; i++) {

 for (int j = i + 1; j < n; j++) {

 // Update max

 max = Math.max(max,

 dist(p[i],

 p[j]));

 }

 }

 // Return actual distance

 return Math.sqrt(max);

 }

 // Driver Code

 public static void main(String[] args)

 {

 // Number of points

 int n = 5;

 Point p[] = new Point[n];

 // Given points

 p[0] = new Point(4, 0);

 p[1] = new Point(0, 2);

 p[2] = new Point(-1, -7);

 p[3] = new Point(1, 10);

 p[4] = new Point(2, -3);

 // Function Call

 System.out.println(maxDist(p));

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

from math import sqrt

# Function calculates distance

# between two points

def dist(p1, p2):

 

 x0 = p1[0] - p2[0]

 y0 = p1[1] - p2[1]

 return x0 * x0 + y0 * y0

# Function to find the maximum

# distance between any two points

def maxDist(p):

 n = len(p)

 maxm = 0

 # Iterate over all possible pairs

 for i in range(n):

 for j in range(i + 1, n):

 

 # Update maxm

 maxm = max(maxm, dist(p[i], p[j]))

 # Return actual distance

 return sqrt(maxm)

 

# Driver Code

if __name__ == '__main__':

 

 # Number of points

 n = 5

 p = []

 

 # Given points

 p.append([4, 0])

 p.append([0, 2])

 p.append([-1, -7])

 p.append([1, 10])

 p.append([2, -3])

 # Function Call

 print(maxDist(p))

# This code is contributed by mohit kumar 29  
  
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

using System;

class GFG {

 

 // Function calculates distance

 // between two points

 static long dist(Tuple<int, int> p1, Tuple<int, int>
p2)

 {

 long x0 = p1.Item1 - p2.Item1;

 long y0 = p1.Item2 - p2.Item2;

 return x0 * x0 + y0 * y0;

 }

 

 // Function to find the maximum

 // distance between any two points

 static double maxDist(Tuple<int, int>[] p)

 {

 int n = p.Length;

 double max = 0;

 

 // Iterate over all possible pairs

 for (int i = 0; i < n; i++) {

 

 for (int j = i + 1; j < n; j++) {

 

 // Update max

 max = Math.Max(max, dist(p[i],p[j]));

 }

 }

 

 // Return actual distance

 return Math.Sqrt(max);

 }

 // Driver code

 static void Main() {

 

 // Given points

 Tuple<int, int>[] p =

 {

 Tuple.Create(4, 0),

 Tuple.Create(0, 2),

 Tuple.Create(-1, -7),

 Tuple.Create(1, 10),

 Tuple.Create(2, -3),

 };

 

 // Function Call

 Console.WriteLine(maxDist(p));

 }

}

// This code is contributed by divyesh072019  
  
---  
  
 __

 __

 **Output:**

    
    
    17.11724276862369

_**Time Complexity:** O(N2), where N is the total number of points. _  
_**Auxiliary Space:** O(1)_

 **Efficient Approach:** The above naive approach can be optimized using
**Rotating Caliper’s Method**.

>  **Rotating Calipers** is a method for solving a number of problems from the
> field of computational geometry. It resembles the idea of rotating an
> adjustable caliper around the outside of a polygon’s convex hull.
> Originally, this method was invented to compute the diameter of convex
> polygons. It can also be used to compute the minimum and maximum distance
> between two convex polygons, the intersection of convex polygons, the
> maximum distance between two points in a polygon, and many things more.

To implement the above method we will use the concept of the Convex Hull.
Before we begin a further discussion about the optimal approach, we need to
know about the following:  

  * **Unsigned Area Of Triangle:** If we are given three points **P1(x1, y1), P2(x2, y2)** and **P3(x3, y3)** then

![\\left \( \\frac {\(x2 - x1\)*\(y3 - y2\) - \(x3 - x2\)*\(y2 - y1\)}{2}
\\right \) ](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-c8d6e0a546cedf413303c800e643cd72_l3.png)

  * is the signed area of triangle. If the area is positive then three points are in the clockwise order, Else they are in anti-clockwise order and if the area equals to zero then, the points are co-linear. If we take **absolute value** , then this will represent the unsigned area of the triangle. Here, unsigned basically means area without direction i.e., we just need the relative absolute value of the area. Therefore, we can remove (1/2) from the formula. Hence,

> Relative Area of Triangle = **abs((x2-x1)*(y3-y2)-(x3-x2)*(y2-y1))**

  * **Antipodal Points:** It is those points which are diametrically opposite to each other. But for us, antipodal points are those which are farthest from each other in the convex polygon. If we choose one point from the given set, then this point can only achieve it’s maximum distance if and only if we can find it’s antipodal point from the given set.

  

  

Below are the steps:

  1. Two points having maximum distance must lie on the boundary of the convex polygon formed from the given set. Therefore, use Graham Scan’s convex hull method to arrange points in counter-clockwise order.
  2. We have **N** points, Initially start from point **P1** and include those points from set of given points such that area of region always increases by including any points from the set.
  3. Starting from point **P1** , Choose **K = 2** and increment **K** while **area(PN, P1, PK)** is increasing and stop before it starts decreasing. Now the current point **PK** might be the antipodal point for **P1**. Similarly, find antipodal point for p2 by finding **area(P1, P2, PK)** and incrementing **K** form where we previously stopped and so on.
  4. Keep updating the maximum distance for each antipodal points occurs in the above steps as the distance between intial point and point by including area was maximum.

Below is the implementation of the above approach:

## Java

 __

 __  
 __

 __

 __  
 __  
 __

// Java Program for the above approach

import java.awt.*;

import java.util.*;

import java.util.Map.Entry;

public class Main {

 // Function to detect the orientation

 static int orientation(Point p,

 Point q,

 Point r)

 {

 int x = area(p, q, r);

 // If area > 0 then

 // points are clockwise

 if (x > 0) {

 return 1;

 }

 // If area<0 then

 // points are counterclockwise

 if (x < 0) {

 return -1;

 }

 // If area is 0 then p, q

 // and r are co-linear

 return 0;

 }

 // Function to find the area

 static int area(Point p, Point q, Point r)

 {

 // 2*(area of triangle)

 return ((p.y - q.y) * (q.x - r.x)

 - (q.y - r.y) * (p.x - q.x));

 }

 // Function to find the absolute Area

 static int absArea(Point p,

 Point q, Point r)

 {

 // Unsigned area

 // 2*(area of triangle)

 return Math.abs(area(p, q, r));

 }

 // Function to find the distance

 static int dist(Point p1, Point p2)

 {

 // squared-distance b/w

 // p1 and p2 for precision

 return ((p1.x - p2.x) * (p1.x - p2.x)

 + (p1.y - p2.y) * (p1.y - p2.y));

 }

 // Function to implement Convex Hull

 // Approach

 static ArrayList<Point>

 convexHull(Point points[])

 {

 int n = points.length;

 Point min = new Point(Integer.MAX_VALUE,

 Integer.MAX_VALUE);

 // Choose point having min.

 // y-coordinate and if two points

 // have same y-coordinate choose

 // the one with minimum x-coordinate

 int ind = -1;

 // Iterate Points[]

 for (int i = 0; i < n; i++) {

 if (min.y > points[i].y) {

 min.y = points[i].y;

 min.x = points[i].x;

 ind = i;

 }

 else if (min.y == points[i].y

 && min.x > points[i].x) {

 min.x = points[i].x;

 ind = i;

 }

 }

 points[ind] = points[0];

 points[0] = min;

 // Sort points which have

 // minimum polar angle wrt

 // Point min

 Arrays.sort(points, 1, n,

 new Comparator<Point>() {

 @Override

 public int compare(Point o1,

 Point o2)

 {

 int o = orientation(min, o1, o2);

 // If points are co-linear

 // choose the one having smaller

 // distance with min first.

 if (o == 0) {

 return dist(o1, min)

 - dist(o2, min);

 }

 // If clockwise then swap

 if (o == 1) {

 return 1;

 }

 // If anticlockwise then

 // don't swap

 return -1;

 }

 });

 Stack<Point> st = new Stack<>();

 // First hull point

 st.push(points[0]);

 int k;

 for (k = 1; k < n - 1; k++) {

 if (orientation(points[0],

 points[k],

 points[k + 1])

 != 0)

 break;

 }

 // Second hull point

 st.push(points[k]);

 for (int i = k + 1; i < n; i++) {

 Point top = st.pop();

 while (orientation(st.peek(),

 top,

 points[i])

 >= 0) {

 top = st.pop();

 }

 st.push(top);

 st.push(points[i]);

 }

 ArrayList<Point> hull

 = new ArrayList<>();

 // Iterate stack and add node to hull

 for (int i = 0; i < st.size(); i++) {

 hull.add(st.get(i));

 }

 return hull;

 }

 // Function to find the maximum

 // distance between any two points

 // from a set of given points

 static double

 rotatingCaliper(Point points[])

 {

 // Takes O(n)

 ArrayList<Point> convexHull

 = convexHull(points);

 int n = convexHull.size();

 // Convex hull point in counter-

 // clockwise order

 Point hull[] = new Point[n];

 n = 0;

 while (n < convexHull.size()) {

 hull[n] = convexHull.get(n++);

 }

 // Base Cases

 if (n == 1)

 return 0;

 if (n == 2)

 return Math.sqrt(dist(hull[0], hull[1]));

 int k = 1;

 // Find the farthest vertex

 // from hull[0] and hull[n-1]

 while (absArea(hull[n - 1],

 hull[0],

 hull[(k + 1) % n])

 > absArea(hull[n - 1],

 hull[0],

 hull[k])) {

 k++;

 }

 double res = 0;

 // Check points from 0 to k

 for (int i = 0, j = k;

 i <= k && j < n; i++) {

 res = Math.max(res,

 Math.sqrt((double)dist(hull[i],

 hull[j])));

 while (j < n

 && absArea(hull[i],

 hull[(i + 1) % n],

 hull[(j + 1) % n])

 > absArea(hull[i],

 hull[(i + 1) % n],

 hull[j])) {

 // Update res

 res = Math.max(

 res,

 Math.sqrt(dist(hull[i],

 hull[(j + 1) % n])));

 j++;

 }

 }

 // Return the result distance

 return res;

 }

 // Driver Code

 public static void main(String[] args)

 {

 // Total points

 int n = 5;

 Point p[] = new Point[n];

 // Given Points

 p[0] = new Point(4, 0);

 p[1] = new Point(0, 2);

 p[2] = new Point(-1, -7);

 p[3] = new Point(1, 10);

 p[4] = new Point(2, -3);

 // Function Call

 System.out.println(rotatingCaliper(p));

 }

}  
  
---  
  
 __

 __

 **Output:**

    
    
    17.11724276862369

**Time Complexity:** _O(N*log N)_  
**Auxiliary Space:** _O(N)_  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


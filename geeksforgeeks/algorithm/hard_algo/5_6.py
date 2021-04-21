Find X and Y intercepts of a line passing through the given points



Given two points on a 2D plane, the task is to find the **x – intercept** and
the **y – intercept** of a line passing through the given points.

 **Examples:**

>  **Input:** points[][] = {{5, 2}, {2, 7}}  
>  **Output:**  
>  6.2  
> 10.333333333333334
>
>  **Input:** points[][] = {{3, 2}, {2, 4}}  
>  **Output:**  
>  4.0  
> 8.0

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:**

  

  

  * Find the slope using the given points.
  * Put the value of the slope in the expression of the line i.e. **y = mx + c**.
  * Now find the value of **c** using the values of any of the given points in the equation **y = mx + c**
  * To find the x-intercept, put **y = 0** in **y = mx + c**.
  * To find the y-intercept, put **x = 0** in **y = mx + c**.

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

 

// Function to find the X and Y intercepts

// of the line passing through

// the given points

void getXandYintercept(int P[], int Q[])

{

 int a = P[1] - Q[1];

 int b = P[0] - Q[0];

 

 // if line is parallel to y axis

 if (b == 0) {

 cout << P[0] << endl; // x - intercept will be p[0]

 cout << "infinity"; // y - intercept will be infinity

 return;

 }

 

 // if line is parallel to x axis

 if (a == 0) {

 cout << "infinity"; // x - intercept will be infinity

 cout << P[1] << endl; // y - intercept will be p[1]

 return;

 }

 

 // Slope of the line

 double m = a / (b * 1.0);

 

 // y = mx + c in where c is unknown

 // Use any of the given point to find c

 int x = P[0];

 int y = P[1];

 double c = y - m * x;

 

 // For finding the x-intercept put y = 0

 y = 0;

 double r = (y - c) / (m * 1.0);

 cout << r << endl;

 

 // For finding the y-intercept put x = 0

 x = 0;

 y = m * x + c;

 printf("%.8f", c);

}

 

// Driver code

int main()

{

 int p1[] = { 5, 2 };

 int p2[] = { 2, 7 };

 getXandYintercept(p1, p2);

 return 0;

}

 

// This code is contributed by Mohit Kumar  
  
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

class GFG {

 

 // Function to find the X and Y intercepts

 // of the line passing through

 // the given points

 static void getXandYintercept(int P[],

 int Q[])

 {

 int a = P[1] - Q[1];

 int b = P[0] - Q[0];

 

 // if line is parallel to y axis

 if (b == 0) {

 

 // x - intercept will be p[0]

 System.out.println(P[0]); 

 

 // y - intercept will be infinity

 System.out.println("infinity");

 return;

 }

 

 // if line is parallel to x axis

 if (a == 0) {

 

 // x - intercept will be infinity 

 System.out.println("infinity"); 

 

 // y - intercept will be p[1]

 System.out.println(P[1]); 

 return;

 }

 

 // Slope of the line

 double m = a / (b * 1.0);

 

 // y = mx + c in where c is unknown

 // Use any of the given point to find c

 int x = P[0];

 int y = P[1];

 double c = y - m * x;

 

 // For finding the x-intercept put y = 0

 y = 0;

 double r = (y - c) / (m * 1.0);

 System.out.println(r);

 

 // For finding the y-intercept put x = 0

 x = 0;

 y = (int)(m * x + c);

 System.out.print(c);

 }

 

 // Driver code

 public static void main(String[] args)

 {

 int p1[] = { 5, 2 };

 int p2[] = { 2, 7 };

 getXandYintercept(p1, p2);

 }

}

 

// This code is contributed by kanugargng  
  
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

 

# Function to find the X and Y intercepts 

# of the line passing through 

# the given points

def getXandYintercept(P, Q):

 

 a = P[1] - Q[1] 

 b = P[0] - Q[0]

 

 # if line is parallel to y axis

 if b == 0:

 print(P[0]) # x - intercept will be p[0]

 print("infinity") # y - intercept will be infinity

 return

 

 # if line is parallel to x axis

 if a == 0:

 print("infinity") # x - intercept will be infinity

 print(P[1]) # y - intercept will be p[1]

 return

 

 

 

 # Slope of the line

 m = a / b

 

 # y = mx + c in where c is unknown 

 # Use any of the given point to find c

 x = P[0]

 y = P[1]

 c = y-m * x

 

 # For finding the x-intercept put y = 0

 y = 0

 x =(y-c)/m

 print(x)

 

 # For finding the y-intercept put x = 0

 x = 0

 y = m * x + c

 print(y) 

 

# Driver code

p1 = [5, 2] 

p2 = [7, 2]

getXandYintercept(p1, p2)  
  
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

 

class GFG {

 

 // Function to find the X and Y intercepts

 // of the line passing through

 // the given points

 static void getXandYintercept(int[] P,

 int[] Q)

 {

 int a = P[1] - Q[1];

 int b = P[0] - Q[0];

 

 // if line is parallel to y axis

 if (b == 0) {

 Console.WriteLine(P[0]); // x - intercept will be p[0]

 Console.WriteLine("infinity"); // y - intercept will be infinity

 return;

 }

 

 // if line is parallel to x axis

 if (a == 0) {

 Console.WriteLine("infinity"); // x - intercept will be infinity

 Console.WriteLine(P[1]); // y - intercept will be p[1]

 return;

 }

 

 // Slope of the line

 double m = a / (b * 1.0);

 

 // y = mx + c in where c is unknown

 // Use any of the given point to find c

 int x = P[0];

 int y = P[1];

 double c = y - m * x;

 

 // For finding the x-intercept put y = 0

 y = 0;

 double r = (y - c) / (m * 1.0);

 Console.WriteLine(r);

 

 // For finding the y-intercept put x = 0

 x = 0;

 y = (int)(m * x + c);

 Console.WriteLine(c);

 }

 

 // Driver code

 public static void Main()

 {

 int[] p1 = { 5, 2 };

 int[] p2 = { 2, 7 };

 getXandYintercept(p1, p2);

 }

}

 

// This code is contributed by AnkitRai01  
  
---  
  
 __

 __

 **Output:**

    
    
    6.2
    10.33333333333
    

**Time Complexity:** O(1)

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


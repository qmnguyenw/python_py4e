Bresenham’s Line Generation Algorithm



Given coordinate of two points A(x1, y1) and B(x2, y2). The task to find all
the intermediate points required for drawing line AB on the computer screen of
pixels. Note that every pixel has integer coordinates.  
Examples:  

    
    
    Input  : A(0,0), B(4,4)
    Output : (0,0), (1,1), (2,2), (3,3), (4,4)
    
    Input  : A(0,0), B(4,2)
    Output : (0,0), (1,0), (2,1), (3,1), (4,2)

Below are some assumptions to keep algorithm simple.  

  1. We draw line from left to right.
  2. x1 < x2 and y1< y2
  3. Slope of the line is between 0 and 1. We draw a line from lower left to upper right.

Let us understand the process by considering the naive way first.  

    
    
    // A **naive way** of drawing line
    void naiveDrawLine(x1, x2, y1, y2)
    {
       m = (y2 - y1)/(x2 - x1)
       for (x  = x1; x <= x2; x++) 
       {    
          // Assuming that the round function finds
          // closest integer to a given float.
          y = round(mx + c);    
          print(x, y); 
       }
    }

Above algorithm works, but it is slow. The idea of Bresenham’s algorithm is to
avoid floating point multiplication and addition to compute mx + c, and then
computing round value of (mx + c) in every step. In Bresenham’s algorithm, we
move across the x-axis in unit intervals.  

  1. We always increase x by 1, and we choose about next y, whether we need to go to y+1 or remain on y. In other words, from any position (Xk, Yk) we need to choose between (Xk \+ 1, Yk) and (Xk \+ 1, Yk \+ 1).   

![](https://media.geeksforgeeks.org/wp-content/uploads/BresenhamLine.png)

  

  

  1. We would like to pick the y value (among Yk \+ 1 and Yk) corresponding to a point that is closer to the original line.

We need to a decision parameter to decide whether to pick Yk \+ 1 or Yk as
next point. The idea is to keep track of slope error from previous increment
to y. If the slope error becomes greater than 0.5, we know that the line has
moved upwards one pixel, and that we must increment our y coordinate and
readjust the error to represent the distance from the top of the new pixel –
which is done by subtracting one from error.  

    
    
    // **Modifying the naive way to use a parameter**
    // **to decide next y**.
    void withDecisionParameter(x1, x2, y1, y2)
    {
       m = (y2 - y1)/(x2 - x1)
       slope_error = [Some Initial Value]
       for (x = x1, y = y1; x = 0.5)  
       {       
          y++;       
          slope_error  -= 1.0;    
       }
    }

 **How to avoid floating point arithmetic**  
The above algorithm still includes floating point arithmetic. To avoid
floating point arithmetic, consider the value below value m.  
m = (y2 – y1)/(x2 – x1)  
We multiply both sides by (x2 – x1)  
We also change slope_error to slope_error * (x2 – x1). To avoid comparison
with 0.5, we further change it to slope_error * (x2 – x1) * 2.  
Also, it is generally preferred to compare with 0 than 1.  

    
    
    // **Modifying the above algorithm to avoid floating**
    // **point arithmetic and use comparison with 0.**
    void bresenham(x1, x2, y1, y2)
    {
       m_new = 2 * (y2 - y1)
       slope_error_new = [Some Initial Value]
       for (x = x1, y = y1; x = 0)  
       {       
          y++;       
          slope_error_new  -= 2 * (x2 - x1);    
       }
    }

The initial value of slope_error_new is 2*(y2 – y1) – (x2 – x1). Refer this
for proof of this value  
Below is the implementation of above algorithm.  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program for Bresenham’s Line Generation

// Assumptions :

// 1) Line is drawn from left to right.

// 2) x1 < x2 and y1 < y2

// 3) Slope of the line is between 0 and 1.

// We draw a line from lower left to upper

// right.

#include<bits/stdc++.h>

using namespace std;

// function for line generation

void bresenham(int x1, int y1, int x2, int y2)

{

 int m_new = 2 * (y2 - y1);

 int slope_error_new = m_new - (x2 - x1);

 for (int x = x1, y = y1; x <= x2; x++)

 {

 cout << "(" << x << "," << y << ")\n";

 // Add slope to increment angle formed

 slope_error_new += m_new;

 // Slope error reached limit, time to

 // increment y and update slope error.

 if (slope_error_new >= 0)

 {

 y++;

 slope_error_new -= 2 * (x2 - x1);

 }

 }

}

// driver function

int main()

{

 int x1 = 3, y1 = 2, x2 = 15, y2 = 5;

 bresenham(x1, y1, x2, y2);

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

// Java program for Bresenhams Line Generation

// Assumptions :

// 1) Line is drawn from left to right.

// 2) x1 < x2 and y1 < y2

// 3) Slope of the line is between 0 and 1.

// We draw a line from lower left to upper

// right.

class GFG

{

 // function for line generation

 static void bresenham(int x1, int y1, int x2,

 int y2)

 {

 int m_new = 2 * (y2 - y1);

 int slope_error_new = m_new - (x2 - x1);

 

 for (int x = x1, y = y1; x <= x2; x++)

 {

 System.out.print("(" +x + "," + y + ")\n");

 // Add slope to increment angle formed

 slope_error_new += m_new;

 // Slope error reached limit, time to

 // increment y and update slope error.

 if (slope_error_new >= 0)

 {

 y++;

 slope_error_new -= 2 * (x2 - x1);

 }

 }

 } 

 // Driver code

 public static void main (String[] args)

 {

 int x1 = 3, y1 = 2, x2 = 15, y2 = 5; 

 bresenham(x1, y1, x2, y2);

 }

}

// This code is contributed by Anant Agarwal.  
  
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

# Python 3 program for Bresenham’s Line Generation

# Assumptions :

# 1) Line is drawn from left to right.

# 2) x1 < x2 and y1 < y2

# 3) Slope of the line is between 0 and 1.

# We draw a line from lower left to upper

# right.

# function for line generation

def bresenham(x1,y1,x2, y2):

 m_new = 2 * (y2 - y1)

 slope_error_new = m_new - (x2 - x1)

 y=y1

 for x in range(x1,x2+1):

 

 print("(",x ,",",y ,")\n")

 # Add slope to increment angle formed

 slope_error_new =slope_error_new + m_new

 # Slope error reached limit, time to

 # increment y and update slope error.

 if (slope_error_new >= 0):

 y=y+1

 slope_error_new =slope_error_new - 2 * (x2 - x1)

 

 

# driver function

if __name__=='__main__':

 x1 = 3

 y1 = 2

 x2 = 15

 y2 = 5

 bresenham(x1, y1, x2, y2)

#This code is contributed by ash264  
  
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

// C# program for Bresenhams Line Generation

// Assumptions :

// 1) Line is drawn from left to right.

// 2) x1 < x2 and y1< y2

// 3) Slope of the line is between 0 and 1.

// We draw a line from lower left to upper

// right.

using System;

class GFG {

 

 // function for line generation

 static void bresenham(int x1, int y1, int x2,

 int y2)

 {

 

 int m_new = 2 * (y2 - y1);

 int slope_error_new = m_new - (x2 - x1);

 

 for (int x = x1, y = y1; x <= x2; x++)

 {

 Console.Write("(" + x + "," + y + ")\n");

 // Add slope to increment angle formed

 slope_error_new += m_new;

 // Slope error reached limit, time to

 // increment y and update slope error.

 if (slope_error_new >= 0)

 {

 y++;

 slope_error_new -= 2 * (x2 - x1);

 }

 }

 } 

 // Driver code

 public static void Main ()

 {

 int x1 = 3, y1 = 2, x2 = 15, y2 = 5;

 

 bresenham(x1, y1, x2, y2);

 }

}

// This code is contributed by nitin mittal.  
  
---  
  
 __

 __

## PHP

 __

 __  
 __

 __

 __  
 __  
 __

<?php

// PHP program for Bresenham’s

// Line Generation Assumptions :

// 1) Line is drawn from

// left to right.

// 2) x1 < x2 and y1 < y2

// 3) Slope of the line is

// between 0 and 1.

// We draw a line from lower

// left to upper right.

// function for line generation

function bresenham($x1, $y1, $x2, $y2)

{

$m_new = 2 * ($y2 - $y1);

$slope_error_new = $m_new - ($x2 - $x1);

for ($x = $x1, $y = $y1; $x <= $x2; $x++)

{

 echo "(" ,$x , "," , $y, ")\n";

 // Add slope to increment

 // angle formed

 $slope_error_new += $m_new;

 // Slope error reached limit,

 // time to increment y and

 // update slope error.

 if ($slope_error_new >= 0)

 {

 $y++;

 $slope_error_new -= 2 * ($x2 - $x1);

 }

}

}

// Driver Code

$x1 = 3; $y1 = 2; $x2 = 15; $y2 = 5;

bresenham($x1, $y1, $x2, $y2);

// This code is contributed by nitin mittal.

?>  
  
---  
  
 __

 __

## Javascript

 __

 __  
 __

 __

 __  
 __  
 __

<script>

// javascript program for Bresenhams Line Generation

// Assumptions :

// 1) Line is drawn from left to right.

// 2) x1 < x2 and y1 < y2

// 3) Slope of the line is between 0 and 1.

// We draw a line from lower left to upper

// right.

 // function for line generation

 function bresenham(x1 , y1 , x2,y2)

 {

 var m_new = 2 * (y2 - y1);

 var slope_error_new = m_new - (x2 - x1);

 

 for (x = x1, y = y1; x <= x2; x++)

 {

 document.write("(" +x + "," + y + ")<br>");

 // Add slope to increment angle formed

 slope_error_new += m_new;

 // Slope error reached limit, time to

 // increment y and update slope error.

 if (slope_error_new >= 0)

 {

 y++;

 slope_error_new -= 2 * (x2 - x1);

 }

 }

 } 

 // Driver code

var x1 = 3, y1 = 2, x2 = 15, y2 = 5; 

bresenham(x1, y1, x2, y2);

// This code is contributed by Amit Katiyar

</script>  
  
---  
  
 __

 __

 **Output :**

    
    
    (3,2)
    (4,3)
    (5,3)
    (6,3)
    (7,3)
    (8,4)
    (9,4)
    (10,4)
    (11,4)
    (12,5)
    (13,5)
    (14,5)
    (15,5) 

The above explanation is to provides a rough idea behind the algorithm. For
detailed explanation and proof, readers can refer below references.  
 **Related Articles:**  

  1. Mid-Point Line Generation Algorithm
  2. DDA algorithm for line drawing

 **Reference :**  
https://csustan.csustan.edu/~tom/Lecture-Notes/Graphics/Bresenham-
Line/Bresenham-Line.pdf  
https://en.wikipedia.org/wiki/Bresenham’s_line_algorithm  
http://graphics.idav.ucdavis.edu/education/GraphicsNotes/Bresenhams-
Algorithm.pdf  
This article is contributed by **Shivam Pradhan (anuj_charm)**. If you like
GeeksforGeeks and would like to contribute, you can also write an article
using contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.  
Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


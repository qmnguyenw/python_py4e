Program to Convert Radian to Degree



Before moving to the actual solution, let’s try to find out what is a degree,
a radian, and their relations.  
 **Radian :** The radian is the standard unit of angular measure, used in many
areas of mathematics. The length of an arc of a unit circle is numerically
equal to the measurement in radians of the angle that it subtends. One radian
is just under 57.3 degrees.  
 **Degree :** A degree (in full, a degree of arc, arc degree, or arcdegree),
usually denoted by ° (the degree symbol), is a measurement of a plane angle,
defined so that a full rotation is 360 degrees.  
The relation 2pi*rad = 360° can be derived using the formula for arc length.  
An arc of a circle with the same length as the radius of that circle subtends
an angle of 1 radian. The circumference subtends an angle of 2pi radians.  
Therefore the formula is:  

    
    
    **degree = radian * (180/pi)**
    where, pi = 22/7

 **Examples:**  

    
    
    Input : radian = 20
    Output : degree = 1145.4545454545455
    Explanation: degree = 20 * (180/pi)
    
    Input : radian = 5
    Output : degree = 286.3636363636364
    Explanation : degree = 20 * (180/pi)

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Note:** In this programs, we have taken the value of pi as 3.14159 to get
standard result in all three languages.  

## C

 __

 __  
 __

 __

 __  
 __  
 __

// C code to convert radian to degree

#include <stdio.h>

// Function for convertion

double Convert(double radian){

 double pi = 3.14159;

 return(radian * (180/pi));

}

// Driver Code

int main(){

 double radian = 5.0;

 double degree = Convert(radian);

 printf("%.5lf", degree);

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

// Java code to convert radian to degree

import java.io.*;

class GFG {

 // Function for convertion

 static double Convert(double radian){

 double pi = 3.14159;

 return(radian * (180/pi));

 }

 // Driver Code

 public static void main (String[] args) {

 double radian = 5.0;

 double degree = Convert(radian);

 System.out.println("degree = "+ degree);

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

# Python code to convert radian to degree

# Function for convertion

def Convert(radian):

 pi = 3.14159

 # Simply used the formula

 degree = radian * (180/pi)

 return degree

# Driver Code

radian = 5

print("degree =",(Convert(radian)))  
  
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

// C# code to convert radian to degree.

using System;

class GFG {

 // Function for convertion

 static double Convert(double radian){

 double pi = 3.14159;

 return(radian * (180 / pi));

 }

 // Driver Code

 public static void Main () {

 double radian = 5.0;

 double degree = Convert(radian);

 Console.Write("degree = " + degree);

 }

}

// This code is contributed by Nitin Mittal.  
  
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

// PHP code to convert radian to degree

// Function for convertion

function Convert($radian)

{

 $pi = 3.14159;

 return($radian * (180 / $pi));

}

// Driver Code

$radian = 5.0;

$degree = Convert($radian);

echo( $degree);

// This code is contributed by nitin mittal

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

// Javascript code to convert radian to degree

// Function for convertion

function Convert(radian){

 let pi = 3.14159;

 return(radian * (180/pi));

}

// Driver Code

 

 let radian = 5.0;

 let degree = Convert(radian);

 document.write(degree);

// This code is contributed Mayank Tyagi

</script>  
  
---  
  
 __

 __

Output :

    
    
    286.47914

 **Reference:**  
https://en.wikipedia.org/wiki/Radian  
https://en.wikipedia.org/wiki/Degree_(angle)  

Want to learn from the best curated videos and practice problems, check out
the **C Foundation Course **for Basic to Advanced C.

  
  

  

My Personal Notes _arrow_drop_up_

Save


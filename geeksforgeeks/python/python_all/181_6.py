Program to Convert Km/hr to miles/hr and vice versa



Given a speed in km/hr, Convert it to m/hr and m/hr to km/hr.

Examples:

    
    
    Input : 150 (km/hr)
    Output : 93.21 
     
    Input : 100 (m/hr)
    Output : 160.92693917
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

The conversion formula for kph to mph is –

    
    
     **1 kilo-metre = 0.621371192 miles**

The conversion formula for mph to kph is –

    
    
     **1 miles = 1.60934 kilo-metre**

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// Cpp program for conversion of

// kmph to mph and vice versa

#include <bits/stdc++.h>

using namespace std;

 

// Function to convert kmph to mph

double kmphTOmph(double kmph)

{

 return 0.6214 * kmph;

}

// Function to convert mph to kmph

double mphTOkmph(double mph)

{

 return mph * 1.60934;

}

 

// Driver code to check the above function

int main()

{

 double kmph = 150;

 double mph = 100;

 cout << "the speed in mph is " << kmphTOmph(kmph) << endl;

 cout << "the speed in kmph is " << mphTOkmph(mph);

 

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

// Java program for the conversion

// kmph to mph and vice versa

import java.io.*;

class GFG {

 

 // Function to convert kmph to mph

 static double kmphTOmph(double kmph)

 {

 return 0.6214 * kmph;

 }

 

 // Function to convert mph to kmph

 static double mphTOkmph(double mph)

 {

 return mph * 1.60934;

 }

 // Driver code to check the above function

 public static void main(String[] args)

 {

 double kmph = 150;

 double mph = 100;

 System.out.println("speed in miles/hr is " + kmphTOmph(kmph));

 System.out.println("speed in km/hr is " + mphTOkmph(mph));

 }

}  
  
---  
  
 __

 __

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python program for the conversion

# kmph to mph and vice versa

 

# Function to convert kmph to mph

def kmphTOmph(kmph):

 mph = 0.6214 * kmph

 return mph 

 

# Function to convert mph to kmph 

def mphTOkmph(mph):

 kmph =(float)(mph * 1.60934)

 return kmph

 

 

kmph = 150

mph = 100

print "speed in miles / hr is ", kmphTOmph(kmph) 

 

print "speed in km / hr is ", mphTOkmph(mph)   
  
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

// C# program for the conversion

// kmph to mph and vice versa

using System;

 

class GFG {

 

 // Function to convert kmph to mph

 static double kmphTOmph(double kmph)

 {

 return 0.6214 * kmph;

 }

 

 // Function to convert mph to kmph

 static double mphTOkmph(double mph)

 {

 return mph * 1.60934;

 }

 

 // Driver code to check the above function

 public static void Main()

 {

 double kmph = 150;

 double mph = 100;

 Console.WriteLine("speed in miles/hr is " + kmphTOmph(kmph));

 Console.WriteLine("speed in km/hr is " + mphTOkmph(mph));

 }

}

 

// This code is contributed by vt_m  
  
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

// PHP program for conversion of 

// kmph to mph and vice versa

 

// Function to convert 

// kmph to mph

function kmphTOmph($kmph)

{

 return 0.6214 * $kmph;

}

 

// Function to convert

// mph to kmph

function mphTOkmph($mph)

{

 return $mph * 1.60934;

}

 

 // Driver Code

 $kmph = 150;

 $mph = 100;

 echo "speed in mph is " ,

 kmphTOmph($kmph),"\n";

 echo "speed in kmph is " , 

 mphTOkmph($mph);

 

// This code is contributed by anuj_67.

?>  
  
---  
  
 __

 __

Output:

    
    
    speed in miles/hr is  93.21
    speed in km/hr is  160.934
    

Want to learn from the best curated videos and practice problems, check out
the **C Foundation Course **for Basic to Advanced C.

  
  

  

My Personal Notes _arrow_drop_up_

Save


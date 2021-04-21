Program for class interval arithmetic mean



Given a class interval and frequency distribution and the task is to find
Arithmetic mean. In case of frequency distribution the raw data is arranged by
intervals having corresponding frequencies. So if we are interested to find
arithmetic mean of the data having class interval we must know the mid
variable x. This variable can be calculated by using mid point of interval.  

> Let lower limit of interval are lower_limit[] = {1, 6, 11, 16, 21}  
> Upper limit of interval are upper_limit[] = {5, 10, 15, 20, 25}  
> and frequency freq[] = {10, 20, 30, 40, 50} are given.  
> Where mid(x) = (lower[i] + upper[i]) / 2;  
> and mean = (freq[0] * mid[0] + freq[1] * mid[1] + . . . + freq[n – 1] *
> mid[n – 1]) / (freq[0] + freq[1] + . . . + freq[n-1])  
> = 2450 / 150  
> = 16.3333  
>

Examples:  

    
    
    Input : lower_limit[] = {1, 6, 11, 16, 21}
            upper_limit[] = {5, 10, 15, 20, 25}
            freq[] = {10, 20, 30, 40, 50}
    Output : 16.3333
    
    Input : lower_limit[] = {10, 20, 30, 40, 50}
            upper_limit[] = {19, 29, 39, 49, 59}
            freq[] = {15, 20, 30, 35, 40}
    Output : 38.6429

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

  

  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// CPP program to find class interval

// arithmetic mean.

#include <bits/stdc++.h>

using namespace std;

// Function to find class interval arithmetic mean.

float mean(int lower_limit[], int upper_limit[],

 int freq[], int n)

{

 float mid[n];

 float sum = 0, freqSum = 0;

 // calculate sum of frequency and sum of

 // multiplication of interval mid value

 // and frequency.

 for (int i = 0; i < n; i++) {

 mid[i] = (lower_limit[i] +

 upper_limit[i]) / 2;

 sum = sum + mid[i] * freq[i];

 freqSum = freqSum + freq[i];

 }

 return sum / freqSum;

}

// Driver function

int main()

{

 int lower_limit[] = { 1, 6, 11, 16, 21 };

 int upper_limit[] = { 5, 10, 15, 20, 25 };

 int freq[] = { 10, 20, 30, 40, 50 };

 int n = sizeof(freq) / sizeof(freq[0]);

 cout << mean(lower_limit, upper_limit, freq, n);

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

// java program to find

// class interval

import java.io.*;

class GFG {

 // Function to find class

 // interval arithmetic mean.

 static float mean(int lower_limit[],

 int upper_limit[], int freq[], int n)

 {

 float mid[] = new float[n];

 float sum = 0, freqSum = 0;

 

 // calculate sum of frequency and sum of

 // multiplication of interval mid value

 // and frequency.

 for (int i = 0; i < n; i++) {

 

 mid[i] = (lower_limit[i] +

 upper_limit[i]) / 2;

 

 sum = sum + mid[i] * freq[i];

 freqSum = freqSum + freq[i];

 }

 

 return sum / freqSum;

 }

 // Driver function

 public static void main (String[] args) {

 

 int lower_limit[] = { 1, 6, 11, 16, 21 };

 int upper_limit[] = { 5, 10, 15, 20, 25 };

 int freq[] = { 10, 20, 30, 40, 50 };

 int n = freq.length;

 

 mean(lower_limit, upper_limit, freq, n);

 System.out.println(mean(lower_limit,

 upper_limit, freq, n));

 }

}

// This code is contributed by vt_m  
  
---  
  
 __

 __

## Python 3

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 program to find class interval

# arithmetic mean.

# Function to find class interval

# arithmetic mean.

def mean(lower_limit, upper_limit, freq, n):

 mid = [0.0] * n

 sum = 0

 freqSum = 0

 # calculate sum of frequency and

 # sum of multiplication of interval

 # mid value and frequency.

 for i in range( 0, n):

 mid[i] = ((lower_limit[i] +

 upper_limit[i]) / 2)

 

 sum = sum + mid[i] * freq[i]

 freqSum = freqSum + freq[i]

 

 return sum / freqSum

# Driver function

lower_limit = [ 1, 6, 11, 16, 21 ]

upper_limit = [ 5, 10, 15, 20, 25 ]

freq = [10, 20, 30, 40, 50]

n = len(freq)

print(round(mean(lower_limit, upper_limit,

 freq, n), 4))

 

# This code is contributed by

# Smitha Dinesh Semwal  
  
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

// C# program to find

// class interval

using System;

class GFG {

 // Function to find class

 // interval arithmetic mean.

 static float mean(int []lower_limit,

 int []upper_limit, int []freq, int n)

 {

 float []mid = new float[n];

 float sum = 0, freqSum = 0;

 

 // calculate sum of frequency and sum of

 // multiplication of interval mid value

 // and frequency.

 for (int i = 0; i < n; i++) {

 

 mid[i] = (lower_limit[i] +

 upper_limit[i]) / 2;

 

 sum = sum + mid[i] * freq[i];

 freqSum = freqSum + freq[i];

 }

 

 return sum / freqSum;

 }

 

 // Driver function

 public static void Main () {

 

 int []lower_limit = { 1, 6, 11, 16, 21 };

 int []upper_limit = { 5, 10, 15, 20, 25 };

 int []freq = { 10, 20, 30, 40, 50 };

 int n = freq.Length;

 

 mean(lower_limit, upper_limit, freq, n);

 Console.WriteLine(mean(lower_limit,

 upper_limit, freq, n));

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

// PHP program to find class interval

// arithmetic mean.

// Function to find class interval

// arithmetic mean.

function mean( $lower_limit, $upper_limit,

 $freq, $n)

{

 $mid = array();

 $sum = 0; $freqSum = 0;

 // calculate sum of frequency and

 // sum of multiplication of interval

 // mid value and frequency.

 for ( $i = 0; $i <$n; $i++)

 {

 $mid[$i] = ($lower_limit[$i] +

 $upper_limit[$i]) / 2;

 $sum = $sum + $mid[$i] * $freq[$i];

 $freqSum = $freqSum + $freq[$i];

 }

 

 return $sum / $freqSum;

}

// Driver function

$lower_limit = array( 1, 6, 11, 16, 21 );

$upper_limit = array( 5, 10, 15, 20, 25 );

$freq = array( 10, 20, 30, 40, 50 );

$n = count($freq);

echo mean($lower_limit, $upper_limit,

 $freq, $n);

// This code is contributed by anuj_67.

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

// JavaScript program to find

// class interval

 // Function to find class

 // leterval arithmetic mean.

 function mean(lower_limit,

 upper_limit, freq, n)

 {

 let mid = [];

 let sum = 0, freqSum = 0;

 

 // calculate sum of frequency and sum of

 // multiplication of leterval mid value

 // and frequency.

 for (let i = 0; i < n; i++) {

 

 mid[i] = (lower_limit[i] +

 upper_limit[i]) / 2;

 

 sum = sum + mid[i] * freq[i];

 freqSum = freqSum + freq[i];

 }

 

 return sum / freqSum;

 }

// Driver Code

 let lower_limit = [ 1, 6, 11, 16, 21 ];

 let upper_limit = [ 5, 10, 15, 20, 25 ];

 let freq = [ 10, 20, 30, 40, 50 ];

 let n = freq.length;

 

 mean(lower_limit, upper_limit, freq, n);

 document.write(mean(lower_limit,

 upper_limit, freq, n));

 

 // This code is contributed by chinmoy1997pal.

</script>  
  
---  
  
 __

 __

Output:  

    
    
    16.3333

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


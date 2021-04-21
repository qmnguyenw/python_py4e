Average of Cubes of first N natural numbers



Given a positive integer **N** , the task is to find the average of cubes of
first **N** natural numbers.  
**Examples:**  

> **Input:** N = 2  
> **Output:** 4.5  
> **Explanation:**  
> For integer N = 2,  
> We hvae ( 13 \+ 23 ) = 1 + 8 = 9  
> average = 9 / 2 that is 4.5  
>  **Input:** N = 3  
> **Output:** 12  
> **Explanation:**  
> For N = 3,  
> We have ( 13 \+ 23 \+ 23 \+ 23 \+ 33 \+ 23 ) = 27 + 8 + 1 = 36  
> average = 36 / 3 that is 12  
>

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Naive Approach:** The naive approach is to find the sum of cubes of first N
natural numbers and divide it by **N**.  
Below is the implementation of above approach:  

## C

 __

 __  
 __

 __

 __  
 __  
 __

// C program for the above approach

#include <stdio.h>

// Function to find average of cubes

double findAverageOfCube(int n)

{

 // Store sum of cubes of

 // numbers in the sum

 double sum = 0;

 // Calculate sum of cubes

 int i;

 for (i = 1; i <= n; i++) {

 sum += i * i * i;

 }

 // Return average

 return sum / n;

}

// Driver Code

int main()

{

 // Given number

 int n = 3;

 // Function Call

 printf("%lf", findAverageOfCube(n));

 return 0;

}  
  
---  
  
 __

 __

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program for the above approach

#include <bits/stdc++.h>

using namespace std;

// Function to find average of cubes

double findAverageOfCube(int n)

{

 // Storing sum of cubes

 // of numbers in sum

 double sum = 0;

 // Calculate sum of cubes

 for (int i = 1; i <= n; i++) {

 sum += i * i * i;

 }

 // Return average

 return sum / n;

}

// Driver Code

int main()

{

 // Given Number

 int n = 3;

 // Function Call

 cout << findAverageOfCube(n);

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

// Java program for the above approach

import java.util.*;

import java.io.*;

class GFG{

// Function to find average of cubes

static double findAverageOfCube(int n)

{

 // Storing sum of cubes

 // of numbers in sum

 double sum = 0;

 // Calculate sum of cubes

 for (int i = 1; i <= n; i++)

 {

 sum += i * i * i;

 }

 // Return average

 return sum / n;

}

// Driver Code

public static void main(String[] args)

{

 // Given Number

 int n = 3;

 // Function Call

 System.out.print(findAverageOfCube(n));

}

}

// This code is contributed by shivanisinghss2110  
  
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

# Python3 program for the above approach

# Function to find average of cubes

def findAverageOfCube(n):

 # Storing sum of cubes

 # of numbers in sum

 sum = 0

 # Calculate sum of cubes

 for i in range(1, n + 1):

 sum += i * i * i

 # Return average

 return round(sum / n, 6)

# Driver Code

if __name__ == '__main__':

 # Given Number

 n = 3

 # Function Call

 print(findAverageOfCube(n))

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

// C# program for the above approach

using System;

class GFG{

// Function to find average of cubes

static double findAverageOfCube(int n)

{

 // Storing sum of cubes

 // of numbers in sum

 double sum = 0;

 // Calculate sum of cubes

 for (int i = 1; i <= n; i++)

 {

 sum += i * i * i;

 }

 // Return average

 return sum / n;

}

// Driver Code

public static void Main()

{

 // Given Number

 int n = 3;

 // Function Call

 Console.Write(findAverageOfCube(n));

}

}

// This code is contributed by Nidhi_biet  
  
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

// javascript program for the above approach

// Function to find average of cubes

function findAverageOfCube( n)

{

 // Store sum of cubes of

 // numbers in the sum

 let sum = 0;

 // Calculate sum of cubes

 let i;

 for (i = 1; i <= n; i++) {

 sum += i * i * i;

 }

 // Return average

 return sum / n;

}

// Driver Code

 // Given number

 let n = 3;

 // Function Call

 document.write(findAverageOfCube(n).toFixed(6));

// This code is contributed by todaysgaurav

</script>  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    12.000000


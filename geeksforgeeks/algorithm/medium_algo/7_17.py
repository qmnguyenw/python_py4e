Program to Calculate e^x by Recursion



The value of Exponential function can be calculated using Taylor Series.

    
    
    ![e^x](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-87aab1063a5654fb43ca5112b3318893_l3.png) = 1 + x/1! + ![x^2](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-bf14022db3ea4fceb345a0446aebe606_l3.png)/2! + ![x^3](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-04d548210aa7c27772c51794e6f580ec_l3.png)/3! + ......
    

To find its value using recursion, we will use static variables. For the power
of x we will use p and for factorials we will use f as static variables.  
The function shown below is used to increase the power of x.

    
    
    p = p*x 

The function below is used to find factorials.

    
    
    f = f*n

The function below is used to calculate the summation of the series.

    
    
    r+p/f

where r is the recursive call to the function.

  

  

Below is the implementation of the above idea.  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation of the approach

#include <stdio.h>

 

// Recursive Function with static

// variables p and f

double e(int x, int n)

{

 static double p = 1, f = 1;

 double r;

 

 // Termination condition

 if (n == 0)

 return 1;

 

 // Recursive call

 r = e(x, n - 1);

 

 // Update the power of x

 p = p * x;

 

 // Factorial

 f = f * n;

 

 return (r + p / f);

}

 

// Driver code

int main()

{

 int x = 4, n = 15;

 printf("%lf \n", e(x, n));

 

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

// Java implementation of the approach

import java.text.*;

 

class GFG

{

 

// Recursive Function with static

// variables p and f

static double p = 1, f = 1;

static double e(int x, int n)

{

 double r;

 

 // Termination condition

 if (n == 0)

 return 1;

 

 // Recursive call

 r = e(x, n - 1);

 

 // Update the power of x

 p = p * x;

 

 // Factorial

 f = f * n;

 

 return (r + p / f);

}

 

// Driver code

public static void main (String[] args) 

{

 int x = 4, n = 15;

 DecimalFormat df = new DecimalFormat("0.######");

 System.out.println(df.format(e(x, n)));

 

}

}

 

// This code is contributed by mits  
  
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

# Python implementation of the approach

 

# Recursive Function 

# global variables p and f

p = 1.0

f = 1.0

 

def e(x, n) :

 

 global p, f

 

 # Termination condition

 if (n == 0) :

 return 1

 

 # Recursive call

 r = e(x, n - 1)

 

 # Update the power of x

 p = p * x

 

 # Factorial

 f = f * n

 

 return (r + p / f)

 

# Driver code

 

x = 4

n = 15

print(e(x, n))

 

# This contributed by ihritik  
  
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

 

class GFG

{

 

// Recursive Function with static

// variables p and f

static double p = 1, f = 1;

static double e(int x, int n)

{

 double r;

 

 // Termination condition

 if (n == 0)

 return 1;

 

 // Recursive call

 r = e(x, n - 1);

 

 // Update the power of x

 p = p * x;

 

 // Factorial

 f = f * n;

 

 return (r + p / f);

}

 

// Driver code

static void Main()

{

 int x = 4, n = 15;

 Console.WriteLine(Math.Round(e(x, n),6));

 

}

}

 

// This code is contributed by mits  
  
---  
  
 __

 __

 **Output:**

    
    
    54.597883
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


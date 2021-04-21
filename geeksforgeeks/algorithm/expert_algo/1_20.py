Find geometric sum of the series using recursion



Given an **integer N** we need to find the geometric sum of the following
series using recursion.

>  **1 + 1/3 + 1/9 + 1/27 + … + 1/(3^n)**

 **Examples:**

    
    
    **Input** N = 5 
    **Output:** 1.49794
    
    **Input:** N = 7
    **Output:** 1.49977
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:**

In the above-mentioned problem, we are asked to use recursion. We will
calculate the last term and call recursion on the remaining n-1 terms each
time. The final sum returned is the result.

  

  

Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// CPP implementation to Find the

// geometric sum of the series using recursion

 

#include <bits/stdc++.h>

using namespace std;

 

// function to find the sum of given series

double sum(int n)

{

 // base case

 if (n == 0)

 return 1;

 

 // calculate the sum each time

 double ans = 1 / (double)pow(3, n) + sum(n - 1);

 

 // return final answer

 return ans;

}

 

// Driver code

int main()

{

 

 // integer initialisation

 int n = 5;

 

 cout << sum(n) << endl;

 

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

// JAVA implementation to Find the

// geometric sum of the series using recursion

 

import java.util.*;

 

class GFG {

 

 static double sum(int n)

 {

 // base case

 if (n == 0)

 return 1;

 

 // calculate the sum each time

 double ans = 1 / (double)Math.pow(3, n) + sum(n - 1);

 

 // return final answer

 return ans;

 }

 

 // Driver code

 public static void main(String[] args)

 {

 // integer initialisation

 int n = 5;

 

 // print result

 System.out.println(sum(n));

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

# CPP implementation to Find the

# geometric sum of the series using recursion

 

 

def sum(n):

 

 # base case 

 if n == 0:

 return 1

 

 # calculate the sum each time

 # and return final answer

 return 1 / pow(3, n) + sum(n-1)

 

n = 5;

 

print(sum(n));  
  
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

// C# implementation to Find the

// geometric sum of the series using recursion

 

using System;

 

class GFG {

 

 static double sum(int n)

 {

 // base case

 if (n == 0)

 return 1;

 

 // calculate the sum each time

 double ans = 1 / (double)Math.Pow(3, n) + sum(n - 1);

 

 // return final answer

 return ans;

 }

 

 // Driver code

 static public void Main()

 {

 int n = 5;

 

 Console.WriteLine(sum(n));

 }

}  
  
---  
  
 __

 __

 **Output:**

    
    
    1.49794
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


Difference between Recursion and Iteration



A program is called recursive when an entity calls itself. A program is call
iterative when there is a loop (or repetition).

 **Example:** Program to find the factorial of a number  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to find factorial of given number

#include<bits/stdc++.h>

using namespace std;

 

// ----- Recursion -----

// method to find factorial of given number

int factorialUsingRecursion(int n)

{

 if (n == 0)

 return 1;

 

 // recursion call

 return n * factorialUsingRecursion(n - 1);

}

 

// ----- Iteration -----

// Method to find the factorial of a given number

int factorialUsingIteration(int n)

{

 int res = 1, i;

 

 // using iteration

 for (i = 2; i <= n; i++)

 res *= i;

 

 return res;

}

 

// Driver method

int main()

{

 int num = 5;

 cout << "Factorial of " << num << 

 " using Recursion is: " <<

 factorialUsingRecursion(5) << endl;

 

 cout << "Factorial of " << num <<

 " using Iteration is: " << 

 factorialUsingIteration(5);

 

 return 0;

}

 

// This code is contributed by mits  
  
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

// Java program to find factorial of given number

class GFG {

 

 // ----- Recursion -----

 // method to find factorial of given number

 static int factorialUsingRecursion(int n)

 {

 if (n == 0)

 return 1;

 

 // recursion call

 return n * factorialUsingRecursion(n - 1);

 }

 

 // ----- Iteration -----

 // Method to find the factorial of a given number

 static int factorialUsingIteration(int n)

 {

 int res = 1, i;

 

 // using iteration

 for (i = 2; i <= n; i++)

 res *= i;

 

 return res;

 }

 

 // Driver method

 public static void main(String[] args)

 {

 int num = 5;

 System.out.println("Factorial of " + num

 + " using Recursion is: "

 + factorialUsingRecursion(5));

 

 System.out.println("Factorial of " + num

 + " using Iteration is: "

 + factorialUsingIteration(5));

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

# Python3 program to find factorial of given number

 

# ----- Recursion -----

# method to find factorial of given number

def factorialUsingRecursion(n):

 if (n == 0):

 return 1;

 

 # recursion call

 return n * factorialUsingRecursion(n - 1);

 

# ----- Iteration -----

# Method to find the factorial of a given number

def factorialUsingIteration(n):

 res = 1;

 

 # using iteration

 for i in range(2, n + 1):

 res *= i;

 

 return res;

 

# Driver method

num = 5;

print("Factorial of",num,"using Recursion is:",

 factorialUsingRecursion(5));

 

print("Factorial of",num,"using Iteration is:",

 factorialUsingIteration(5));

 

# This code is contributed by mits  
  
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

// C# program to find factorial of

// given number

using System;

 

class GFG

{

 

 // ----- Recursion -----

 // method to find factorial of 

 // given number

 static int factorialUsingRecursion(int n)

 {

 if (n == 0)

 return 1;

 

 // recursion call

 return n * factorialUsingRecursion(n - 1);

 }

 

 // ----- Iteration -----

 // Method to find the factorial of

 // a given number

 static int factorialUsingIteration(int n)

 {

 int res = 1, i;

 

 // using iteration

 for (i = 2; i <= n; i++)

 res *= i;

 

 return res;

 }

 

 // Driver Code

 public static void Main(String[] args)

 {

 int num = 5;

 Console.WriteLine("Factorial of " + num + 

 " using Recursion is: " + 

 factorialUsingRecursion(5));

 

 Console.WriteLine("Factorial of " + num + 

 " using Iteration is: " + 

 factorialUsingIteration(5));

 }

}

 

// This code has been contributed by Rajput-Ji   
  
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

// PHP program to find factorial of given number

 

 // ----- Recursion -----

 // method to find factorial of given number

 function factorialUsingRecursion($n)

 {

 if ($n == 0)

 return 1;

 

 // recursion call

 return $n * factorialUsingRecursion($n - 1);

 }

 

 // ----- Iteration -----

 // Method to find the factorial of a given number

 function factorialUsingIteration($n)

 {

 $res = 1;

 

 // using iteration

 for ($i = 2; $i <= $n; $i++)

 $res *= $i;

 

 return $res;

 }

 

 // Driver method

 $num = 5;

 print("Factorial of ".$num." using Recursion is: ".

 factorialUsingRecursion(5)."\n");

 

 print("Factorial of ".$num." using Iteration is: ".

 factorialUsingIteration(5)."\n");

 

// This code is contributed by mits

?>  
  
---  
  
 __

 __

 **Output:**

    
    
    Factorial of 5 using Recursion is: 120
    Factorial of 5 using Iteration is: 120
    

**Below are the detailed example to illustrate the difference between the
two:**

  1.  **Time Complexity:** Finding the Time complexity of Recursion is more difficult than that of Iteration.
    *  **Recursion** : Time complexity of recursion can be found by finding the value of the nth recursive call in terms of the previous calls. Thus, finding the destination case in terms of the base case, and solving in terms of the base case gives us an idea of the time complexity of recursive equations. Please see Solving Recurrences for more details.
    *  **Iteration** : Time complexity of iteration can be found by finding the number of cycles being repeated inside the loop.
  2.  **Usage:** Usage of either of these techniques is a trade-off between time complexity and size of code. If time complexity is the point of focus, and number of recursive calls would be large, it is better to use iteration. However, if time complexity is not an issue and shortness of code is, recursion would be the way to go.
    *  **Recursion** : Recursion involves calling the same function again, and hence, has a very small length of code. However, as we saw in the analysis, the time complexity of recursion can get to be exponential when there are a considerable number of recursive calls. Hence, usage of recursion is advantageous in shorter code, but higher time complexity.
    *  **Iteration** : Iteration is repetition of a block of code. This involves a larger size of code, but the time complexity is generally lesser than it is for recursion.
  3.  **Overhead:** Recursion has a large amount of Overhead as compared to Iteration.
    *  **Recursion** : Recursion has the overhead of repeated function calls, that is due to repetitive calling of the same function, the time complexity of the code increases manifold.
    *  **Iteration** : Iteration does not involve any such overhead.
  4.  **Infinite Repetition:** Infinite Repetition in recursion can lead to CPU crash but in iteration, it will stop when memory is exhausted.
    *  **Recursion** : In Recursion, Infinite recursive calls may occur due to some mistake in specifying the base condition, which on never becoming false, keeps calling the function, which may lead to system CPU crash.
    *  **Iteration** : Infinite iteration due to mistake in iterator assignment or increment, or in the terminating condition, will lead to infinite loops, which may or may not lead to system errors, but will surely stop program execution any further.

Property| Recursion| Iteration|  **Definition**|  Function calls itself.| A
set of instructions repeatedly executed.|  **Application**|  For functions.|
For loops.|  **Termination**|  Through base case, where there will be no
function call.| When the termination condition for the iterator ceases to be
satisfied.|  **Usage**|  Used when code size needs to be small, and time
complexity is not an issue.| Used when time complexity needs to be balanced
against an expanded code size.|  **Code Size**|  Smaller code size| Larger
Code Size.|  **Time Complexity**|  Very high(generally exponential) time
complexity.| Relatively lower time complexity(generally polynomial-
logarithmic).  
---|---|---  
  
Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save


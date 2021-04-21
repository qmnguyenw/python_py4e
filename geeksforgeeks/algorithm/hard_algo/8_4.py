The Two Water Jug Puzzle



You are on the side of the river. You are given a **m** liter jug and a **n**
liter jug where **0 < m < n**. Both the jugs are initially empty. The jugs
don’t have markings to allow measuring smaller quantities. You have to use the
jugs to measure d liters of water where d < n. Determine the minimum no of
operations to be performed to obtain d liters of water in one of jug.  
The operations you can perform are:

  1. Empty a Jug
  2. Fill a Jug
  3. Pour water from one jug to the other until one of the jugs is either empty or full.

Recommended: Please solve it on “ _ ** _PRACTICE_**_ ” first, before moving on
to the solution.  

There are several ways of solving this problem including BFS and DP. In this
article, an arithmetic approach to solving the problem is discussed. The
problem can be modeled by means of the Diophantine equation of the form mx +
ny = d which is solvable if and only if gcd(m, n) divides d. Also, the
solution x,y for which equation is satisfied can be given using the Extended
Euclid algorithm for GCD.  
For example, if we have a jug J1 of 5 liters (n = 5) and another jug J2 of 3
liters (m = 3) and we have to measure 1 liter of water using them. The
associated equation will be 5n + 3m = 1. First of all this problem can be
solved since gcd(3,5) = 1 which divides 1 (See this for detailed explanation).
Using the Extended Euclid algorithm, we get values of n and m for which the
equation is satisfied which are n = 2 and m = -3. These values of n, m also
have some meaning like here n = 2 and m = -3 means that we have to fill J1
twice and empty J2 thrice.  
Now to find the minimum no of operations to be performed we have to decide
which jug should be filled first. Depending upon which jug is chosen to be
filled and which to be emptied we have two different solutions and the minimum
among them would be our answer.

 **Solution 1 (Always pour from m liter jug into n liter jug)**

  1. Fill the m litre jug and empty it into n liter jug.
  2. Whenever the m liter jug becomes empty fill it.
  3. Whenever the n liter jug becomes full empty it.
  4. Repeat steps 1,2,3 till either n liter jug or the m liter jug contains d litres of water.

Each of steps 1, 2 and 3 are counted as one operation that we perform. Let us
say algorithm 1 achieves the task in C1 no of operations.

 **Solution 2 (Always pour from n liter jug into m liter jug)**

  

  

  1. Fill the n liter jug and empty it into m liter jug.
  2. Whenever the n liter jug becomes empty fill it.
  3. Whenever the m liter jug becomes full empty it.
  4. Repeat steps 1, 2 and 3 till either n liter jug or the m liter jug contains d liters of water.

Let us say solution 2 achieves the task in C2 no of operations.  
Now our final solution will be a minimum of C1 and C2.  
Now we illustrate how both of the solutions work. Suppose there are a 3 liter
jug and a 5 liter jug to measure 4 liters water so **m = 3,n = 5 and d = 4**.
The associated Diophantine equation will be 3m + 5n = 4. We us pair (x, y) to
represent amounts of water inside the 3-liter jug and 5-liter jug respectively
in each pouring step.

 **Using Solution 1, successive pouring steps are:**

    
    
    (0,0)->(3,0)->(0,3)->(3,3)->(1,5)->(1,0)->(0,1)->(3,1)->(0,4)

Hence the no of operations you need to perform are **8.**

 **Using Solution 2, successive pouring steps are:**

    
    
    (0,0)->(0,5)->(3,2)->(0,2)->(2,0)->(2,5)->(3,4)

Hence the no of operations you need to perform are **6.**  
Therefore, we would use solution 2 to measure 4 liters of water in 6
operations or moves.

Based on the explanation here is the implementation.

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to count minimum number of steps

// required to measure d litres water using jugs

// of m liters and n liters capacity.

#include <bits/stdc++.h>

using namespace std;

// Utility function to return GCD of 'a'

// and 'b'.

int gcd(int a, int b)

{

 if (b==0)

 return a;

 return gcd(b, a%b);

}

/* fromCap -- Capacity of jug from which

 water is poured

 toCap -- Capacity of jug to which

 water is poured

 d -- Amount to be measured */

int pour(int fromCap, int toCap, int d)

{

 // Initialize current amount of water

 // in source and destination jugs

 int from = fromCap;

 int to = 0;

 // Initialize count of steps required

 int step = 1; // Needed to fill "from" Jug

 // Break the loop when either of the two

 // jugs has d litre water

 while (from != d && to != d)

 {

 // Find the maximum amount that can be

 // poured

 int temp = min(from, toCap - to);

 // Pour "temp" liters from "from" to "to"

 to += temp;

 from -= temp;

 // Increment count of steps

 step++;

 if (from == d || to == d)

 break;

 // If first jug becomes empty, fill it

 if (from == 0)

 {

 from = fromCap;

 step++;

 }

 // If second jug becomes full, empty it

 if (to == toCap)

 {

 to = 0;

 step++;

 }

 }

 return step;

}

// Returns count of minimum steps needed to

// measure d liter

int minSteps(int m, int n, int d)

{

 // To make sure that m is smaller than n

 if (m > n)

 swap(m, n);

 // For d > n we cant measure the water

 // using the jugs

 if (d > n)

 return -1;

 // If gcd of n and m does not divide d

 // then solution is not possible

 if ((d % gcd(n,m)) != 0)

 return -1;

 // Return minimum two cases:

 // a) Water of n liter jug is poured into

 // m liter jug

 // b) Vice versa of "a"

 return min(pour(n,m,d), // n to m

 pour(m,n,d)); // m to n

}

// Driver code to test above

int main()

{

 int n = 3, m = 5, d = 4;

 printf("Minimum number of steps required is %d",

 minSteps(m, n, d));

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

// Java program to count minimum number of

// steps required to measure d litres water

// using jugs of m liters and n liters capacity.

import java.io.*;

class GFG{

// Utility function to return GCD of 'a'

// and 'b'.

public static int gcd(int a, int b)

{

 if (b == 0)

 return a;

 

 return gcd(b, a % b);

}

/* fromCap -- Capacity of jug from which

 water is poured

 toCap -- Capacity of jug to which

 water is poured

 d -- Amount to be measured */

public static int pour(int fromCap, int toCap,

 int d)

{

 

 // Initialize current amount of water

 // in source and destination jugs

 int from = fromCap;

 int to = 0;

 // Initialize count of steps required

 int step = 1; // Needed to fill "from" Jug

 // Break the loop when either of the two

 // jugs has d litre water

 while (from != d && to != d)

 {

 

 // Find the maximum amount that can be

 // poured

 int temp = Math.min(from, toCap - to);

 // Pour "temp" liters from "from" to "to"

 to += temp;

 from -= temp;

 // Increment count of steps

 step++;

 if (from == d || to == d)

 break;

 // If first jug becomes empty, fill it

 if (from == 0)

 {

 from = fromCap;

 step++;

 }

 // If second jug becomes full, empty it

 if (to == toCap)

 {

 to = 0;

 step++;

 }

 }

 return step;

}

// Returns count of minimum steps needed to

// measure d liter

public static int minSteps(int m, int n, int d)

{

 

 // To make sure that m is smaller than n

 if (m > n)

 {

 int t = m;

 m = n;

 n = t;

 }

 // For d > n we cant measure the water

 // using the jugs

 if (d > n)

 return -1;

 // If gcd of n and m does not divide d

 // then solution is not possible

 if ((d % gcd(n, m)) != 0)

 return -1;

 // Return minimum two cases:

 // a) Water of n liter jug is poured into

 // m liter jug

 // b) Vice versa of "a"

 return Math.min(pour(n, m, d), // n to m

 pour(m, n, d)); // m to n

}

// Driver code

public static void main(String[] args)

{

 int n = 3, m = 5, d = 4;

 System.out.println("Minimum number of " +

 "steps required is " +

 minSteps(m, n, d));

}

}

// This code is contributed by RohitOberoi  
  
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

# Python3 implementation of program to count

# minimum number of steps required to measure

# d litre water using jugs of m liters and n

# liters capacity.

def gcd(a, b):

 if b==0:

 return a

 return gcd(b, a%b)

''' fromCap -- Capacity of jug from which

 water is poured

 toCap -- Capacity of jug to which

 water is poured

 d -- Amount to be measured '''

def Pour(toJugCap, fromJugCap, d):

 # Initialize current amount of water

 # in source and destination jugs

 fromJug = fromJugCap

 toJug = 0

 # Initialize steps required

 step = 1

 while ((fromJug is not d) and (toJug is not d)):

 

 # Find the maximum amount that can be

 # poured

 temp = min(fromJug, toJugCap-toJug)

 # Pour 'temp' liter from 'fromJug' to 'toJug'

 toJug = toJug + temp

 fromJug = fromJug - temp

 step = step + 1

 if ((fromJug == d) or (toJug == d)):

 break

 # If first jug becomes empty, fill it

 if fromJug == 0:

 fromJug = fromJugCap

 step = step + 1

 # If second jug becomes full, empty it

 if toJug == toJugCap:

 toJug = 0

 step = step + 1

 

 return step

# Returns count of minimum steps needed to

# measure d liter

def minSteps(n, m, d):

 if m> n:

 temp = m

 m = n

 n = temp

 

 if (d%(gcd(n,m)) is not 0):

 return -1

 

 # Return minimum two cases:

 # a) Water of n liter jug is poured into

 # m liter jug

 return(min(Pour(n,m,d), Pour(m,n,d)))

# Driver code

if __name__ == '__main__':

 n = 3

 m = 5

 d = 4

 print('Minimum number of steps required is',

 minSteps(n, m, d))

 

# This code is contributed by Sanket Badhe  
  
---  
  
 __

 __

 **Output:**

    
    
    Minimum number of steps required is 6

 **Another detailed Explanation**
:http://web.mit.edu/neboat/Public/6.042/numbertheory1.pdf

This article is contributed by **Madhur Modi.** If you like GeeksforGeeks and
would like to contribute, you can also write an article and mail your article
to contribute@geeksforgeeks.org. See your article appearing on the
GeeksforGeeks main page and help other Geeks.  
Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


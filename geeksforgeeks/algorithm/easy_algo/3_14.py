Twisted Tower of Hanoi Problem



The basic version of the Tower of Hanoi can be found here.  
It is a twisted Tower of Hanoi problem. In which, all rules are the same with
an addition of a rule:  
 **You can not move any disk directly from the first rod to last rod** i.e.,
If you want to move a disk from the first rod to last rod then you have to
move the first rod to middle rod first and then to the last one.

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:**

  *  **Base Case:** If the number of disk is 1, then move it to the middle rod first and then move it to the last rod.
  *  **Recursive Case:** In the recursive case following steps will produce the optimal solution:(All these moves are following the rules of twisted Tower of Hanoi problem)
    1. We will move first n-1 disks to the last rod first.
    2. Then move the largest disk to the middle rod.
    3. Move first n-1 disks from the last rod to the first rod.
    4. Move the largest disk at the middle rod to the last rod.
    5. Move all n-1 disks from the first rode to the last rod.

Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation

#include <iostream>

using namespace std;

 

// Function to print the moves

void twistedTOH(int n, char first,

 char middle, char last)

{

 // Base case

 if (n == 1) {

 

 cout << "Move disk " << n

 << " from rod " << first

 << " to " << middle

 << " and then to "

 << last << endl;

 

 return;

 }

 

 // Move n-1 disks from first to last

 twistedTOH(n - 1, first, middle, last);

 

 // Move largest disk from first to middle

 cout << "Move disk " << n

 << " from rod " << first

 << " to " << middle << endl;

 

 // Move n-1 disks from last to first

 twistedTOH(n - 1, last, middle, first);

 

 // Move nth disk from middle to last

 cout << "Move disk " << n

 << " from rod " << middle

 << " to " << last << endl;

 

 // Move n-1 disks from first to last

 twistedTOH(n - 1, first, middle, last);

}

 

// Driver's Code

int main()

{

 // Number of disks

 int n = 2;

 

 // Rods are in order

 // first(A), middle(B), last(C)

 twistedTOH(n, 'A', 'B', 'C');

 

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

import java.util.*;

 

class GFG

{

 

// Function to print the moves

static void twistedTOH(int n, char first,

 char middle, char last)

{

 // Base case

 if (n == 1)

 {

 

 System.out.println("Move disk " + n + " from rod " +

 first + " to " + middle + 

 " and then to " + last);

 

 return;

 }

 

 // Move n-1 disks from first to last

 twistedTOH(n - 1, first, middle, last);

 

 // Move largest disk from first to middle

 System.out.println("Move disk " + n + 

 " from rod " + first + 

 " to " + middle);

 

 // Move n-1 disks from last to first

 twistedTOH(n - 1, last, middle, first);

 

 // Move nth disk from middle to last

 System.out.println("Move disk " + n + 

 " from rod " + middle + 

 " to " + last);

 

 // Move n-1 disks from first to last

 twistedTOH(n - 1, first, middle, last);

}

 

// Driver Code

public static void main(String[] args)

{

 // Number of disks

 int n = 2;

 

 // Rods are in order

 // first(A), middle(B), last(C)

 twistedTOH(n, 'A', 'B', 'C');

}

}

 

// This code is contributed by PrinciRaj1992  
  
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

# Python3 implementation of above approach

 

# Function to print the moves 

def twistedTOH(n, first, middle, last): 

 

 # Base case 

 if (n == 1): 

 

 print("Move disk", n, "from rod", first, 

 "to", middle, "and then to", last) 

 

 return

 

 # Move n-1 disks from first to last 

 twistedTOH(n - 1, first, middle, last) 

 

 # Move largest disk from first to middle 

 print("Move disk", n, "from rod",

 first, "to", middle) 

 

 # Move n-1 disks from last to first 

 twistedTOH(n - 1, last, middle, first) 

 

 # Move nth disk from middle to last 

 print("Move disk", n, "from rod", 

 middle, "to", last) 

 

 # Move n-1 disks from first to last 

 twistedTOH(n - 1, first, middle, last)

 

# Driver Code 

 

# Number of disks 

n = 2

 

# Rods are in order 

# first(A), middle(B), last(C) 

twistedTOH(n, 'A', 'B', 'C') 

 

# This code is contributed by

# divyamohan123  
  
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

 

// Function to print the moves

static void twistedTOH(int n, char first,

 char middle, char last)

{

 // Base case

 if (n == 1)

 {

 Console.WriteLine("Move disk " + n + " from rod " +

 first + " to " + middle + 

 " and then to " + last);

 

 return;

 }

 

 // Move n-1 disks from first to last

 twistedTOH(n - 1, first, middle, last);

 

 // Move largest disk from first to middle

 Console.WriteLine("Move disk " + n + 

 " from rod " + first + 

 " to " + middle);

 

 // Move n-1 disks from last to first

 twistedTOH(n - 1, last, middle, first);

 

 // Move nth disk from middle to last

 Console.WriteLine("Move disk " + n + 

 " from rod " + middle + 

 " to " + last);

 

 // Move n-1 disks from first to last

 twistedTOH(n - 1, first, middle, last);

}

 

// Driver Code

public static void Main(String[] args)

{

 // Number of disks

 int n = 2;

 

 // Rods are in order

 // first(A), middle(B), last(C)

 twistedTOH(n, 'A', 'B', 'C');

}

}

 

// This code is contributed by PrinciRaj1992  
  
---  
  
 __

 __

 **Output:**

    
    
    Move disk 1 from rod A to B and then to C
    Move disk 2 from rod A to B
    Move disk 1 from rod C to B and then to A
    Move disk 2 from rod B to C
    Move disk 1 from rod A to B and then to C
    

Recurrence formula:

    
    
    T(n) = T(n-1) + 1 + T(n-1) + 1 + T(n-1)
         = 3 * T(n-1) + 2
    
    where **n** is the number of disks.
    

By solving this recurrence the **Time Complexity will be O(3 n)**.

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save


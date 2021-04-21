Maximize big when both big and small can be exchanged



Given **N** Big Candies and **M** Small Candies. One Big Candy can be bought
by paying **X** small candies. Alternatively, one big candy can be sold for
**Y** small candies. The task is to find the maximum number of big candies
that can be bought.

 **Examples:**

>  **Input:** N = 3, M = 10, X = 4, Y = 2  
>  **Output:** 5  
> 8 small candies are exchanged for 2 big candies.
>
>  **Input:** N = 3, M = 10, X = 1, Y = 2  
>  **Output:** 16  
> Sell all the initial big candies to get 6 small candies.  
> Now 16 small candies can be exchanged for 16 big candies.

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

In first example, Big candies cannot be sold for profit. So, only the
remaining small candies can be exchanged for big candies.  
In second example, Big candies can be sold for profit.

  

  

 **Approach:** If initial big candies can be sold for profit i.e. **X < Y**
then sell the big candies and update the count of small and big candies. Then,
sell all of the updated small candies in order to buy big candies.

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation of the approach

#include <iostream>

using namespace std;

 

 // Function to return the maximum big 

 // candies that can be bought

 int max_candies(int bigCandies, 

 int smallCandies,int X, int Y)

 {

 // If initial big candies 

 // can be sold for profit

 if (X < Y) 

 {

 smallCandies += Y * bigCandies;

 bigCandies = 0;

 }

 

 // Update big candies that can be bought

 bigCandies += (smallCandies / X);

 

 return bigCandies;

 }

 

 // Driver code

 int main() 

 {

 int N = 3, M = 10;

 int X = 4, Y = 2;

 cout << (max_candies(N, M, X, Y));

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

class GFG {

 

 // Function to return the maximum big candies

 // that can be bought

 static int max_candies(int bigCandies, int smallCandies,

 int X, int Y)

 {

 // If initial big candies can be sold for profit

 if (X < Y) {

 

 smallCandies += Y * bigCandies;

 bigCandies = 0;

 }

 

 // Update big candies that can be bought

 bigCandies += (smallCandies / X);

 

 return bigCandies;

 }

 

 // Driver code

 public static void main(String[] args)

 {

 int N = 3, M = 10;

 int X = 4, Y = 2;

 

 System.out.println(max_candies(N, M, X, Y));

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

# Python3 implementation of the approach

 

# Function to return the maximum big candies

# that can be bought

def max_candies(bigCandies, smallCandies, X, Y):

 

 # If initial big candies can 

 # be sold for profit

 if(X < Y): 

 

 smallCandies += Y * bigCandies

 bigCandies = 0

 

 # Update big candies that can be bought

 bigCandies += (smallCandies // X)

 

 return bigCandies

 

# Driver code

N = 3

M = 10

X = 4

Y = 2

print(max_candies(N, M, X, Y))

 

# This code is contributed by Code_Mech  
  
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

 

 // Function to return the maximum 

 // big candies that can be bought

 static int max_candies(int bigCandies,

 int smallCandies,

 int X, int Y)

 {

 // If initial big candies

 // can be sold for profit

 if (X < Y)

 {

 smallCandies += Y * bigCandies;

 bigCandies = 0;

 }

 

 // Update big candies that can be bought

 bigCandies += (smallCandies / X);

 

 return bigCandies;

 }

 

 // Driver code

 static public void Main ()

 {

 int N = 3, M = 10;

 int X = 4, Y = 2;

 Console.WriteLine(max_candies(N, M, X, Y));

 }

}

 

// This Code is contributed by ajit...   
  
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

// PHP implementation of the approach

 

// Function to return the maximum big 

// candies that can be bought

function max_candies($bigCandies, 

 $smallCandies, $X, $Y)

{

 // If initial big candies can be

 // sold for profit

 if ($X < $Y) 

 {

 

 $smallCandies += $Y * $bigCandies;

 $bigCandies = 0;

 }

 

 // Update big candies that can be bought

 $bigCandies += (int)($smallCandies / $X);

 

 return $bigCandies;

}

 

// Driver code

$N = 3;

$M = 10;

$X = 4;

$Y = 2;

 

echo (max_candies($N, $M, $X, $Y));

 

// This code is contributed by akt_mit

?>  
  
---  
  
 __

 __

 **Output:**

    
    
    5
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


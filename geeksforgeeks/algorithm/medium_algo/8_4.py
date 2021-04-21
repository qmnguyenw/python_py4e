Minimum possible final health of the last monster in a game



Given **N** monsters, each monster has initial health **h[i]** which is an
integer. A monster is alive if its health is greater than **0**. In each turn
a random monster kills another random monster, the monster which is attacked,
its health reduces by the amount of health of the attacking monster. This
process is continued until a single monster is left. What will be the minimum
possible health of the last remained monster. In others words, the task is to
play the game in such a way that monster which is left in the end has the
least possible health.

 **Examples:**

>  **Input:** h[] = {2, 14, 28, 56}  
>  **Output:** 2  
> When only the first monster keeps on attacking the remaining 3 monsters, the
> final health of the last monster will be 2, which is minimum.
>
>  **Input:** h[] = {7, 17, 9, 100, 25}  
>  **Output:** 1
>
>  **Input:** h[] = {5, 5, 5}  
>  **Output:** 5
>
>  
>
>
>  
>

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** It can be observed from the problem that one has to find a
certain value of health of the monster, let’s say k which can kill other
monsters including self. Once this crucial observation is made problem becomes
easy. Suppose we have two monsters with health **h1** and **h2** , and let’s
say **h2 > h1**. We can see that in a random choice, the optimal way would be
to pick a monster with lower health and reduce the health of the other monster
till its health becomes less than the health of the attacking monster. After
that we will pick the second monster whose health has became less than **h1**
and the process will continue till only one monster is left. So at last we
will be left with the minimum value which would be **gcd(h1, h2)**. This gcd
method can be extended for all the monsters.  
 **So our resultant minimum possible health of the monster will be the gcd of
all the health of given monsters i.e. H(min) = gcd(h1, h2, …, hn).**

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

#include <bits/stdc++.h>

using namespace std;

 

// Function to return the gcd of two numbers

int gcd(int a, int b)

{

 if (a == 0)

 return b;

 return gcd(b % a, a);

}

 

// Function to return the minimum

// possible health for the monster

int solve(int* health, int n)

{

 // gcd of first and second element

 int currentgcd = gcd(health[0], health[1]);

 

 // gcd for all subsequent elements

 for (int i = 2; i < n; ++i) {

 currentgcd = gcd(currentgcd, health[i]);

 }

 return currentgcd;

}

 

// Driver code

int main()

{

 int health[] = { 4, 6, 8, 12 };

 int n = sizeof(health) / sizeof(health[0]);

 cout << solve(health, n);

 

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

 

// Function to return the gcd of two numbers

static int gcd(int a, int b)

{

 if (a == 0)

 return b;

 return gcd(b % a, a);

}

 

// Function to return the minimum

// possible health for the monster

static int solve(int health[], int n)

{

 // gcd of first and second element

 int currentgcd = gcd(health[0], health[1]);

 

 // gcd for all subsequent elements

 for (int i = 2; i < n; ++i) 

 {

 currentgcd = gcd(currentgcd, health[i]);

 }

 return currentgcd;

}

 

// Driver code

public static void main(String args[])

{

 int health[] = { 4, 6, 8, 12 };

 int n = health.length;

 System.out.println(solve(health, n));

}

}

 

// This code is contributed by

// Surendra_Gangwar  
  
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

 

# Function to return the gcd of two numbers

def gcd(a, b):

 

 if (a == 0):

 return b

 return gcd(b % a, a)

 

# Function to return the minimum

# possible health for the monster

def solve(health, n):

 

 # gcd of first and second element

 currentgcd = gcd(health[0], health[1])

 

 # gcd for all subsequent elements

 for i in range(2, n):

 currentgcd = gcd(currentgcd, 

 health[i])

 return currentgcd

 

# Driver code

health = [4, 6, 8, 12]

n = len(health)

print(solve(health, n))

 

# This code is contributed by mohit kumar  
  
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

 

// Function to return the gcd of two numbers 

static int gcd(int a, int b) 

{ 

 if (a == 0) 

 return b; 

 return gcd(b % a, a); 

} 

 

// Function to return the minimum 

// possible health for the monster 

static int solve(int []health, int n) 

{ 

 // gcd of first and second element 

 int currentgcd = gcd(health[0], health[1]); 

 

 // gcd for all subsequent elements 

 for (int i = 2; i < n; ++i) 

 { 

 currentgcd = gcd(currentgcd, health[i]); 

 } 

 return currentgcd; 

} 

 

// Driver code 

public static void Main(String []args) 

{ 

 int []health = { 4, 6, 8, 12 }; 

 int n = health.Length; 

 Console.WriteLine(solve(health, n)); 

} 

} 

 

// This code is contributed by Arnab Kundu  
  
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

 

// Function to return the gcd of two numbers

function gcd($a, $b)

{

 if ($a == 0)

 return $b;

 return gcd($b % $a, $a);

}

 

// Function to return the minimum

// possible health for the monster

function solve($health, $n)

{

 // gcd of first and second element

 $currentgcd = gcd($health[0], 

 $health[1]);

 

 // gcd for all subsequent elements

 for ($i = 2; $i < $n; ++$i)

 {

 $currentgcd = gcd($currentgcd,

 $health[$i]);

 }

 return $currentgcd;

}

 

// Driver code

$health = array(4, 6, 8, 12);

$n = sizeof($health);

echo solve($health, $n);

 

// This code is contributed by Akanksha Rai

?>  
  
---  
  
 __

 __

 **Output:**

    
    
    2
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


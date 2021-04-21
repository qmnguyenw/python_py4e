Find distinct integers for a triplet with given product



Given an integer **X** , the task is to find the three distinct integers
greater than **1** i.e. **A** , **B** and **C** such that **(A * B * C) = X**.
If no such triplet exists then print **-1**.  
 **Examples:**

> **Input:** X = 64  
> **Output:** 2 4 8  
> (2 * 4 * 8) = 64  
>  **Input:** X = 32  
> **Output:** -1  
> No such triplet exists.

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:** Suppose we have a triplet **(A, B, C)**. Notice that, for their
product to be equal to **X** , each of the integer has to be a factor of
**X**. So, store all the factors of **X** in **O(sqrt(X))** time using the
approach discussed in this article.  
There will be at most **sqrt(X)** factors now. Next, iterate on each factor by
running two loops, one picking **A** and another picking **B**. Now if this
triplet is valid i.e. **C = X / (A * B)** where **C** is also a factor of
**X**. To check that, store all the factors in an unordered_set. If a valid
triplet is found then print the triplet else print **-1**.  
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

// Function to find the required triplets

void findTriplets(int x)

{

 // To store the factors

 vector<int> fact;

 unordered_set<int> factors;

 // Find factors in sqrt(x) time

 for (int i = 2; i <= sqrt(x); i++) {

 if (x % i == 0) {

 fact.push_back(i);

 if (x / i != i)

 fact.push_back(x / i);

 factors.insert(i);

 factors.insert(x / i);

 }

 }

 bool found = false;

 int k = fact.size();

 for (int i = 0; i < k; i++) {

 // Choose a factor

 int a = fact[i];

 for (int j = 0; j < k; j++) {

 // Choose another factor

 int b = fact[j];

 // These conditions need to be

 // met for a valid triplet

 if ((a != b) && (x % (a * b) == 0)

 && (x / (a * b) != a)

 && (x / (a * b) != b)

 && (x / (a * b) != 1)) {

 // Print the valid triplet

 cout << a << " " << b << " "

 << (x / (a * b));

 found = true;

 break;

 }

 }

 // Triplet found

 if (found)

 break;

 }

 // Triplet not found

 if (!found)

 cout << "-1";

}

// Driver code

int main()

{

 int x = 105;

 findTriplets(x);

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

// Function to find the required triplets

static void findTriplets(int x)

{

 // To store the factors

 Vector<Integer> fact = new Vector<Integer>();

 HashSet<Integer> factors = new HashSet<Integer>();

 // Find factors in Math.sqrt(x) time

 for (int i = 2; i <= Math.sqrt(x); i++)

 {

 if (x % i == 0)

 {

 fact.add(i);

 if (x / i != i)

 fact.add(x / i);

 factors.add(i);

 factors.add(x / i);

 }

 }

 boolean found = false;

 int k = fact.size();

 for (int i = 0; i < k; i++)

 {

 // Choose a factor

 int a = fact.get(i);

 for (int j = 0; j < k; j++)

 {

 // Choose another factor

 int b = fact.get(j);

 // These conditions need to be

 // met for a valid triplet

 if ((a != b) && (x % (a * b) == 0)

 && (x / (a * b) != a)

 && (x / (a * b) != b)

 && (x / (a * b) != 1))

 {

 // Print the valid triplet

 System.out.print(a+ " " + b + " "

 + (x / (a * b)));

 found = true;

 break;

 }

 }

 // Triplet found

 if (found)

 break;

 }

 // Triplet not found

 if (!found)

 System.out.print("-1");

}

// Driver code

public static void main(String[] args)

{

 int x = 105;

 findTriplets(x);

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

# Python3 implementation of the approach

from math import sqrt

# Function to find the required triplets

def findTriplets(x) :

 # To store the factors

 fact = [];

 factors = set();

 # Find factors in sqrt(x) time

 for i in range(2, int(sqrt(x))) :

 if (x % i == 0) :

 fact.append(i);

 

 if (x / i != i) :

 fact.append(x // i);

 

 factors.add(i);

 factors.add(x // i);

 found = False;

 k = len(fact);

 

 for i in range(k) :

 # Choose a factor

 a = fact[i];

 

 for j in range(k) :

 # Choose another factor

 b = fact[j];

 # These conditions need to be

 # met for a valid triplet

 if ((a != b) and (x % (a * b) == 0)

 and (x / (a * b) != a)

 and (x / (a * b) != b)

 and (x / (a * b) != 1)) :

 # Print the valid triplet

 print(a,b,x // (a * b));

 found = True;

 break;

 

 # Triplet found

 if (found) :

 break;

 # Triplet not found

 if (not found) :

 print("-1");

# Driver code

if __name__ == "__main__" :

 x = 105;

 findTriplets(x);

# This code is contributed by AnkitRai01  
  
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

using System.Collections.Generic;

class GFG

{

// Function to find the required triplets

static void findTriplets(int x)

{

 // To store the factors

 List<int> fact = new List<int>();

 HashSet<int> factors = new HashSet<int>();

 // Find factors in Math.Sqrt(x) time

 for (int i = 2; i <= Math.Sqrt(x); i++)

 {

 if (x % i == 0)

 {

 fact.Add(i);

 if (x / i != i)

 fact.Add(x / i);

 factors.Add(i);

 factors.Add(x / i);

 }

 }

 bool found = false;

 int k = fact.Count;

 for (int i = 0; i < k; i++)

 {

 // Choose a factor

 int a = fact[i];

 for (int j = 0; j < k; j++)

 {

 // Choose another factor

 int b = fact[j];

 // These conditions need to be

 // met for a valid triplet

 if ((a != b) && (x % (a * b) == 0)

 && (x / (a * b) != a)

 && (x / (a * b) != b)

 && (x / (a * b) != 1))

 {

 // Print the valid triplet

 Console.Write(a+ " " + b + " "

 + (x / (a * b)));

 found = true;

 break;

 }

 }

 // Triplet found

 if (found)

 break;

 }

 // Triplet not found

 if (!found)

 Console.Write("-1");

}

// Driver code

public static void Main(String[] args)

{

 int x = 105;

 findTriplets(x);

}

}

// This code is contributed by 29AjayKumar  
  
---  
  
 __

 __

 **Output:**

    
    
    3 5 7

**Time Complexity:** O(N), N=X

 **Auxiliary Space:** O(N)

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save


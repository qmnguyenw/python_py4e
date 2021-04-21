Find all the possible remainders when N is divided by all positive integers
from 1 to N+1



Given a large integer **N** , the task is to find all the possible remainders
when **N** is divided by all the positive integers from **1** to **N + 1**.

 **Examples:**

>  **Input:** N = 5  
>  **Output:** 0 1 2 5  
> 5 % 1 = 0  
> 5 % 2 = 1  
> 5 % 3 = 2  
> 5 % 4 = 1  
> 5 % 5 = 0  
> 5 % 6 = 5
>
>  **Input:** N = 11  
>  **Output:** 0 1 2 3 5 11

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Naive approach:** Run a loop from **1** to **N + 1** and return all the
unique remainders found when dividing **N** by any integer from the range. But
this approach is not efficient for larger values of **N**.

  

  

 **Efficient approach:** It can be observed that one part of the answer will
always contain numbers between **0** to **ceil(sqrt(n))**. It can be proven by
running the naive algorithm on smaller values of **N** and checking the
remainders obtained or by solving the equation **ceil(N / k) = x** or **x ≤ (N
/ k) < x + 1** where **x** is one of the remainders for all integers **k**
when **N** is divided by **k** for **k** from **1** to **N + 1**.  
The solution to the above inequality is nothing but integers **k** from **(N /
(x + 1), N / x]** of length **N / x – N / (x + 1) = N / (x 2 \+ x)**.
Therefore, iterate from **k = 1** to **ceil(sqrt(N))** and store all the
unique **N % k**. What if the above **k** is greater than **ceil(sqrt(N))**?
They will always correspond to values **0 ≤ x < ceil(sqrt(N))**. So, again
start storing remainders from **N / (ceil(sqrt(N)) – 1** to **0** and return
the final answer with all the possible remainders.

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

 

typedef long long int ll;

 

// Function to find all the distinct

// remainders when n is divided by

// all the elements from

// the range [1, n + 1]

void findRemainders(ll n)

{

 

 // Set will be used to store

 // the remainders in order

 // to eliminate duplicates

 set<ll> vc;

 

 // Find the remainders

 for (ll i = 1; i <= ceil(sqrt(n)); i++)

 vc.insert(n / i);

 for (ll i = n / ceil(sqrt(n)) - 1; i >= 0; i--)

 vc.insert(i);

 

 // Print the contents of the set

 for (auto it : vc)

 cout << it << " ";

}

 

// Driver code

int main()

{

 ll n = 5;

 

 findRemainders(n);

 

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

 

// Function to find all the distinct

// remainders when n is divided by

// all the elements from

// the range [1, n + 1]

static void findRemainders(long n)

{

 

 // Set will be used to store

 // the remainders in order

 // to eliminate duplicates

 HashSet<Long> vc = new HashSet<Long>();

 

 // Find the remainders

 for (long i = 1; i <= Math.ceil(Math.sqrt(n)); i++)

 vc.add(n / i);

 for (long i = (long) (n / Math.ceil(Math.sqrt(n)) - 1); 

 i >= 0; i--)

 vc.add(i);

 

 // Print the contents of the set

 for (long it : vc)

 System.out.print(it+ " ");

}

 

// Driver code

public static void main(String[] args)

{

 long n = 5;

 

 findRemainders(n);

}

}

 

// This code is contributed by 29AjayKumar  
  
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

from math import ceil, floor, sqrt

 

# Function to find all the distinct

# remainders when n is divided by

# all the elements from

# the range [1, n + 1]

def findRemainders(n):

 

 # Set will be used to store

 # the remainders in order

 # to eliminate duplicates

 vc = dict()

 

 # Find the remainders

 for i in range(1, ceil(sqrt(n)) + 1):

 vc[n // i] = 1

 for i in range(n // ceil(sqrt(n)) - 1, -1,
-1):

 vc[i] = 1

 

 # Print the contents of the set

 for it in sorted(vc):

 print(it, end = " ")

 

# Driver code

n = 5

 

findRemainders(n)

 

# This code is contributed by Mohit Kumar  
  
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

 

// Function to find all the distinct

// remainders when n is divided by

// all the elements from

// the range [1, n + 1]

static void findRemainders(long n)

{

 

 // Set will be used to store

 // the remainders in order

 // to eliminate duplicates

 List<long> vc = new List<long>();

 

 // Find the remainders

 

 for (long i = 1; i <= Math.Ceiling(Math.Sqrt(n)); i++)

 vc.Add(n / i);

 for (long i = (long) (n / Math.Ceiling(Math.Sqrt(n)) - 1); 

 i >= 0; i--)

 vc.Add(i);

 vc.Reverse();

 

 // Print the contents of the set

 foreach (long it in vc)

 Console.Write(it + " ");

}

 

// Driver code

public static void Main(String[] args)

{

 long n = 5;

 

 findRemainders(n);

}

}

 

// This code is contributed by PrinciRaj1992  
  
---  
  
 __

 __

 **Output:**

    
    
    0 1 2 5
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


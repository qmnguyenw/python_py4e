Check if there exists a prime number which gives Y after being repeatedly
subtracted from X



Given two integers **X** and **Y** where **X > Y**, the task is to check if
there exists an prime number **P** such that if **P** is repeatedly subtracted
from **X** then it gives **Y**.

 **Examples:**

>  **Input:** X = 100, Y = 98  
>  **Output:** Yes  
> (100 – (2 * 1) = 98)
>
>  **Input:** X = 45, Y = 31  
>  **Output:** Yes  
> (45 – (7 * 2)) = 31

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Naive approach:** Run a loop for every integer starting from **2** to
**x**. If the current number is a prime number and it meets the criteria given
in the question, then it is the required number.

  

  

 **Efficient approach:** Notice that for a valid prime **p** , **x – k * p =
y** or **x – y = k * p**. Suppose, **p = 2** then **(x – y) = 2, 4, 6, …**
(all even numbers). This means if **(x – y)** is even then the answer is
always true. If **(x – y)** is an odd number other than **1** , it will always
have a prime factor. Either it itself is a prime or it is a product of a
smaller prime and some other integers. So the answer is True for all odd
numbers other than **1**.  
What if **(x – y) = 1** , it is neither a prime nor composite. So this is the
only case where the answer is false.

Below is the implementation of the approach:  

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

 

// Function that returns true if any

// prime number satisfies

// the given conditions

bool isPossible(int x, int y)

{

 

 // No such prime exists

 if ((x - y) == 1)

 return false;

 

 return true;

}

 

// Driver code

int main()

{

 int x = 100, y = 98;

 

 if (isPossible(x, y))

 cout << "Yes";

 else

 cout << "No";

 

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

 

// Function that returns true if any

// prime number satisfies

// the given conditions

static boolean isPossible(int x, int y)

{

 

 // No such prime exists

 if ((x - y) == 1)

 return false;

 

 return true;

}

 

// Driver code

public static void main(String[] args)

{

 int x = 100, y = 98;

 

 if (isPossible(x, y))

 System.out.print("Yes");

 else

 System.out.print("No");

}

}

 

// This code is contributed by Rajput-Ji  
  
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

 

# Function that returns true if any

# prime number satisfies

# the given conditions

def isPossible(x, y):

 

 # No such prime exists

 if ((x - y) == 1):

 return False

 

 return True

 

# Driver code

x = 100

y = 98

 

if (isPossible(x, y)):

 print("Yes")

else:

 print("No")

 

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

 

class GFG

{

 

// Function that returns true if any

// prime number satisfies

// the given conditions

static bool isPossible(int x, int y)

{

 

 // No such prime exists

 if ((x - y) == 1)

 return false;

 

 return true;

}

 

// Driver code

public static void Main(String[] args)

{

 int x = 100, y = 98;

 

 if (isPossible(x, y))

 Console.Write("Yes");

 else

 Console.Write("No");

}

}

 

// This code is contributed by 29AjayKumar  
  
---  
  
 __

 __

 **Output:**

    
    
    Yes
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


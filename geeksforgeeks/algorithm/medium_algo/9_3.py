Maximum Bitwise AND pair from given range



Given a range **[L, R]** , the task is to find a pair **(X, Y)** such that **L
≤ X < Y ≤ R** and **X & Y** is maximum among all the possible pairs then print
the bitwise AND of the found pair.

 **Examples:**

>  **Input:** L = 1, R = 9  
>  **Output:** 8  
> In all the possible pairs, pair **(8, 9)** gives the maximum value for
> bitwise AND.
>
>  **Input:** L = 523641, R = 985624  
>  **Output:** 985622

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Naive Approach:** Iterate from **L** to **R** and check the bitwise AND for
every possible pair and print the maximum value in the end.

  

  

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

 

// Function to return the maximum bitwise AND

// possible among all the possible pairs

int maxAND(int L, int R)

{

 int maximum = L & R;

 

 for (int i = L; i < R; i++)

 for (int j = i + 1; j <= R; j++)

 

 // Maximum among all (i, j) pairs

 maximum = max(maximum, (i & j));

 

 return maximum;

}

 

// Driver code

int main()

{

 int L = 1, R = 632;

 cout << maxAND(L, R);

 

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

class GFG

{

 

// Function to return the maximum bitwise AND

// possible among all the possible pairs

static int maxAND(int L, int R)

{

 int maximum = L & R;

 

 for (int i = L; i < R; i++)

 for (int j = i + 1; j <= R; j++)

 

 // Maximum among all (i, j) pairs

 maximum = Math.max(maximum, (i & j));

 

 return maximum;

}

 

// Driver code

public static void main(String[] args) 

{

 int L = 1, R = 632;

 System.out.println(maxAND(L, R));

}

}

 

// This code contributed by Rajput-Ji  
  
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

# Python 3 implementation of the approach

 

# Function to return the maximum bitwise AND

# possible among all the possible pairs

def maxAND(L, R):

 maximum = L & R

 

 for i in range(L, R, 1):

 for j in range(i + 1, R + 1, 1):

 

 # Maximum among all (i, j) pairs

 maximum = max(maximum, (i & j))

 

 return maximum

 

# Driver code

if __name__ == '__main__':

 L = 1

 R = 632

 print(maxAND(L, R))

 

# This code is contributed by

# Surendra_Gangwar  
  
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

 

// Function to return the maximum bitwise AND 

// possible among all the possible pairs 

static int maxAND(int L, int R) 

{ 

 int maximum = L & R; 

 

 for (int i = L; i < R; i++) 

 for (int j = i + 1; j <= R; j++) 

 

 // Maximum among all (i, j) pairs 

 maximum = Math.Max(maximum, (i & j)); 

 

 return maximum; 

} 

 

// Driver code 

public static void Main(String[] args) 

{ 

 int L = 1, R = 632; 

 Console.WriteLine(maxAND(L, R)); 

} 

} 

 

// This code has been contributed by 29AjayKumar  
  
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

 

// Function to return the maximum bitwise AND

// possible among all the possible pairs

function maxAND($L, $R)

{

 $maximum = $L & $R;

 

 for ($i = $L; $i < $R; $i++)

 for ($j = $i + 1; $j <= $R; $j++)

 

 // Maximum among all (i, j) pairs

 $maximum = max($maximum, ($i & $j));

 

 return $maximum;

}

 

// Driver code

$L = 1; $R = 632;

echo(maxAND($L, $R));

 

// This code contributed by Code_Mech.

?>  
  
---  
  
 __

 __

 **Output:**

    
    
    630
    

**Time Complexity:** O(n2)

 **Efficient Approach:** If we carefully observe in the range [L, R], the
maximum AND is possible either between the **AND of (R) and (R – 1)** or **AND
of (R – 1) and (R – 2)**.

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

 

// Function to return the maximum bitwise AND

// possible among all the possible pairs

int maxAND(int L, int R)

{

 

 // If there is only a single value

 // in the range [L, R]

 if (L == R)

 return L;

 

 // If there are only two values

 // in the range [L, R]

 else if ((R - L) == 1)

 return (R & L);

 else {

 if (((R - 1) & R) > ((R - 2) & (R - 1)))

 return ((R - 1) & R);

 else

 return ((R - 2) & (R - 1));

 }

}

 

// Driver code

int main()

{

 int L = 1, R = 632;

 cout << maxAND(L, R);

 

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

class GfG 

{ 

 

// Function to return the maximum bitwise AND 

// possible among all the possible pairs 

static int maxAND(int L, int R) 

{ 

 

 // If there is only a single value 

 // in the range [L, R] 

 if (L == R) 

 return L; 

 

 // If there are only two values 

 // in the range [L, R] 

 else if ((R - L) == 1) 

 return (R & L); 

 else { 

 if (((R - 1) & R) > ((R - 2) & (R - 1))) 

 return ((R - 1) & R); 

 else

 return ((R - 2) & (R - 1)); 

 } 

} 

 

// Driver code 

public static void main(String[] args) 

{ 

 int L = 1, R = 632; 

 System.out.println(maxAND(L, R)); 

}

} 

 

// This code is contributed by

// Prerna Saini  
  
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

 

# Function to return the maximum bitwise AND

# possible among all the possible pairs

def maxAND(L, R):

 

 # If there is only a single value

 # in the range [L, R]

 if (L == R):

 return L;

 

 # If there are only two values

 # in the range [L, R]

 elif ((R - L) == 1):

 return (R & L);

 else:

 if (((R - 1) & R) >

 ((R - 2) & (R - 1))):

 return ((R - 1) & R);

 else:

 return ((R - 2) & (R - 1));

 

# Driver code

L = 1;

R = 632;

print(maxAND(L, R));

 

# This code contributed by PrinciRaj1992   
  
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

 

class GfG 

{ 

 

 // Function to return the maximum bitwise AND 

 // possible among all the possible pairs 

 static int maxAND(int L, int R) 

 { 

 

 // If there is only a single value 

 // in the range [L, R] 

 if (L == R) 

 return L; 

 

 // If there are only two values 

 // in the range [L, R] 

 else if ((R - L) == 1) 

 return (R & L); 

 else

 { 

 if (((R - 1) & R) > ((R - 2) & (R - 1))) 

 return ((R - 1) & R); 

 else

 return ((R - 2) & (R - 1)); 

 } 

 } 

 

 // Driver code 

 public static void Main() 

 { 

 int L = 1, R = 632; 

 Console.WriteLine(maxAND(L, R)); 

 } 

} 

 

// This code is contributed by Ryuga  
  
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

 

// Function to return the maximum bitwise AND

// possible among all the possible pairs

function maxAND($L, $R)

{

 

 // If there is only a single value

 // in the range [L, R]

 if ($L == $R)

 return $L;

 

 // If there are only two values

 // in the range [L, R]

 else if (($R - $L) == 1)

 return ($R & $L);

 else

 {

 if ((($R - 1) & $R) > (($R - 2) & ($R - 1)))

 return (($R - 1) & $R);

 else

 return (($R - 2) & ($R - 1));

 }

}

 

// Driver code

$L = 1;

$R = 632;

echo maxAND($L, $R);

 

// This code is contributed by mits

?>  
  
---  
  
 __

 __

 **Output:**

    
    
    630
    

**Time Complexity:** O(1)

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


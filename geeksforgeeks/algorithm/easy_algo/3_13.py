Color all boxes in line such that every M consecutive boxes are unique



Given **N** boxes that are kept in a straight line and **M** colors such that
**M ≤ N**. The position of the boxes cannot be changed. The task is to find
the number of ways to color the boxes such that if any **M** consecutive set
of boxes is considered then the color of each box is unique. Since the answer
could be large, print the answer modulo 109 \+ 7.

 **Example:**

>  **Input:** N = 3, M = 2  
>  **Output:** 2  
> If colours are c1 and c2 the only possible  
> ways are {c1, c2, c1} and {c2, c1, c2}.
>
>  **Input:** N = 13, M = 10  
>  **Output:** 3628800

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** The number of ways are independent of **N** and only depends on
**M**. First **M** boxes can be coloured with the given **M** colours without
repetition then the same pattern can be repeated for the next set of **M**
boxes. This can be done for every permutation of the colours. So, the number
of ways to color the boxes will be **M!**.

  

  

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

 

#define MOD 1000000007

 

// Function to return (m! % MOD)

int modFact(int n, int m)

{

 int result = 1;

 for (int i = 1; i <= m; i++)

 result = (result * i) % MOD;

 

 return result;

}

 

// Driver code

int main()

{

 int n = 3, m = 2;

 

 cout << modFact(n, m);

 

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

// Java implementation of the above approach

class GFG

{

 static final int MOD = 1000000007;

 

 // Function to return (m! % MOD) 

 static int modFact(int n, int m) 

 { 

 int result = 1; 

 for (int i = 1; i <= m; i++) 

 result = (result * i) % MOD; 

 

 return result; 

 } 

 

 // Driver code 

 public static void main (String[] args) 

 { 

 int n = 3, m = 2; 

 

 System.out.println(modFact(n, m)); 

 } 

}

 

// This code is contributed by AnkitRai01  
  
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

MOD = 1000000007

 

# Function to return (m! % MOD) 

def modFact(n, m) :

 

 result = 1

 for i in range(1, m + 1) : 

 result = (result * i) % MOD 

 

 return result 

 

# Driver code 

n = 3

m = 2

 

print(modFact(n, m)) 

 

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

// C# implementation of the above approach

using System;

class GFG

{

 const int MOD = 1000000007;

 

 // Function to return (m! % MOD) 

 static int modFact(int n, int m) 

 { 

 int result = 1; 

 for (int i = 1; i <= m; i++) 

 result = (result * i) % MOD; 

 

 return result; 

 } 

 

 // Driver code 

 public static void Main() 

 { 

 int n = 3, m = 2; 

 

 Console.WriteLine(modFact(n, m)); 

 } 

}

 

// This code is contributed by Nidhi_biet  
  
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


All possible values of floor(N/K) for all values of K



Given a function **f(K) = floor(N/K)** ( **N >0** and **K >0**), the task is
to find all possible values of **f(K)** for a given **N** where **K** takes
all values in the range **[1, Inf]**.  
 **Examples:**  

> **Input:** N = 5  
> **Output:** 0 1 2 5  
> **Explanation:**  
> 5 divide 1 = 5  
> 5 divide 2 = 2  
> 5 divide 3 = 1  
> 5 divide 4 = 1  
> 5 divide 5 = 1  
> 5 divide 6 = 0  
> 5 divide 7 = 0  
> So all possible distinct values of f(k) are {0, 1, 2, 5}.  
>  **Input:** N = 11  
> **Output:** 0 1 2 3 5 11  
> **Explanation:**  
> 11 divide 1 = 11  
> 11 divide 2 = 5  
> 11 divide 3 = 3  
> 11 divide 4 = 2  
> 11 divide 5 = 2  
> 11 divide 6 = 1  
> 11 divide 7 = 1  
> …  
> …  
> 11 divided 11 = 1  
> 11 divides 12 = 0  
> So all possible distinct values of f(k) are {0, 1, 2, 3, 5, 11}.  
>

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Naive Approach:**  
The **simplest approach** to the iterate over **[1, N+1]** and store in a
**set**, all values of **(N/i)** ( 1 ? i ? N + 1) to avoid duplication.  
Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ Program for the

// above approach 

#include <bits/stdc++.h> 

using namespace std; 

 

// Function to print all 

// possible values of 

// floor(N/K) 

void allQuotients(int N) 

{ 

 set<int> s; 

 

 // loop from 1 to N+1 

 for (int k = 1; k <= N + 1; k++) { 

 s.insert(N / k); 

 } 

 

 for (auto it : s) 

 cout << it << " "; 

} 

 

int main() 

{ 

 int N = 5; 

 allQuotients(N); 

 

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

// Java program for the above approach

import java.util.*; 

 

class GFG{ 

 

// Function to print all 

// possible values of 

// Math.floor(N/K) 

static void allQuotients(int N) 

{ 

 HashSet<Integer> s = new HashSet<Integer>(); 

 

 // loop from 1 to N+1 

 for(int k = 1; k <= N + 1; k++) 

 { 

 s.add(N / k); 

 } 

 

 for(int it : s) 

 System.out.print(it + " "); 

} 

 

// Driver code 

public static void main(String[] args) 

{ 

 int N = 5; 

 

 allQuotients(N); 

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

# Python3 program for the above approach

 

# Function to print all possible 

# values of floor(N/K)

def allQuotients(N):

 

 s = set()

 

 # Iterate from 1 to N+1

 for k in range(1, N + 2):

 s.add(N // k)

 

 for it in s:

 print(it, end = ' ')

 

# Driver code

if __name__ == '__main__':

 

 N = 5

 

 allQuotients(N)

 

# This code is contributed by himanshu77  
  
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

// C# program for the above approach

using System;

using System.Collections.Generic;

 

class GFG{

 

// Function to print all possible

// values of Math.floor(N/K) 

static void allQuotients(int N) 

{ 

 SortedSet<int> s = new SortedSet<int>(); 

 

 // Loop from 1 to N+1 

 for(int k = 1; k <= N + 1; k++) 

 { 

 s.Add(N / k); 

 } 

 

 foreach(int it in s) 

 { 

 Console.Write(it + " "); 

 }

} 

 

// Driver code

static void Main()

{

 int N = 5; 

 

 allQuotients(N);

}

}

 

// This code is contributed by divyeshrabadiya07  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    0 1 2 5
    
    


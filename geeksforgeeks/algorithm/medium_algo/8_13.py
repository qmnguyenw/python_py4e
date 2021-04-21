Number of ways to pair people



Given that there are p people in a party. Each person can either join dance as
a single individual or as a pair with any other. The task is to find the
number of different ways in which p people can join the dance.

 **Examples:**

    
    
    **Input :** p = 3
    **Output :** 4
    Let the three people be P1, P2 and P3
    Different ways are: {P1, P2, P3}, {{P1, P2}, P3},
    {{P1, P3}, P2} and {{P2, P3}, P1}.
    
    **Input :** p = 2
    **Output :** 2
    The groups are: {P1, P2} and {{P1, P2}}.
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** The idea is to use dynamic programming to solve this problem.
There are two situations: Either the person join dance as single individual or
as a pair. For the first case the problem reduces to finding the solution for
p-1 people. For the second case, there are p-1 choices to select an individual
for pairing and after selecting an individual for pairing the problem reduces
to finding solution for p-2 people as two people among p are already paired.

So the formula for dp is:

    
    
    **dp[p] = dp[p-1] + (p-1) * dp[p-2]**.
    

Below is the implementation of the above approach:  

## C++

  

  

 __

 __  
 __

 __

 __  
 __  
 __

// CPP program to find number of ways to

// pair people in party

 

#include <bits/stdc++.h>

using namespace std;

 

// Function to find number of ways to

// pair people in party

int findWaysToPair(int p)

{

 // To store count of number of ways.

 int dp[p + 1];

 

 dp[1] = 1;

 dp[2] = 2;

 

 // Using the recurrence defined find

 // count for different values of p.

 for (int i = 3; i <= p; i++) {

 dp[i] = dp[i - 1] + (i - 1) * dp[i - 2];

 }

 

 return dp[p];

}

 

// Driver code

int main()

{

 int p = 3;

 cout << findWaysToPair(p);

 return 0;

}  
  
---  
  
 __

 __


Find minimum number of steps to reach the end of String



Given a binary string **str** of length **N** and an integer **K** , the task
is to find the minimum number of steps required to move from **str[0]** to
**str[N – 1]** with the following moves:

  1. From an index **i** , the only valid moves are **i + 1** , **i + 2** and **i + K**
  2. An index **i** can only be visited if **str[i] = ‘1’**

 **Examples:**

>  **Input:** str = “101000011”, K = 5  
>  **Output:** 3  
> str[0] -> str[2] -> str[7] -> str[8]
>
>  **Input:** str = “1100000100111”, K = 6  
>  **Output:** -1  
> There is no possible path.
>
>  **Input:** str = “10101010101111010101”, K = 4  
>  **Output:** 6
>
>  
>
>
>  
>

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** The idea is to use dynamic programming to solve the problem.

  * It is given that for any index **i** , it is possible to move to an index i+1, i+2 or i+K.
  * One of the three possibilities will give the required result that is the minimum number of steps to reach the end.
  * Therefore, the dp[] array is created and is filled in a bottom-up manner.

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

 

// Function to return the minimum number

// of steps to reach the end

int minSteps(string str, int n, int k)

{

 

 // If the end can't be reached

 if (str[n - 1] == '0')

 return -1;

 

 // Already at the end

 if (n == 1)

 return 0;

 

 // If the length is 2 or 3 then the end

 // can be reached in a single step

 if (n < 4)

 return 1;

 

 // For the other cases, solve the problem

 // using dynamic programming

 int dp[n];

 

 // It requires no move from the

 // end to reach the end

 dp[n - 1] = 0;

 

 // From the 2nd last and the 3rd last

 // index, only a single move is required

 dp[n - 2] = 1;

 dp[n - 3] = 1;

 

 // Update the answer for every index

 for (int i = n - 4; i >= 0; i--) {

 

 // If the current index is not reachable

 if (str[i] == '0')

 continue;

 

 // To store the minimum steps required

 // from the current index

 int steps = INT_MAX;

 

 // If it is a valid move then update

 // the minimum steps required

 if (i + k < n && str[i + k] == '1')

 steps = min(steps, dp[i + k]);

 

 if (str[i + 1] == '1')

 steps = min(steps, dp[i + 1]);

 

 if (str[i + 2] == '1')

 steps = min(steps, dp[i + 2]);

 

 // Update the minimum steps requried starting

 // from the current index

 dp[i] = (steps == INT_MAX) ? steps : 1 + steps;

 }

 

 // Cannot reach the end starting from str[0]

 if (dp[0] == INT_MAX)

 return -1;

 

 // Return the minimum steps required

 return dp[0];

}

 

// Driver code

int main()

{

 string str = "101000011";

 int n = str.length();

 int k = 5;

 

 cout << minSteps(str, n, k);

 

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

 

 final static int INT_MAX = Integer.MAX_VALUE ;

 

 // Function to return the minimum number 

 // of steps to reach the end 

 static int minSteps(String str, int n, int k) 

 { 

 

 // If the end can't be reached 

 if (str.charAt(n - 1) == '0') 

 return -1; 

 

 // Already at the end 

 if (n == 1) 

 return 0; 

 

 // If the length is 2 or 3 then the end 

 // can be reached in a single step 

 if (n < 4) 

 return 1; 

 

 // For the other cases, solve the problem 

 // using dynamic programming 

 int dp[] = new int[n]; 

 

 // It requires no move from the 

 // end to reach the end 

 dp[n - 1] = 0; 

 

 // From the 2nd last and the 3rd last 

 // index, only a single move is required 

 dp[n - 2] = 1; 

 dp[n - 3] = 1; 

 

 // Update the answer for every index 

 for (int i = n - 4; i >= 0; i--) 

 { 

 

 // If the current index is not reachable 

 if (str.charAt(i) == '0') 

 continue; 

 

 // To store the minimum steps required 

 // from the current index 

 int steps =INT_MAX ; 

 

 // If it is a valiINT_MAXd move then update 

 // the minimum steps required 

 if (i + k < n && str.charAt(i + k) == '1') 

 steps = Math.min(steps, dp[i + k]); 

 

 if (str.charAt(i + 1) == '1') 

 steps = Math.min(steps, dp[i + 1]); 

 

 if (str.charAt(i + 2) == '1') 

 steps = Math.min(steps, dp[i + 2]); 

 

 // Update the minimum steps requried starting 

 // from the current index 

 dp[i] = (steps == INT_MAX) ? steps : 1 + steps; 

 } 

 

 // Cannot reach the end starting from str[0] 

 if (dp[0] == INT_MAX) 

 return -1; 

 

 // Return the minimum steps required 

 return dp[0]; 

 } 

 

 // Driver code 

 public static void main(String[] args) 

 { 

 String str = "101000011"; 

 int n = str.length(); 

 int k = 5; 

 

 System.out.println(minSteps(str, n, k)); 

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

import sys

 

INT_MAX = sys.maxsize;

 

# Function to return the minimum number 

# of steps to reach the end 

def minSteps(string , n, k) :

 

 # If the end can't be reached 

 if (string[n - 1] == '0') :

 return -1; 

 

 # Already at the end 

 if (n == 1) :

 return 0; 

 

 # If the length is 2 or 3 then the end 

 # can be reached in a single step 

 if (n < 4) :

 return 1; 

 

 # For the other cases, solve the problem 

 # using dynamic programming 

 dp = [0] * n; 

 

 # It requires no move from the 

 # end to reach the end 

 dp[n - 1] = 0; 

 

 # From the 2nd last and the 3rd last 

 # index, only a single move is required 

 dp[n - 2] = 1; 

 dp[n - 3] = 1; 

 

 # Update the answer for every index 

 for i in range(n - 4, -1, -1) :

 

 # If the current index is not reachable 

 if (string[i] == '0') :

 continue; 

 

 # To store the minimum steps required 

 # from the current index 

 steps = INT_MAX; 

 

 # If it is a valid move then update 

 # the minimum steps required 

 if (i + k < n and string[i + k] == '1') :

 steps = min(steps, dp[i + k]); 

 

 if (string[i + 1] == '1') :

 steps = min(steps, dp[i + 1]); 

 

 if (string[i + 2] == '1') :

 steps = min(steps, dp[i + 2]); 

 

 # Update the minimum steps requried starting 

 # from the current index 

 dp[i] = steps if (steps == INT_MAX) else (1 +
steps); 

 

 # Cannot reach the end starting from str[0] 

 if (dp[0] == INT_MAX) :

 return -1; 

 

 # Return the minimum steps required 

 return dp[0]; 

 

# Driver code 

if __name__ == "__main__" : 

 

 string = "101000011"; 

 n = len(string); 

 k = 5; 

 

 print(minSteps(string, n, k)); 

 

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

 

class GFG 

{

 

 static int INT_MAX = int.MaxValue ;

 

 // Function to return the minimum number 

 // of steps to reach the end 

 static int minSteps(string str, int n, int k) 

 { 

 

 // If the end can't be reached 

 if (str[n - 1] == '0') 

 return -1; 

 

 // Already at the end 

 if (n == 1) 

 return 0; 

 

 // If the length is 2 or 3 then the end 

 // can be reached in a single step 

 if (n < 4) 

 return 1; 

 

 // For the other cases, solve the problem 

 // using dynamic programming 

 int []dp = new int[n]; 

 

 // It requires no move from the 

 // end to reach the end 

 dp[n - 1] = 0; 

 

 // From the 2nd last and the 3rd last 

 // index, only a single move is required 

 dp[n - 2] = 1; 

 dp[n - 3] = 1; 

 

 // Update the answer for every index 

 for (int i = n - 4; i >= 0; i--) 

 { 

 

 // If the current index is not reachable 

 if (str[i] == '0') 

 continue; 

 

 // To store the minimum steps required 

 // from the current index 

 int steps = INT_MAX ; 

 

 // If it is a valiINT_MAXd move then update 

 // the minimum steps required 

 if (i + k < n && str[i + k] == '1') 

 steps = Math.Min(steps, dp[i + k]); 

 

 if (str[i + 1] == '1') 

 steps = Math.Min(steps, dp[i + 1]); 

 

 if (str[i + 2] == '1') 

 steps = Math.Min(steps, dp[i + 2]); 

 

 // Update the minimum steps requried starting 

 // from the current index 

 dp[i] = (steps == INT_MAX) ? steps : 1 + steps; 

 } 

 

 // Cannot reach the end starting from str[0] 

 if (dp[0] == INT_MAX) 

 return -1; 

 

 // Return the minimum steps required 

 return dp[0]; 

 } 

 

 // Driver code 

 public static void Main() 

 { 

 string str = "101000011"; 

 int n = str.Length; 

 int k = 5; 

 

 Console.WriteLine(minSteps(str, n, k)); 

 } 

}

 

// This code is contributed by AnkitRai01  
  
---  
  
 __

 __

 **Output:**

    
    
    3
    

**Time Complexity:** O(N) where N is the length of the string.

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


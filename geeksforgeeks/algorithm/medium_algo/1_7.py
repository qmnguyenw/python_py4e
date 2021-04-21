Largest odd divisor Game to check which player wins



Two players are playing a game starting with a **number n**. In each turn, a
player can make any one of the subsequent moves:  

  * Divide n by any of its **odd divisors** greater than 1. Divisors of a number include the number itself.
  * Subtract 1 from n if n > k where k < n.

Player 1 makes the primary move, print “yes” if player 1 wins otherwise print
“no” if both play optimally. The player who is unable to make a move loses the
game.  
 **Examples:**  

> **Input:** n = 12, k = 1  
> **Output:** Yes  
> **Explanation:**  
> Player 1 first move = 12 / 3 = 4  
> Player 2 first move = 4 – 1 = 3  
> Player 1 second move = 3 / 3 = 1  
> Player 2 second move can be done and hence he looses.  
> **Input:** n = 1, k = 1  
>  **Output:** No  
> **Explanation:**  
> Player 1 first move is not possible because n = k and hence player 1 looses.

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** The idea is to analyze the problem for the following 3 cases:  

  

  

  * When integer **n is odd** , player 1 can divide n by itself, since it is odd and hence n / n = 1, and player 2 loses. Note that here n = 1 is an exception.
  * When integer **n is even and has no odd divisors greater than 1** then n is of the form 2x. Player 1 is bound to subtract it by 1 making n odd. So if x > 1, player 2 wins. Note that for x = 1, n – 1 is equal to 1, so Player 1 wins.
  * When **integer n is even and has odd divisors** , the task remains to check if n is divisible by 4 then player 1 can divide n by its largest odd factor after which n becomes of the form 2x where x > 1, so again player 1 wins.
  * Otherwise, n must be of form **2 * p** , where p is odd. If **p is prime** , player 1 loses since he can either reduce n by 1 or divide it by p both of which would be losing for him. If **p is not prime** then p must be of the form p1 * p2 where p1 is prime and p2 is any odd number > 1, for which player 1 can win by dividing n by p2.

Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation to find the

// Largest Odd Divisor Game to

// check which player wins

#include <bits/stdc++.h>

using namespace std;

 

// Function to find the

// Largest Odd Divisor Game to

// check which player wins

void findWinner(int n, int k)

{

 int cnt = 0;

 

 // Check if n == 1 then

 // player 2 will win

 if (n == 1)

 cout << "No" << endl;

 

 // Check if n == 2 or n is odd

 else if ((n & 1) or n == 2)

 cout << "Yes" << endl;

 

 else {

 int tmp = n;

 int val = 1;

 

 // While n is greater than k and

 // divisible by 2 keep

 // incrementing tha val

 while (tmp > k and tmp % 2 == 0) {

 tmp /= 2;

 val *= 2;

 }

 

 // Loop to find greatest

 // odd divisor

 for (int i = 3; i <= sqrt(tmp); i++) {

 while (tmp % i == 0) {

 cnt++;

 tmp /= i;

 }

 }

 if (tmp > 1)

 cnt++;

 

 // Check if n is a power of 2

 if (val == n)

 cout << "No" << endl;

 

 else if (n / tmp == 2 and cnt == 1)

 cout << "No" << endl;

 

 // Check if cnt is not one

 // then player 1 wins

 else

 cout << "Yes" << endl;

 }

}

 

// Driver code

int main()

{

 long long n = 1, k = 1;

 findWinner(n, k);

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

// Java implementation to find the

// Largest Odd Divisior Game to

// check which player wins

import java.util.*;

 

class GFG{

 

// Function to find the

// Largest Odd Divisior Game to

// check which player wins

public static void findWinner(int n, int k)

{

 int cnt = 0;

 

 // Check if n == 1 then

 // player 2 will win

 if (n == 1)

 System.out.println("No");

 

 // Check if n == 2 or n is odd

 else if ((n & 1) != 0 || n == 2)

 System.out.println("Yes");

 

 else

 {

 int tmp = n;

 int val = 1;

 

 // While n is greater than k and

 // divisible by 2 keep

 // incrementing tha val

 while (tmp > k && tmp % 2 == 0)

 {

 tmp /= 2;

 val *= 2;

 }

 

 // Loop to find greatest

 // odd divisor

 for(int i = 3; 

 i <= Math.sqrt(tmp); i++)

 {

 while (tmp % i == 0)

 {

 cnt++;

 tmp /= i;

 }

 }

 if (tmp > 1)

 cnt++;

 

 // Check if n is a power of 2

 if (val == n)

 System.out.println("No");

 

 else if (n / tmp == 2 && cnt == 1)

 System.out.println("No");

 

 // Check if cnt is not one

 // then player 1 wins

 else

 System.out.println("Yes");

 }

}

 

// Driver code

public static void main(String[] args)

{

 int n = 1, k = 1;

 

 findWinner(n, k);

}

}

 

// This code is contributed by jrishabh99   
  
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

# Python3 implementation to find

# the Largest Odd Divisor Game 

# to check which player wins 

import math 

 

# Function to find the Largest 

# Odd Divisor Game to check

# which player wins 

def findWinner(n, k): 

 

 cnt = 0; 

 

 # Check if n == 1 then 

 # player 2 will win 

 if (n == 1):

 print("No"); 

 

 # Check if n == 2 or n is odd 

 elif ((n & 1) or n == 2):

 print("Yes"); 

 

 else:

 tmp = n; 

 val = 1; 

 

 # While n is greater than k and 

 # divisible by 2 keep 

 # incrementing tha val 

 while (tmp > k and tmp % 2 == 0): 

 tmp //= 2; 

 val *= 2; 

 

 # Loop to find greatest 

 # odd divisor 

 for i in range(3, int(math.sqrt(tmp)) + 1): 

 while (tmp % i == 0):

 cnt += 1; 

 tmp //= i; 

 

 if (tmp > 1):

 cnt += 1; 

 

 # Check if n is a power of 2 

 if (val == n):

 print("No"); 

 

 elif (n / tmp == 2 and cnt == 1):

 print("No"); 

 

 # Check if cnt is not one 

 # then player 1 wins 

 else:

 print("Yes"); 

 

# Driver code 

if __name__ == "__main__": 

 

 n = 1; k = 1; 

 

 findWinner(n, k); 

 

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

// C# implementation to find the

// Largest Odd Divisior Game to

// check which player wins

using System;

 

class GFG{

 

// Function to find the

// Largest Odd Divisior Game to

// check which player wins

public static void findWinner(int n, int k)

{

 int cnt = 0;

 

 // Check if n == 1 then

 // player 2 will win

 if (n == 1)

 Console.Write("No");

 

 // Check if n == 2 or n is odd

 else if ((n & 1) != 0 || n == 2)

 Console.Write("Yes");

 

 else

 {

 int tmp = n;

 int val = 1;

 

 // While n is greater than k and

 // divisible by 2 keep

 // incrementing tha val

 while (tmp > k && tmp % 2 == 0)

 {

 tmp /= 2;

 val *= 2;

 }

 

 // Loop to find greatest

 // odd divisor

 for(int i = 3; 

 i <= Math.Sqrt(tmp); i++)

 {

 while (tmp % i == 0)

 {

 cnt++;

 tmp /= i;

 }

 }

 if (tmp > 1)

 cnt++;

 

 // Check if n is a power of 2

 if (val == n)

 Console.Write("No");

 

 else if (n / tmp == 2 && cnt == 1)

 Console.Write("No");

 

 // Check if cnt is not one

 // then player 1 wins

 else

 Console.Write("Yes");

 }

}

 

// Driver code

public static void Main(string[] args)

{

 int n = 1, k = 1;

 

 findWinner(n, k);

}

}

// This code is contributed by rutvik_56  
  
---  
  
 __

 __

 **Output:**

    
    
    No
    

_**Time Complexity:** O(sqrt(n)) _  
_**Auxiliary Space:** O(1)_  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


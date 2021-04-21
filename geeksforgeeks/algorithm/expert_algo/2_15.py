Restore a permutation from the given helper array



Given an array **Q[]** of size **N – 1** such that each **Q[i] = P[i + 1] –
P[i]** where **P[]** is the premutation of the first **N** natural numbers,
the task is to find this permutation. If no valid permutation **P[]** can be
found then print **-1**.

 **Examples:**

>  **Input:** Q[] = {-2, 1}  
>  **Output:** 3 1 2
>
>  **Input:** Q[] = {1, 1, 1, 1}  
>  **Output:** 1 2 3 4 5

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** This is a mathematical algorithmic question. Lets denote **P[i]
= x**. Therefore **P[i + 1] = P[i] + (P[i + 1] – P[i]) = x + Q[i]** (Since
**Q[i] = P[i + 1] – P[i]** ).  
Therefore, **P[i + 2]= P[i] + (P[i + 1] – P[i]) + (P[i + 2] – P[i + 1]) = x +
Q[i] + Q[i + 1]**. Observe, the pattern forming here. **P** is nothing but
**[x, x + Q[1], x + Q[1] + Q[2] + … + x + Q[1] + Q[2] + … + Q[n – 1]]** where
**x = P[i]** which is still unknown.

  

  

Lets have a permutation **P’** where **P'[i] = P[i] – x**. Therefore, **P’ =
[0, Q[1], Q[1] + Q[2], Q[1] + Q[2] + Q[3], …, Q[1] + Q[2] + … + Q[n – 1]]**.

To find **x** , lets find the smallest element in **P’**. Let it be **P'[k]**.
Therefore, **x = 1 – P'[k]**. This is because, the original permutation **P**
has integers from **1** to **n** and so **1** can be the minimum element in
**P**. After finding **x** , add **x** to each **P’** to get the original
permutation **P**.

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

 

// Function to find the required permutation

void findPerm(int Q[], int n)

{

 

 int minval = 0, qsum = 0;

 for (int i = 0; i < n - 1; i++) {

 

 // Each element in P' is like a

 // cumulative sum in Q

 qsum += Q[i];

 

 // minval is the minimum

 // value in P'

 if (qsum < minval)

 minval = qsum;

 }

 vector<int> P(n);

 P[0] = 1 - minval;

 

 // To check if each entry in P

 // is from the range [1, n]

 bool permFound = true;

 for (int i = 0; i < n - 1; i++) {

 P[i + 1] = P[i] + Q[i];

 

 // Invalid permutation

 if (P[i + 1] > n || P[i + 1] < 1) {

 permFound = false;

 break;

 }

 }

 

 // If a valid permutation exists

 if (permFound) {

 

 // Print the permutation

 for (int i = 0; i < n; i++) {

 cout << P[i] << " ";

 }

 }

 else {

 

 // No valid permutation

 cout << -1;

 }

}

 

// Driver code

int main()

{

 int Q[] = { -2, 1 };

 int n = 1 + (sizeof(Q) / sizeof(int));

 

 findPerm(Q, n);

 

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

 

// Function to find the required permutation

static void findPerm(int Q[], int n)

{

 

 int minval = 0, qsum = 0;

 for (int i = 0; i < n - 1; i++) 

 {

 

 // Each element in P' is like a

 // cumulative sum in Q

 qsum += Q[i];

 

 // minval is the minimum

 // value in P'

 if (qsum < minval)

 minval = qsum;

 }

 int []P = new int[n];

 P[0] = 1 - minval;

 

 // To check if each entry in P

 // is from the range [1, n]

 boolean permFound = true;

 for (int i = 0; i < n - 1; i++) 

 {

 P[i + 1] = P[i] + Q[i];

 

 // Invalid permutation

 if (P[i + 1] > n || P[i + 1] < 1)

 {

 permFound = false;

 break;

 }

 }

 

 // If a valid permutation exists

 if (permFound)

 {

 

 // Print the permutation

 for (int i = 0; i < n; i++) 

 {

 System.out.print(P[i]+ " ");

 }

 }

 else

 {

 

 // No valid permutation

 System.out.print(-1);

 }

}

 

// Driver code

public static void main(String[] args)

{

 int Q[] = { -2, 1 };

 int n = 1 + Q.length;

 

 findPerm(Q, n);

 

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

 

# Function to find the required permutation 

def findPerm(Q, n) : 

 

 minval = 0; qsum = 0; 

 for i in range(n - 1) :

 

 # Each element in P' is like a 

 # cumulative sum in Q 

 qsum += Q[i]; 

 

 # minval is the minimum 

 # value in P' 

 if (qsum < minval) :

 minval = qsum; 

 

 P = [0]*n; 

 P[0] = 1 - minval; 

 

 # To check if each entry in P 

 # is from the range [1, n] 

 permFound = True; 

 

 for i in range(n - 1) :

 P[i + 1] = P[i] + Q[i]; 

 

 # Invalid permutation 

 if (P[i + 1] > n or P[i + 1] < 1) :

 permFound = False; 

 break; 

 

 # If a valid permutation exists 

 if (permFound) :

 

 # Print the permutation 

 for i in range(n) :

 print(P[i],end=" "); 

 else :

 

 # No valid permutation 

 print(-1); 

 

# Driver code 

if __name__ == "__main__" : 

 

 Q = [ -2, 1 ]; 

 n = 1 + len(Q) ;

 

 findPerm(Q, n); 

 

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

 

// Function to find the required permutation

static void findPerm(int []Q, int n)

{

 

 int minval = 0, qsum = 0;

 for (int i = 0; i < n - 1; i++) 

 {

 

 // Each element in P' is like a

 // cumulative sum in Q

 qsum += Q[i];

 

 // minval is the minimum

 // value in P'

 if (qsum < minval)

 minval = qsum;

 }

 int []P = new int[n];

 P[0] = 1 - minval;

 

 // To check if each entry in P

 // is from the range [1, n]

 bool permFound = true;

 for (int i = 0; i < n - 1; i++) 

 {

 P[i + 1] = P[i] + Q[i];

 

 // Invalid permutation

 if (P[i + 1] > n || P[i + 1] < 1)

 {

 permFound = false;

 break;

 }

 }

 

 // If a valid permutation exists

 if (permFound)

 {

 

 // Print the permutation

 for (int i = 0; i < n; i++) 

 {

 Console.Write(P[i]+ " ");

 }

 }

 else

 {

 

 // No valid permutation

 Console.Write(-1);

 }

}

 

// Driver code

public static void Main(String[] args)

{

 int []Q = { -2, 1 };

 int n = 1 + Q.Length;

 

 findPerm(Q, n);

}

}

 

// This code is contributed by PrinciRaj1992  
  
---  
  
 __

 __

 **Output:**

    
    
    3 1 2
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


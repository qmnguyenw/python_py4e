Count of integers of the form (2^x * 3^y) in the range [L, R]



Given a range **[L, R]** where **0 ≤ L ≤ R ≤ 10 8**. The task is to find the
count of integers from the given range that can be represented as **(2 x) *
(3y)**.

 **Examples:**

>  **Input:** L = 1, R = 10  
>  **Output:** 7  
> The numbers are 1, 2, 3, 4, 6, 8 and 9
>
>  **Input:** L = 100, R = 200  
>  **Output:** 5  
> The numbers are 108, 128, 144, 162 and 192

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** Since the numbers, which are powers of two and three, quickly
grow, you can use the following algorithm. For all the numbers of the form
**(2 x) * (3y)** in the range **[1, 10 8]** store them in a vector. Later sort
the vector. Then the required answer can be calculated using an upper bound.
Pre-calculating these integers will be helpful when there are a number of
queries of the form **[L, R]**.

  

  

Below is the implementation of the above approach:

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

 

#define MAXI (int)(1e8)

 

// To store all valid integers

vector<int> v;

 

// Function to find all the integers of the

// form (2^x * 3^y) in the range [0, 1000000]

void precompute()

{

 

 // To store powers of 2 and 3

 // initialized to 2^0 and 3^0

 int x = 1, y = 1;

 

 // While current power of 2

 // is within the range

 while (x <= MAXI) {

 

 // While number is within the range

 while (x * y <= MAXI) {

 

 // Add the number to the vector

 v.push_back(x * y);

 

 // Next power of 3

 y *= 3;

 }

 

 // Next power of 2

 x *= 2;

 

 // Reset to 3^0

 y = 1;

 }

 

 // Sort the vector

 sort(v.begin(), v.end());

}

 

// Function to find the count of numbers

// in the range [l, r] which are

// of the form (2^x * 3^y)

void countNum(int l, int r)

{

 cout << upper_bound(v.begin(), v.end(), r)

 - upper_bound(v.begin(), v.end(), l - 1);

}

 

// Driver code

int main()

{

 int l = 100, r = 200;

 

 // Pre-compute all the valid numbers

 precompute();

 

 countNum(l, r);

 

 return 0;

}  
  
---  
  
 __

 __

 **Output:**

    
    
    5
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


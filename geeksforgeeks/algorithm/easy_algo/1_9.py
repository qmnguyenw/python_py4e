Find all powers of 2 less than or equal to a given number



Given a positive number **N** , the task is to find out all the perfect powers
of two which are less than or equal to the given number **N**.

 **Examples:**

>  **Input:** N = 63  
>  **Output:** 32 16 8 4 2 1  
>  **Explanation:**  
>  There are total of 6 powers of 2, which are less than or equal to the given
> number N.
>
>  **Input:** N = 193  
>  **Output:** 128 64 32 16 8 4 2 1  
>  **Explaination:**  
>  There are total of 8 powers of 2, which are less than or equal to the given
> number N.

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Naive Approach:** The idea is to traverse each number from N to 1 and check
if it is a perfect power of 2 or not. If yes, then print that number.

  

  

 **Another Approach:** The idea is to find all powers of 2 and simply print
the powers that are lesser than or equal to N.

 **Another Approach:** The idea is based on the concept that all powers of 2
has all bits set, in its binary form. Bitset function is used in this approach
solve the above problem. Below are the steps:

  1. Find the largest power of 2(say **temp** ) which is used to evaluate the number less than or equal to **N**.
  2. Initialise an bitset array **arr[]** of maximum size **64** , to store the binary representation of the given number **N**.
  3. Reset all the bits in the bitset array using reset() function.
  4. Iterate a loop from **total to 0** , and sequentially make each bit **1** , and find the value of that binary expression and then reset the bit.

Below is the implementation of the above approach:

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program for the above approach

 

#include <bits/stdc++.h>

using namespace std;

const int MAX = 64;

 

// Function to return max exponent of

// 2 which evaluates a number less

// than or equal to N

int max_exponent(int n)

{

 return (int)(log2(n));

}

 

// Function to print all the powers

// of 2 less than or equal to N

void all_powers(int N)

{

 bitset<64> arr(N);

 

 // Reset all the bits

 arr.reset();

 

 int total = max_exponent(N);

 

 // Iterate from total to 0

 for (int i = total; i >= 0; i--) {

 

 // Reset the next bit

 arr.reset(i + 1);

 

 // Set the current bit

 arr.set(i);

 

 // Value of the binary expression

 cout << arr.to_ulong() << " ";

 }

}

 

// Driver Code

int main()

{

 // Given Number

 int N = 63;

 

 // Function Call

 all_powers(N);

 return 0;

}  
  
---  
  
 __

 __

 **Output:**

    
    
    32 16 8 4 2 1
    

**Time Complexity:** _O(log N)_  
 **Auxiliary Space:** _O(1)_

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


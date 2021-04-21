Program to find the Nth natural number with exactly two bits set



Given an integer **N** , the task is to find the **Nth** natural number with
exactly two bits set.  
**Examples:**  

> **Input:** N = 4  
> **Output:** 9  
> **Explanation:**  
> Numbers with exactly two bits set: 3, 5, 6, 9, 10, 12, …  
> 4th number in this is 9  
>  **Input:** N = 15  
> **Output:** 48  
>

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Naive Approach:**  

  1. Run a loop through all natural numbers, and for each number, check if it has two bits set or not by counting set bits in a number.
  2. Print the Nth number having two set bits.

 **Efficient Approach:**  

  1. Find the leftmost set bit by finding the partition to which N belongs (Partition ‘i’ has ‘i’ numbers in it).
  2. To find the other set bit, we’ll have to first find the distance of N from the last number of the previous partition. Based on their difference, we set the corresponding bit.  

![](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20200415213737/03.png)

  1. **Note:** To set ith bit (i = 0, 1, 2…) in a number **K**:   

    
    
    k = k | (1<<(i))

  1.  **Below is the implementation of the above approach:**  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ Code to find the Nth number

// with exactly two bits set

#include <bits/stdc++.h>

using namespace std;

// Function to find the Nth number

// with exactly two bits set

void findNthNum(long long int N)

{

 long long int bit_L = 1, last_num = 0;

 // Keep incrementing until

 // we reach the partition of 'N'

 // stored in bit_L

 while (bit_L * (bit_L + 1) / 2 < N) {

 last_num = last_num + bit_L;

 bit_L++;

 }

 // set the rightmost bit

 // based on bit_R

 int bit_R = N - last_num - 1;

 cout << (1 << bit_L) + (1 << bit_R)

 << endl;

}

// Driver code

int main()

{

 long long int N = 13;

 findNthNum(N);

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

// Java Code to find the Nth number

// with exactly two bits set

class GFG{

 

// Function to find the Nth number

// with exactly two bits set

static void findNthNum(int N)

{

 

 int bit_L = 1, last_num = 0;

 

 // Keep incrementing until

 // we reach the partition of 'N'

 // stored in bit_L

 while (bit_L * (bit_L + 1) / 2 < N) {

 last_num = last_num + bit_L;

 bit_L++;

 }

 

 // set the rightmost bit

 // based on bit_R

 int bit_R = N - last_num - 1;

 

 System.out.print((1 << bit_L) + (1 << bit_R)

 +"\n");

}

 

// Driver code

public static void main(String[] args)

{

 int N = 13;

 

 findNthNum(N);

}

}

// This code is contributed by Princi Singh  
  
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

# Python Code to find the Nth number

# with exactly two bits set

# Function to find the Nth number

# with exactly two bits set

def findNthNum(N):

 bit_L = 1;

 last_num = 0;

 # Keep incrementing until

 # we reach the partition of 'N'

 # stored in bit_L

 while (bit_L * (bit_L + 1) / 2 < N):

 last_num = last_num + bit_L;

 bit_L+=1;

 

 # set the rightmost bit

 # based on bit_R

 bit_R = N - last_num - 1;

 print((1 << bit_L) + (1 << bit_R));

# Driver code

if __name__ == '__main__':

 N = 13;

 findNthNum(N);

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

// C# Code to find the Nth number

// with exactly two bits set

using System;

class GFG{

 

// Function to find the Nth number

// with exactly two bits set

static void findNthNum(int N)

{

 

 int bit_L = 1, last_num = 0;

 

 // Keep incrementing until

 // we reach the partition of 'N'

 // stored in bit_L

 while (bit_L * (bit_L + 1) / 2 < N) {

 last_num = last_num + bit_L;

 bit_L++;

 }

 

 // set the rightmost bit

 // based on bit_R

 int bit_R = N - last_num - 1;

 

 Console.Write((1 << bit_L) + (1 << bit_R)

 +"\n");

}

 

// Driver code

public static void Main(String[] args)

{

 int N = 13;

 

 findNthNum(N);

}

}

// This code is contributed by Princi Singh  
  
---  
  
 __

 __

## Javascript

 __

 __  
 __

 __

 __  
 __  
 __

<script>

// JavaScript Code to find the Nth number

// with exactly two bits set

// Function to find the Nth number

// with exactly two bits set

function findNthNum(N)

{

 let bit_L = 1, last_num = 0;

 // Keep incrementing until

 // we reach the partition of 'N'

 // stored in bit_L

 while (bit_L * (bit_L + 1) / 2 < N) {

 last_num = last_num + bit_L;

 bit_L++;

 }

 // set the rightmost bit

 // based on bit_R

 let bit_R = N - last_num - 1;

 document.write((1 << bit_L) + (1 << bit_R)

 + "<br>");

}

// Driver code

let N = 13;

findNthNum(N);

// This code is contributed by Mayank Tyagi

</script>  
  
---  
  
 __

 __

  1. 

**Output:**

    
    
    36

  1. **Time Complexity :** O(Partition of Number)  

Want to learn from the best curated videos and practice problems, check out
the **C++ Foundation Course **for Basic to Advanced C++ and **C++ STL Course**
for foundation plus STL. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save


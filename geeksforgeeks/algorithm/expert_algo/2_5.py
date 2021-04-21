Transform N to Minimum possible value



Given two numbers and **N** and **D**. Apply any of two below operations to
**N** :

  1. add **D** to **N**
  2. change **N** to **digitsum(N)** , where **digitsum(N)** is the sum of digits of **N**

The task is to transform **N** to the minimum possible value. Print the
minimum possible value of **N** and the number of times the given operations
applied(any one of them). The number of operations must be minimum.

 **Examples:**

>  **Input :** N = 2, D = 1  
>  **Output :** 1 9  
> Perfome Type1 opeation 8 times and Type2 opeation 1 time
>
>  **Input :** N = 9, D = 3  
>  **Output :** 3, 2  
> Apply one type1 operation first and then type2 operation
>
>  
>
>
>  
>

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Prerequisites:**  
1\. Digital Root (repeated digital sum) of the given large integer  
2\. Numbers in a Range with given Digital Root

 **Approach :**  
Let Dr(x) be a function defined for integer x as :

  * Dr(x) = x, if 0 <= x <= 9
  * else, Dr(x) = Dr(Sum-of-digits(x))

The function Dr(x) is the digital root of a number x.

  * Dr(a+b) = Dr(Dr(a) + Dr(b))
  * Dr(ab) = Dr(Dr(a) * Dr(b))

 **Important observation :** The minimum value is always the minimum over :
Dr(N + kD) for some non-negative integer k.

    
    
    Dr(N + kD) = Dr(Dr(N) + Dr(kD))          (1)
    

Now, Dr(kd) = Dr(Dr(k) * Dr(D))  
Possible values of Dr(k) are 0, 1, 2…9, given by numbers k=0, 1, 2…9

    
    
    Dr(x) = Dr(Sum-of-digits(x))             (2)
    

  * The minimum value for N is equal to the minimum value for Sum-of-digits(N). If we reduce this answer once and add D, the minimum value that can be obtained wouldn’t change. So, if it is required to perform a reduce operation and then an add operation, then we can do the add operation and then the reduce operation without affecting the possible roots we can reach. This is evident from combination of formulae (1) and (2)
  * So, we can do all add operations first, all reduce operations later, and reach any number that can be possibly reached by any set of operations. Using the above claims, we can prove the minimum possible value is the minimum of Dr(N + kD) where 0 <= k <= 9.
  * To find the minimum number of steps, note that the relative order of the add and Sum-of-digits operations does affect the answer. Also, note that the Sum-of-digits function is an decreases extremely fast.
  * Any number <= 1010 goes to a number <= 90, any number <= 90 goes to something <= 18 and so on. In short, any number can be reduced to its digital root in <= 5 steps.
  * Via this, we can prove that the value of the minimum steps can never be greater than 15. This is a loose upper bound, not the exact one.
  * Use brute force recursion algorithm, that at each step branches in 2 different directions, one x = Sum-of-digits(x), the other being x = x+D, but only until a recursion depth of 15. In this way, we stop after exploring 215 different ways.

Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// CPP program to transform N to the minimum value

#include <bits/stdc++.h>

using namespace std;

 

// Intialising the answer

int min_val = INT_MAX;

int min_steps = 0;

 

// Function to find the digitsum

int sumOfDigits(int n)

{

 string s = to_string(n);

 

 int sum = 0;

 

 // Iterate over all digits and add them

 for (int i = 0; i < s.length(); i++) {

 sum += (s[i] - '0');

 }

 

 // Return the digit su,

 return sum;

}

 

// Function to transform N to the minimum value

void Transform(int n, int d, int steps)

{

 // If the final value is lesser than least value

 if (n < min_val) {

 min_val = n;

 min_steps = steps;

 }

 

 // If final value is equal to least value then check 

 // for lesser number of steps to reach this value

 else if (n == min_val) {

 min_steps = min(min_steps, steps);

 }

 

 // The value will be obtained in less than 15 steps as 

 // proved so applying normal recursive operations

 if (steps < 15) {

 Transform(sumOfDigits(n), d, steps + 1);

 Transform(n + d, d, steps + 1);

 }

}

 

// Driver code

int main()

{

 int N = 9, D = 3;

 

 // Function call

 Transform(N, D, 0);

 

 // Print the answers

 cout << min_val << " " << min_steps;

 

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

// JAVA program to transform N to the minimum value

import java.util.*;

 

class GFG{

 

// Intialising the answer

static int min_val = Integer.MAX_VALUE;

static int min_steps = 0;

 

// Function to find the digitsum

static int sumOfDigits(int n)

{

 String s = String.valueOf(n);

 

 int sum = 0;

 

 // Iterate over all digits and add them

 for (int i = 0; i < s.length(); i++) {

 sum += (s.charAt(i) - '0');

 }

 

 // Return the digit su,

 return sum;

}

 

// Function to transform N to the minimum value

static void Transform(int n, int d, int steps)

{

 // If the final value is lesser than least value

 if (n < min_val) {

 min_val = n;

 min_steps = steps;

 }

 

 // If final value is equal to least value then check 

 // for lesser number of steps to reach this value

 else if (n == min_val) {

 min_steps = Math.min(min_steps, steps);

 }

 

 // The value will be obtained in less than 15 steps as 

 // proved so applying normal recursive operations

 if (steps < 15) {

 Transform(sumOfDigits(n), d, steps + 1);

 Transform(n + d, d, steps + 1);

 }

}

 

// Driver code

public static void main(String[] args)

{

 int N = 9, D = 3;

 

 // Function call

 Transform(N, D, 0);

 

 // Print the answers

 System.out.print(min_val+ " " + min_steps);

 

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

# Python3 program to transform N to the minimum value

import sys;

 

# Intialising the answer

min_val = sys.maxsize;

min_steps = 0;

 

# Function to find the digitsum

def sumOfDigits(n) :

 

 s = str(n);

 

 sum = 0;

 

 # Iterate over all digits and add them

 for i in range(len(s)) :

 sum += (ord(s[i]) - ord('0'));

 

 # Return the digit su,

 return sum;

 

# Function to transform N to the minimum value

def Transform(n, d, steps) :

 global min_val;global min_steps;

 

 # If the final value is lesser than least value

 if (n < min_val) :

 min_val = n;

 min_steps = steps;

 

 # If final value is equal to least value then check 

 # for lesser number of steps to reach this value

 elif (n == min_val) :

 min_steps = min(min_steps, steps);

 

 # The value will be obtained in less than 15 steps as 

 # proved so applying normal recursive operations

 if (steps < 15) :

 Transform(sumOfDigits(n), d, steps + 1);

 Transform(n + d, d, steps + 1);

 

# Driver code

if __name__ == "__main__" :

 

 N = 9; D = 3;

 

 # Function call

 Transform(N, D, 0);

 

 # Print the answers

 print(min_val, min_steps);

 

# This code is contributed by Yash_R  
  
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

// C# program to transform N to the minimum value

using System;

 

class GFG{

 

// Intialising the answer

static int min_val = int.MaxValue;

static int min_steps = 0;

 

// Function to find the digitsum

static int sumOfDigits(int n)

{

 string s = n.ToString(); 

 

 int sum = 0;

 

 // Iterate over all digits and add them

 for (int i = 0; i < s.Length; i++) {

 sum += (s[i] - '0');

 }

 

 // Return the digit su,

 return sum;

}

 

// Function to transform N to the minimum value

static void Transform(int n, int d, int steps)

{

 // If the final value is lesser than least value

 if (n < min_val) {

 min_val = n;

 min_steps = steps;

 }

 

 // If final value is equal to least value then check 

 // for lesser number of steps to reach this value

 else if (n == min_val) {

 min_steps = Math.Min(min_steps, steps);

 }

 

 // The value will be obtained in less than 15 steps as 

 // proved so applying normal recursive operations

 if (steps < 15) {

 Transform(sumOfDigits(n), d, steps + 1);

 Transform(n + d, d, steps + 1);

 }

}

 

// Driver code

public static void Main(string[] args)

{

 int N = 9, D = 3;

 

 // Function call

 Transform(N, D, 0);

 

 // Print the answers

 Console.Write(min_val+ " " + min_steps); 

}

}

 

// This code is contributed by Yash_R  
  
---  
  
 __

 __

 **Output:**

    
    
    3 2
    

**Time Complexity :**![O\(T \\cdot 2^{15} \\cdot log_{10} N
\)](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-764ce1e3beb2dcbffc168e2faad0e628_l3.png)

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


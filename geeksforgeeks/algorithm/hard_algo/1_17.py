Minimum flips required in a binary string such that all K-size substring
contains 1



Given a binary string **str** of size **N** and a positive integer **K** , the
task is to find the minimum number of flips required to make all substring of
size **K** contain at least one ‘1’.

 **Examples:**

>  **Input:** str = “0001”, K = 2  
>  **Output:** 1  
>  **Explanation:**  
>  Flipping the bit at index 1 modifies str to “0101”.  
> All substrings of size 2 are “01”, “10”, and “01”.  
> Each substring contains at least one 1.
>
>  **Input:** str = “101”, K = 2  
>  **Output:** 0  
>  **Explanation:**  
>  All substrings of size 2 are “10” and “01”.  
> Since both of them already have at least one ‘1’, no flips required in the
> original string.

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:**  
Follow the steps below to solve the problem:

  

  

  1. The idea is use Sliding Window Technique to check whether every substring of length K contains any ‘1’ or not.
  2. Maintain a variable **last_idx** to store the **last index** of a window where the character was ‘1’. The value of this variable will be **-1** if there is **no ‘1’** present in the current window.
  3. For any such window, we will increment the number of flips by flipping the character at **last index of the current window** to **‘1’** and update the index **last_idx** to that index.
  4. Flipping the last character of the current window ensures that the following **K-1** windows will have at least one ‘1’ as well. Thus, this approach minimizes the number of flips required.
  5. Repeat this process for the rest of the string and print the final count of flips required.

Below is the implementation of the above approach :  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to find the

// minimum numbers of flips 

// required in a binary string 

// such that all substrings of 

// size K has atleast one 1 

 

#include <bits/stdc++.h> 

using namespace std; 

 

// Function to calculate and 

// return the minimum number 

// of flips to make string valid 

int minimumMoves(string S, int K) 

{ 

 int N = S.length(); 

 

 // Stores the count 

 // of required flips 

 int ops = 0; 

 

 // Stores the last index 

 // of '1' in the string 

 int last_idx = -1; 

 

 // Check for the first 

 // substring of length K 

 for (int i = 0; i < K; i++) { 

 

 // If i-th character 

 // is '1' 

 if (S[i] == '1') 

 last_idx = i; 

 } 

 

 // If the substring had 

 // no '1' 

 if (last_idx == -1) { 

 

 // Increase the 

 // count of required 

 // flips 

 ++ops; 

 

 // Flip the last 

 // index of the 

 // window 

 S[K - 1] = '1'; 

 

 // Update the last 

 // index which 

 // contains 1 

 last_idx = K - 1; 

 } 

 

 // Check for remaining substrings 

 for (int i = 1; i < N - K + 1; i++) { 

 

 // If last_idx does not 

 // belong to current 

 // window make it -1 

 if (last_idx < i) 

 last_idx = -1; 

 

 // If the last character of 

 // the current substring 

 // is '1', then update 

 // last_idx to i+k-1; 

 if (S[i + K - 1] == '1') 

 last_idx = i + K - 1; 

 

 // If last_idx == -1, then 

 // the current substring 

 // has no 1 

 if (last_idx == -1) { 

 

 // Increase the count 

 // of flips 

 ++ops; 

 

 // Update the last 

 // index of the 

 // current window 

 S[i + K - 1] = '1'; 

 

 // Store the last 

 // index of current 

 // window as the 

 // index of last '1' 

 // in the string 

 last_idx = i + K - 1; 

 } 

 } 

 // Return the number 

 // of operations 

 return ops; 

} 

 

// Driver Code 

int main() 

{ 

 string S = "001010000"; 

 int K = 3; 

 cout << minimumMoves(S, K); 

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

// Java program to find the

// minimum numbers of flips 

// required in a binary string 

// such that all substrings of 

// size K has atleast one 1 

class GFG{ 

 

// Function to calculate and 

// return the minimum number 

// of flips to make string valid 

public static int minimumMoves(String s, int K) 

{ 

 StringBuilder S = new StringBuilder(s); 

 int N = S.length(); 

 

 // Stores the count 

 // of required flips 

 int ops = 0; 

 

 // Stores the last index 

 // of '1' in the string 

 int last_idx = -1; 

 

 // Check for the first 

 // substring of length K 

 for(int i = 0; i < K; i++) 

 { 

 

 // If i-th character 

 // is '1' 

 if (S.charAt(i) == '1') 

 last_idx = i; 

 } 

 

 // If the substring had 

 // no '1' 

 if (last_idx == -1) 

 { 

 

 // Increase the count 

 // of required flips 

 ++ops; 

 

 // Flip the last index 

 // of the window 

 S.setCharAt(K - 1, '1'); 

 

 // Update the last index 

 // which contains 1 

 last_idx = K - 1; 

 } 

 

 // Check for remaining substrings 

 for(int i = 1; i < N - K + 1; i++) 

 { 

 

 // If last_idx does not 

 // belong to current 

 // window make it -1 

 if (last_idx < i) 

 last_idx = -1; 

 

 // If the last character of 

 // the current substring 

 // is '1', then update 

 // last_idx to i+k-1; 

 if (S.charAt(i + K - 1) == '1') 

 last_idx = i + K - 1; 

 

 // If last_idx == -1, then 

 // the current substring 

 // has no 1 

 if (last_idx == -1) 

 { 

 

 // Increase the count 

 // of flips 

 ++ops; 

 

 // Update the last index 

 // of the current window 

 S.setCharAt(i + K - 1, '1'); 

 

 // Store the last index 

 // of current window as 

 // the index of last '1' 

 // in the string 

 last_idx = i + K - 1; 

 } 

 } 

 

 // Return the number 

 // of operations 

 return ops; 

} 

 

// Driver Code 

public static void main(String[] args) 

{ 

 String S = "001010000"; 

 int K = 3; 

 

 System.out.println(minimumMoves(S, K)); 

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

# Python3 program to find the minimum

# numbers of flips required in a binary 

# string such that all substrings of 

# size K has atleast one 1 

 

# Function to calculate and 

# return the minimum number 

# of flips to make string valid 

def minimumMoves(S, K): 

 

 N = len(S) 

 

 # Stores the count 

 # of required flips 

 ops = 0

 

 # Stores the last index 

 # of '1' in the string 

 last_idx = -1

 

 # Check for the first 

 # substring of length K 

 for i in range(K): 

 

 # If i-th character 

 # is '1' 

 if (S[i] == '1'): 

 last_idx = i 

 

 # If the substring had 

 # no '1' 

 if (last_idx == -1): 

 

 # Increase the count 

 # of required flips 

 ops += 1

 

 # Flip the last index 

 # of the window 

 S[K - 1] = '1'

 

 # Update the last index 

 # which contains 1 

 last_idx = K - 1

 

 # Check for remaining substrings 

 for i in range(N - K + 1): 

 

 # If last_idx does not 

 # belong to current 

 # window make it -1 

 if (last_idx < i): 

 last_idx = -1

 

 # If the last character of 

 # the current substring 

 # is '1', then update 

 # last_idx to i + k-1; 

 if (S[i + K - 1] == '1'): 

 last_idx = i + K - 1

 

 # If last_idx == -1, then 

 # the current substring 

 # has no 1 

 if (last_idx == -1): 

 

 # Increase the count 

 # of flips 

 ops += 1

 

 # Update the last index 

 # of the current window 

 S = S[:i + K - 1] + '1' + S[i + K:] 

 

 # Store the last index of 

 # current window as the index 

 # of last '1' in the string 

 last_idx = i + K - 1

 

 # Return the number 

 # of operations 

 return ops 

 

# Driver Code 

S = "001010000"

K = 3; 

 

print(minimumMoves(S, K)) 

 

# This code is contributed by yatinagg   
  
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

// C# program to find the

// minimum numbers of flips

// required in a binary string

// such that all substrings of

// size K has atleast one 1

using System;

using System.Text;

 

class GFG{

 

// Function to calculate and

// return the minimum number

// of flips to make string valid

public static int minimumMoves(String s, int K)

{

 StringBuilder S = new StringBuilder(s);

 int N = S.Length;

 

 // Stores the count

 // of required flips

 int ops = 0;

 

 // Stores the last index

 // of '1' in the string

 int last_idx = -1;

 

 // Check for the first

 // substring of length K

 for(int i = 0; i < K; i++)

 {

 

 // If i-th character

 // is '1'

 if (S[i] == '1')

 last_idx = i;

 }

 

 // If the substring had

 // no '1'

 if (last_idx == -1)

 {

 

 // Increase the count

 // of required flips

 ++ops;

 

 // Flip the last index 

 // of the window

 S.Insert(K - 1, '1');

 

 // Update the last index 

 // which contains 1

 last_idx = K - 1;

 }

 

 // Check for remaining substrings

 for(int i = 1; i < N - K + 1; i++)

 {

 

 // If last_idx does not

 // belong to current

 // window make it -1

 if (last_idx < i)

 last_idx = -1;

 

 // If the last character of

 // the current substring

 // is '1', then update

 // last_idx to i+k-1;

 if (S[i + K - 1] == '1')

 last_idx = i + K - 1;

 

 // If last_idx == -1, then

 // the current substring

 // has no 1

 if (last_idx == -1)

 {

 

 // Increase the count

 // of flips

 ++ops;

 

 // Update the last index

 // of the current window

 S.Insert(i + K - 1, '1');

 

 // Store the last index 

 // of current window as

 // the index of last '1'

 // in the string

 last_idx = i + K - 1;

 }

 }

 

 // Return the number

 // of operations

 return ops;

}

 

// Driver Code

public static void Main(String[] args)

{

 String S = "001010000";

 int K = 3;

 

 Console.WriteLine(minimumMoves(S, K));

}

}

 

// This code is contributed by gauravrajput1  
  
---  
  
 __

 __

 **Output:**

    
    
    1
    

_**Time Complexity:** O(N)_  
 _ **Auxiliary Space:** O(1)_

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


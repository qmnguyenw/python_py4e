Minimum jumps required to group all 1s together in a given Binary string



Given a binary string **S** , the task is to count the minimum number of jumps
required to group all 1’s together.  
**Examples:**

>  **Input:** S = “000010011000100”  
> **Output:** 5  
> **Explanation:**  
> 0000 **1** 0011000100 -> 000000111000100 requires 2 jumps.  
> 000000111000 **1** 00 -> 000000111100000 requires 3 jumps.  
> Hence, at least 5 jumps are required to group all 1’s together.
>
> **Input:** S = “100010001”  
> **Output:** 6  
> **Explanation:**  
> **1** 00010001 -> 000 **1** 10001 requires 3 jumps.  
> 00011000 **1** -> 00011 **1** 000 requires 3 jumps.

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:**  
We can observe that in order to minimize the number of jumps required for
grouping all 1’s together, they need to be grouped near the **median** of
their current positions. Calculate the median and the number of moves required
to shift the 1’s to the _nearest position of **0**_ in the _left of the
median_. Perform the same operation for the _right of the median_.  
Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ Program to find the minimum

// number of jumps required to

// group all ones together in

// the binary string

#include <bits/stdc++.h>

using namespace std;

 

// Function to get the

// minimum jump value

int getMinJumps(string s)

{

 // Store all indices

 // of ones

 vector<int> ones;

 

 int jumps = 0, median = 0, ind = 0;

 

 // Populating one's indices

 for (int i = 0; i < s.length(); i++) {

 if (s[i] == '1')

 ones.push_back(i);

 }

 

 if (ones.size() == 0)

 return jumps;

 

 // Calculate median

 median = ones[ones.size() / 2];

 ind = median;

 

 // Jumps required for 1's

 // to the left of median

 for (int i = ind; i >= 0; i--) {

 if (s[i] == '1') {

 jumps += ind - i;

 ind--;

 }

 }

 ind = median;

 

 // Jumps required for 1's

 // to the right of median

 for (int i = ind; i < s.length(); i++) {

 if (s[i] == '1') {

 jumps += i - ind;

 ind++;

 }

 }

 

 // Return the final answer

 return jumps;

}

 

// Driver Code

int main()

{

 string S = "00100000010011";

 cout << getMinJumps(S) << '\n';

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

// Java Program to find the minimum

// number of jumps required to 

// group all ones together in 

// the binary string 

import java.io.*; 

import java.util.*; 

 

class GFG{

 

// Function to get the 

// minimum jump value 

public static int getMinJumps(String s) 

{ 

 

 // Store all indices 

 // of ones 

 Vector<Integer> ones = new Vector<Integer>();

 

 int jumps = 0, median = 0, ind = 0; 

 

 // Populating one's indices 

 for(int i = 0; i < s.length(); i++) 

 { 

 if (s.charAt(i) == '1') 

 ones.add(i); 

 } 

 

 if (ones.size() == 0) 

 return jumps; 

 

 // Calculate median 

 median = (int)ones.get(ones.size() / 2); 

 ind = median; 

 

 // Jumps required for 1's 

 // to the left of median 

 for(int i = ind; i >= 0; i--) 

 { 

 if (s.charAt(i) == '1') 

 { 

 jumps += ind - i; 

 ind--; 

 } 

 } 

 ind = median; 

 

 // Jumps required for 1's 

 // to the right of median 

 for(int i = ind; i < s.length(); i++) 

 { 

 if (s.charAt(i) == '1')

 { 

 jumps += i - ind; 

 ind++; 

 } 

 } 

 

 // Return the final answer 

 return jumps; 

} 

 

// Driver code

public static void main(String[] args)

{

 String S = "00100000010011"; 

 

 System.out.println(getMinJumps(S));

}

}

 

// This code is contributed by divyeshrabadiya07  
  
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

# number of jumps required to group 

# all ones together in the binary string 

 

# Function to get the

# minimum jump value

def getMinJumps(s):

 

 # Store all indices

 # of ones

 ones = []

 

 jumps, median, ind = 0, 0, 0

 

 # Populating one's indices

 for i in range(len(s)):

 if(s[i] == '1'):

 ones.append(i)

 

 if(len(ones) == 0):

 return jumps

 

 # Calculate median

 median = ones[len(ones) // 2]

 ind = median

 

 # Jumps required for 1's

 # to the left of median

 for i in range(ind, -1, -1):

 if(s[i] == '1'):

 jumps += ind - i

 ind -= 1

 

 ind = median

 

 # Jumps required for 1's

 # to the right of median

 for i in range(ind, len(s)):

 if(s[i] == '1'):

 jumps += i - ind

 ind += 1

 

 # Return the final answer

 return jumps

 

# Driver Code

if __name__ == '__main__':

 

 s = "00100000010011"

 

 print(getMinJumps(s))

 

# This code is contributed by Shivam Singh  
  
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

// C# program to find the minimum

// number of jumps required to 

// group all ones together in 

// the binary string 

using System; 

using System.Collections; 

using System.Collections.Generic;

 

class GFG{ 

 

// Function to get the 

// minimum jump value 

public static int getMinJumps(string s) 

{ 

 

 // Store all indices 

 // of ones 

 ArrayList ones = new ArrayList();

 

 int jumps = 0, median = 0, ind = 0; 

 

 // Populating one's indices 

 for(int i = 0; i < s.Length; i++) 

 { 

 if (s[i] == '1') 

 ones.Add(i); 

 } 

 

 if (ones.Count== 0) 

 return jumps; 

 

 // Calculate median 

 median = (int)ones[ones.Count / 2]; 

 ind = median; 

 

 // Jumps required for 1's 

 // to the left of median 

 for(int i = ind; i >= 0; i--) 

 { 

 if (s[i] == '1') 

 { 

 jumps += ind - i; 

 ind--; 

 } 

 } 

 ind = median; 

 

 // Jumps required for 1's 

 // to the right of median 

 for(int i = ind; i < s.Length; i++) 

 { 

 if (s[i] == '1') 

 { 

 jumps += i - ind; 

 ind++; 

 } 

 } 

 

 // Return the final answer 

 return jumps; 

} 

 

// Driver code 

public static void Main(string[] args) 

{ 

 string S = "00100000010011"; 

 

 Console.Write(getMinJumps(S)); 

} 

} 

 

// This code is contributed by rutvik_56  
  
---  
  
 __

 __

 **Output:**

    
    
    10
    

_**Time Complexity:** O(N) _  
_**Auxiliary Space:** O(N)_  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save


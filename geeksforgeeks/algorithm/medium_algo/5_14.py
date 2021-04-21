Number of subsequences in a given binary string divisible by 2



Given a binary string **str** of length **N** , the task is to find the count
of subsequences of **str** which are divisible by **2**. Leading zeros in a
sub-sequence is allowed.

 **Examples:**

>  **Input:** str = “101”  
>  **Output:** 2  
> “0” and “10” are the only subsequences  
> which are divisible by 2.
>
>  **Input:** str = “10010”  
>  **Output:** 22

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Naive approach:** A naive approach will be to generate all possible sub-
sequences and check if they are divisible by 2. The time complexity for this
will be O(2N * N).

  

  

 **Efficient approach:** It can be observed that any binary number is
divisible by **2** only if it ends with a **0**. Now, the task is to just
count the number of subsequences ending with **0**. So, for every index **i**
such that **str[i] = ‘0’** , find the number of subsequences ending at **i**.
This value is equal to **2 i** (0-based indexing). Thus, the final answer will
be equal to the summation of **2 i** for all **i** such that **str[i] = ‘0’**.

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

 

// Function to return the count

// of the required subsequences

int countSubSeq(string str, int len)

{

 // To store the final answer

 int ans = 0;

 

 // Multiplier

 int mul = 1;

 

 // Loop to find the answer

 for (int i = 0; i < len; i++) {

 

 // Condition to update the answer

 if (str[i] == '0')

 ans += mul;

 // updating multiplier

 mul *= 2;

 }

 

 return ans;

}

 

// Driver code

int main()

{

 string str = "10010";

 int len = str.length();

 

 cout << countSubSeq(str, len);

 

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

 

// Function to return the count

// of the required subsequences

static int countSubSeq(String str, int len)

{

 // To store the final answer

 int ans = 0;

 

 // Multiplier

 int mul = 1;

 

 // Loop to find the answer

 for (int i = 0; i < len; i++) 

 {

 

 // Condition to update the answer

 if (str.charAt(i) == '0')

 ans += mul;

 

 // updating multiplier

 mul *= 2;

 }

 return ans;

}

 

// Driver code

public static void main(String[] args)

{

 String str = "10010";

 int len = str.length();

 

 System.out.print(countSubSeq(str, len));

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

 

# Function to return the count

# of the required subsequences

def countSubSeq(strr, lenn):

 

 # To store the final answer

 ans = 0

 

 # Multiplier

 mul = 1

 

 # Loop to find the answer

 for i in range(lenn):

 

 # Condition to update the answer

 if (strr[i] == '0'):

 ans += mul

 

 # updating multiplier

 mul *= 2

 

 return ans

 

# Driver code

strr = "10010"

lenn = len(strr)

 

print(countSubSeq(strr, lenn))

 

# This code is contributed by Mohit Kumar  
  
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

 

 // Function to return the count 

 // of the required subsequences 

 static int countSubSeq(string str, int len) 

 { 

 // To store the final answer 

 int ans = 0; 

 

 // Multiplier 

 int mul = 1; 

 

 // Loop to find the answer 

 for (int i = 0; i < len; i++) 

 { 

 

 // Condition to update the answer 

 if (str[i] == '0') 

 ans += mul; 

 

 // updating multiplier 

 mul *= 2; 

 } 

 return ans; 

 } 

 

 // Driver code 

 static public void Main ()

 { 

 string str = "10010"; 

 int len = str.Length; 

 

 Console.WriteLine(countSubSeq(str, len)); 

 } 

}

 

// This code is contributed by AnkitRai01  
  
---  
  
 __

 __

  
 **Output:**

    
    
    22
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


Longest subsequence having difference atmost K



Given a string **S** of length **N** and an integer **K** , the task is to
find the length of longest sub-sequence such that the difference between the
ASCII values of adjacent characters in the subsequence is not more than K.

 **Examples:**

    
    
    **Input:** N = 7, K = 2, S = "afcbedg"
    **Output:** 4
    **Explantion:**
    Longest special sequence present 
    in "afcbedg" is a, c, b, d.
    It is special because |a - c| <= 2, 
    |c - b| <= 2 and | b-d| <= 2
    
    **Input:** N = 13, K = 3, S = "geeksforgeeks"
    **Output:** 7
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Naive approach:** A brute force solution is to generate all the possible
subsequences of various lengths and compute the maximum length of the valid
subsequence. The time complexity will be exponential.

 **Efficient Approach:** An efficient approach is to use the concept **Dynamic
Programming**

  * Create an array **dp** of 0’s with size equal to length of string.
  * Create an supporting array **max_length** with 0’s of size 26.
  * Iterate the string character by character and for each character determine the upper and lower bounds.
  * Iterate nested loop in the range of lower and upper bounds.
  * Fill the dp array with the maximum value between current **dp** indices and current max_length indices+1.
  * Fill the max_length array with maximum value between current **dp** indices and current max_length indices.
  * Longest sub sequence length is the maximum value in **dp** array.
  * Let us consider an example:  

> input string **s** is “afcbedg” and **k** is 2
>
>  
>
>
>  
>
>   * for 1st iteration value of i is ‘a’ and range of j is (0, 2)  
> and current dp = [1, 0, 0, 0, 0, 0, 0]
>   * for 2nd iteration value of i is ‘f’ and range of j is (3, 7)  
> and current dp = [1, 1, 0, 0, 0, 0, 0]
>   * for 3rd iteration value of i is ‘c’ and range of j is (0, 4)  
> and current dp = [1, 1, 2, 0, 0, 0, 0]
>   * for 4th iteration value of i is ‘b’ and range of j is (0, 3)  
> and current dp = [1, 1, 2, 3, 0, 0, 0]
>   * for 5th iteration value of i is ‘e’ and range of j is (2, 6)  
> and current dp = [1, 1, 2, 3, 3, 0, 0]
>   * for 6th iteration value of i is ‘d’ and range of j is (1, 5)  
> and current dp = [1, 1, 2, 3, 3, 4, 0]
>   * for 7th iteration value of i is ‘g’ and range of j is (4, 8)  
> and current dp = [1, 1, 2, 3, 3, 4, 4]
>
> longest length is the maximum value in dp so maximum length is 4

Below is the implementation of the above approach:  

## C++

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

 

// Function to find

// the longest Special Sequence

int longest_subseq(int n, int k, string s)

{

 

 // Creating a list with

 // all 0's of size

 // equal to the length of string

 vector<int> dp(n, 0);

 

 // Supporting list with

 // all 0's of size 26 since

 // the given string consists

 // of only lower case alphabets

 int max_length[26] = {0};

 

 for (int i = 0; i < n; i++) 

 {

 

 // Converting the ascii value to

 // list indices

 int curr = s[i] - 'a';

 

 // Determining the lower bound

 int lower = max(0, curr - k);

 

 // Determining the upper bound

 int upper = min(25, curr + k);

 

 // Filling the dp array with values

 for (int j = lower; j < upper + 1; j++)

 {

 dp[i] = max(dp[i], max_length[j] + 1);

 }

 //Filling the max_length array with max

 //length of subsequence till now

 max_length[curr] = max(dp[i], max_length[curr]);

 }

 

 int ans = 0;

 

 for(int i:dp) ans = max(i, ans);

 

 // return the max length of subsequence

 return ans;

}

 

// Driver Code

int main()

{

 string s = "geeksforgeeks";

 int n = s.size();

 int k = 3;

 cout << (longest_subseq(n, k, s));

 return 0;

}

 

// This code is contributed by Mohit Kumar  
  
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

// Java program for the above approach

class GFG

{

 

// Function to find

// the longest Special Sequence

static int longest_subseq(int n, int k, String s)

{

 

 // Creating a list with

 // all 0's of size

 // equal to the length of String

 int []dp = new int[n];

 

 // Supporting list with

 // all 0's of size 26 since

 // the given String consists

 // of only lower case alphabets

 int []max_length = new int[26];

 

 for (int i = 0; i < n; i++) 

 {

 

 // Converting the ascii value to

 // list indices

 int curr = s.charAt(i) - 'a';

 

 // Determining the lower bound

 int lower = Math.max(0, curr - k);

 

 // Determining the upper bound

 int upper = Math.min(25, curr + k);

 

 // Filling the dp array with values

 for (int j = lower; j < upper + 1; j++)

 {

 dp[i] = Math.max(dp[i], max_length[j] + 1);

 }

 

 // Filling the max_length array with max

 // length of subsequence till now

 max_length[curr] = Math.max(dp[i], max_length[curr]);

 }

 

 int ans = 0;

 

 for(int i:dp) ans = Math.max(i, ans);

 

 // return the max length of subsequence

 return ans;

}

 

// Driver Code

public static void main(String[] args)

{

 String s = "geeksforgeeks";

 int n = s.length();

 int k = 3;

 System.out.print(longest_subseq(n, k, s));

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

# Function to find

# the longest Special Sequence

def longest_subseq(n, k, s):

 

 # Creating a list with 

 # all 0's of size

 # equal to the length of string

 dp = [0] * n

 

 # Supporting list with 

 # all 0's of size 26 since 

 # the given string consists 

 # of only lower case alphabets

 max_length = [0] * 26

 

 for i in range(n):

 

 # Converting the ascii value to

 # list indices

 curr = ord(s[i]) - ord('a')

 # Determining the lower bound

 lower = max(0, curr - k)

 # Determining the upper bound

 upper = min(25, curr + k)

 # Filling the dp array with values

 for j in range(lower, upper + 1):

 

 dp[i] = max(dp[i], max_length[j]+1)

 # Filling the max_length array with max

 # length of subsequence till now

 max_length[curr] = max(dp[i], max_length[curr])

 

 # return the max length of subsequence

 return max(dp)

 

# driver code

def main():

 s = "geeksforgeeks"

 n = len(s)

 k = 3

 print(longest_subseq(n, k, s))

 

main()  
  
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

// C# program for the above approach

using System;

 

class GFG

{

 

// Function to find

// the longest Special Sequence

static int longest_subseq(int n, int k, String s)

{

 

 // Creating a list with

 // all 0's of size

 // equal to the length of String

 int []dp = new int[n];

 

 // Supporting list with

 // all 0's of size 26 since

 // the given String consists

 // of only lower case alphabets

 int []max_length = new int[26];

 

 for (int i = 0; i < n; i++) 

 {

 

 // Converting the ascii value to

 // list indices

 int curr = s[i] - 'a';

 

 // Determining the lower bound

 int lower = Math.Max(0, curr - k);

 

 // Determining the upper bound

 int upper = Math.Min(25, curr + k);

 

 // Filling the dp array with values

 for (int j = lower; j < upper + 1; j++)

 {

 dp[i] = Math.Max(dp[i], max_length[j] + 1);

 }

 

 // Filling the max_length array with max

 // length of subsequence till now

 max_length[curr] = Math.Max(dp[i], max_length[curr]);

 }

 

 int ans = 0;

 

 foreach(int i in dp) ans = Math.Max(i, ans);

 

 // return the max length of subsequence

 return ans;

}

 

// Driver Code

public static void Main(String[] args)

{

 String s = "geeksforgeeks";

 int n = s.Length;

 int k = 3;

 Console.Write(longest_subseq(n, k, s));

}

}

 

// This code is contributed by Rajput-Ji  
  
---  
  
 __

 __

 **Output:**

    
    
    7
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


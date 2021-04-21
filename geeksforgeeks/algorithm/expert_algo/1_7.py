Count possible decodings of a given Digit Sequence | Set 2



Given an encoded string **str** consisting of digits and ***** which can be
filled by any digit **1 – 9** , the task is to find the number of ways to
decode that string into a sequence of alphabets **A-Z**.

 **Note:** The input string contains number from 0-9 and character ‘*’ only.  
 **Examples:**

>  **Input:** str = “1*”  
>  **Output:** 18  
>  **Explanation:**  
>  Since * can be replaced by any value from (1-9),  
> The given string can be decoded as A[A-I] + [J-R] = 9 + 9 ways
>
>  **Input:** str = “12*3”  
>  **Output:** 28

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Naive Approach:** A simple solution is to solve the problem using recursion
considering all the possible decodings of the string. Below is the recursion
tree for the problem:

  

  

    
    
                       12*3
                  /             \
               12*(3)           12(*3) 
             /     \            /      \
        12(*)(3)  1(2*)(3)  1(2)(*3)   ""
          /    \      \       /
    1(2)(*)(3) ""     ""     ""   
        /
       ""
    

**Efficient Approach:** The idea is to solve the problem using Dynamic
Programming using the optimal substructure for considering all the cases of
the current and the previous digits of the string and their number of ways to
decode the string.

 **Definition of the DP State:** In this problem the
![dp\[i\]](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-
caf135312f4c511cdbea44349805bb7a_l3.png) denotes the number of ways to decode
the string upto the ![i^{th}](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-fed8e1e15a62215e09e863591008fc5b_l3.png) index.

 **Intial DP States:** Intially the value of the DP states are defined as
below:

    
    
    // Number of ways to decode 
    // an empty string
    dp[0] = 1
    
    // Number of ways to decode the
    // first character
    if (s[0] == '*')
        dp[1] = 9  // 9 ways
    else 
        dp[1] = 1
    

**Optimal Sub-structure:** There are generally two ways to decode the current
character of the string:

  *  **Including the current character as single-digit to decode:** If the current character is used as single-digit then there can be generally two cases for the character to be:
    *  **Case 1:** If current character is equal to the !["*"](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-bd0593d7841793a217e825166732d6c2_l3.png), Then there are 9 possible ways to take any digit from [1-9] and decode it as any character from [A-Z].
        
        
        if (current == "*")
            dp[i] += 9 * dp[i-1]
        

    * **Case 2:** If current character is equal to any other digit from [0-9], Then the number of possible ways to decode is equal to the number of way to decode the string upto ![\(i-1\)^{th}](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-cbedadc5dcad348e81a0c21235993dad_l3.png) index.
        
        
        if (current != "*")
             dp[i] += dp[i-1]
        

  * **Including the current character as two-digits to decode:** If the current character is to be decoded as two-digits then there are two possible cases:
    *  **Case 1:** If the previous character is equal to the !["1"](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-1973c9de4b6ed8cb932cf34f9617b071_l3.png) or !["2"](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-bfe32c195466151f9eb2f64adda93b46_l3.png), then there can be two more possible subcases which will depend upon the current character:
      *  **Case 1.1:** If the current character is equal to the !["*"](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-bd0593d7841793a217e825166732d6c2_l3.png), then total possible ways to decode are 9 if the previous character is 1, otherwise 6 if previous character is 2.
      *  **Case 1.2:** If the current character is less than equal to 6, Then the total number of possible way to decode the string will depend only on the number of way to decode upto the previous character. That is ![dp\[i-2\]](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-1072191aab574b3d1552e1b2abe0be42_l3.png)
    * **Case 2:** If the previous character is !["*"](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-bd0593d7841793a217e825166732d6c2_l3.png), then there can be two more possible subcases which will depend upon the current character:
      *  **Case 2.1:** If the current character is also !["*"](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-bd0593d7841793a217e825166732d6c2_l3.png), Then the total number of cases will be ![15 * dp\[i-2\]](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-7b2541dd976064b8d11cb0c38cd7acb1_l3.png), because the single digits of decoding ways of previous character must be already included.
      *  **Case 2.2:** If the current character is less than 6, Then the total number of ways will be ![2*dp\[i-2\]](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-d3ce6ef2b7634e379242989822bdfbe9_l3.png), because then the number of ways to choose the digits of the first character is 2. That is [1, 2].
      *  **Case 2.3:** If the current character is any digits, Then the total number of ways will be the number of ways to decode uptill the previous digit only. That is ![dp\[i-2\]](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-1072191aab574b3d1552e1b2abe0be42_l3.png).

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation to count the

// possible decodings of the given 

// digit sequence

 

#include <bits/stdc++.h>

using namespace std;

 

// Function to count the number of 

// ways to decode the given digit 

// sequence 

int waysToDecode2(string s) {

 int n = s.size();

 

 // Array to store the dp states 

 vector<int> dp(n+1,0);

 

 // Case of empty string

 dp[0]=1; 

 

 // Condition to check if the 

 // first character of string is 0

 if(s[0]=='0')

 return 0;

 

 // Base case for single length 

 // string

 dp[1]= ((s[0]=='*')? 9 : 1);

 

 // Bottom-up dp for the string

 for(int i=2;i<=n;i++)

 {

 // Previous character

 char first= s[i-2];

 

 // Current character

 char second= s[i-1]; 

 

 // Case to include the Current

 // digit as a single digit for 

 // decoding the string

 if(second=='*')

 {

 dp[i]+= 9*dp[i-1];

 }

 else if(second>'0')

 dp[i]+=dp[i-1];

 

 // Case to include the current 

 // character as two-digit for 

 // decoding the string

 if(first=='1'|| first=='2')

 {

 

 // Condition to check if the 

 // current character is "*"

 if(second=='*')

 {

 if(first=='1')

 dp[i]+= 9 * dp[i-2];

 else if(first=='2')

 dp[i]+= 6 * dp[i-2]; 

 }

 

 // Condition to check if the 

 // current character is less than 

 // or equal to 26

 else if(((first-'0')* 10 + 

 (second-'0'))<= 26)

 dp[i]+=dp[i-2];

 }

 

 // Condition to check if the 

 // Previous digit is equal to "*"

 else if(first=='*')

 {

 if(second=='*')

 {

 dp[i]+= 15 * dp[i-2];

 }

 else if(second<='6')

 dp[i]+= 2* dp[i-2];

 else

 dp [i]+= dp[i-2];

 }

 }

 return dp[n];

}

 

// Driver Code

int main() {

 string str = "12*3";

 

 // Function Call

 cout << waysToDecode2(str) << endl;

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

// Java implementation to count the

// possible decodings of the given 

// digit sequence

class GFG{

 

// Function to count the number of 

// ways to decode the given digit 

// sequence 

static int waysToDecode2(char []s) 

{

 

 int n = s.length;

 

 // Array to store the dp states 

 int []dp = new int[n + 1];

 

 // Case of empty String

 dp[0] = 1; 

 

 // Condition to check if the 

 // first character of String is 0

 if(s[0] == '0')

 return 0;

 

 // Base case for single length 

 // String

 dp[1] = ((s[0] == '*') ? 9 : 1);

 

 // Bottom-up dp for the String

 for(int i = 2; i <= n; i++)

 {

 

 // Previous character

 char first = s[i - 2];

 

 // Current character

 char second = s[i - 1]; 

 

 // Case to include the Current

 // digit as a single digit for 

 // decoding the String

 if(second == '*')

 {

 dp[i] += 9 * dp[i - 1];

 }

 else if(second > '0')

 dp[i] += dp[i - 1];

 

 // Case to include the current 

 // character as two-digit for 

 // decoding the String

 if(first == '1' || first == '2')

 {

 

 // Condition to check if the 

 // current character is "*"

 if(second == '*')

 {

 if(first == '1')

 dp[i] += 9 * dp[i - 2];

 else if(first == '2')

 dp[i] += 6 * dp[i - 2]; 

 }

 

 // Condition to check if the 

 // current character is less than 

 // or equal to 26

 else if(((first - '0') * 10 + 

 (second - '0')) <= 26)

 {

 dp[i] += dp[i - 2];

 }

 }

 

 // Condition to check if the 

 // previous digit is equal to "*"

 else if(first == '*')

 {

 if(second == '*')

 {

 dp[i] += 15 * dp[i - 2];

 }

 else if(second <= '6')

 {

 dp[i] += 2 * dp[i - 2];

 }

 else

 {

 dp[i] += dp[i - 2];

 }

 }

 }

 return dp[n];

}

 

// Driver Code

public static void main(String[] args)

{

 String str = "12*3";

 

 // Function Call

 System.out.print(waysToDecode2(

 str.toCharArray()) + "\n");

}

}

 

// This code is contributed by amal kumar choubey  
  
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

// C# implementation to count the

// possible decodings of the given 

// digit sequence

using System;

 

class GFG{

 

// Function to count the number of 

// ways to decode the given digit 

// sequence 

static int waysToDecode2(char []s) 

{

 int n = s.Length;

 

 // Array to store the dp states 

 int []dp = new int[n + 1];

 

 // Case of empty String

 dp[0] = 1; 

 

 // Condition to check if the 

 // first character of String is 0

 if(s[0] == '0')

 return 0;

 

 // Base case for single length 

 // String

 dp[1] = ((s[0] == '*') ? 9 : 1);

 

 // Bottom-up dp for the String

 for(int i = 2; i <= n; i++)

 {

 

 // Previous character

 char first = s[i - 2];

 

 // Current character

 char second = s[i - 1]; 

 

 // Case to include the current

 // digit as a single digit for 

 // decoding the String

 if(second == '*')

 {

 dp[i] += 9 * dp[i - 1];

 }

 else if(second > '0')

 {

 dp[i] += dp[i - 1];

 }

 

 // Case to include the current 

 // character as two-digit for 

 // decoding the String

 if(first == '1' || first == '2')

 {

 

 // Condition to check if the 

 // current character is "*"

 if(second == '*')

 {

 if(first == '1')

 {

 dp[i] += 9 * dp[i - 2];

 }

 else if(first == '2')

 {

 dp[i] += 6 * dp[i - 2];

 } 

 }

 

 // Condition to check if the 

 // current character is less than 

 // or equal to 26

 else if(((first - '0') * 10 + 

 (second - '0')) <= 26)

 {

 dp[i] += dp[i - 2];

 }

 }

 

 // Condition to check if the 

 // previous digit is equal to "*"

 else if(first == '*')

 {

 if(second == '*')

 {

 dp[i] += 15 * dp[i - 2];

 }

 else if(second <= '6')

 {

 dp[i] += 2 * dp[i - 2];

 }

 else

 {

 dp[i] += dp[i - 2];

 }

 }

 }

 return dp[n];

}

 

// Driver Code

public static void Main(String[] args)

{

 String str = "12*3";

 

 // Function Call

 Console.Write(waysToDecode2(

 str.ToCharArray()) + "\n");

}

}

 

// This code is contributed by amal kumar choubey  
  
---  
  
 __

 __

 **Output:**

    
    
    28
    

**Performance Analysis:**

  *  **Time Complexity:** O(N)
  *  **Auxiliary Space:** O(N)

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


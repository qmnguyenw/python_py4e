Count the number of ways to construct the target string



Given an array of strings A, each of the same length and a target string S,
find the number of ways to construct the target string using characters from
strings in the given array such that the indices of the characters used in
string construction form a strictly increasing sequence. Multiple characters
can also be used from the same string. Since the answer can be very large,
take modulo with (10^9 + 7)  

**Examples:**

    
    
    **Input :**  A = ["adc", "aec", "erg"], S = "ac"
    **Output :** 4
    Target string can be formed in following ways :
    1) 1st character of "adc" and the 3rd character of "adc".
    2) 1st character of "adc" and the 3rd character of "aec".
    3) 1st character of "aec" and the 3rd character of "adc".
    4) 1st character of "aec" and the 3rd character of "aec".
    
    **Input :** A = ["afsdc", "aeeeedc", "ddegerg"], S = "ae"
    **Output :** 12
    

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

###  **Approach** :

  * We will use Dynamic Programming to solve the problem. 
  * For each string in the array, store the positions in which characters occurred in the string in a common list (L). Our aim is to use the characters whose indices form a strictly increasing sequence, so it doesn’t matter which string they come from. 
  * Traverse the target string, and keep the information of the previously picked index (prev). For the current position of the target, string check whether this character has occurred at any index greater than prev by searching in L. This can be done naively using recursion but we can memorize it using dp table.   

    
    
    Following are the states of dp :
    dp[pos][prev], 
    where pos represents the position we are at in the target string, 
    and prev represents the previously picked index.
    

  

  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ Program to Count the number of ways to

// construct the target string

#include <bits/stdc++.h>

using namespace std;

int mod = 1000000007;

int dp[1000][1000];

int calculate(int pos, int prev, string s, vector<int>* index)

{

 // base case

 if (pos == s.length())

 return 1;

 // If current subproblem has been solved, use the value

 if (dp[pos][prev] != -1)

 return dp[pos][prev];

 // current character

 int c = s[pos] - 'a';

 // search through all the indiced at which the current

 // character occurs. For each index greater than prev,

 // take the index and move

 // to the next position, and add to the answer.

 int answer = 0;

 for (int i = 0; i < index.size(); i++) {

 if (index[i] > prev) {

 answer = (answer % mod + calculate(pos + 1,

 index[i], s, index) % mod) % mod;

 }

 }

 // Store and return the solution for this subproblem

 return dp[pos][prev] = answer;

}

int countWays(vector<string>& a, string s)

{

 int n = a.size();

 // preprocess the strings by storing for each

 // character of every string, the index of their

 // occurrence we will use a common list for all

 // because of only the index matter

 // in the string from which the character was picked

 vector<int> index[26];

 for (int i = 0; i < n; i++) {

 for (int j = 0; j < a[i].length(); j++) {

 // we are storing j+1 because the initial picked index

 // in the recursive step will ne 0.

 // This is just for ease of implementation

 index[a[i][j] - 'a'].push_back(j + 1);

 }

 }

 // initialise dp table. -1 represents that

 // the subproblem hasn't been solved

 memset(dp, -1, sizeof(dp));

 return calculate(0, 0, s, index);

}

// Driver Code

int main()

{

 vector<string> A;

 A.push_back("adc");

 A.push_back("aec");

 A.push_back("erg");

 string S = "ac";

 cout << countWays(A, S);

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

// Java Program to Count the number of ways to

// conthe target String

import java.util.*;

class GFG{

 

static int mod = 1000000007;

 

static int [][]dp = new int[1000][1000];

 

static int calculate(int pos, int prev, String s, Vector<Integer>
index)

{

 

 // base case

 if (pos == s.length())

 return 1;

 

 // If current subproblem has been solved, use the value

 if (dp[pos][prev] != -1)

 return dp[pos][prev];

 

 // search through all the indiced at which the current

 // character occurs. For each index greater than prev,

 // take the index and move

 // to the next position, and add to the answer.

 int answer = 0;

 for (int i = 0; i < index.size(); i++) {

 if (index.get(i).compareTo(prev) >= 0) {

 answer = (answer % mod + calculate(pos + 1,

 index.get(i), s, index) % mod) % mod;

 }

 }

 

 // Store and return the solution for this subproblem

 return dp[pos][prev] = answer;

}

 

static int countWays(Vector<String> a, String s)

{

 int n = a.size();

 

 // preprocess the Strings by storing for each

 // character of every String, the index of their

 // occurrence we will use a common list for all

 // because of only the index matter

 // in the String from which the character was picked

 Vector<Integer> []index = new Vector[26];

 for (int i = 0; i < 26; i++)

 index[i] = new Vector<Integer>();

 for (int i = 0; i < n; i++) {

 for (int j = 0; j < a.get(i).length(); j++) {

 

 // we are storing j+1 because the initial picked index

 // in the recursive step will ne 0.

 // This is just for ease of implementation

 index[a.get(i).charAt(j) - 'a'].add(j + 1);

 }

 }

 

 // initialise dp table. -1 represents that

 // the subproblem hasn't been solved

 for(int i = 0;i< 1000;i++)

 {

 for (int j = 0; j < 1000; j++) {

 dp[i][j] = -1;

 }

 }

 

 return calculate(0, 0, s, index[0]);

}

 

// Driver Code

public static void main(String[] args)

{

 Vector<String> A = new Vector<String>();

 A.add("adc");

 A.add("aec");

 A.add("erg");

 

 String S = "ac";

 

 System.out.print(countWays(A, S));

}

}

// This code is contributed by Princi Singh  
  
---  
  
 __

 __

## Python 3

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 Program to Count the number of ways to

# construct the target string

mod = 1000000007

dp = [[-1 for i in range(1000)] for j in
range(1000)];

def calculate(pos, prev, s,index):

 # base case

 if (pos == len(s)):

 return 1

 # If current subproblem has been solved, use the value

 if (dp[pos][prev] != -1):

 return dp[pos][prev]

 # current character

 c = ord(s[pos]) - ord('a');

 # search through all the indiced at which the current

 # character occurs. For each index greater than prev,

 # take the index and move

 # to the next position, and add to the answer.

 answer = 0

 for i in range(len(index)):

 if (index[i] > prev):

 answer = (answer % mod + calculate(pos + 1,index[i], s,
index) % mod) % mod

 

 dp[pos][prev] = 4

 # Store and return the solution for this subproblem

 return dp[pos][prev]

def countWays(a, s):

 n = len(a)

 # preprocess the strings by storing for each

 # character of every string, the index of their

 # occurrence we will use a common list for all

 # because of only the index matter

 # in the string from which the character was picked

 index = [[] for i in range(26)]

 for i in range(n):

 for j in range(len(a[i])):

 # we are storing j+1 because the initial picked index

 # in the recursive step will ne 0.

 # This is just for ease of implementation

 index[ord(a[i][j]) - ord('a')].append(j + 1);

 # initialise dp table. -1 represents that

 # the subproblem hasn't been solve

 return calculate(0, 0, s, index[0])

# Driver Code

if __name__ == '__main__':

 A = []

 A.append("adc")

 A.append("aec")

 A.append("erg")

 S = "ac"

 print(countWays(A, S))

# This code is contributed by Surendra_Gangwar  
  
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

// C# Program to Count the number of ways to

// conthe target String

using System;

using System.Collections.Generic;

class GFG{

 

static int mod = 1000000007;

 

static int [,]dp = new int[1000,1000];

 

static int calculate(int pos, int prev, String s, List<int>
index)

{

 

 // base case

 if (pos == s.Length)

 return 1;

 

 // If current subproblem has been solved, use the value

 if (dp[pos,prev] != -1)

 return dp[pos,prev];

 

 

 // search through all the indiced at which the current

 // character occurs. For each index greater than prev,

 // take the index and move

 // to the next position, and add to the answer.

 int answer = 0;

 for (int i = 0; i < index.Count; i++) {

 if (index[i].CompareTo(prev) >= 0) {

 answer = (answer % mod + calculate(pos + 1,

 index[i], s, index) % mod) % mod;

 }

 }

 

 // Store and return the solution for this subproblem

 return dp[pos,prev] = answer;

}

 

static int countWays(List<String> a, String s)

{

 int n = a.Count;

 

 // preprocess the Strings by storing for each

 // character of every String, the index of their

 // occurrence we will use a common list for all

 // because of only the index matter

 // in the String from which the character was picked

 List<int> []index = new List<int>[26];

 for (int i = 0; i < 26; i++)

 index[i] = new List<int>();

 for (int i = 0; i < n; i++) {

 for (int j = 0; j < a[i].Length; j++) {

 

 // we are storing j+1 because the initial picked index

 // in the recursive step will ne 0.

 // This is just for ease of implementation

 index[a[i][j] - 'a'].Add(j + 1);

 }

 }

 

 // initialise dp table. -1 represents that

 // the subproblem hasn't been solved

 for(int i = 0;i< 1000;i++)

 {

 for (int j = 0; j < 1000; j++) {

 dp[i,j] = -1;

 }

 }

 

 return calculate(0, 0, s, index[0]);

}

 

// Driver Code

public static void Main(String[] args)

{

 List<String> A = new List<String>();

 A.Add("adc");

 A.Add("aec");

 A.Add("erg");

 

 String S = "ac";

 

 Console.Write(countWays(A, S));

}

}

// This code is contributed by sapnasingh4991  
  
---  
  
 __

 __

 **Output:**

    
    
    4
    
    
    
    

**Time complexity :** O(M * N2), where M is the length of the target string,
and N is the length of each of the array strings.

### Approach: (Dynamic programming + counter+twopointers)

  1. The idea is to First store all the occurrences of the string by traversing all the possible positions in a default dictionary
  2. Now define another function and start from the 0th position by placing the two pointers over the 0th index and start recursion
  3. For the recursion first, we should define the base cases in order to terminate the recursion at some point

Base cases are mentioned below:

> 1.if i==n: # if i is equal to n
>
> return 1 #return
>
> 2\. if start==m: # if start is equal to m
>
> return 0 #
>
> 1.In the first base case if the given i == n that means only one character
> exists we simple return 1
>
>  
>
>
>  
>
>
> 2\. if the start == length of the first character of the string we return 0
> since we just terminate our recursion

Main condition:

  * Now we will perform the pair recursion and check whether the target can be formed from the given string if yes we will simply increment the counter:

> ans = 0 # initilaize the ans with 0
>
> ans += back(i, start + 1) # recursive call and stroe the result in ans
> variable

  * Likewise, we will multiply the recursion call with the given string and check whether the target can be generated from the string:

> if positions[start][target[i]]: # check the condition
>
> ans += positions[start][target[i]] * back(i + 1, start + 1) # multiply with
> the each charecter and the recursive call

  * Finally, we return the answer

    
    
     **Time complexity:** O(2^n)
    **space complexity: O(N)**

 **Implementation:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

from collections import defaultdict,Counter

# total ways calculator function

def numWays(words,target):

 

 # length of first word

 m = len(words[0])

 

 # length of the target

 n = len(target)

 

 # stroing in default dict

 positions = defaultdict(Counter)

 

 # traversing array

 for i in range(len(words)):

 

 # traversing like 2d row and col

 for j in range(m):

 

 # store the occurences in dict

 positions[j][words[i][j]] += 1

 

 # define the back function 

 def back(i, start):

 

 # if i is equal to n

 if i==n:

 return 1

 

 # if start is equal to m

 if start==m:

 return 0

 

 # initilaize the ans with 0 

 ans = 0

 

 # recursive call and store

 # the result in ans variable

 ans += back(i, start + 1)

 

 # check the condition

 if positions[start][target[i]]:

 

 # multiply with the each charecter and the recursive call

 ans += positions[start][target[i]] * back(i + 1, start
+ 1)

 return ans

 

 return back(0,0)

# Function Call

words = ["abba","baab"]

target = "bab"

print(numWays(words,target))

# This code is contributed by saikumar kudikala  
  
---  
  
 __

 __

 **Output**

    
    
    4
    
    
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


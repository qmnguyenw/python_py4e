Count of substrings of length K with exactly K distinct characters



Given a string **str** of lowercase alphabets and an integer **K** , the task
is to count all substrings of length **K** which have exactly **K** distinct
characters.

 **Example:**

>  **Input:** str = “abcc”, K = 2  
>  **Output:** 2  
>  **Explanation:**  
>  Possible substrings of length K = 2 are  
> ab : 2 distinct characters  
> bc : 2 distinct characters  
> cc : 1 distinct character  
> Only two valid substrings exist {“ab”, “bc”}.
>
>  **Input:** str = “aabab”, K = 3  
>  **Output:** 0  
>  **Explanation:**  
>  Possible substrings of length K = 3 are  
> aab : 2 distinct characters  
> aba : 2 distinct characters  
> bab : 2 distinct characters  
> No substrings of length 3 exists with exactly 3 distinct characters

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Naive approach:**  
The idea is to generate all substrings of length **K** and for each substring
count number of distinct characters. If the length of a string is **N** , then
there can be **N – K + 1** substrings of length **K**. Generating these
substrings will require **O(N)** complexity, and for checking each substring
requires **O(K)** complexity, hence making the overall complexity as
**O(N*K).**

  

  

 **Efficient approach:**  
The idea is to use Window Sliding Technique. Maintain a window of size **K**
and keep a count of all the characters in the window using a HashMap. Traverse
through the string reducing the count of the first character of the previous
window and adding the frequency of the last character of the current window in
the **HashMap**. If the count of distinct characters in a window of length
**K** is equal to **K** , increment the answer by 1.

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to find the

// count of k length substrings 

// with k distinct characters 

// using sliding window 

#include <bits/stdc++.h> 

using namespace std; 

 

// Function to return the 

// required count of substrings 

int countSubstrings(string str, int K) 

{ 

 int N = str.size(); 

 // Store the count 

 int answer = 0; 

 

 // Store the count of 

 // distinct characters 

 // in every window 

 unordered_map<char, int> map; 

 

 // Store the frequency of 

 // the first K length substring 

 for (int i = 0; i < K; i++) { 

 

 // Increase frequency of 

 // i-th character 

 map[str[i]]++; 

 } 

 

 // If K distinct characters 

 // exist 

 if (map.size() == K) 

 answer++; 

 

 // Traverse the rest of the 

 // substring 

 for (int i = K; i < N; i++) { 

 

 // Increase the frequency 

 // of the last character 

 // of the current substring 

 map[str[i]]++; 

 // Decrease the frequency 

 // of the first character 

 // of the previous substring 

 map[str[i - K]]--; 

 

 // If the character is not present 

 // in the current substring 

 if (map[str[i - K]] == 0) { 

 map.erase(str[i - K]); 

 } 

 

 // If the count of distinct 

 // characters is 0 

 if (map.size() == K) { 

 answer++; 

 } 

 } 

 

 // Return the count 

 return answer; 

} 

 

// Driver code 

int main() 

{ 

 // string str 

 string str = "aabcdabbcdc"; 

 

 // integer K 

 int K = 3; 

 

 // Print the count of K length 

 // substrings with k distinct characters 

 cout << countSubstrings(str, K) << endl; 

 

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

// Java program to find the count

// of k length substrings with k 

// distinct characters using 

// sliding window 

import java.util.*; 

 

class GFG{ 

 

// Function to return the 

// required count of substrings 

public static int countSubstrings(String str, 

 int K) 

{ 

 int N = str.length(); 

 

 // Store the count 

 int answer = 0; 

 

 // Store the count of 

 // distinct characters 

 // in every window 

 Map<Character, 

 Integer> map = new HashMap<Character, 

 Integer>(); 

 

 // Store the frequency of 

 // the first K length substring 

 for(int i = 0; i < K; i++) 

 { 

 

 // Increase frequency of 

 // i-th character 

 if (map.get(str.charAt(i)) == null) 

 { 

 map.put(str.charAt(i), 1); 

 } 

 else

 { 

 map.put(str.charAt(i), 

 map.get(str.charAt(i)) + 1); 

 } 

 } 

 

 // If K distinct characters 

 // exist 

 if (map.size() == K) 

 answer++; 

 

 // Traverse the rest of the 

 // substring 

 for(int i = K; i < N; i++) 

 { 

 

 // Increase the frequency 

 // of the last character 

 // of the current substring 

 if (map.get(str.charAt(i)) == null) 

 { 

 map.put(str.charAt(i), 1); 

 } 

 else

 { 

 map.put(str.charAt(i), 

 map.get(str.charAt(i)) + 1); 

 } 

 

 // Decrease the frequency 

 // of the first character 

 // of the previous substring 

 map.put(str.charAt(i - K), 

 map.get(str.charAt(i - K)) - 1); 

 

 // If the character is not present 

 // in the current substring 

 if (map.get(str.charAt(i - K)) == 0) 

 { 

 map.remove(str.charAt(i - K)); 

 } 

 

 // If the count of distinct 

 // characters is 0 

 if (map.size() == K) 

 { 

 answer++; 

 } 

 } 

 

 // Return the count 

 return answer; 

} 

 

// Driver code 

public static void main(String[] args) 

{ 

 

 // string str 

 String str = "aabcdabbcdc"; 

 

 // integer K 

 int K = 3; 

 

 // Print the count of K length 

 // substrings with k distinct characters 

 System.out.println(countSubstrings(str, K)); 

} 

} 

 

// This code is contributed by grand_master   
  
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

# Python3 program to find the

# count of k length substrings 

# with k distinct characters 

# using sliding window 

 

# Function to return the 

# required count of substrings 

def countSubstrings(str, K): 

 

 N = len(str) 

 

 # Store the count 

 answer = 0

 

 # Store the count of 

 # distinct characters 

 # in every window 

 map = {} 

 

 # Store the frequency of 

 # the first K length substring 

 for i in range(K): 

 

 # Increase frequency of 

 # i-th character 

 map[str[i]] = map.get(str[i], 0) + 1

 

 # If K distinct characters 

 # exist 

 if (len(map) == K): 

 answer += 1

 

 # Traverse the rest of the 

 # substring 

 for i in range(K, N): 

 

 # Increase the frequency 

 # of the last character 

 # of the current substring 

 map[str[i]] = map.get(str[i], 0) + 1

 

 # Decrease the frequency 

 # of the first character 

 # of the previous substring 

 map[str[i - K]] -= 1

 

 # If the character is not present 

 # in the current substring 

 if (map[str[i - K]] == 0): 

 del map[str[i - K]] 

 

 # If the count of distinct 

 # characters is 0 

 if (len(map) == K): 

 answer += 1

 

 # Return the count 

 return answer 

 

# Driver code 

if __name__ == '__main__': 

 

 str = "aabcdabbcdc"

 

 # Integer K 

 K = 3

 

 # Print the count of K length 

 # substrings with k distinct characters 

 print(countSubstrings(str, K)) 

 

# This code is contributed by mohit kumar 29   
  
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

// C# program to find the count

// of k length substrings with k 

// distinct characters using 

// sliding window 

using System;

using System.Collections.Generic; 

 

class GFG{

 

// Function to return the 

// required count of substrings 

public static int countSubstrings(string str,

 int K) 

{ 

 int N = str.Length;

 

 // Store the count 

 int answer = 0; 

 

 // Store the count of 

 // distinct characters 

 // in every window 

 Dictionary<char, 

 int> map = new Dictionary<char, 

 int>(); 

 

 // Store the frequency of 

 // the first K length substring 

 for(int i = 0; i < K; i++) 

 { 

 

 // Increase frequency of 

 // i-th character

 if(!map.ContainsKey(str[i]))

 {

 map[str[i]] = 1;

 }

 else

 {

 map[str[i]]++; 

 }

 } 

 

 // If K distinct characters 

 // exist 

 if (map.Count == K) 

 answer++; 

 

 // Traverse the rest of the 

 // substring 

 for(int i = K; i < N; i++)

 { 

 

 // Increase the frequency 

 // of the last character 

 // of the current substring 

 if(!map.ContainsKey(str[i]))

 {

 map[str[i]] = 1;

 }

 else

 {

 map[str[i]]++; 

 }

 

 // Decrease the frequency 

 // of the first character 

 // of the previous substring

 map[str[i - K]]--;

 

 // If the character is not present 

 // in the current substring 

 if (map[str[i - K]] == 0)

 { 

 map.Remove(str[i - K]); 

 } 

 

 // If the count of distinct 

 // characters is 0 

 if (map.Count == K)

 { 

 answer++; 

 } 

 } 

 

 // Return the count 

 return answer; 

} 

 

// Driver code 

public static void Main(string[] args) 

{ 

 

 // string str 

 string str = "aabcdabbcdc"; 

 

 // integer K 

 int K = 3; 

 

 // Print the count of K length 

 // substrings with k distinct characters 

 Console.Write(countSubstrings(str, K));

} 

}

 

// This code is contributed by rutvik_56  
  
---  
  
 __

 __

 **Output:**

    
    
    5
    

**Time Complexity:** O(N)

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


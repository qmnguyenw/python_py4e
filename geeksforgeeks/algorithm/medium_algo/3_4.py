Largest lexicographical string with at most K consecutive elements



Given a string **S** , the task is to find the largest lexicographical string
with no more than **K** consecutive occurrence of an element by either re-
arranging or deleting the elements.  
 **Examples:**

> **Input:** S = “baccc”  
> K = 2  
> **Output:** Result = “ccbca”  
> **Explanation:** Since K=2, a maximum of 2 same characters can be placed
> consecutively.  
> No. of ‘c’ = 3.  
> No. of ‘b’ = 1.  
> No. of ‘a’ = 1.  
> Since the largest lexicographical string has to be printed, therefore, the
> answer is “ccbca”.
>
>  **Input:** S = “xxxxzaz”  
> K = 3  
> **Output:** result = “zzxxxax”

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:**

  1. Form a frequency array of size 26, where index i is chosen using (a character in a string – ‘a’).
  2. Initialize an empty string to store corresponding changes.
  3. For i=25 to 0, do:
    * If frequency at index i is greater than k, then append (i + ‘a’) K-times. Decrease frequency by K at index i.find the next greatest priority element and append to answer and decrease the frequency at the respective index by 1.
    * If frequency at index i is greater than 0 but less than k, then append (i + ‘a’) times its frequency.
    * If frequency at index i is 0, then that index cannot be used to form an element and therefore check for the next possible highest priority element.  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ code for the above approach

#include <bits/stdc++.h>

using namespace std;

#define ll long long int

// Function to find the

// largest lexicographical

// string with given constraints.

string getLargestString(string s,

 ll k)

{

 // vector containing frequency

 // of each character.

 vector<int> frequency_array(26, 0);

 // assigning frequency to

 for (int i = 0;

 i < s.length(); i++) {

 frequency_array[s[i] - 'a']++;

 }

 // empty string of string class type

 string ans = "";

 // loop to iterate over

 // maximum priority first.

 for (int i = 25; i >= 0;) {

 // if frequency is greater than

 // or equal to k.

 if (frequency_array[i] > k) {

 // temporary variable to operate

 // in-place of k.

 int temp = k;

 string st(1, i + 'a');

 while (temp > 0) {

 // concatenating with the

 // resultant string ans.

 ans += st;

 temp--;

 }

 frequency_array[i] -= k;

 // handling k case by adjusting

 // with just smaller priority

 // element.

 int j = i - 1;

 while (frequency_array[j]

 <= 0

 && j >= 0) {

 j--;

 }

 // condition to verify if index

 // j does have frequency

 // greater than 0;

 if (frequency_array[j] > 0

 && j >= 0) {

 string str(1, j + 'a');

 ans += str;

 frequency_array[j] -= 1;

 }

 else {

 // if no such element is found

 // than string can not be

 // processed further.

 break;

 }

 }

 // if frequency is greater than 0

 // and less than k.

 else if (frequency_array[i] > 0) {

 // here we don't need to fix K

 // consecutive element criteria.

 int temp = frequency_array[i];

 frequency_array[i] -= temp;

 string st(1, i + 'a');

 while (temp > 0) {

 ans += st;

 temp--;

 }

 }

 // otherwise check for next

 // possible element.

 else {

 i--;

 }

 }

 return ans;

}

// Driver program

int main()

{

 string S = "xxxxzza";

 int k = 3;

 cout << getLargestString(S, k)

 << endl;

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

// Java code for

// the above approach

import java.util.*;

class GFG{

// Function to find the

// largest lexicographical

// String with given constraints.

static String getLargestString(String s,

 int k)

{

 // Vector containing frequency

 // of each character.

 int []frequency_array = new int[26];

 // Assigning frequency

 for (int i = 0;

 i < s.length(); i++)

 {

 frequency_array[s.charAt(i) - 'a']++;

 }

 // Empty String of

 // String class type

 String ans = "";

 // Loop to iterate over

 // maximum priority first.

 for (int i = 25; i >= 0😉

 {

 // If frequency is greater than

 // or equal to k.

 if (frequency_array[i] > k)

 {

 // Temporary variable to

 // operate in-place of k.

 int temp = k;

 String st = String.valueOf((char)(i + 'a'));

 while (temp > 0)

 {

 // Concatenating with the

 // resultant String ans.

 ans += st;

 temp--;

 }

 frequency_array[i] -= k;

 // Handling k case by adjusting

 // with just smaller priority

 // element.

 int j = i - 1;

 

 while (frequency_array[j] <= 0 &&

 j >= 0)

 {

 j--;

 }

 // Condition to verify if index

 // j does have frequency

 // greater than 0;

 if (frequency_array[j] > 0 &&

 j >= 0)

 {

 String str = String.valueOf((char)(j + 'a'));

 ans += str;

 frequency_array[j] -= 1;

 }

 else

 {

 // If no such element is found

 // than String can not be

 // processed further.

 break;

 }

 }

 // If frequency is greater than 0

 // and less than k.

 else if (frequency_array[i] > 0)

 {

 // Here we don't need to fix K

 // consecutive element criteria.

 int temp = frequency_array[i];

 frequency_array[i] -= temp;

 String st = String.valueOf((char)(i + 'a'));

 

 while (temp > 0)

 {

 ans += st;

 temp--;

 }

 }

 // Otherwise check for next

 // possible element.

 else

 {

 i--;

 }

 }

 return ans;

}

// Driver code

public static void main(String[] args)

{

 String S = "xxxxzza";

 int k = 3;

 System.out.print(getLargestString(S, k));

}

}

// This code is contributed by shikhasingrajput  
  
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

# Python3 code for the above approach

# Function to find the

# largest lexicographical

# string with given constraints.

def getLargestString(s, k):

 # Vector containing frequency

 # of each character.

 frequency_array = [0] * 26

 # Assigning frequency to

 for i in range(len(s)):

 frequency_array[ord(s[i]) -

 ord('a')] += 1

 

 # Empty string of

 # string class type

 ans = ""

 # Loop to iterate over

 # maximum priority first.

 i = 25

 while i >= 0:

 # If frequency is greater than

 # or equal to k.

 if (frequency_array[i] > k):

 # Temporary variable to

 # operate in-place of k.

 temp = k

 st = chr( i + ord('a'))

 

 while (temp > 0):

 # concatenating with the

 # resultant string ans.

 ans += st

 temp -= 1

 

 frequency_array[i] -= k

 # Handling k case by adjusting

 # with just smaller priority

 # element.

 j = i - 1

 

 while (frequency_array[j] <= 0 and

 j >= 0):

 j -= 1

 

 # Condition to verify if index

 # j does have frequency

 # greater than 0;

 if (frequency_array[j] > 0 and

 j >= 0):

 str1 = chr(j + ord( 'a'))

 ans += str1

 frequency_array[j] -= 1

 

 else:

 # if no such element is found

 # than string can not be

 # processed further.

 break

 

 # If frequency is greater than 0

 #and less than k.

 elif (frequency_array[i] > 0):

 # Here we don't need to fix K

 # consecutive element criteria.

 temp = frequency_array[i]

 frequency_array[i] -= temp

 st = chr(i + ord('a'))

 while (temp > 0):

 ans += st

 temp -= 1

 

 # Otherwise check for next

 # possible element.

 else:

 i -= 1

 

 return ans 

# Driver code

if __name__ == "__main__":

 

 S = "xxxxzza"

 k = 3

 print (getLargestString(S, k))

 

# This code is contributed by Chitranayal  
  
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

// C# code for

// the above approach

using System;

class GFG{

// Function to find the

// largest lexicographical

// String with given constraints.

static String getLargestString(String s,

 int k)

{

 // List containing frequency

 // of each character.

 int []frequency_array = new int[26];

 // Assigning frequency

 for (int i = 0; i < s.Length; i++)

 {

 frequency_array[s[i] - 'a']++;

 }

 // Empty String of

 // String class type

 String ans = "";

 // Loop to iterate over

 // maximum priority first.

 for (int i = 25; i >= 0;)

 {

 // If frequency is greater than

 // or equal to k.

 if (frequency_array[i] > k)

 {

 // Temporary variable to

 // operate in-place of k.

 int temp = k;

 String st = String.Join("",

 (char)(i + 'a'));

 

 while (temp > 0)

 {

 // Concatenating with the

 // resultant String ans.

 ans += st;

 temp--;

 }

 frequency_array[i] -= k;

 // Handling k case by adjusting

 // with just smaller priority

 // element.

 int j = i - 1;

 

 while (frequency_array[j] <= 0 &&

 j >= 0)

 {

 j--;

 }

 // Condition to verify if index

 // j does have frequency

 // greater than 0;

 if (frequency_array[j] > 0 &&

 j >= 0)

 {

 String str = String.Join("",

 (char)(j + 'a'));

 ans += str;

 frequency_array[j] -= 1;

 }

 else

 {

 // If no such element is found

 // than String can not be

 // processed further.

 break;

 }

 }

 // If frequency is greater than 0

 // and less than k.

 else if (frequency_array[i] > 0)

 {

 // Here we don't need to fix K

 // consecutive element criteria.

 int temp = frequency_array[i];

 frequency_array[i] -= temp;

 String st = String.Join("",

 (char)(i + 'a'));

 

 while (temp > 0)

 {

 ans += st;

 temp--;

 }

 }

 // Otherwise check for next

 // possible element.

 else

 {

 i--;

 }

 }

 return ans;

}

// Driver code

public static void Main(String[] args)

{

 String S = "xxxxzza";

 int k = 3;

 Console.Write(getLargestString(S, k));

}

}

// This code is contributed by Princi Singh  
  
---  
  
 __

 __

 **Output**

    
    
    zzxxxax
    
    
    

_**Time Complexity:** O(N) _

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save


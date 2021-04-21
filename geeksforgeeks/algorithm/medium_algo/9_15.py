Form lexicographically smallest string with minimum replacements having equal
number of 0s, 1s and 2s



Given a string **str** of length **n** (n is a multiple of 3) containing
characters only from the set **{0, 1, 2}**. The task is to update the string
such that each character has the same frequency with minimum number of
operations. In a single operation, any character of the string can be replaced
with any other character (also from the same set). If there are multiple
strings possible then print the lexicographically smallest one.

 **Examples:**

>  **Input:** str = “000000”  
>  **Output:** 001122  
> Replace 3rd and 4th ‘0’ with ‘1’ and 5th and 6th ‘0’ with ‘2’ such that
> given condition is satisfied and it forms lexicographically smallest string
>
>  **Input:** str = “211200”  
>  **Output:** 211200  
> The string already has equal number of 0s, 1s and 2s, hence there is no need
> to perform any operation.

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** This problem can be solved using greedy approach. We need only
**n / 3** number of characters of each type where **n** is the size of the
string. Iterate over the string and count the number of characters of each
type. Again, iterate over the string and now check if the current character’s
count is equal to **n / 3** then there is no need to perform any operation on
the current character.  
However, if **count(currentChar) != n / 3** then we may need to perform
replacement operation depending on the value of the character in such a way
that it maintains smallest lexicographical order as follows:

  

  

  * If the current character is zero(0) and we have already processed required number of zeroes, then this character needs to be replaced with either one(1) if **count[1] < (n / 3)** or with two(1) if **count[2] < (n / 3)**.
  * If the current character is one(1), then we can either replace it with zero(0) if **count[0] < (n / 3)** or with two(2) if **count[2] < (n / 3)** and we have already processed required number of ones to maintain lowest lexicographical order
  * If the current character is two(2), then we can either replace it with zero(0) if **count[0] < (n / 3)** or with two(2) if **count[2] < (n / 3)**.

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

 

// Function that returns the modified lexicographically

// smallest string after performing minimum number

// of given operations

string formStringMinOperations(string s)

{

 // Stores the initial frequencies of characters

 // 0s, 1s and 2s

 int count[3] = { 0 };

 for (auto& c : s)

 count++;

 

 // Stores number of processed characters upto that

 // point of each type

 int processed[3] = { 0 };

 

 // Required number of characters of each type

 int reqd = (int)s.size() / 3;

 for (int i = 0; i < s.size(); i++) {

 

 // If the current type has already reqd

 // number of characters, no need to perform

 // any operation

 if (count[s[i] - '0'] == reqd)

 continue;

 

 // Process all 3 cases

 if (s[i] == '0' && count[0] > reqd &&

 processed[0] >= reqd) {

 

 // Check for 1 first

 if (count[1] < reqd) {

 s[i] = '1';

 count[1]++;

 count[0]--;

 }

 

 // Else 2

 else if (count[2] < reqd) {

 s[i] = '2';

 count[2]++;

 count[0]--;

 }

 }

 

 // Here we need to check processed[1] only

 // for 2 since 0 is less than 1 and we can

 // replace it anytime

 if (s[i] == '1' && count[1] > reqd) {

 if (count[0] < reqd) {

 s[i] = '0';

 count[0]++;

 count[1]--;

 }

 else if (count[2] < reqd &&

 processed[1] >= reqd) {

 s[i] = '2';

 count[2]++;

 count[1]--;

 }

 }

 

 // Here we can replace 2 with 0 and 1 anytime

 if (s[i] == '2' && count[2] > reqd) {

 if (count[0] < reqd) {

 s[i] = '0';

 count[0]++;

 count[2]--;

 }

 else if (count[1] < reqd) {

 s[i] = '1';

 count[1]++;

 count[2]--;

 }

 }

 

 // keep count of processed characters of each

 // type

 processed[s[i] - '0']++;

 }

 return s;

}

 

// Driver Code

int main()

{

 string s = "011200";

 cout << formStringMinOperations(s);

 

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

 

 // Function that returns the 

 // modified lexicographically

 // smallest String after 

 // performing minimum number

 // of given operations

 static String formStringMinOperations(char[] s) 

 {

 

 // Stores the initial frequencies 

 // of characters 0s, 1s and 2s

 int count[] = new int[3];

 for (char c : s) 

 {

 count[(int)c - 48] += 1;

 }

 

 // Stores number of processed characters 

 // upto that point of each type

 int processed[] = new int[3];

 

 // Required number of characters of each type

 int reqd = (int) s.length / 3;

 for (int i = 0; i < s.length; i++) 

 {

 

 // If the current type has already 

 // reqd number of characters, no 

 // need to perform any operation

 if (count[s[i] - '0'] == reqd) 

 {

 continue;

 }

 

 // Process all 3 cases

 if (s[i] == '0' && count[0] > reqd

 && processed[0] >= reqd) 

 {

 

 // Check for 1 first

 if (count[1] < reqd) 

 {

 s[i] = '1';

 count[1]++;

 count[0]--;

 } 

 

 // Else 2

 else if (count[2] < reqd) 

 {

 s[i] = '2';

 count[2]++;

 count[0]--;

 }

 }

 

 // Here we need to check processed[1] only

 // for 2 since 0 is less than 1 and we can

 // replace it anytime

 if (s[i] == '1' && count[1] > reqd) 

 {

 if (count[0] < reqd) 

 {

 s[i] = '0';

 count[0]++;

 count[1]--;

 } 

 else if (count[2] < reqd

 && processed[1] >= reqd) 

 {

 s[i] = '2';

 count[2]++;

 count[1]--;

 }

 }

 

 // Here we can replace 2 with 0 and 1 anytime

 if (s[i] == '2' && count[2] > reqd) 

 {

 if (count[0] < reqd)

 {

 s[i] = '0';

 count[0]++;

 count[2]--;

 } 

 else if (count[1] < reqd) 

 {

 s[i] = '1';

 count[1]++;

 count[2]--;

 }

 }

 

 // keep count of processed 

 // characters of each type

 processed[s[i] - '0']++;

 }

 return String.valueOf(s);

 }

 

 // Driver Code

 public static void main(String[] args) 

 {

 String s = "011200";

 System.out.println(formStringMinOperations(s.toCharArray()));

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

import math

 

# Function that returns the modified 

# lexicographically smallest string after 

# performing minimum number of given operations 

def formStringMinOperations(ss):

 

 # Stores the initial frequencies of 

 # characters 0s, 1s and 2s 

 count = [0] * 3;

 s = list(ss);

 for i in range(len(s)): 

 count[ord(s[i]) - ord('0')] += 1; 

 

 # Stores number of processed characters 

 # upto that point of each type 

 processed = [0] * 3; 

 

 # Required number of characters of each type 

 reqd = math.floor(len(s) / 3); 

 for i in range(len(s)): 

 

 # If the current type has already reqd 

 # number of characters, no need to 

 # perform any operation 

 if (count[ord(s[i]) - ord('0')] == reqd): 

 continue; 

 

 # Process all 3 cases 

 if (s[i] == '0' and count[0] > reqd and

 processed[0] >= reqd):

 

 # Check for 1 first 

 if (count[1] < reqd):

 s[i] = '1'; 

 count[1] += 1; 

 count[0] -= 1; 

 

 # Else 2 

 elif (count[2] < reqd): 

 s[i] = '2'; 

 count[2] += 1; 

 count[0] -= 1; 

 

 # Here we need to check processed[1] only 

 # for 2 since 0 is less than 1 and we can 

 # replace it anytime 

 if (s[i] == '1' and count[1] > reqd):

 if (count[0] < reqd):

 s[i] = '0'; 

 count[0] += 1; 

 count[1] -= 1; 

 elif (count[2] < reqd and

 processed[1] >= reqd):

 s[i] = '2'; 

 count[2] += 1; 

 count[1] -= 1; 

 

 # Here we can replace 2 with 0 and 1 anytime 

 if (s[i] == '2' and count[2] > reqd):

 if (count[0] < reqd):

 s[i] = '0'; 

 count[0] += 1; 

 count[2] -= 1; 

 elif (count[1] < reqd):

 s[i] = '1'; 

 count[1] += 1; 

 count[2] -= 1; 

 

 # keep count of processed characters 

 # of each type 

 processed[ord(s[i]) - ord('0')] += 1; 

 return ''.join(s); 

 

# Driver Code 

s = "011200"; 

print(formStringMinOperations(s)); 

 

# This code is contributed by mits  
  
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

 

 // Function that returns the 

 // modified lexicographically

 // smallest String after 

 // performing minimum number

 // of given operations

 static String formStringMinOperations(char[] s) 

 {

 

 // Stores the initial frequencies 

 // of characters 0s, 1s and 2s

 int []count = new int[3];

 foreach (char c in s) 

 {

 count[(int)c - 48] += 1;

 }

 

 // Stores number of processed characters 

 // upto that point of each type

 int []processed = new int[3];

 

 // Required number of characters of each type

 int reqd = (int) s.Length / 3;

 for (int i = 0; i < s.Length; i++) 

 {

 

 // If the current type has already 

 // reqd number of characters, no 

 // need to perform any operation

 if (count[s[i] - '0'] == reqd) 

 {

 continue;

 }

 

 // Process all 3 cases

 if (s[i] == '0' && count[0] > reqd

 && processed[0] >= reqd) 

 {

 

 // Check for 1 first

 if (count[1] < reqd) 

 {

 s[i] = '1';

 count[1]++;

 count[0]--;

 } 

 

 // Else 2

 else if (count[2] < reqd) 

 {

 s[i] = '2';

 count[2]++;

 count[0]--;

 }

 }

 

 // Here we need to check processed[1] only

 // for 2 since 0 is less than 1 and we can

 // replace it anytime

 if (s[i] == '1' && count[1] > reqd) 

 {

 if (count[0] < reqd) 

 {

 s[i] = '0';

 count[0]++;

 count[1]--;

 } 

 else if (count[2] < reqd

 && processed[1] >= reqd) 

 {

 s[i] = '2';

 count[2]++;

 count[1]--;

 }

 }

 

 // Here we can replace 2 with 0 and 1 anytime

 if (s[i] == '2' && count[2] > reqd) 

 {

 if (count[0] < reqd)

 {

 s[i] = '0';

 count[0]++;

 count[2]--;

 } 

 else if (count[1] < reqd) 

 {

 s[i] = '1';

 count[1]++;

 count[2]--;

 }

 }

 

 // keep count of processed 

 // characters of each type

 processed[s[i] - '0']++;

 }

 return String.Join("",s);

 }

 

 // Driver Code

 public static void Main(String[] args) 

 {

 String s = "011200";

 Console.WriteLine(formStringMinOperations(s.ToCharArray()));

 }

}

 

// This code is contributed by Rajput-Ji  
  
---  
  
 __

 __

## PHP

 __

 __  
 __

 __

 __  
 __  
 __

<?php

// PHP implementation of the approach 

 

// Function that returns the modified lexicographically 

// smallest string after performing minimum number 

// of given operations 

function formStringMinOperations($s) 

{ 

 // Stores the initial frequencies of 

 // characters 0s, 1s and 2s 

 $count = array_fill(0, 3, 0);

 

 for ($i = 0; $i < strlen($s) ; $i++) 

 $count[$s[$i] - '0']++; 

 

 // Stores number of processed characters 

 // upto that point of each type 

 $processed = array_fill(0, 3, 0); 

 

 // Required number of characters of each type 

 $reqd = floor(strlen($s) / 3); 

 for ($i = 0; $i < strlen($s); $i++) 

 { 

 

 // If the current type has already reqd 

 // number of characters, no need to 

 // perform any operation 

 if ($count[$s[$i] - '0'] == $reqd) 

 continue; 

 

 // Process all 3 cases 

 if ($s[$i] == '0' && $count[0] > $reqd && 

 $processed[0] >= $reqd)

 { 

 

 // Check for 1 first 

 if ($count[1] < $reqd)

 { 

 $s[$i] = '1'; 

 $count[1]++; 

 $count[0]--; 

 } 

 

 // Else 2 

 else if ($count[2] < $reqd) 

 { 

 $s[$i] = '2'; 

 $count[2]++; 

 $count[0]--; 

 } 

 } 

 

 // Here we need to check processed[1] only 

 // for 2 since 0 is less than 1 and we can 

 // replace it anytime 

 if ($s[$i] == '1' && $count[1] > $reqd) 

 { 

 if ($count[0] < $reqd) 

 { 

 $s[$i] = '0'; 

 $count[0]++; 

 $count[1]--; 

 } 

 else if (count[2] < $reqd && 

 $processed[1] >= $reqd) 

 { 

 $s[$i] = '2'; 

 $count[2]++; 

 $count[1]--; 

 } 

 } 

 

 // Here we can replace 2 with 0 and 1 anytime 

 if ($s[$i] == '2' && $count[2] > $reqd)

 { 

 if ($count[0] < $reqd)

 { 

 $s[$i] = '0'; 

 $count[0]++; 

 $count[2]--; 

 } 

 else if ($count[1] < $reqd) 

 { 

 $s[$i] = '1'; 

 $count[1]++; 

 $count[2]--; 

 } 

 } 

 

 // keep count of processed characters 

 // of each type 

 $processed[$s[$i] - '0']++; 

 } 

 return $s; 

} 

 

// Driver Code 

$s = "011200"; 

echo formStringMinOperations($s); 

 

// This code is contributed by Ryuga

?>  
  
---  
  
 __

 __

 **Output:**

    
    
    011202
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


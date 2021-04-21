Minimum number of operations to move all uppercase characters before all lower
case characters



Given a string **str** , containing upper case and lower case characters. In a
single operations, any lowercase character can be converted to an uppercase
character and vice versa. The task is to print the minimum number of such
operations required so that the resultant string consists of zero or more
upper case characters followed by zero or more lower case characters.

 **Examples:**

>  **Input:** str = “geEks”  
>  **Output:** 1  
> Either the first 2 characters can be converted to uppercase characters i.e.
> “GEEks” with 2 operations.  
> Or the third character can be converted to a lowercase character i.e.
> “geeks” with a single operation.
>
>  **Input:** str = “geek”  
>  **Output:** 0  
> The string is already in the specified format.

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** There are two possible cases:

  

  

  * Find the index of the last uppercase character in the string and convert all the lowercase characters appearing before it into uppercase characters.
  * Or, find the index of the first lowercase character in the string and convert all the uppercase characters appearing after it into lowercase characters.

Choose the case where the operations required are minimum.

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

#include<bits/stdc++.h>

using namespace std;

 

// Function to return the minimum

// number of operations required

int minOperations(string str, int n)

{

 

 // To store the indices of the last uppercase

 // and the first lowercase character

 int i, lastUpper = -1, firstLower = -1;

 

 // Find the last uppercase character

 for (i = n - 1; i >= 0; i--)

 {

 if (isupper(str[i]))

 {

 lastUpper = i;

 break;

 }

 }

 

 // Find the first lowercase character

 for (i = 0; i < n; i++) 

 {

 if (islower(str[i])) 

 {

 firstLower = i;

 break;

 }

 }

 

 // If all the characters are either

 // uppercase or lowercase

 if (lastUpper == -1 || firstLower == -1)

 return 0;

 

 // Count of uppercase characters that appear

 // after the first lowercase character

 int countUpper = 0;

 for (i = firstLower; i < n; i++) 

 {

 if (isupper(str[i])) 

 {

 countUpper++;

 }

 }

 

 // Count of lowercase characters that appear

 // before the last uppercase character

 int countLower = 0;

 for (i = 0; i < lastUpper; i++) 

 {

 if (islower(str[i])) 

 {

 countLower++;

 }

 }

 

 // Return the minimum operations required

 return min(countLower, countUpper);

}

 

// Driver Code

int main()

{

 string str = "geEksFOrGEekS";

 int n = str.length();

 cout << minOperations(str, n) << endl;

}

 

// This code is contributed by

// Surendra_Gangwar  
  
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

class GFG {

 

 // Function to return the minimum

 // number of operations required

 static int minOperations(String str, int n)

 {

 

 // To store the indices of the last uppercase

 // and the first lowercase character

 int i, lastUpper = -1, firstLower = -1;

 

 // Find the last uppercase character

 for (i = n - 1; i >= 0; i--) {

 if (Character.isUpperCase(str.charAt(i))) {

 lastUpper = i;

 break;

 }

 }

 

 // Find the first lowercase character

 for (i = 0; i < n; i++) {

 if (Character.isLowerCase(str.charAt(i))) {

 firstLower = i;

 break;

 }

 }

 

 // If all the characters are either

 // uppercase or lowercase

 if (lastUpper == -1 || firstLower == -1)

 return 0;

 

 // Count of uppercase characters that appear

 // after the first lowercase character

 int countUpper = 0;

 for (i = firstLower; i < n; i++) {

 if (Character.isUpperCase(str.charAt(i))) {

 countUpper++;

 }

 }

 

 // Count of lowercase characters that appear

 // before the last uppercase character

 int countLower = 0;

 for (i = 0; i < lastUpper; i++) {

 if (Character.isLowerCase(str.charAt(i))) {

 countLower++;

 }

 }

 

 // Return the minimum operations required

 return Math.min(countLower, countUpper);

 }

 

 // Driver Code

 public static void main(String args[])

 {

 String str = "geEksFOrGEekS";

 int n = str.length();

 System.out.println(minOperations(str, n));

 }

}  
  
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

# Python 3 implementation of the approach

 

# Function to return the minimum

# number of operations required

def minOperations(str, n):

 

 # To store the indices of the last uppercase

 # and the first lowercase character

 lastUpper = -1

 firstLower = -1

 

 # Find the last uppercase character

 for i in range( n - 1, -1, -1):

 if (str[i].isupper()):

 lastUpper = i

 break

 

 # Find the first lowercase character

 for i in range(n):

 if (str[i].islower()):

 firstLower = i

 break

 

 # If all the characters are either

 # uppercase or lowercase

 if (lastUpper == -1 or firstLower == -1):

 return 0

 

 # Count of uppercase characters that appear

 # after the first lowercase character

 countUpper = 0

 for i in range( firstLower,n):

 if (str[i].isupper()):

 countUpper += 1

 

 # Count of lowercase characters that appear

 # before the last uppercase character

 countLower = 0

 for i in range(lastUpper):

 if (str[i].islower()):

 countLower += 1

 

 # Return the minimum operations required

 return min(countLower, countUpper)

 

# Driver Code

if __name__ == "__main__":

 

 str = "geEksFOrGEekS"

 n = len(str)

 print(minOperations(str, n))

 

# This code is contributed by Ita_c.  
  
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

 

 // Function to return the minimum 

 // number of operations required 

 static int minOperations(string str, int n) 

 { 

 

 // To store the indices of the last uppercase 

 // and the first lowercase character 

 int i, lastUpper = -1, firstLower = -1; 

 

 // Find the last uppercase character 

 for (i = n - 1; i >= 0; i--) 

 { 

 if (Char.IsUpper(str[i])) 

 { 

 lastUpper = i; 

 break; 

 } 

 } 

 

 // Find the first lowercase character 

 for (i = 0; i < n; i++)

 { 

 if (Char.IsLower(str[i])) 

 { 

 firstLower = i; 

 break; 

 } 

 } 

 

 // If all the characters are either 

 // uppercase or lowercase 

 if (lastUpper == -1 || firstLower == -1) 

 return 0; 

 

 // Count of uppercase characters that appear 

 // after the first lowercase character 

 int countUpper = 0; 

 for (i = firstLower; i < n; i++)

 { 

 if (Char.IsUpper(str[i]))

 { 

 countUpper++; 

 } 

 } 

 

 // Count of lowercase characters that appear 

 // before the last uppercase character 

 int countLower = 0; 

 for (i = 0; i < lastUpper; i++)

 { 

 if (Char.IsLower(str[i])) 

 { 

 countLower++; 

 } 

 } 

 

 // Return the minimum operations required 

 return Math.Min(countLower, countUpper); 

 } 

 

 // Driver Code 

 public static void Main() 

 { 

 string str = "geEksFOrGEekS"; 

 int n = str.Length; 

 Console.WriteLine(minOperations(str, n)); 

 } 

} 

 

// This code is contributed by Ryuga  
  
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

 

// Function to return the minimum

// number of operations required

function minOperations($str, $n)

{

 

 // To store the indices of the last uppercase

 // and the first lowercase character

 $i; $lastUpper = -1; $firstLower = -1;

 

 // Find the last uppercase character

 for ($i = $n - 1; $i >= 0; $i--)

 {

 if (ctype_upper($str[$i]))

 {

 $lastUpper = $i;

 break;

 }

 }

 

 // Find the first lowercase character

 for ($i = 0; $i < $n; $i++) 

 {

 if (ctype_lower($str[$i])) 

 {

 $firstLower = $i;

 break;

 }

 }

 

 // If all the characters are either

 // uppercase or lowercase

 if ($lastUpper == -1 || $firstLower == -1)

 return 0;

 

 // Count of uppercase characters that appear

 // after the first lowercase character

 $countUpper = 0;

 for ($i = $firstLower; $i < $n; $i++) 

 {

 if (ctype_upper($str[$i])) 

 {

 $countUpper++;

 }

 }

 

 // Count of lowercase characters that appear

 // before the last uppercase character

 $countLower = 0;

 for ($i = 0; $i < $lastUpper; $i++)

 {

 if (ctype_lower($str[$i])) 

 {

 $countLower++;

 }

 }

 

 // Return the minimum operations required

 return min($countLower, $countUpper);

 }

 

 // Driver Code

 {

 $str = "geEksFOrGEekS";

 $n = strlen($str);

 echo(minOperations($str, $n));

 }

 

// This code is contributed by Code_Mech

?>  
  
---  
  
 __

 __

 **Output:**

    
    
    6
    

**Time Complexity:** O(N) where N is the length of the string.

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


Check if all bits can be made same by single flip



Given a binary string, find if it is possible to make all its digits equal
(either all 0’s or all 1’s) by flipping exactly one bit.

    
    
    Input: 101
    Output: Yes
    Explanation: In 101, the 0 can be flipped
                 to make it all 1
    
    Input: 11
    Output: No
    Explanation: No matter whichever digit you 
      flip, you will not get the desired string.
    
    Input: 1
    Output: Yes
    Explanation: We can flip 1, to make all 0's

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Method 1 (Counting 0’s and 1’s)**  
If all digits of a string can be made identical by doing exactly one flip,
that means the string has all its digits equal to one another except this
digit which has to be flipped, and this digit must be different than all other
digits of the string. The value of this digit could be either zero or one.
Hence, this string will either have exactly one digit equal to zero, and all
other digits equal to one, or exactly one digit equal to one, and all other
digit equal to zero.  
Therefore, we only need to check whether the string has exactly one digit
equal to zero/one, and if so, the answer is yes; otherwise the answer is no.

Below is the implementation of above idea.

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to check if a sinle bit can

// be flipped tp make all ones

#include <bits/stdc++.h>

using namespace std;

// This function returns true if we can

// bits same in given binary string str.

bool canMakeAllSame(string str)

{

 int zeros = 0, ones = 0;

 // Traverse through given string and

 // count numbers of 0's and 1's

 for (char ch : str)

 (ch == '0') ? ++zeros : ++ones;

 // Return true if any of the two counts

 // is 1

 return (zeros == 1 || ones == 1);

}

// Driver code

int main()

{

 canMakeAllSame("101") ? printf("Yes\n") :
printf("No\n");

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

// Java program to check if a single bit can

// be flipped to make all ones

public class GFG {

 // This function returns true if we can

 // bits same in given binary string str.

 static boolean canMakeAllSame(String str)

 {

 int zeros = 0, ones = 0;

 // Traverse through given string and

 // count numbers of 0's and 1's

 for (int i = 0; i < str.length(); i++) {

 char ch = str.charAt(i);

 if (ch == '0')

 ++zeros;

 else

 ++ones;

 }

 // Return true if any of the two counts

 // is 1

 return (zeros == 1 || ones == 1);

 }

 // Driver code

 public static void main(String args[])

 {

 System.out.println(canMakeAllSame("101") ? "Yes" : "No");

 }

}

// This code is contributed by Sumit Ghosh  
  
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

# python program to check if a sinle

# bit can be flipped tp make all ones

# This function returns true if we can

# bits same in given binary string str.

def canMakeAllSame(str):

 zeros = 0

 ones = 0

 # Traverse through given string and

 # count numbers of 0's and 1's

 for i in range(0, len(str)):

 ch = str[i];

 if (ch == '0'):

 zeros = zeros + 1

 else:

 ones = ones + 1

 # Return true if any of the two

 # counts is 1

 return (zeros == 1 or ones == 1);

# Driver code

if(canMakeAllSame("101")):

 print("Yes\n")

else:

 print("No\n")

# This code is contributed by Sam007.  
  
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

// C# program to check if a single bit can

// be flipped to make all ones

using System;

class GFG {

 

 // This function returns true if we can

 // bits same in given binary string str.

 static bool canMakeAllSame(string str)

 {

 int zeros = 0, ones = 0;

 // Traverse through given string and

 // count numbers of 0's and 1's

 for (int i = 0; i < str.Length; i++) {

 char ch = str[i];

 if (ch == '0')

 ++zeros;

 else

 ++ones;

 }

 // Return true if any of the two counts

 // is 1

 return (zeros == 1 || ones == 1);

 }

 // Driver code

 public static void Main()

 {

 Console.WriteLine(canMakeAllSame("101") ? "Yes" : "No");

 }

}

// This code is contributed by Sam007  
  
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

// PHP program to check if a sinle bit can

// be flipped tp make all ones

 

// This function returns true if we can

// bits same in given binary string str.

function canMakeAllSame($str)

{

 $zeros = 0;

 $ones = 0;

 

 // Traverse through given string and

 // count numbers of 0's and 1's

 

 for($i=0;$i<strlen($str);$i++)

 {

 $ch = $str[$i];

 if ($ch == '0')

 ++$zeros ;

 else

 ++$ones;

 }

 // Return true if any of the two counts

 // is 1

 return ($zeros == 1 || $ones == 1);

}

 

// Driver code

 if (canMakeAllSame("101") )

 echo "Yes\n" ;

 else echo "No\n";

 return 0;

?>  
  
---  
  
 __

 __

## Javascript

 __

 __  
 __

 __

 __  
 __  
 __

<script>

// Javascript program to check if a single bit can

// be flipped to make all ones

 

 // This function returns true if we can

 // bits same in given binary string str.

 function canMakeAllSame(str)

 {

 let zeros = 0, ones = 0;

 

 // Traverse through given string and

 // count numbers of 0's and 1's

 for (let i = 0; i < str.length; i++) {

 let ch = str[i];

 if (ch == '0')

 ++zeros;

 else

 ++ones;

 }

 

 // Return true if any of the two counts

 // is 1

 return (zeros == 1 || ones == 1);

 }

 

 // Driver code

 document.write(canMakeAllSame("101") ? "Yes" : "No");

 

 // This code is contributed by rag2127

</script>  
  
---  
  
 __

 __

 **Output:**

    
    
    Yes

 **Time complexity :** O(n) where n is the length of the string.

  

  

 **Method 2 (Counting 0’s and 1’s)**  
The idea is to compute sum of all bits. If sum is n-1 or 1, then output is
true, else false. This solution doesn’t require a comparison in a loop.

Below is the implementation of above idea.

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// Check if all bits can be made same by single flip

// Idea is to add the integer value all the elements

// in the given string.

// If the sum is 1 it indicates that there is

// only single '1' in the string.

// If the sum is 0 it indicates that there is only

// single '0' in the string.

// It takes O(n) time.

#include <bits/stdc++.h>

using namespace std;

bool isOneFlip(string str)

{

 int sum = 0;

 int n = str.length();

 // Traverse through given string and

 // count the total sum of numbers

 for (int i = 0; i < n; i++)

 sum += str[i] - '0';

 // Return true if any of the two counts

 // is 1

 return (sum == n - 1 || sum == 1);

}

// Main function

int main()

{

 isOneFlip("101111111111") ? printf("Yes\n") :
printf("No\n");

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

/*Check if all bits can be made same by single

flip. Idea is to add the integer value all the

elements in the given string.

If the sum is 1 it indicates that there is

 only single '1' in the string.

If the sum is 0 it indicates that there is only

 single '0' in the string.

It takes O(n) time.*/

public class GFG {

 static boolean isOneFlip(String str)

 {

 int sum = 0;

 int n = str.length();

 // Traverse through given string and

 // count the total sum of numbers

 for (int i = 0; i < n; i++)

 sum += str.charAt(i) - '0';

 // Return true if any of the two counts

 // is 1

 return (sum == n - 1 || sum == 1);

 }

 // Main function

 public static void main(String args[])

 {

 System.out.println(isOneFlip("101111111111") ? "Yes" : "No");

 }

}

// This code is contributed by Sumit Ghosh  
  
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

# Check if all bits can be made same

# by single flip Idea is to add the

# integer value all the elements in

# the given string. If the sum is 1

# it indicates that there is only

# single '1' in the string. If the

# sum is 0 it indicates that there

# is only single '0' in the string.

# It takes O(n) time.

def isOneFlip(str):

 sum = 0

 n = len(str)

 # Traverse through given string

 # and count the total sum of

 # numbers

 for i in range( 0, n ):

 sum += int(str[i]) - int('0')

 # Return true if any of the two

 # counts is 1

 return (sum == n - 1 or sum == 1)

# Main function

(print("Yes") if isOneFlip("101111111111")

 else print("No"))

# This code is contributed by Smitha  
  
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

/*Check if all bits can be made same by single

 flip. Idea is to add the integer value all the

 elements in the given string.

 If the sum is 1 it indicates that there is

 only single '1' in the string.

 If the sum is 0 it indicates that there is only

 single '0' in the string.

 It takes O(n) time.*/

using System;

class GFG {

 

 static bool isOneFlip(string str)

 {

 int sum = 0;

 int n = str.Length;

 // Traverse through given string and

 // count the total sum of numbers

 for (int i = 0; i < n; i++)

 sum += str[i] - '0';

 // Return true if any of the two counts

 // is 1

 return (sum == n - 1 || sum == 1);

 }

 // Driver code

 public static void Main()

 {

 Console.WriteLine(isOneFlip("101111111111") ? "Yes" : "No");

 }

}

// This code is contributed by Sam007  
  
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

// Check if all bits can be made same by

// single flip Idea is to add the integer

// value all the elements in the given

// string. If the sum is 1 it indicates

// that there is only single '1' in the

// string. If the sum is 0 it indicates

// that there is only single '0' in the

// string. It takes O(n) time.

function isOneFlip($str)

{

 $sum = 0;

 $n = strlen($str);

 // Traverse through given string and

 // count the total sum of numbers

 for ( $i = 0; $i < $n; $i++)

 $sum += $str[$i] - '0';

 // Return true if any of the two counts

 // is 1

 return ($sum == $n - 1 || $sum == 1);

}

// Main function

 if(isOneFlip("101111111111") )

 echo "Yes\n";

 else

 echo "No\n";

// This code is contributed by aj_36

?>  
  
---  
  
 __

 __

## Javascript

 __

 __  
 __

 __

 __  
 __  
 __

<script>

/*Check if all bits can be made same by single

flip. Idea is to add the integer value all the

elements in the given string.

If the sum is 1 it indicates that there is

 only single '1' in the string.

If the sum is 0 it indicates that there is only

 single '0' in the string.

It takes O(n) time.*/

function isOneFlip(str)

{

 let sum = 0;

 let n = str.length;

 // Traverse through given string and

 // count the total sum of numbers

 for(let i = 0; i < n; i++)

 sum += str[i] - '0';

 // Return true if any of the two counts

 // is 1

 return (sum == n - 1 || sum == 1);

}

// Driver code

document.write(isOneFlip("101111111111") ?

 "Yes" : "No");

// This code is contributed by avanitrachhadiya2155

</script>  
  
---  
  
 __

 __

 **Output:**

    
    
    Yes

Thanks to **Sourabh Gavhale** for suggesting this solution

This article is contributed by **Subrata Ghosh**. If you like GeeksforGeeks
and would like to contribute, you can also write an article using
contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.  
Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


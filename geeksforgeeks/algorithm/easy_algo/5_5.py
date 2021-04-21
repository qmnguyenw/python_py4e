Find N % 4 (Remainder with 4) for a large value of N



Given a string **str** representing a large integer, the task is to find the
result of **N % 4**.  
 **Examples:**  

> **Input:** N = 81  
> **Output:** 1  
>  **Input:** N = 46234624362346435768440  
> **Output:** 0  
>

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:** The remainder of division by 4 is dependent on only the last 2
digits of a number, so instead of dividing N we divide only the last two
digits of N and find the remainder.  
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

// Function to return s % n

int findMod4(string s, int n)

{

 // To store the number formed by

 // the last two digits

 int k;

 // If it contains a single digit

 if (n == 1)

 k = s[0] - '0';

 // Take last 2 digits

 else

 k = (s[n - 2] - '0') * 10

 + s[n - 1] - '0';

 return (k % 4);

}

// Driver code

int main()

{

 string s = "81";

 int n = s.length();

 cout << findMod4(s, n);

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

 

// Function to return s % n

static int findMod4(String s, int n)

{

 // To store the number formed by

 // the last two digits

 int k;

 // If it contains a single digit

 if (n == 1)

 k = s.charAt(0) - '0';

 // Take last 2 digits

 else

 k = (s.charAt(n - 2) - '0') * 10

 + s.charAt(n - 1) - '0';

 return (k % 4);

}

// Driver code

public static void main(String[] args)

{

 String s = "81";

 int n = s.length();

 System.out.println(findMod4(s, n));

}

}

// This code is contributed by Code_Mech.  
  
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

# Python 3 implementation of the approach

# Function to return s % n

def findMod4(s, n):

 

 # To store the number formed by

 # the last two digits

 

 # If it contains a single digit

 if (n == 1):

 k = ord(s[0]) - ord('0')

 # Take last 2 digits

 else:

 k = ((ord(s[n - 2]) - ord('0')) * 10 +

 ord(s[n - 1]) - ord('0'))

 return (k % 4)

# Driver code

if __name__ == '__main__':

 s = "81"

 n = len(s)

 print(findMod4(s, n))

# This code is contributed by

# Surendra_Gangwar  
  
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

 

// Function to return s % n

static int findMod4(string s, int n)

{

 // To store the number formed by

 // the last two digits

 int k;

 // If it contains a single digit

 if (n == 1)

 k = s[0] - '0';

 // Take last 2 digits

 else

 k = (s[n - 2]- '0') * 10

 + s[n - 1] - '0';

 return (k % 4);

}

// Driver code

public static void Main()

{

 string s = "81";

 int n = s.Length;

 Console.WriteLine(findMod4(s, n));

}

}

// This code is contributed by Code_Mech.  
  
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

// Function to return s % n

function findMod4($s, $n)

{

 // To store the number formed by

 // the last two digits

 $k;

 // If it contains a single digit

 if ($n == 1)

 $k = $s[0] - '0';

 // Take last 2 digits

 else

 $k = ($s[$n - 2] - '0') * 10

 + $s[$n - 1] - '0';

 return ($k % 4);

}

// Driver code

{

 $s = "81";

 $n = strlen($s);

 echo(findMod4($s, $n));

}

// This code is contributed by Code_Mech.  
  
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

// Javascript implementation of the approach

// Function to return s % n

function findMod4(s, n)

{

 // To store the number formed by

 // the last two digits

 var k=0;

 // If it contains a single digit

 if (n == 1)

 k = s[0] - '0';

 // Take last 2 digits

 else

 k = (s[n - 2] - '0') * 10

 + s[n - 1] - '0';

 return (k % 4);

}

// Driver code

var s = "81";

var n = s.length;

document.write(findMod4(s, n));

// This code is contributed by nood2000.

</script>  
  
---  
  
 __

 __

 **Output:**

    
    
    1

**Time Complexity:** O(1)  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save


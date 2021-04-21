Minimum bit flips such that every K consecutive bits contain at least one set
bit



Given a binary string **S** , and an integer **K** , the task is to find the
minimum number of flips required such that every substring of length K
contains at least one **‘1’**.  
 **Examples:**  

> **Input:** S = “10000001” K = 2  
> **Output:** 3  
> **Explanation:**  
>  We need only 3 changes in string S ( at position 2, 4 and 6 ) so that the
> string contain at least one ‘1’ in every sub-string of length 2.  
>  **Input:** S = “000000” K = 3  
> **Output:** 2  
> **Explanation:**  
>  We need only 3 changes in string S ( at position 2 and 5 ) so that the
> string contain at least one ‘1’ in every sub-string of length 3.  
>  **Input:** S = “111010111” K = 2  
> **Output:** 0  
>

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Naive Approach:**  
To solve the problem, the simplest approach is to iterate for each substring
of length K and find the minimum number of flips required to satisfy the given
condition.  
_**Time complexity:** O(N * K)_  
 **Efficient Approach:**  
The idea is to use Sliding Window Approach.  

  * Set a window size of **K**.
  * Store the index of previous appearance of 1.
  * If the current bit is unset and the difference between the current **i th** bit and the **previous set bit** exceeds **K** , set the current bit and store the current index as that of the previous set bit and proceed further.

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

// Function to count min flips

int CountMinFlips(string s, int n,

 int k)

{

 // To store the count of minimum

 // flip required

 int cnt = 0;

 // To store the position of last '1'

 int prev = -1;

 for (int i = 0; i < k; i++) {

 // Track last position of '1'

 // in current window of size k

 if (s[i] == '1') {

 prev = i;

 }

 }

 // If no '1' is present in the current

 // window of size K

 if (prev == -1) {

 cnt++;

 // Set last index of window '1'

 s[k - 1] = '1';

 // Track previous '1'

 prev = k - 1;

 }

 // Traverse the given string

 for (int i = k; i < n; i++) {

 // If the current bit is not set,

 // then the condition for fliping

 // the current bit

 if (s[i] != '1') {

 if (prev <= (i - k)) {

 // Set i'th index to '1'

 s[i] = '1';

 // Track previous one

 prev = i;

 // Increment count

 cnt++;

 }

 }

 // Else update the prev set bit

 // position to current position

 else {

 prev = i;

 }

 }

 // Return the final count

 return (cnt);

}

// Driver Code

int main()

{

 // Given binary string

 string str = "10000001";

 // Size of given string str

 int n = str.size();

 // Window size

 int k = 2;

 // Function Call

 cout << CountMinFlips(str, n, k)

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

// Java program for the above approach

import java.util.*;

class GFG{

// Function to count min flips

static int CountMinFlips(char []s, int n,

 int k)

{

 

 // To store the count of minimum

 // flip required

 int cnt = 0;

 // To store the position of last '1'

 int prev = -1;

 for(int i = 0; i < k; i++)

 {

 

 // Track last position of '1'

 // in current window of size k

 if (s[i] == '1')

 {

 prev = i;

 }

 }

 // If no '1' is present in the current

 // window of size K

 if (prev == -1)

 {

 cnt++;

 // Set last index of window '1'

 s[k - 1] = '1';

 // Track previous '1'

 prev = k - 1;

 }

 // Traverse the given String

 for(int i = k; i < n; i++)

 {

 

 // If the current bit is not set,

 // then the condition for fliping

 // the current bit

 if (s[i] != '1')

 {

 if (prev <= (i - k))

 {

 

 // Set i'th index to '1'

 s[i] = '1';

 

 // Track previous one

 prev = i;

 

 // Increment count

 cnt++;

 }

 }

 

 // Else update the prev set bit

 // position to current position

 else

 {

 prev = i;

 }

 }

 

 // Return the final count

 return (cnt);

}

// Driver Code

public static void main(String[] args)

{

 // Given binary String

 String str = "10000001";

 // Size of given String str

 int n = str.length();

 // Window size

 int k = 2;

 // Function Call

 System.out.print(CountMinFlips(

 str.toCharArray(), n, k) + "\n");

}

}

// This code is contributed by Rohit_ranjan  
  
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

# Python3 code to count minimum no.

# of flips required such that

# every substring of length K

# contain at least one '1'.

# Function to count min flips

def CountMinFlips(s, n, k):

 cnt = 0

 prev = -1

 for i in range(0, k):

 # Track last position of '1'

 # in current window of size k

 if(s[i]=='1'):

 prev = i;

 

 # means no '1' is present

 if(prev == -1):

 cnt += 1

 # track previous '1'

 prev = k-1;

 

 

 for i in range(k, n):

 if(s[i] != '1'):

 if( prev <= (i-k) ):

 

 # track previous one

 prev = i;

 

 # increment count

 cnt += 1

 else:

 prev = i

 

 return(cnt);

# Driver code

s = "10000001"

n = len(s)

k = 2

print(CountMinFlips(s, n, k))  
  
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

class GFG{

// Function to count min flips

static int CountMinFlips(char []s, int n,

 int k)

{

 

 // To store the count of minimum

 // flip required

 int cnt = 0;

 // To store the position of last '1'

 int prev = -1;

 for(int i = 0; i < k; i++)

 {

 

 // Track last position of '1'

 // in current window of size k

 if (s[i] == '1')

 {

 prev = i;

 }

 }

 // If no '1' is present in the current

 // window of size K

 if (prev == -1)

 {

 cnt++;

 // Set last index of window '1'

 s[k - 1] = '1';

 // Track previous '1'

 prev = k - 1;

 }

 // Traverse the given String

 for(int i = k; i < n; i++)

 {

 

 // If the current bit is not set,

 // then the condition for fliping

 // the current bit

 if (s[i] != '1')

 {

 if (prev <= (i - k))

 {

 

 // Set i'th index to '1'

 s[i] = '1';

 

 // Track previous one

 prev = i;

 

 // Increment count

 cnt++;

 }

 }

 

 // Else update the prev set bit

 // position to current position

 else

 {

 prev = i;

 }

 }

 

 // Return the readonly count

 return (cnt);

}

// Driver Code

public static void Main(String[] args)

{

 // Given binary String

 String str = "10000001";

 // Size of given String str

 int n = str.Length;

 // Window size

 int k = 2;

 // Function Call

 Console.Write(CountMinFlips(

 str.ToCharArray(), n, k) + "\n");

}

}

// This code is contributed by sapnasingh4991  
  
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

// javascript program for the above approach

// Function to count min flips

function CountMinFlips(s , n,k)

{

 

 // To store the count of minimum

 // flip required

 var cnt = 0;

 // To store the position of last '1'

 var prev = -1;

 for(i = 0; i < k; i++)

 {

 

 // Track last position of '1'

 // in current window of size k

 if (s[i] == '1')

 {

 prev = i;

 }

 }

 // If no '1' is present in the current

 // window of size K

 if (prev == -1)

 {

 cnt++;

 // Set last index of window '1'

 s[k - 1] = '1';

 // Track previous '1'

 prev = k - 1;

 }

 // Traverse the given String

 for(i = k; i < n; i++)

 {

 

 // If the current bit is not set,

 // then the condition for fliping

 // the current bit

 if (s[i] != '1')

 {

 if (prev <= (i - k))

 {

 

 // Set i'th index to '1'

 s[i] = '1';

 

 // Track previous one

 prev = i;

 

 // Increment count

 cnt++;

 }

 }

 

 // Else update the prev set bit

 // position to current position

 else

 {

 prev = i;

 }

 }

 

 // Return the final count

 return (cnt);

}

// Driver Code

 // Given binary String

 var str = "10000001";

 // Size of given String str

 var n = str.length;

 // Window size

 var k = 2;

 // Function Call

 document.write(CountMinFlips(

 str, n, k) );

// This code contributed by shikhasingrajput

</script>  
  
---  
  
 __

 __

 **Output:**

    
    
    3

**Time complexity:** _O(N + K)_  
**Auxiliary Space:** _O(1)_  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


Find the number of Chicks in a Zoo at Nth day



Given that a zoo has a single chick. A chick gives birth to 2 chicks everyday
and the life expectancy of a chick is 6 days. The task is to find the number
of chicks on the **N th** day.

 **Examples:**

>  **Input:** N = 3  
>  **Output:** 9  
> First day: 1 chick  
> Second day: 1 + 2 = 3  
> Third day: 3 + 6 = 9
>
>  **Input:** N = 12  
>  **Output:** 173988

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Simple approach:** It is given that the life expectancy of a chick is 6
days, so no chick dies till the sixth day. Every day population of current day
will be 3 time of previous day. One more thing is to note that the chick born
on ith day is not counted on that day, it will be counted in the next day and
the changes begin from seventh day. So main calculation starts from seventh
day onwards.

  

  

 **On Seventh Day:** Chicks from the 1st day die so based on manual
calculation it will be 726.  
 **On Eigth Day:** Two new born chicks born on (8-6)th i.e 2nd day dies. This
will affect the current population by 2/3. This population needs to be get
deducted from the previous day population because today i.e 8th day more
newborns will we born so we cannot deduct directly from today’s population.
This will then be multiplied by three times because of newborns born on that
day.

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

#define ll long long int

 

// Function to return the number

// of chicks on the nth day

ll getChicks(int n)

{

 

 // Size of dp[] has to be

 // at least 6 (1-based indexing)

 int size = max(n, 7);

 ll dp[size];

 

 dp[0] = 0;

 dp[1] = 1;

 

 // Every day current population

 // will be three times of the previous day

 for (int i = 2; i <= 6; i++) {

 dp[i] = dp[i - 1] * 3;

 }

 

 // Manually calculated value

 dp[7] = 726;

 

 // From 8th day onwards

 for (int i = 8; i <= n; i++) {

 

 // Chick population decreases by 2/3 everyday.

 // For 8th day on [i-6] i.e 2nd day population

 // was 3 and so 2 new born die on the 6th day

 // and so on for the upcoming days

 dp[i] = (dp[i - 1] - (2 * dp[i - 6] / 3)) * 3;

 }

 

 return dp[n];

}

 

// Driver code

int main()

{

 int n = 3;

 

 cout << getChicks(n);

 

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

 

import java.util.*;

 

public class GFG {

 

 

// Function to return the number

// of chicks on the nth day

static long getChicks(int n)

{

 

 // Size of dp[] has to be

 // at least 6 (1-based indexing)

 int size = Math.max(n, 7);

 long []dp = new long[size];

 

 dp[0] = 0;

 dp[1] = 1;

 

 // Every day current population

 // will be three times of the previous day

 for (int i = 2; i < 6; i++) {

 dp[i] = dp[i - 1] * 3;

 }

 

 // Manually calculated value

 dp[6] = 726;

 

 // From 8th day onwards

 for (int i = 8; i <= n; i++) {

 

 // Chick population decreases by 2/3 everyday.

 // For 8th day on [i-6] i.e 2nd day population

 // was 3 and so 2 new born die on the 6th day

 // and so on for the upcoming days

 dp[i] = (dp[i - 1] - (2 * dp[i - 6] / 3)) * 3;

 }

 

 return dp[n];

}

 

// Driver code

public static void main(String[] args) {

int n = 3;

 

 System.out.println(getChicks(n));

 }

}

// This code has been contributed by 29AjayKumar  
  
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



# Python implementation of the approach

 

# Function to return the number

# of chicks on the nth day

def getChicks(n):

 

 # Size of dp[] has to be

 # at least 6 (1-based indexing)

 size = max(n, 7);

 dp = [0]*size;

 

 dp[0] = 0;

 dp[1] = 1;

 

 # Every day current population

 # will be three times of the previous day

 for i in range(2,7):

 dp[i] = dp[i - 1] * 3;

 

 # Manually calculated value

 dp[6] = 726;

 

 # From 8th day onwards

 for i in range(8,n+1):

 

 # Chick population decreases by 2/3 everyday.

 # For 8th day on [i-6] i.e 2nd day population

 # was 3 and so 2 new born die on the 6th day

 # and so on for the upcoming days

 dp[i] = (dp[i - 1] - (2 * dp[i - 6] //
3)) * 3;

 

 return dp[n];

 

# Driver code

n = 3;

 

print(getChicks(n));

 

# This code is contributed by Princi Singh  
  
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

 

// Function to return the number

// of chicks on the nth day

static long getChicks(int n)

{

 

 // Size of dp[] has to be

 // at least 6 (1-based indexing)

 int size = Math.Max(n, 7);

 long []dp = new long[size];

 

 dp[0] = 0;

 dp[1] = 1;

 

 // Every day current population

 // will be three times of the previous day

 for (int i = 2; i < 6; i++) 

 {

 dp[i] = dp[i - 1] * 3;

 }

 

 // Manually calculated value

 dp[6] = 726;

 

 // From 8th day onwards

 for (int i = 8; i <= n; i++) 

 {

 

 // Chick population decreases by 2/3 everyday.

 // For 8th day on [i-6] i.e 2nd day population

 // was 3 and so 2 new born die on the 6th day

 // and so on for the upcoming days

 dp[i] = (dp[i - 1] - (2 * dp[i - 6] / 3)) * 3;

 }

 

 return dp[n];

}

 

// Driver code

static public void Main ()

{

 

 int n = 3;

 Console.WriteLine(getChicks(n));

}

}

 

// This code has been contributed by @Tushil..  
  
---  
  
 __

 __

 **Output:**

    
    
    9
    

**Efficient approach:** If you look closely, you can observe a pattern that is
number of chicks for Nth day in the zoo can be calculated directly using the
formula **pow(3, N – 1)**.

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

#define ll long long int

 

// Function to return the number

// of chicks on the nth day

ll getChicks(int n)

{

 

 ll chicks = (ll)pow(3, n - 1);

 

 return chicks;

}

 

// Driver code

int main()

{

 int n = 3;

 

 cout << getChicks(n);

 

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

import java.io.*;

 

class GFG 

{

 

// Function to return the number

// of chicks on the nth day

static int getChicks(int n)

{

 

 int chicks = (int)Math.pow(3, n - 1);

 

 return chicks;

}

 

// Driver code

public static void main (String[] args) 

{

 

 int n = 3;

 System.out.println (getChicks(n));

}

}

 

// This code is contributed by Tushil.  
  
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

 

# Function to return the number

# of chicks on the nth day

def getChicks( n):

 

 chicks = pow(3, n - 1)

 

 return chicks

 

# Driver code

if __name__ == "__main__":

 n = 3

 

 print ( getChicks(n))

 

# This code is contributed by ChitraNayal  
  
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

 

 // Function to return the number 

 // of chicks on the nth day 

 static int getChicks(int n) 

 { 

 

 int chicks = (int)Math.Pow(3, n - 1); 

 

 return chicks; 

 } 

 

 // Driver code 

 public static void Main() 

 { 

 

 int n = 3; 

 Console.WriteLine(getChicks(n)); 

 } 

} 

 

// This code is contributed by AnkitRai01  
  
---  
  
 __

 __

 **Output:**

    
    
    9
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


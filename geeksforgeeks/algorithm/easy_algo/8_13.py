Minimum number of equal amount bags to collect at least M money



Given unlimited number of coins of two denomination **X** and **Y**. Also
given bags with capacity of **N** rupees, independent of number of coins. The
task is to find the minimum number of bags such that each bag contains the
same amount of rupees and sum of all the bags amount is at least **M**.  
 **Examples :**  

    
    
    **Input :** M = 27, N = 12, X = 2, Y = 5. 
    **Output :** 3
    We put 2 coins of X, 1 coin of Y in each bag. 
    So we have 9 rupees in each bag and we need 
    at least 3 bags (Note that 27/9 = 3). There 
    is no way to obtain sum with lesser number
    of bags.
    
    **Input :** M = 45, N = 9, X = 4, Y = 5. 
    **Output :** 5

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

The task is to minimize the number of bags, thus need to maximize the amount
in a bag such that amount in all bags is same. Suppose we take, ‘p’ number of
X coins and ‘q’ number of Y coins, then the task is to maximize p*X + q*Y. And
also, p*X + q*Y <= N.  
Now, to find the maximum possible value of Left Hand Side of the equation,
vary p from 0 to N/X, then find the maximum possible q for the particular p.
Then, out of all such pairs, take the (p, q) pair which gives maximum value of
p*X + q*Y.  
Below is the implementation of above idea :  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to find minimum number of bags such

// that each bag contains same amount and sum is at

// least M.

#include<bits/stdc++.h>

using namespace std;

// Return minimum number of bags required.

int minBags(int M, int N, int X, int Y)

{

 // Initialize maximum amount in a bag

 int maxAmount = 0;

 // Finding maximum possible q for the particular p.

 for (int p = 0; p <= N/X; p++)

 {

 int q = (N - p * X) / Y;

 maxAmount = max(maxAmount, p*X + q*Y);

 }

 // Calculating the minimum number of bags.

 int result = M/maxAmount;

 result += (M % maxAmount == 0? 0: 1);

 return result;

}

// Driven Program

int main()

{

 int M = 45, N = 9;

 int X = 4, Y = 5;

 cout << minBags(M, N, X, Y) << endl;

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

// Java program to find minimum number

// of bags such that each bag contains

// same amount and sum is at least M

import java.io.*;

public class GFG {

 

// Return minimum number of bags required.

static int minBags(int M, int N,

 int X, int Y)

{

 

 // Initialize maximum amount in a bag

 int maxAmount = 0;

 // Finding maximum possible q

 // for the particular p.

 for (int p = 0; p <= N / X; p++)

 {

 int q = (N - p * X) / Y;

 maxAmount = Math.max(maxAmount, p * X +

 q * Y);

 }

 // Calculating the minimum number of bags.

 int result = M / maxAmount;

 result += (M % maxAmount == 0? 0: 1);

 return result;

}

 // Driver Code

 static public void main (String[] args)

 {

 int M = 45, N = 9;

 int X = 4, Y = 5;

 System.out.println(minBags(M, N, X, Y));

 }

}

// This code is contributed by vt_m.  
  
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

# Python 3 program to find minimum number

# of bags such that each bag contains same

# amount and sum is at least M.

# Return minimum number of bags required.

def minBags(M, N, X, Y):

 

 # Initialize maximum amount in a bag

 maxAmount = 0

 # Finding maximum possible q for

 # the particular p.

 for p in range(0, int(N / X) + 1, 1):

 q = int((N - p * X) / Y)

 maxAmount = max(maxAmount, p * X + q * Y)

 # Calculating the minimum number of bags.

 result = int(M / maxAmount)

 if(M % maxAmount == 0):

 result += 0

 else:

 result += 1

 return result

# Driver Code

if __name__ == '__main__':

 M = 45

 N = 9

 X = 4

 Y = 5

 print(minBags(M, N, X, Y))

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

// C# program to find minimum number of

// bags such that each bag contains same

// amount and sum is at least M.

using System;

public class GFG

{

 

// Return minimum number of bags required.

static int minBags(int M, int N,

 int X, int Y)

{

 

 // Initialize maximum amount in a bag

 int maxAmount = 0;

 // Finding maximum possible q

 // for the particular p.

 for (int p = 0; p <= N / X; p++)

 {

 int q = (N - p * X) / Y;

 maxAmount = Math.Max(maxAmount, p * X +

 q * Y);

 }

 // Calculating the minimum number of bags.

 int result = M / maxAmount;

 result += (M % maxAmount == 0? 0: 1);

 return result;

}

 // Driver Code

 static public void Main ()

 {

 int M = 45, N = 9;

 int X = 4, Y = 5;

 Console.WriteLine(minBags(M, N, X, Y));

 }

}

// This code is contributed by vt_m.  
  
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

// PHP program to find minimum

// number of bags such that each

// bag contains same amount and

// sum is at least M.

// Return minimum number

// of bags required.

function minBags($M, $N, $X, $Y)

{

 // Initialize maximum

 // amount in a bag

 $maxAmount = 0;

 // Finding maximum possible

 // q for the particular p.

 for ($p = 0; $p <= $N / $X; $p++)

 {

 $q = ($N - $p * $X) / $Y;

 $maxAmount = max($maxAmount,

 $p * $X + $q * $Y);

 }

 // Calculating the minimum

 // number of bags.

 $result = $M / $maxAmount;

 $result += ($M % $maxAmount == 0? 0: 1);

 return $result;

}

// Driver Code

$M = 45; $N = 9;

$X = 4 ; $Y = 5;

echo minBags($M, $N, $X, $Y) ;

// This code is contributed by nitin mittal.

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

// Javascript program to find minimum number

// of bags such that each bag contains

// same amount and sum is at least M

// Return minimum number of bags required.

function minBags(M, N, X, Y)

{

 

 // Initialize maximum amount in a bag

 let maxAmount = 0;

 

 // Finding maximum possible q

 // for the particular p.

 for (let p = 0; p <= N / X; p++)

 {

 let q = (N - p * X) / Y;

 

 maxAmount = Math.max(maxAmount, p * X +

 q * Y);

 }

 

 // Calculating the minimum number of bags.

 let result = M / maxAmount;

 result += (M % maxAmount == 0? 0: 1);

 

 return result;

}

 

// Driver code 

 let M = 45, N = 9;

 let X = 4, Y = 5;

 

 document.write(minBags(M, N, X, Y));

 

 // This code is contributed by susmitakundugoaldanga.

</script>  
  
---  
  
 __

 __

 **Output :**  

    
    
    5

 **Time Complexity :** O(N/X)  
This article is contributed by **Anuj Chauhan**. If you like GeeksforGeeks and
would like to contribute, you can also write an article using
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


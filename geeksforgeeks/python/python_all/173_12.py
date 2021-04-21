Maximum litres of water that can be bought with N Rupees



Given ![N](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-8cff99e18eacd6e6c40f76db5b6f580a_l3.png) Rupees. A liter
**plastic bottle** of water costs ![A](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-e63249dbcb7bc1df2ae6aa725a10a1ad_l3.png)
Rupees and a litre of **glass bottle** of water costs
![B](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-e87b11a274ac203c994e721bfef1cc87_l3.png) Rupees. But the
empty glass bottle after buying can be exchanged for
![C](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-0b25da2171dcfd1283c429cf446b3e4b_l3.png) Rupees. Find the
maximum liters of water which can be bought with
![N](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-8cff99e18eacd6e6c40f76db5b6f580a_l3.png) Rupees.

 **Examples:**

>  **Input:** N = 10 , A = 11 , B = 9 , C = 8  
>  **Output:** 2  
> One glass bottle can be bought and then can be returned to buy one more
> glass bottle
>
>  **Input:** N = 15 , A = 6 , B = 4 , C = 3  
>  **Output:** 12

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** If we have at least ![b](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-84c9ca09709086867a3040914718f2bb_l3.png) money
then cost of one glass bottle is **b – c**. This means that if **a ≤ (b – c)**
then we don’t need to buy glass bottles, only plastic ones, and the answer
will be **floor(n / a)**. Otherwise we need to buy glass bottles while we can.  
So, if we have at least ![b](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-84c9ca09709086867a3040914718f2bb_l3.png) money, then we
will buy **floor((n – c) / (b – c))** glass bottles and then spend rest of the
money on plastic ones.

  

  

Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// CPP implementation of the above approach

#include<bits/stdc++.h>

using namespace std;

 

 

void maxLitres(int budget,int plastic,int glass,int
refund)

{

 

 // if buying glass bottles is profitable

 if (glass - refund < plastic)

 {

 // Glass bottles that can be bought

 int ans = max((budget - refund) / (glass - refund), 0);

 

 // Change budget according the bought bottles

 budget -= ans * (glass - refund);

 

 // Plastic bottles that can be bought

 ans += budget / plastic;

 cout<<ans<<endl;

 }

 

 // if only plastic bottles need to be bought

 else

 cout<<(budget / plastic)<<endl;

}

 

 

 

// Driver Code

int main()

{

 int budget = 10, plastic=11, glass=9, refund = 8;

 maxLitres(budget, plastic, glass, refund);

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

// Java implementation of the above approach

class GFG 

{

 

 static void maxLitres(int budget, int plastic, 

 int glass, int refund)

 {

 

 // if buying glass bottles is profitable 

 if (glass - refund < plastic)

 {

 

 // Glass bottles that can be bought 

 int ans = Math.max((budget - refund) / (glass - refund), 0);

 

 // Change budget according the bought bottles 

 budget -= ans * (glass - refund);

 

 // Plastic bottles that can be bought 

 ans += budget / plastic;

 System.out.println(ans);

 } 

 

 // if only plastic bottles need to be bought 

 else

 {

 System.out.println((budget / plastic));

 }

 

 }

 

 // Driver Code 

 public static void main(String[] args) 

 {

 int budget = 10, plastic = 11, glass = 9, refund = 8;

 maxLitres(budget, plastic, glass, refund);

 }

}

 

/* This code contributed by PrinciRaj1992 */  
  
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

# Python3 implementation of the above approach

 

def maxLitres(budget, plastic, glass, refund):

 

 # if buying glass bottles is profitable

 if glass - refund < plastic:

 

 # Glass bottles that can be bought

 ans = max((budget - refund) // (glass - refund),
0)

 

 # Change budget according the bought bottles

 budget -= ans * (glass - refund)

 

 # Plastic bottles that can be bought

 ans += budget // plastic

 print(ans)

 

 # if only plastic bottles need to be bought

 else:

 print(budget // plastic)

 

# Driver Code

budget, plastic, glass, refund = 10, 11, 9, 8

maxLitres(budget, plastic, glass, refund)  
  
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

// C# implementation of the above approach

using System; 

 

class GFG 

{

 

 static void maxLitres(int budget, int plastic, 

 int glass, int refund)

 {

 

 // if buying glass bottles is profitable 

 if (glass - refund < plastic)

 {

 

 // Glass bottles that can be bought 

 int ans = Math.Max((budget - refund) / (glass - refund), 0);

 

 // Change budget according the bought bottles 

 budget -= ans * (glass - refund);

 

 // Plastic bottles that can be bought 

 ans += budget / plastic;

 Console.WriteLine(ans);

 } 

 

 // if only plastic bottles need to be bought 

 else

 {

 Console.WriteLine((budget / plastic));

 }

 

 }

 

 // Driver Code 

 public static void Main(String[] args) 

 {

 int budget = 10, plastic = 11, glass = 9, refund = 8;

 maxLitres(budget, plastic, glass, refund);

 }

}

 

// This code contributed by Rajput-Ji  
  
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

// PHP implementation of the above approach

 

function maxLitres($budget, $plastic, 

 $glass, $refund)

{

 

 // if buying glass bottles is profitable

 if ($glass - $refund < $plastic)

 {

 // Glass bottles that can be bought

 $ans = max((int)($budget - $refund) / 

 ($glass - $refund), 0);

 

 // Change budget according the bought bottles

 $budget -= $ans * ($glass - $refund);

 

 // Plastic bottles that can be bought

 $ans += (int)($budget / $plastic);

 echo $ans . "\n";

 }

 

 // if only plastic bottles need to be bought

 else

 echo (int)($budget / $plastic) . "\n";

}

 

// Driver Code

$budget = 10;

$plastic = 11;

$glass = 9;

$refund = 8;

maxLitres($budget, $plastic, 

 $glass, $refund);

 

// This code is contributed by mits

?>  
  
---  
  
 __

 __

 **Output:**

    
    
    2
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save


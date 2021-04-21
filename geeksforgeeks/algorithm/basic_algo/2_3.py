Count squares with odd side length in Chessboard



Given a **N * N** chessboard, the task is to count the number of squares
having the odd side length.

 **Example:**

>  **Input:** N = 3  
>  **Output:** 10  
> 9 squares are possible whose sides are 1  
> and a single square with side = 3  
> 9 + 1 = 10
>
>  **Input:** N = 8  
>  **Output:** 120

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** For all odd numbers from **1** to **N** and then calculate the
number of squares that can be formed having that odd side. For the **i th**
side, the count of squares is equal to **(N – i + 1) 2**. Further add all such
count of squares.

  

  

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

 

// Function to return the count

// of odd length squares possible

int count_square(int n)

{

 

 // To store the required count

 int count = 0;

 

 // For all odd values of i

 for (int i = 1; i <= n; i = i + 2) {

 

 // Add the count of possible

 // squares of length i

 int k = n - i + 1;

 count += (k * k);

 }

 

 // Return the required count

 return count;

}

 

// Driver code

int main()

{

 int N = 8;

 

 cout << count_square(N);

 

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

class GFG {

 

 // Function to return the count

 // of odd length squares possible

 static int count_square(int n)

 {

 

 // To store the required count

 int count = 0;

 

 // For all odd values of i

 for (int i = 1; i <= n; i = i + 2) {

 

 // Add the count of possible

 // squares of length i

 int k = n - i + 1;

 count += (k * k);

 }

 

 // Return the required count

 return count;

 }

 

 // Driver code

 public static void main(String[] args)

 {

 int N = 8;

 

 System.out.println(count_square(N));

 }

}

 

// This code is contributed by Rajput-Ji  
  
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

 

# Function to return the count

# of odd length squares possible

def count_square(n):

 

 # To store the required count

 count = 0;

 

 # For all odd values of i

 for i in range(1, n + 1, 2):

 

 # Add the count of possible

 # squares of length i

 k = n - i + 1;

 count += (k * k);

 

 # Return the required count

 return count;

 

# Driver code

N = 8;

print(count_square(N));

 

# This code has been contributed by 29AjayKumar  
  
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

 

class GFG {

 

 // Function to return the count

 // of odd length squares possible

 static int count_square(int n)

 {

 

 // To store the required count

 int count = 0;

 

 // For all odd values of i

 for (int i = 1; i <= n; i = i + 2) {

 

 // Add the count of possible

 // squares of length i

 int k = n - i + 1;

 count += (k * k);

 }

 

 // Return the required count

 return count;

 }

 

 // Driver code

 public static void Main()

 {

 int N = 8;

 

 Console.WriteLine(count_square(N));

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

 

// Function to return the count 

// of odd length squares possible 

function count_square($n) 

{ 

 

 // To store the required count 

 $count = 0; 

 

 // For all odd values of i 

 for ($i = 1; $i <= $n; $i = $i + 2)

 { 

 

 // Add the count of possible 

 // squares of length i 

 $k =$n - $i + 1; 

 $count += ($k * $k); 

 } 

 

 // Return the required count 

 return $count; 

} 

 

// Driver code 

$N = 8; 

 

echo count_square($N); 

 

// This code is contributed by AnkitRai01

?>  
  
---  
  
 __

 __

 **Output:**

    
    
    120
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


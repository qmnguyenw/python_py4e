Count Fibonacci numbers in given range in O(Log n) time and O(1) space



Given a range, count Fibonacci numbers in given range. First few Fibonacci
numbers are 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 141, ..  
**Example :**

    
    
    Input: low = 10, high = 100
    Output: 5
    There are five Fibonacci numbers in given
    range, the numbers are 13, 21, 34, 55 and 89.
    
    Input: low = 10, high = 20
    Output: 1
    There is only one Fibonacci Number, 13.
    
    Input: low = 0, high = 1
    Output: 3
    Fibonacci numbers are 0, 1 and 1

 **We strongly recommend you to minimize your browser and try this yourself
first.**  
A **Brute Force Solution** is to one by one find all Fibonacci Numbers and
count all Fibonacci numbers in given range  
An **Efficient Solution** is to use previous Fibonacci Number to generate next
using simple Fibonacci formula that fn = fn-1 \+ fn-2.  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to count Fibonacci numbers in given range

#include <bits/stdc++.h>

using namespace std;

// Returns count of fibonacci numbers in [low, high]

int countFibs(int low, int high)

{

 // Initialize first three Fibonacci Numbers

 int f1 = 0, f2 = 1, f3 = 1;

 // Count fibonacci numbers in given range

 int result = 0;

 while (f1 <= high)

 {

 if (f1 >= low)

 result++;

 f1 = f2;

 f2 = f3;

 f3 = f1 + f2;

 }

 return result;

}

// Driver program

int main()

{

int low = 10, high = 100;

cout << "Count of Fibonacci Numbers is "

 << countFibs(low, high);

return 0;

}  
  
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

# Python3 program to count Fibonacci

# numbers in given range

# Returns count of fibonacci

# numbers in [low, high]

def countFibs(low, high):

 

 # Initialize first three

 # Fibonacci Numbers

 f1, f2, f3 = 0, 1, 1

 # Count fibonacci numbers in

 # given range

 result = 0

 while (f1 <= high):

 if (f1 >= low):

 result += 1

 f1 = f2

 f2 = f3

 f3 = f1 + f2

 return result

# Driver Code

low, high = 10, 100

print("Count of Fibonacci Numbers is",

 countFibs(low, high))

# This code is contributed

# by mohit kumar  
  
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

// C# program to count Fibonacci

// numbers in given range

using System;

public class GFG

{

 

 // Returns count of fibonacci

 // numbers in [low, high]

 static int countFibs(int low,

 int high)

 {

 

 // Initialize first three

 // Fibonacci Numbers

 int f1 = 0, f2 = 1, f3 = 1;

 

 // Count fibonacci numbers

 // in given range

 int result = 0;

 

 while (f1 <= high)

 {

 if (f1 >= low)

 result++;

 f1 = f2;

 f2 = f3;

 f3 = f1 + f2;

 }

 

 return result;

 }

 

 // Driver Code

 public static void Main(String []args)

 {

 int low = 10, high = 100;

 Console.WriteLine("Count of Fibonacci Numbers is "

 + countFibs(low, high));

 }

}

 

// This code is contributed by Sam007.  
  
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

// PHP program to count

// Fibonacci numbers in

// given range

// Returns count of fibonacci

// numbers in [low, high]

function countFibs($low, $high)

{

 // Initialize first

 // three Fibonacci Numbers

 $f1 = 0; $f2 = 1; $f3 = 1;

 // Count fibonacci

 // numbers in given range

 $result = 0;

 while ($f1 <= $high)

 {

 if ($f1 >= $low)

 $result++;

 $f1 = $f2;

 $f2 = $f3;

 $f3 = $f1 + $f2;

 }

 return $result;

}

// Driver Code

$low = 10; $high = 100;

echo "Count of Fibonacci Numbers is ",

 countFibs($low, $high);

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

// JavaScript program to count Fibonacci

// numbers in given range

 // Returns count of fibonacci

 // numbers in [low, high]

 function countFibs(low, high)

 {

 

 // Initialize first three

 // Fibonacci Numbers

 let f1 = 0, f2 = 1, f3 = 1;

 

 // Count fibonacci numbers

 // in given range

 let result = 0;

 

 while (f1 <= high)

 {

 if (f1 >= low)

 result++;

 f1 = f2;

 f2 = f3;

 f3 = f1 + f2;

 }

 

 return result;

 }

// Driver program

 let low = 10, high = 100;

 document.write("Count of Fibonacci Numbers is "

 + countFibs(low, high));

// This code is contributed by susmitakundugoaldanga.

</script>  
  
---  
  
 __

 __

 **Output :**

    
    
    Count of Fibonacci Numbers is 5

 **Time Complexity Analysis:**  
Consider the that Fibonacci Numbers can be written as below  
![fib\(n\)=\\left \[ \\frac {1}{\\sqrt{5}}\\left \( \\frac {1+\\sqrt{5}}{2}
\\right \)^n \\right \]\\sim c*1.62^n  ](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-671d93ffe86555059d11ba59480b8176_l3.png)  
![for n\\sim c*1.62^n we make
O\(n'\)comparisons,we,thus,needO\(log\(n\)\)comparisons.
](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-43c96652b8dd7f8304a226225fdf3875_l3.png)  
So the value of Fibonacci numbers grow exponentially. It means that the while
loop grows exponentially till it reaches ‘high’. So the loop runs **O(Log
(high))** times.  
One solution could be directly use above formula to find count of Fibonacci
Numbers, but that is not practically feasible (See this for details).  
 **Auxiliary Space:** O(1)  
This article is contributed by **Sudhanshu Gupta**. Please write comments if
you find anything incorrect, or you want to share more information about the
topic discussed above  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save


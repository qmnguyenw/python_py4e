Fifth root of a number



Given a number, print floor of 5’th root of the number.  
 **Examples:**  

    
    
    Input  : n = 32
    Output : 2
    2 raise to power 5 is 32
    
    Input  : n = 250
    Output : 3
    Fifth square root of 250 is between 3 and 4
    So floor value is 3.

 **Method 1 (Simple)**  
A simple solution is initialize result as 0, keep incrementing result while
result5 is smaller than or equal to n. Finally return result – 1.  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// A C++ program to find floor of 5th root

#include<bits/stdc++.h>

using namespace std;

// Returns floor of 5th root of n

int floorRoot5(int n)

{

 // Base cases

 if (n == 0 || n == 1)

 return n;

 // Initialize result

 int res = 0;

 // Keep incrementing res while res^5 is

 // smaller than or equal to n

 while (res*res*res*res*res <= n)

 res++;

 // Return floor of 5'th root

 return res-1;

}

// Driver program

int main()

{

 int n = 250;

 cout << "Floor of 5'th root is "

 << floorRoot5(n);

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

// Java program to find floor of 5th root

class GFG {

 

// Returns floor of 5th root of n

static int floorRoot5(int n)

{

 

 // Base cases

 if (n == 0 || n == 1)

 return n;

 // Initialize result

 int res = 0;

 // Keep incrementing res while res^5

 // is smaller than or equal to n

 while (res * res * res * res * res <= n)

 res++;

 // Return floor of 5'th root

 return res-1;

}

 // Driver Code

 public static void main(String []args)

 {

 int n = 250;

 System.out.println("Floor of 5'th root is "

 + floorRoot5(n));

 }

}

// This code is contributed by Anshul Aggarwal.  
  
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

# A Python3 program to find the floor

# of the 5th root

# Returns floor of 5th root of n

def floorRoot5(n):

 # Base cases

 if n == 0 and n == 1:

 return n

 # Initialize result

 res = 0

 # Keep incrementing res while res^5

 # is smaller than or equal to n

 while res * res * res * res * res <= n:

 res += 1

 # Return floor of 5'th root

 return res-1

# Driver Code

if __name__ == "__main__":

 n = 250

 print("Floor of 5'th root is",

 floorRoot5(n))

# This code is contributed by Rituraj Jain  
  
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

// C# program to find floor of 5th root

using System;

class GFG {

 

// Returns floor of 5th root of n

static int floorRoot5(int n)

{

 

 // Base cases

 if (n == 0 || n == 1)

 return n;

 // Initialize result

 int res = 0;

 // Keep incrementing res while res^5

 // is smaller than or equal to n

 while (res * res * res * res * res <= n)

 res++;

 // Return floor of 5'th root

 return res-1;

}

 // Driver Code

 public static void Main()

 {

 int n = 250;

 Console.Write("Floor of 5'th root is "

 + floorRoot5(n));

 }

}

// This code is contributed by Sumit Sudhakar.  
  
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

// PHP program to find

// floor of 5th root

// Returns floor of

// 5th root of n

function floorRoot5($n)

{

 

 // Base cases

 if ($n == 0 || $n == 1)

 return $n;

 // Initialize result

 $res = 0;

 // Keep incrementing res while

 // res^5 is smaller than or

 // equal to n

 while ($res * $res * $res *

 $res * $res <= $n)

 $res++;

 // Return floor

 // of 5'th root

 return $res - 1;

}

 // Driver Code

 $n = 250;

 echo "Floor of 5'th root is "

 , floorRoot5($n);

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

// JavaScript program to find floor of 5th root

// Returns floor of 5th root of n

function floorRoot5(n)

{

 

 // Base cases

 if (n == 0 || n == 1)

 return n;

 

 // Initialize result

 let res = 0;

 

 // Keep incrementing res while res^5

 // is smaller than or equal to n

 while (res * res * res * res * res <= n)

 res++;

 

 // Return floor of 5'th root

 return res-1;

}

// Driver Code

 let n = 250;

 document.write("Floor of 5'th root is "

 + floorRoot5(n));

</script>  
  
---  
  
 __

 __

 **Output:**

    
    
    Floor of 5'th root is 3

Time complexity of above solution is **O(n 1/5)**. We can do better. See below
solution.  
**Method 2 (Binary Search)**  
The idea is to do Binary Search. We start from n/2 and if its 5’th power is
more than n, we recur for interval from n/2+1 to n. Else if power is less, we
recur for interval 0 to n/2-1  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// A C++ program to find floor of 5'th root

#include<bits/stdc++.h>

using namespace std;

// Returns floor of 5'th root of n

int floorRoot5(int n)

{

 // Base cases

 if (n == 0 || n == 1)

 return n;

 // Do Binary Search for floor of 5th square root

 int low = 1, high = n, ans = 0;

 while (low <= high)

 {

 // Find the middle point and its power 5

 int mid = (low + high) / 2;

 long int mid5 = mid*mid*mid*mid*mid;

 // If mid is the required root

 if (mid5 == n)

 return mid;

 // Since we need floor, we update answer when

 // mid5 is smaller than n, and move closer to

 // 5'th root

 if (mid5 < n)

 {

 low = mid + 1;

 ans = mid;

 }

 else // If mid^5 is greater than n

 high = mid - 1;

 }

 return ans;

}

// Driver program

int main()

{

 int n = 250;

 cout << "Floor of 5'th root is "

 << floorRoot5(n);

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

// A Java program to find

// floor of 5'th root

class GFG {

 

 // Returns floor of 5'th

 // root of n

 static int floorRoot5(int n)

 {

 

 // Base cases

 if (n == 0 || n == 1)

 return n;

 

 // Do Binary Search for

 // floor of 5th square root

 int low = 1, high = n, ans = 0;

 while (low <= high)

 {

 

 // Find the middle point

 // and its power 5

 int mid = (low + high) / 2;

 long mid5 = mid * mid * mid *

 mid * mid;

 

 // If mid is the required root

 if (mid5 == n)

 return mid;

 

 // Since we need floor,

 // we update answer when

 // mid5 is smaller than n,

 // and move closer to

 // 5'th root

 if (mid5 < n)

 {

 low = mid + 1;

 ans = mid;

 }

 

 // If mid^5 is greater

 // than n

 else

 high = mid - 1;

 }

 return ans;

 }

 

 // Driver Code

 public static void main(String []args)

 {

 int n = 250;

 System.out.println("Floor of 5'th root is " +

 floorRoot5(n));

 }

}

// This code is contributed by Anshul Aggarwal.  
  
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

# A Python3 program to find the floor

# of 5'th root

# Returns floor of 5'th root of n

def floorRoot5(n):

 # Base cases

 if n == 0 or n == 1:

 return n

 # Do Binary Search for floor of

 # 5th square root

 low, high, ans = 1, n, 0

 while low <= high:

 

 # Find the middle point and its power 5

 mid = (low + high) // 2

 mid5 = mid * mid * mid * mid * mid

 # If mid is the required root

 if mid5 == n:

 return mid

 # Since we need floor, we update answer

 # when mid5 is smaller than n, and move

 # closer to 5'th root

 if mid5 < n:

 

 low = mid + 1

 ans = mid

 

 else: # If mid^5 is greater than n

 high = mid - 1

 

 return ans

# Driver Code

if __name__ == "__main__":

 n = 250

 print("Floor of 5'th root is", floorRoot5(n))

# This code is contributed by Rituraj Jain  
  
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

// A C# program to find

// floor of 5'th root

using System;

class GFG {

 

 // Returns floor of 5'th

 // root of n

 static int floorRoot5(int n)

 {

 

 // Base cases

 if (n == 0 || n == 1)

 return n;

 

 // Do Binary Search for

 // floor of 5th square root

 int low = 1, high = n, ans = 0;

 while (low <= high)

 {

 

 // Find the middle point

 // and its power 5

 int mid = (low + high) / 2;

 long mid5 = mid * mid * mid *

 mid * mid;

 

 // If mid is the required root

 if (mid5 == n)

 return mid;

 

 // Since we need floor,

 // we update answer when

 // mid5 is smaller than n,

 // and move closer to

 // 5'th root

 if (mid5 < n)

 {

 low = mid + 1;

 ans = mid;

 }

 

 // If mid^5 is greater

 // than n

 else

 high = mid - 1;

 }

 return ans;

 }

 

 // Driver Code

 public static void Main(String []args)

 {

 int n = 250;

 Console.WriteLine("Floor of 5'th root is " +

 floorRoot5(n));

 }

}

// This code is contributed by Anshul Aggarwal.  
  
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

// A PHP program to find floor of 5'th root

// Returns floor of 5'th root of n

function floorRoot5($n)

{

 // Base cases

 if ($n == 0 || $n == 1)

 return $n;

 // Do Binary Search for floor of 5th square root

 $low = 1;

 $high = $n;

 $ans = 0;

 while ($low <= $high)

 {

 // Find the middle point and its power 5

 $mid = (int)(($low + $high) / 2);

 $mid5 = $mid*$mid*$mid*$mid*$mid;

 // If mid is the required root

 if ($mid5 == $n)

 return $mid;

 // Since we need floor, we update answer when

 // mid5 is smaller than n, and move closer to

 // 5'th root

 if ($mid5 < $n)

 {

 $low = $mid + 1;

 $ans = $mid;

 }

 else // If mid^5 is greater than n

 $high = $mid - 1;

 }

 return $ans;

}

 // Driver code

 $n = 250;

 echo "Floor of 5'th root is ".floorRoot5($n);

 

// This code is contributed by mits

?>  
  
---  
  
 __

 __

 **Output:**

    
    
    Floor of 5'th root is 3

Time complexity of above solution is **O(Log n)**  
We can also use Newton Raphson Method to find exact root. See this for
implementation.  
Source : http://qa.geeksforgeeks.org/7487/program-calculate-fifth-without-
using-mathematical-operators  
Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save


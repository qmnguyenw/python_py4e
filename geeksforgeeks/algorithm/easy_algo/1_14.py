Check if sum of any subarray is Palindrome or not



Given an array **arr[]** of size **N**. the task is to check whether there
exists any subarray of **size atleast 2** such that its sum is palindrome. If
such a subarray exists, then print **YES**. Otherwise, print **NO**.

 **Examples:**

>  **Input:** arr[] = {10, 6, 7, 9, 12}  
>  **Output:** Yes  
>  **Explanation:**  
>  The subarray [6, 7, 9] with sum 22 is palindrome.
>
>  **Input:** arr[] = {15, 4, 8, 2}  
>  **Output:** No  
>  **Explanation:**  
>  No such subarray exists.

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:**  
To solve the problem follow the steps below:

  

  

  * Create a **prefix sum array** of the given array.
  * Iterate over the array using nested for loops to denote start and end of subarrays. The sum of the subarray within the indices [x, y] can be obtained by **pref[y] – pref[x – 1]**.
  * Check if this sum is Palindrome or not. If any of the sum if palindrome print “Yes”, otherwise print “No”.

Below is the implementation of above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to check if sum of any

// subarray of size atleast 2 is

// palindrome or not

 

#include <bits/stdc++.h>

using namespace std;

 

// Function which checks whether

// a given number is palindrome or not

bool checkPalindrome(int n)

{

 // Store the reverse of

 // the number n

 int rev = 0;

 for (int x = n; x != 0; x /= 10) {

 int d = x % 10;

 rev = rev * 10 + d;

 }

 if (rev == n)

 return true;

 

 else

 return false;

}

 

// Function which checks if the

// requires subarray exists or not

void findSubarray(int ar[], int n)

{

 // Making a prefix sum array of ar[]

 int pref[n];

 pref[0] = ar[0];

 

 for (int x = 1; x < n; x++)

 pref[x] = pref[x - 1] + ar[x];

 

 // Boolean variable that will store

 // whether such subarray exists or not

 bool found = false;

 for (int x = 0; x < n; x++) {

 for (int y = x + 1; y < n; y++) {

 // sum stores the sum of subarray

 // from index x to y of array

 int sum = pref[y];

 if (x > 0) {

 sum -= pref[x - 1];

 }

 if (checkPalindrome(sum)) {

 // Required subarray is found

 found = true;

 break;

 }

 }

 

 if (found)

 break;

 }

 if (found)

 cout << "Yes" << endl;

 

 else

 cout << "No" << endl;

}

 

// Driver code

int main()

{

 int ar[] = { 1, 11, 20, 35 };

 

 int n = sizeof(ar) / sizeof(ar[0]);

 

 findSubarray(ar, n);

 

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

// Java program to check if sum of any

// subarray of size atleast 2 is 

// palindrome or not 

class GFG{

 

// Function which checks whether 

// a given number is palindrome or not 

static boolean checkPalindrome(int n) 

{ 

 

 // Store the reverse of 

 // the number n 

 int rev = 0; 

 for(int x = n; x != 0; x /= 10) 

 { 

 int d = x % 10; 

 rev = rev * 10 + d; 

 } 

 if (rev == n) 

 return true; 

 else

 return false; 

} 

 

// Function which checks if the 

// requires subarray exists or not 

static void findSubarray(int []ar, int n) 

{ 

 

 // Making a prefix sum array of ar[] 

 int []pref = new int[n]; 

 pref[0] = ar[0]; 

 

 for(int x = 1; x < n; x++) 

 pref[x] = pref[x - 1] + ar[x]; 

 

 // Boolean variable that will store 

 // whether such subarray exists or not 

 boolean found = false; 

 

 for(int x = 0; x < n; x++) 

 { 

 for(int y = x + 1; y < n; y++) 

 { 

 

 // sum stores the sum of subarray 

 // from index x to y of array 

 int sum = pref[y]; 

 if (x > 0) 

 { 

 sum -= pref[x - 1]; 

 } 

 if (checkPalindrome(sum)) 

 { 

 

 // Required subarray is found 

 found = true; 

 break; 

 } 

 } 

 if (found) 

 break; 

 } 

 if (found) 

 System.out.println("Yes"); 

 else

 System.out.println("No"); 

} 

 

// Driver code 

public static void main(String args[]) 

{ 

 int []ar = { 1, 11, 20, 35 }; 

 int n = ar.length; 

 

 findSubarray(ar, n); 

} 

} 

 

// This code is contributed by AnkitRai01  
  
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

# Python3 program to check if sum of

# any subarray of size atleast 2 is

# palindrome or not

 

# Function which checks whether a 

# given number is palindrome or not

def checkPalindrome(n):

 

 # Store the reverse 

 # of the number n

 rev = 0

 x = n

 

 while(x != 0):

 d = x % 10

 rev = rev * 10 + d

 x = x // 10

 

 if (rev == n):

 return True

 else:

 return False

 

# Function which checks if the

# requires subarray exists or not

def findSubarray(ar, n):

 

 # Making a prefix sum array of ar[]

 pref = [0 for i in range(n)]

 pref[0] = ar[0]

 

 for x in range(1, n):

 pref[x] = pref[x - 1] + ar[x]

 

 # Boolean variable that will store

 # whether such subarray exists or not

 found = False

 

 for x in range(n):

 for y in range(x + 1, n, 1):

 

 # Sum stores the sum of subarray

 # from index x to y of array

 sum = pref[y]

 if (x > 0):

 sum -= pref[x - 1]

 

 if (checkPalindrome(sum)):

 

 # Required subarray is found

 found = True

 break

 

 if (found):

 break

 if (found):

 print("Yes")

 else:

 print("No")

 

# Driver code

if __name__ == '__main__':

 

 ar = [ 1, 11, 20, 35 ]

 n = len(ar)

 

 findSubarray(ar, n)

 

# This code is contributed by Surendra_Gangwar  
  
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

// C# program to check if sum of any

// subarray of size atleast 2 is

// palindrome or not

using System;

 

class GFG{

 

// Function which checks whether

// a given number is palindrome or not

static bool checkPalindrome(int n)

{

 // Store the reverse of

 // the number n

 int rev = 0;

 for(int x = n; x != 0; x /= 10) 

 {

 int d = x % 10;

 rev = rev * 10 + d;

 }

 if (rev == n)

 return true;

 else

 return false;

}

 

// Function which checks if the

// requires subarray exists or not

static void findSubarray(int []ar, int n)

{

 // Making a prefix sum array of ar[]

 int []pref = new int[n];

 pref[0] = ar[0];

 

 for(int x = 1; x < n; x++)

 pref[x] = pref[x - 1] + ar[x];

 

 // Boolean variable that will store

 // whether such subarray exists or not

 bool found = false;

 for(int x = 0; x < n; x++)

 {

 for(int y = x + 1; y < n; y++) 

 {

 // sum stores the sum of subarray

 // from index x to y of array

 int sum = pref[y];

 if (x > 0) 

 {

 sum -= pref[x - 1];

 }

 if (checkPalindrome(sum))

 {

 

 // Required subarray is found

 found = true;

 break;

 }

 }

 if (found)

 break;

 }

 if (found)

 Console.WriteLine("Yes");

 else

 Console.WriteLine("No");

}

 

// Driver code

public static void Main()

{

 int []ar = { 1, 11, 20, 35 };

 int n = ar.Length;

 

 findSubarray(ar, n);

}

}

 

// This code is contributed by Code_Mech  
  
---  
  
 __

 __

 **Output:**

    
    
    Yes
    

_**Time Complexity:** O(N2)  
 **Auxiliary Space:** O(1)_

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


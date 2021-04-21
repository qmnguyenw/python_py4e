Factorial of an Array of integers



Given an array with positive integers. The task is to find the factorial of
all the array elements.

 **Note** : As the numbers would be very large, print them by taking modulus
with 109+7.

 **Examples:**

    
    
    **Input** : arr[] = {3, 10, 200, 20, 12}
    **Output** : 6 3628800 722479105 146326063 479001600
    
    **Input** : arr[] = {5, 7, 10}
    **Output** : 120 5040 3628800 
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Naive approach :** We know that there is a simple approach to calculate the
factorial of a number. We can run a loop for all array values and can find the
factorial of every number using the above approach.

 **Time Complexity** would be **O(N 2)**  
 **Space Complexity** would be **O(1)**

  

  

 **Efficient Approach :** We know that the factorial of a number:

    
    
    **N! = N*(N-1)*(N-2)*(N-3)*****3*2*1**
    

The recursive formulae to calculate factorial of a number is:

    
    
    fact(N) = N*fact(N-1).
    

Hence we will build an array in a bottom-up manner using the above recursion.
Once we have stored the values in the array then we can answer the queries in
O(1) time. Hence the overall time complexity would be O(N). We can use this
method only if the array values are less than 10^6. Otherwise, we would not be
able to store them in an array.

Below is the implementation of the above approach :  

## C/C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation of the approach

 

#include <iostream>

#include <vector>

using namespace std;

#define MOD 1000000007

#define SIZE 10000

 

// Function to calculate the factorial

// using dynamic programing

void factorial(vector<long long int>& fact)

{

 int i;

 fact[0] = 1;

 for (i = 1; i <= SIZE; i++) {

 

 // Calculation of factorial

 // As fact[i-1] stores the factorial of n-1

 // so factorial of n is fact[i] = (fact[i-1]*i)

 fact[i] = (fact[i - 1] * i) % MOD;

 }

}

 

// Function to print factorial of every element

// of the array

void PrintFactorial(vector <long long int> &fact;,

 int arr[],int n){

 for(int i=0;i<n;i+=1){

 

 // Printing the stored value of arr[i]!

 cout<<fact[arr[i]]<<" ";

 }

}

 

// Driver code

int main()

{

 // vector to store the factorial values

 // max_element(arr) should be less than SIZE

 vector<long long int> fact(SIZE + 1, 0);

 

 int arr[5] = {3, 10, 200, 20, 12};

 int n = sizeof(arr)/sizeof(arr[0]);

 

 // Function to store factorial values mod 10**9+7

 factorial(fact);

 

 // Function to print the factorial values mod 10**9+7

 PrintFactorial(fact,arr,n);

 

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

 

class Sol

{

 

static int MOD = 1000000007 ;

static int SIZE = 10000; 

 

 

// vector to store the factorial values 

// max_element(arr) should be less than SIZE 

static Vector<Long> fact = new Vector<Long>();

 

// Function to calculate the factorial 

// using dynamic programing 

static void factorial() 

{ 

 int i; 

 fact.add((long)1); 

 for (i = 1; i <= SIZE; i++) 

 { 

 

 // Calculation of factorial 

 // As fact[i-1] stores the factorial of n-1 

 // so factorial of n is fact[i] = (fact[i-1]*i) 

 fact.add((fact.get(i - 1) * i) % MOD); 

 } 

} 

 

// Function to print factorial of every element 

// of the array 

static void PrintFactorial(int arr[],int n)

{ 

 for(int i = 0; i < n; i += 1)

 { 

 

 // Printing the stored value of arr[i]! 

 System.out.print(fact.get(arr[i])+" "); 

 } 

} 

 

// Driver code 

public static void main(String args[])

{ 

 

 int arr[] = {3, 10, 200, 20, 12}; 

 int n = arr.length; 

 

 // Function to store factorial values mod 10**9+7 

 factorial(); 

 

 // Function to print the factorial values mod 10**9+7 

 PrintFactorial(arr,n); 

}

} 

 

// This code is contributed by Arnab Kundu  
  
---  
  
 __

 __

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python implementation of the above Approach

mod = 1000000007

SIZE = 10000

 

# declaring list initially and making

# it 1 i.e for every index 

fact = [1]*SIZE

 

# Calculation of factorial using Dynamic programing

def factorial(): 

 for i in range(1, SIZE): 

 

 # Calculation of factorial

 # As fact[i-1] stores the factorial of n-1

 # so factorial of n is fact[i] = (fact[i-1]*i) 

 fact[i] = (fact[i-1]*i) % mod

 

# function call

factorial()

 

# Driver code

arr=[3,10,200,20,12]

for i in arr:

 print fact[i],  
  
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

 

$MOD = 1000000007 ;

$SIZE = 10000 ;

 

// Function to calculate the factorial 

// using dynamic programing 

function factorial($fact) 

{ 

 $fact[0] = 1; 

 for ($i = 1; $i <= $GLOBALS['SIZE']; $i++) 

 { 

 

 // Calculation of factorial 

 // As fact[i-1] stores the factorial of n-1 

 // so factorial of n is fact[i] = (fact[i-1]*i) 

 $fact[$i] = ($fact[$i - 1] * $i) %
$GLOBALS['MOD']; 

 } 

 return $fact;

} 

 

// Function to print factorial of every element 

// of the array 

function PrintFactorial($fact, $arr, $n)

{ 

 for($i = 0; $i < $n; $i++)

 { 

 

 // Printing the stored value of arr[i]! 

 echo $fact[$arr[$i]]," "; 

 } 

} 

 

 // Driver code 

 // vector to store the factorial values 

 // max_element(arr) should be less than SIZE 

 $fact = array_fill(0,$SIZE + 1, 0); 

 

 $arr = array(3, 10, 200, 20, 12); 

 $n = count($arr); 

 

 // Function to store factorial values mod 10**9+7 

 $fact = factorial($fact); 

 

 // Function to print the factorial values mod 10**9+7 

 PrintFactorial($fact,$arr,$n); 

 

 // This code is contributed by AnkitRai01

?>  
  
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

// C# implementation of above approach

using System.Collections.Generic;

using System;

 

class Sol

{

 

static int MOD = 1000000007 ;

static int SIZE = 10000; 

 

 

// vector to store the factorial values 

// max_element(arr) should be less than SIZE 

static List<long> fact = new List<long>();

 

// Function to calculate the factorial 

// using dynamic programing 

static void factorial() 

{ 

 int i; 

 fact.Add((long)1); 

 for (i = 1; i <= SIZE; i++) 

 { 

 

 // Calculation of factorial 

 // As fact[i-1] stores the factorial of n-1 

 // so factorial of n is fact[i] = (fact[i-1]*i) 

 fact.Add((fact[i - 1] * i) % MOD); 

 } 

} 

 

// Function to print factorial of every element 

// of the array 

static void PrintFactorial(int []arr,int n)

{ 

 for(int i = 0; i < n; i += 1)

 { 

 

 // Printing the stored value of arr[i]! 

 Console.Write(fact[arr[i]]+" "); 

 } 

} 

 

// Driver code 

public static void Main(String []args)

{ 

 

 int []arr = {3, 10, 200, 20, 12}; 

 int n = arr.Length; 

 

 // Function to store factorial values mod 10**9+7 

 factorial(); 

 

 // Function to print the factorial values mod 10**9+7 

 PrintFactorial(arr,n); 

}

}

 

// This code is contributed by 29AjayKumar  
  
---  
  
 __

 __

 **Output:**

    
    
    6 3628800 722479105 146326063 479001600
    

**Time Complexity** : O(N)  
 **Space Complexity** : O(N)

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


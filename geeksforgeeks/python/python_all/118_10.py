Lehmann’s Primality Test



An integer p greater than one is prime iff the only divisors of p are 1 and p.
First few prime numbers are 2, 3, 5, 7, 11, 13, …

The **Lehmann’s test** is a probabilistic primality test for an natural number
n, it can test the primality of any kind of number(whether a large odd number
is prime or not). The Lehmann’s test is a variation of Fermat’s Primality
Test.

The approach used is as follows:  
If ‘n’ is an odd number and ‘a’ is a random integer less than n but greater
than 1, then

    
    
    x = (a^((n-1)/2)) (mod n)

It is computed.

  1. If x is 1 or -1(or n-1), then n may be prime.
  2. If x is not 1 or -1(or n-1), then n is definitely composite.

The fact that any composite number can be turned out to be a prime, in this
case, depends on the random value ‘a’. If all the values of a and n are co-
prime, then n can be said as a prime number.

    
    
     **Example-1:**
    **Input:** n = 13 
    **Output:** 13 is Prime 
    
    **Explanation:** 
    Let a = 3, then, 
    3^((13-1)/2) % 13 = 729 % 13 = 1
    Hence, 13 is Prime.
    
    **Example-2:**
    **Input:** n = 91
    **Output:** 91 is Composite
    
    **Explanation:** 
    Let a = 3, then, 
    3^((91-1)/2) % 91 = 27
    Hence, 91 is Composite. 

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ code for Lehmann's Primality Test

#include<stdio.h>

#include<stdlib.h>

#include<ctime>

#include<bits/stdc++.h>

using namespace std;

 

// function to check Lehmann's test

int lehmann(int n, int t)

{

 

 // generating a random base less than n

 int a = 2 + (rand() % (n - 1));

 

 // calculating exponent

 int e = (n - 1) / 2;

 

 // iterate to check for different base values 

 // for given number of tries 't'

 while(t > 0)

 {

 

 // calculating final value using formula

 int result =((int)(pow(a, e)))% n;

 

 //if not equal, try for different base

 if((result % n) == 1 || (result % n) == (n - 1)) 

 {

 a = 2 + (rand() % (n - 1));

 t -= 1;

 }

 

 // else return negative

 else

 return -1;

 }

 

 // return positive after attempting

 return 1;

}

 

// Driver code

int main()

{

 int n = 13 ; // number to be tested

 int t = 10 ; // number of tries

 

 // if n is 2, it is prime

 if(n == 2)

 cout << "2 is Prime.";

 

 // if even, it is composite

 if(n % 2 == 0)

 cout << n << " is Composite";

 

 // if odd, check

 else

 {

 int flag = lehmann(n, t);

 

 if(flag ==1)

 cout << n << " may be Prime.";

 

 else

 cout << n << " is Composite.";

 } 

}

 

// This code is contibuted by chitranayal  
  
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

// Java code for Lehmann's Primality Test

 

// importing "random" for random operations 

import java.util.Random;

 

class GFG

{

 

 // function to check Lehmann's test 

 static int lehmann(int n, int t)

 {

 

 // create instance of Random class 

 Random rand = new Random(); 

 

 // generating a random base less than n 

 int a = rand.nextInt(n - 3) + 2;

 

 // calculating exponent 

 float e = (n - 1) / 2;

 

 // iterate to check for different base values 

 // for given number of tries 't' 

 while(t > 0)

 {

 

 // calculating final value using formula 

 int result = ((int)(Math.pow(a, e))) % n;

 

 // if not equal, try for different base 

 if((result % n) == 1 || (result % n) == (n - 1))

 {

 a = rand.nextInt(n - 3) + 2;

 t -= 1;

 }

 

 // else return negative 

 else

 return -1;

 

 }

 

 // return positive after attempting 

 return 1;

 }

 

 // Driver code 

 public static void main (String[] args)

 {

 int n = 13; // number to be tested 

 int t = 10; // number of tries 

 

 // if n is 2, it is prime 

 if(n == 2)

 System.out.println(" 2 is Prime."); 

 

 // if even, it is composite 

 if(n % 2 == 0)

 System.out.println(n + " is Composite");

 

 // if odd, check 

 else

 {

 long flag = lehmann(n, t);

 

 if(flag == 1)

 System.out.println(n + " may be Prime.");

 

 else

 System.out.println(n + " is Composite."); 

 }

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

# Python code for Lehmann's Primality Test

 

# importing "random" for random operations

import random

 

# function to check Lehmann's test

def lehmann(n, t):

 

 # generating a random base less than n

 a = random.randint(2, n-1)

 

 # calculating exponent

 e =(n-1)/2

 

 # iterate to check for different base values 

 # for given number of tries 't'

 while(t>0):

 

 # calculating final value using formula

 result =((int)(a**e))% n

 

 # if not equal, try for different base

 if((result % n)== 1 or (result %
n)==(n-1)):

 a = random.randint(2, n-1)

 t-= 1

 

 # else return negative

 else:

 return -1

 

 # return positive after attempting

 return 1

 

# Driver code

n = 13 # number to be tested

t = 10 # number of tries

 

# if n is 2, it is prime

if(n is 2):

 print("2 is Prime.")

 

# if even, it is composite

if(n % 2 == 0):

 print(n, "is Composite")

 

# if odd, check

else:

 flag = lehmann(n, t)

 

 if(flag is 1):

 print(n, "may be Prime.")

 

 else:

 print(n, "is Composite.")  
  
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

// C# code for Lehmann's Primality Test

using System;

 

class GFG

{

 

// function to check Lehmann's test 

static int lehmann(int n, int t)

{

 

 // create instance of Random class 

 Random rand = new Random(); 

 

 // generating a random base less than n 

 int a = rand.Next(n - 3) + 2;

 

 // calculating exponent 

 float e = (n - 1) / 2;

 

 // iterate to check for different base values 

 // for given number of tries 't' 

 while(t > 0)

 {

 

 // calculating final value using formula 

 int result = ((int)(Math.Pow(a, e))) % n;

 

 // if not equal, try for different base 

 if((result % n) == 1 || 

 (result % n) == (n - 1))

 {

 a = rand.Next(n - 3) + 2;

 t -= 1;

 }

 

 // else return negative 

 else

 return -1;

 

 }

 

 // return positive after attempting 

 return 1;

}

 

// Driver code 

public static void Main (String[] args)

{

 int n = 13; // number to be tested 

 int t = 10; // number of tries 

 

 // if n is 2, it is prime 

 if(n == 2)

 Console.WriteLine(" 2 is Prime."); 

 

 // if even, it is composite 

 if(n % 2 == 0)

 Console.WriteLine(n + " is Composite");

 

 // if odd, check 

 else

 {

 long flag = lehmann(n, t);

 

 if(flag == 1)

 Console.WriteLine(n + " may be Prime.");

 

 else

 Console.WriteLine(n + " is Composite."); 

 }

}

}

 

// This code is contributed by Rajput-Ji  
  
---  
  
 __

 __

 **Output:**

    
    
    13 may be Prime.
    

Attention reader! Don’t stop learning now. Get hold of all the important CS
Theory concepts for SDE interviews with the **CS Theory Course** at a student-
friendly price and become industry ready.

  
  

  

My Personal Notes _arrow_drop_up_

Save


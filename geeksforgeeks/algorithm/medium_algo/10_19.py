Count numbers in a range having GCD of powers of prime factors equal to 1



Given a range represented by two positive integers **L** and **R**. The task
is to count the numbers from the range having GCD of powers of prime factors
equal to 1. In other words, if a number **X** has its prime factorization of
the form **2 p1 * 3p2 * 5p3 * …** then the GCD of **p 1, p2, p3, …** should be
equal to **1**.

 **Examples:**

>  **Input:** L = 2, R = 5  
>  **Output:** 3  
> 2, 3, and 5 are the required numbers having GCD of powers of prime factors
> equal to 1.  
> 2 = 21  
> 3 = 31  
> 5 = 51
>
>  **Input:** L = 13, R = 20  
>  **Output:** 7

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Prerequisites:** Perfect Powers in a Range  
 **Naive Approach:** Iterate over all numbers from **L** to **R** and prime
factorise each number then calculate the GCD of powers of the prime factors.
If the **GCD = 1** , increment a **count** variable and finally return it as
the answer.

  

  

 **Efficient Approach:** The key idea here is to notice that the valid numbers
are not perfect powers since the powers of prime factors number are in such a
way that their GCD is always greater than 1. In other words, all perfect
powers are not valid numbers.  
 **For e.g.**

> 2500 is perfect power whose prime factorization is 2500 = 22 * 54. Now the
> GCD of (2, 4) = 2 which is greater than 1.  
> If some number has xth power of a factor in its prime factorization, then
> the powers of other prime factors will have to be multiples of x in order
> for the number to be invalid.

Hence, we can find the total number of perfect powers lying in the range and
subtract it from the total numbers.

Below is the implementation of the above approach:  

## CPP

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

 

#define N 1000005

#define MAX 1e18

 

// Vector to store powers greater than 3

vector<long int> powers;

 

// Set to store perfect squares

set<long int> squares;

 

// Set to store powers other than perfect squares

set<long int> s;

 

void powersPrecomputation()

{

 for (long int i = 2; i < N; i++) {

 

 // Pushing squares

 squares.insert(i * i);

 

 // if the values is already a perfect square means

 // present in the set

 if (squares.find(i) != squares.end())

 continue;

 

 long int temp = i;

 

 // Run loop until some power of current number

 // doesn't exceed MAX

 while (i * i <= MAX / temp) {

 temp *= (i * i);

 

 // Pushing only odd powers as even power of a number 

 // can always be expressed as a perfect square 

 // which is already present in set squares

 s.insert(temp);

 }

 }

 

 // Inserting those sorted

 // values of set into a vector

 for (auto x : s)

 powers.push_back(x);

}

 

long int calculateAnswer(long int L, long int R)

{

 

 // Precompute the powers

 powersPrecomputation();

 

 // Calculate perfect squares in

 // range using sqrtl function

 long int perfectSquares = floor(sqrtl(R)) - floor(sqrtl(L -
1));

 

 // Calculate upper value of R

 // in vector using binary search

 long int high = upper_bound(powers.begin(),

 powers.end(), R)

 - powers.begin();

 

 // Calculate lower value of L

 // in vector using binary search

 long int low = lower_bound(powers.begin(),

 powers.end(), L)

 - powers.begin();

 

 // Calculate perfect powers

 long perfectPowers = perfectSquares + (high - low);

 

 // Compute final answer

 long ans = (R - L + 1) - perfectPowers;

 return ans;

}

 

// Driver Code

int main()

{

 long int L = 13, R = 20;

 cout << calculateAnswer(L, R);

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

// Java implementation of above idea

import java.util.*;

 

class GFG 

{

 

 static int N = 1000005;

 static long MAX = (long) 1e18;

 

 // Vector to store powers greater than 3

 static Vector<Long> powers = new Vector<>();

 

 // Set to store perfect squares

 static TreeSet<Long> squares = new TreeSet<>();

 

 // Set to store powers other than perfect squares

 static TreeSet<Long> s = new TreeSet<>();

 

 static void powersPrecomputation()

 {

 for (long i = 2; i < N; i++)

 {

 

 // Pushing squares

 squares.add(i * i);

 

 // if the values is already a perfect square means

 // present in the set

 if (squares.contains(i))

 continue;

 

 long temp = i;

 

 // Run loop until some power of current number

 // doesn't exceed MAX

 while (i * i <= MAX / temp)

 {

 temp *= (i * i);

 

 // Pushing only odd powers as even power of a number

 // can always be expressed as a perfect square

 // which is already present in set squares

 s.add(temp);

 }

 }

 

 // Inserting those sorted

 // values of set into a vector

 for (long x : s)

 powers.add(x);

 }

 

 static long calculateAnswer(long L, long R)

 {

 

 // Precompute the powers

 powersPrecomputation();

 

 // Calculate perfect squares in

 // range using sqrtl function

 long perfectSquares = (long) (Math.floor(Math.sqrt(R)) - 

 Math.floor(Math.sqrt(L - 1)));

 

 // Calculate upper value of R

 // in vector using binary search

 long high = Collections.binarySearch(powers, R);

 

 // Calculate lower value of L

 // in vector using binary search

 long low = Collections.binarySearch(powers, L);

 

 // Calculate perfect powers

 long perfectPowers = perfectSquares + (high - low);

 

 // Compute final answer

 long ans = (R - L + 1) - perfectPowers;

 return ans;

 }

 

 // Driver Code

 public static void main(String[] args)

 {

 long L = 13, R = 20;

 System.out.println(calculateAnswer(L, R));

 }

}

 

// This code is contributed by

// sanjeev2552  
  
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

# Python3 implementation of the approach

from bisect import bisect as upper_bound

from bisect import bisect_left as lower_bound

from math import floor

N = 1000005

MAX = 10**18

 

# Vector to store powers greater than 3

powers = []

 

# Set to store perfect squares

squares = dict()

 

# Set to store powers other than perfect squares

s = dict()

 

def powersPrecomputation():

 

 for i in range(2, N):

 

 # Pushing squares

 squares[i * i] = 1

 

 # if the values is already a perfect square means

 # present in the set

 if (i not in squares.keys()):

 continue

 

 temp = i

 

 # Run loop until some power of current number

 # doesn't exceed MAX

 while (i * i <= (MAX // temp)):

 temp *= (i * i)

 

 # Pushing only odd powers as even power of a number

 # can always be expressed as a perfect square

 # which is already present in set squares

 s[temp]=1

 

 # Inserting those sorted

 # values of set into a vector

 for x in s:

 powers.append(x)

 

def calculateAnswer(L, R):

 

 # Precompute the powers

 powersPrecomputation()

 

 # Calculate perfect squares in

 # range using sqrtl function

 perfectSquares = floor((R)**(.5)) - floor((L -
1)**(.5))

 

 # Calculate upper value of R

 # in vector using binary search

 high = upper_bound(powers,R)

 

 # Calculate lower value of L

 # in vector using binary search

 low = lower_bound(powers,L)

 

 # Calculate perfect powers

 perfectPowers = perfectSquares + (high - low)

 

 # Compute final answer

 ans = (R - L + 1) - perfectPowers

 

 return ans

 

 

# Driver Code

 

L = 13

R = 20

print(calculateAnswer(L, R))

 

# This code is contributed by mohit kumar 29  
  
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

// C# implementation of above idea

using System;

using System.Collections.Generic;

 

public class GFG 

{

 

 static int N = 100005;

 static long MAX = (long) 1e18;

 

 // List to store powers greater than 3

 static List<long> powers = new List<long>();

 

 // Set to store perfect squares

 static HashSet<long> squares = new HashSet<long>();

 

 // Set to store powers other than perfect squares

 static HashSet<long> s = new HashSet<long>();

 

 static void powersPrecomputation()

 {

 for (long i = 2; i < N; i++)

 {

 

 // Pushing squares

 squares.Add(i * i);

 

 // if the values is already a perfect square means

 // present in the set

 if (squares.Contains(i))

 continue;

 

 long temp = i;

 

 // Run loop until some power of current number

 // doesn't exceed MAX

 while (i * i <= MAX / temp)

 {

 temp *= (i * i);

 

 // Pushing only odd powers as even power of a number

 // can always be expressed as a perfect square

 // which is already present in set squares

 s.Add(temp);

 }

 }

 

 // Inserting those sorted

 // values of set into a vector

 foreach (long x in s)

 powers.Add(x);

 }

 

 static long calculateAnswer(long L, long R)

 {

 

 // Precompute the powers

 powersPrecomputation();

 

 // Calculate perfect squares in

 // range using sqrtl function

 long perfectSquares = (long) (Math.Floor(Math.Sqrt(R)) - 

 Math.Floor(Math.Sqrt(L - 1)));

 

 // Calculate upper value of R

 // in vector using binary search

 long high = Array.BinarySearch(powers.ToArray(), R);

 

 // Calculate lower value of L

 // in vector using binary search

 long low = Array.BinarySearch(powers.ToArray(), L);

 

 // Calculate perfect powers

 long perfectPowers = perfectSquares + (high - low);

 

 // Compute readonly answer

 long ans = (R - L + 1) - perfectPowers;

 return ans;

 }

 

 // Driver Code

 public static void Main(String[] args)

 {

 long L = 13, R = 20;

 Console.WriteLine(calculateAnswer(L, R));

 }

}

 

// This code is contributed by 29AjayKumar  
  
---  
  
 __

 __

 **Output:**

    
    
    7
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


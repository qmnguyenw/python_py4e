Largest Divisor of a Number not divisible by a perfect square



Given a positive integer, **N**. Find the largest divisor of the given number
that is not divisible by a perfect square greater than 1.

 **Examples:**

    
    
    **Input :** 12
    **Output :** 6
    **Explanation :** Divisors of 12 are 1, 2, 3, 4, 6 and 12. 
    Since 12 is divisible by 4 (a perfect square), 
    it can't be required divisor. 6 is not divisible 
    by any perfect square.
     
    **Input :** 97
    **Output :** 97

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

A **simple approach** is to find all the divisors of the given number **N** by
iterating up to the square root of N and keep them in sorted order(Descending)
in a list. Here we are inserting them in a set in descending order to keep
them sorted. Also, make a list of all perfect squares up to 1010 by iterating
from 1 to 105.  
Now for each divisor starting from the greatest one check whether it is
divisible by any perfect square in the list or not. If a divisor is not
divisible by any perfect, simply return it as the answer.

Below is the implementation of the above approach.

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ Program to find the largest

// divisor not divisible by any

// perfect square greater than 1

#include <bits/stdc++.h>

using namespace std;

const int MAX = 1e5;

// Function to find the largest

// divisor not divisible by any

// perfect square greater than 1

int findLargestDivisor(int n)

{

 // set to store divisors in

 // descending order

 int m = n;

 set<int, greater<int> > s;

 s.insert(1);

 s.insert(n);

 for (int i = 2; i < sqrt(n) + 1; i++) {

 // If the number is divisible

 // by i, then insert it

 if (n % i == 0) {

 s.insert(n / i);

 s.insert(i);

 while (m % i == 0)

 m /= i;

 }

 }

 if (m > 1)

 s.insert(m);

 // Vector to store perfect squares

 vector<int> vec;

 for (int i = 2; i <= MAX; i++)

 vec.push_back(i * i);

 // Check for each divisor, if it is not

 // divisible by any perfect square,

 // simply return it as the answer.

 for (auto d : s) {

 int divi = 0;

 for (int j = 0; j < vec.size()

 && vec[j] <= d;

 j++) {

 if (d % vec[j] == 0) {

 divi = 1;

 break;

 }

 }

 if (!divi)

 return d;

 }

}

// Driver Code

int main()

{

 int n = 12;

 cout << findLargestDivisor(n) << endl;

 n = 97;

 cout << findLargestDivisor(n) << endl;

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

// Java Program to find the largest

// divisor not divisible by any

// perfect square greater than 1

import java.util.*;

class Main{

 

static int MAX = (int)1e5;

 

// Function to find the largest

// divisor not divisible by any

// perfect square greater than 1

public static int findLargestDivisor(int n)

{

 // set to store divisors in

 // descending order

 int m = n;

 Set<Integer> s =

 new HashSet<Integer>();

 s.add(1);

 s.add(n);

 for (int i = 2;

 i < (int)Math.sqrt(n) + 1; i++)

 {

 // If the number is divisible

 // by i, then insert it

 if (n % i == 0)

 {

 s.add(n / i);

 s.add(i);

 while (m % i == 0)

 m /= i;

 }

 }

 if (m > 1)

 s.add(m);

 List<Integer> l =

 new ArrayList<Integer>(s);

 Collections.sort(l);

 Collections.reverse(l);

 // Vector to store

 // perfect squares

 Vector<Integer> vec =

 new Vector<Integer>();

 for (int i = 2; i <= MAX; i++)

 vec.add(i * i);

 // Check for each divisor, if

 // it is not divisible by any

 // perfect square, simply return

 // it as the answer.

 for (int d : l)

 {

 int divi = 0;

 

 for (int j = 0;

 j < vec.size() &&

 vec.get(j) <= d; j++)

 {

 if (d % vec.get(j) == 0)

 {

 divi = 1;

 break;

 }

 }

 if (divi == 0)

 return d;

 }

 return 0;

}

// Driver code 

public static void main(String[] args)

{

 int n = 12;

 System.out.println(findLargestDivisor(n));

 n = 97;

 System.out.println(findLargestDivisor(n));

}

}

// This code is contributed by divyeshrabadiya07  
  
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

# Python3 Program to find the largest

# divisor not divisible by any

# perfect square greater than 1

MAX = 10 ** 5

# Function to find the largest

# divisor not divisible by any

# perfect square greater than 1

def findLargestDivisor(n):

 # set to store divisors in

 # descending order

 m = n

 s = set()

 s.add(1)

 s.add(n)

 for i in range(2, int(n ** (0.5)) + 1):

 

 # If the number is divisible

 # by i, then insert it

 if n % i == 0:

 s.add(n // i)

 s.add(i)

 while m % i == 0:

 m //= i

 

 if m > 1:

 s.add(m)

 # Vector to store perfect squares

 vec = [i**2 for i in range(2, MAX + 1)]

 # Check for each divisor, if it is not

 # divisible by any perfect square,

 # simply return it as the answer.

 for d in sorted(s, reverse = True):

 

 divi, j = 0, 0

 while j < len(vec) and vec[j] <= d:

 if d % vec[j] == 0:

 divi = 1

 break

 j += 1

 

 if not divi:

 return d

# Driver Code

if __name__ == "__main__":

 n = 12

 print(findLargestDivisor(n))

 n = 97

 print(findLargestDivisor(n))

 

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

// C# program to find the largest

// divisor not divisible by any

// perfect square greater than 1

using System;

using System.Collections.Generic;

class GFG{

 

static int MAX = (int)1e5;

// Function to find the largest

// divisor not divisible by any

// perfect square greater than 1

static int findLargestDivisor(int n)

{

 

 // Set to store divisors in

 // descending order

 int m = n;

 

 HashSet<int> s = new HashSet<int>();

 s.Add(1);

 s.Add(n);

 

 for(int i = 2;

 i < (int)Math.Sqrt(n) + 1;

 i++)

 {

 

 // If the number is divisible

 // by i, then insert it

 if (n % i == 0)

 {

 s.Add(n / i);

 s.Add(i);

 

 while (m % i == 0)

 m /= i;

 }

 }

 

 if (m > 1)

 s.Add(m);

 

 List<int> l = new List<int>(s);

 l.Sort();

 l.Reverse();

 

 // Vector to store

 // perfect squares

 List<int> vec = new List<int>();

 

 for(int i = 2; i <= MAX; i++)

 vec.Add(i * i);

 

 // Check for each divisor, if

 // it is not divisible by any

 // perfect square, simply return

 // it as the answer.

 foreach(int d in l)

 {

 int divi = 0;

 

 for(int j = 0;

 j < vec.Count && vec[j] <= d;

 j++)

 {

 if (d % vec[j] == 0)

 {

 divi = 1;

 break;

 }

 }

 if (divi == 0)

 return d;

 }

 return 0;

} 

// Driver code

static void Main()

{

 int n = 12;

 Console.WriteLine(findLargestDivisor(n));

 

 n = 97;

 Console.WriteLine(findLargestDivisor(n));

}

}

// This code is contributed by divyesh072019  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    6
    97


Find all divisors of N2 using N



Given a number **N** , the task is to print all distinct divisors of **N 2**.  
 **Examples:**  

> **Input:** N = 4  
> **Output:** 1 2 4 8 16  
> **Explanation:**  
>  N = 4, N2 = 16  
> Divisors of 16 are: 1 2 4 8 16  
> **Input:** N = 8  
>  **Output:** 1 2 4 8 16 32 64  
>

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Naive Approach:**  
Find all divisors of a natural number using sqrt(N) approach. But this
solution is not efficient as the time complexity would be **O(N)**.  
 **Efficient Approach:**  

  * We try to generate divisors of N2 from divisors of N using the sqrt(N) approach. As,  

**For example:** If N = 4, to generate divisors of 42 = 16, we would first
calculate the divisors of 4 = 1, 2, 4. Now we will iterate over this generated
divisors to calculate divisors of 42 that are 1, 2, 4, 8, and 16.  
Below is the implementation of the above approach.  

  

  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ code to print all

// divisors of N*N using N

#include <bits/stdc++.h>

using namespace std;

// Function to find Divisor of N

void DivisorOfN(vector<int>& v,

 map<int, bool>& marked,

 int n)

{

 // sqrt(N) approach

 // to find divisors of N

 for (int i = 1; i <= sqrt(n); i++) {

 if (n % i == 0) {

 if (n / i == i) {

 v.push_back(i);

 marked[i] = true;

 }

 else {

 v.push_back(i);

 v.push_back(n / i);

 marked[i] = true;

 marked[n / i] = true;

 }

 }

 }

}

// Function to print all divisor of N*N

void PrintDivisors(int n)

{

 // Vector v to store divisors of n

 vector<int> v;

 // Map to avoid repeated divisors

 map<int, bool> marked;

 // Store all divisor of n

 DivisorOfN(v, marked, n);

 int size = v.size();

 // Iterating over vector v

 // to generate divisors of N*N

 for (int i = 0; i < size; i++) {

 for (int j = i; j < size; j++) {

 int check = v[i] * v[j];

 // Checking if element is

 // already present

 if (marked[check] != true) {

 v.push_back(v[i] * v[j]);

 // marking element true

 // after adding in vector

 marked[v[i] * v[j]] = true;

 }

 }

 }

 sort(v.begin(), v.end());

 printf("Divisors of %d are: ", n * n);

 for (int i = 0; i < v.size(); i++) {

 printf("%d ", v[i]);

 }

 printf("\n");

}

// Driver Code

int main()

{

 PrintDivisors(4);

 PrintDivisors(8);

 PrintDivisors(10);

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

// Java code to print all

// divisors of N*N using N

import java.util.*;

class GFG

{

 // Vector v to store divisors of n

 static List<Integer> v = new ArrayList<>();

 // Map to avoid repeated divisors

 static HashMap<Integer, Boolean> marked = new HashMap<>();

 // Function to find Divisor of N

 static void DivisorOfN(int n)

 {

 // sqrt(N) approach

 // to find divisors of N

 for (int i = 1; i <= Math.sqrt(n); i++)

 {

 if (n % i == 0)

 {

 if (n / i == i)

 {

 v.add(i);

 marked.put(i, true);

 }

 else

 {

 v.add(i);

 v.add(n / i);

 marked.put(i, true); 

 marked.put(n / i, true);

 }

 }

 }

 }

 // Function to print all divisor of N*N

 static void PrintDivisors(int n)

 {

 // Store all divisor of n

 DivisorOfN(n);

 int size = v.size();

 // Iterating over vector v

 // to generate divisors of N*N

 for (int i = 0; i < size; i++)

 {

 for (int j = i; j < size; j++)

 {

 int check = v.get(i) * v.get(j);

 // Checking if element is

 // already present

 if (!marked.containsKey(check))

 {

 v.add(v.get(i) * v.get(j));

 // marking element true

 // after adding in vector

 marked.put(v.get(i) * v.get(j), true);

 }

 }

 }

 Collections.sort(v); 

 System.out.print("Divisors of " + n * n + " are: ");

 for (int i = 0; i < v.size(); i++)

 {

 System.out.print(v.get(i) + " ");

 }

 System.out.println();

 v.clear();

 marked.clear();

 }

 // Driver code

 public static void main(String[] args)

 {

 PrintDivisors(4);

 PrintDivisors(8);

 PrintDivisors(10);

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

# Python3 code to print all

# divisors of N*N using

from math import sqrt

# Function to find Divisor of N

def DivisorOfN(v, marked, n):

 # sqrt(N) approach

 # to find divisors of N

 for i in range(1,int(sqrt(n)) + 1, 1):

 if (n % i == 0):

 if (n // i == i):

 v.append(i)

 marked[i] = True

 else:

 v.append(i)

 v.append(n // i)

 marked[i] = True

 marked[n // i] = True

# Function to print all divisor of N*N

def PrintDivisors(n):

 # Vector v to store divisors of n

 v = []

 # Map to avoid repeated divisors

 marked = {i:False for i in range(1000)}

 # Store all divisor of n

 DivisorOfN(v, marked, n)

 size = len(v)

 # Iterating over vector v

 # to generate divisors of N*N

 for i in range(size):

 for j in range(i,size,1):

 check = v[i] * v[j]

 # Checking if element is

 # already present

 if (marked[check] != True):

 v.append(v[i] * v[j])

 # marking element true

 # after adding in vector

 marked[v[i] * v[j]] = True

 v.sort(reverse = False)

 print("Divisors of",n * n,"are: ",end = "")

 for i in range(len(v)):

 print(v[i],end = " ")

 

 print("\n",end = "")

# Driver Code

if __name__ == '__main__':

 PrintDivisors(4)

 PrintDivisors(8)

 PrintDivisors(10)

# This code is contributed by Bhupendra_Singh  
  
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

// C# code to print all

// divisors of N*N using N

using System;

using System.Collections.Generic;

class GFG {

 

 // Vector v to store divisors of n

 static List<int> v = new List<int>();

 

 // Map to avoid repeated divisors

 static Dictionary<int, bool> marked = new
Dictionary<int, bool>();

 

 // Function to find Divisor of N

 static void DivisorOfN(int n)

 {

 // sqrt(N) approach

 // to find divisors of N

 for (int i = 1; i <= Math.Sqrt(n); i++)

 {

 

 if (n % i == 0)

 {

 if (n / i == i)

 {

 v.Add(i);

 marked[i] = true;

 }

 else

 {

 v.Add(i);

 v.Add(n / i);

 marked[i] = true;

 marked[n / i] = true;

 }

 }

 }

 }

 // Function to print all divisor of N*N

 static void PrintDivisors(int n)

 {

 

 // Store all divisor of n

 DivisorOfN(n);

 

 int size = v.Count;

 

 // Iterating over vector v

 // to generate divisors of N*N

 for (int i = 0; i < size; i++)

 {

 for (int j = i; j < size; j++)

 {

 int check = v[i] * v[j];

 

 // Checking if element is

 // already present

 if (!marked.ContainsKey(check))

 {

 v.Add(v[i] * v[j]);

 

 // marking element true

 // after adding in vector

 marked[v[i] * v[j]] = true;

 }

 }

 }

 

 v.Sort();

 

 Console.Write("Divisors of " + n * n + " are: ");

 for (int i = 0; i < v.Count; i++)

 {

 Console.Write(v[i] + " ");

 }

 Console.WriteLine();

 

 v.Clear();

 marked.Clear();

 }

 // Driver code

 static void Main()

 {

 PrintDivisors(4);

 PrintDivisors(8);

 PrintDivisors(10);

 }

}

// This code is contributed by divyesh072019  
  
---  
  
 __

 __

 **Output:**

    
    
    Divisors of 16 are: 1 2 4 8 16 
    Divisors of 64 are: 1 2 4 8 16 32 64 
    Divisors of 100 are: 1 2 4 5 10 20 25 50 100

_**Time Complexity:** O(sqrt(N) + a2)_ where, a is number of divisor of N.  
 **Note:** How this approach is different from Find all divisors of a natural
number?  
Let N = 5, therefore we need to find all divisors of 25.  

  * **Using approach used in** **Find all divisors of a natural number** **:** we will iterate using i from 1 to sqrt(25) = 5 and check for i and n/i.  
 _ **Time Complexity:** O(sqrt(25))_  

  * **Using approach used in this article:** we will find divisor of 5 by using the above-mentioned articles approach which will be done in sqrt(5) time complexity. Now for all divisor of 5 i.e. 1, 5 we will store this in an array and multiply it pairwise with the help of 2 loops { (1*1, 1*5, 5*1, 5*5) } and choose the unique ones i.e. 1, 5, 25. This will take a^2 time (where a is the number of the divisor of 5, which is 2 here)   
_**Time Complexity:** O(sqrt(5) + 2^2)_

This article only works better than the above-mentioned article when the
number of divisors of the number is less.  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


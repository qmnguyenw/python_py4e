Delete odd and even numbers at alternate step such that sum of remaining
elements is minimized



Given an array **arr[]** of **N** elements. At any step, we can delete a
number of a different **parity** from the just previous step, i.e., if, at the
previous step, an odd number was deleted then delete an even number in the
current step or vice versa.  
It is allowed to start by deleting any number. Deletion is possible till we
can delete numbers of different parity at every step. The task is to find the
minimum possible sum of the elements left at the end.

 **Examples:**

> **Input:** arr[] = {1, 5, 7, 8, 2}  
> **Output:** 0  
> Delete elements in the order 1, 2, 5, 8 and finally 7.  
> There are multiple ways of deletion,  
> resulting in the same minimized sum.
>
> **Input:** arr[] = {2, 2, 2, 2}  
> **Output:** 6  
> Delete 2 in first step.  
> Cannot delete any number, since there are no odd numbers left.  
> Hence, the leftover elements sum is 6.

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:** The following ways can be followed to solve the above problem:

  

  

  * Count the number of odd and even elements and store in vectors **v1** and **v2**.
  * Check if the number of odd and even elements are the same or differ by **1** , then we can perform N steps, resulting in leftover sum as 0.
  * If the size differs by more than 1, then only there will be leftover elements.
  * In order to minimize the leftover sum of elements, we select the larger elements first.
  * Hence, the sum of the X smaller elements will be the answer, where X is **v2.size() – v1.size() – 1** or **v1.size() – v2.size() – 1** depending on the count of even and odd elements.

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

// Function to find the minimized sum

int MinimizeleftOverSum(int a[], int n)

{

 vector<int> v1, v2;

 for (int i = 0; i < n; i++) {

 if (a[i] % 2)

 v1.push_back(a[i]);

 else

 v2.push_back(a[i]);

 }

 // If more odd elements

 if (v1.size() > v2.size()) {

 // Sort the elements

 sort(v1.begin(), v1.end());

 sort(v2.begin(), v2.end());

 // Left-over elements

 int x = v1.size() - v2.size() - 1;

 int sum = 0;

 int i = 0;

 // Find the sum of leftover elements

 while (i < x) {

 sum += v1[i++];

 }

 // Return the sum

 return sum;

 }

 // If more even elements

 else if (v2.size() > v1.size()) {

 // Sort the elements

 sort(v1.begin(), v1.end());

 sort(v2.begin(), v2.end());

 // Left-over elements

 int x = v2.size() - v1.size() - 1;

 int sum = 0;

 int i = 0;

 // Find the sum of leftover elements

 while (i < x) {

 sum += v2[i++];

 }

 // Return the sum

 return sum;

 }

 // If same elements

 else

 return 0;

}

// Driver code

int main()

{

 int a[] = { 2, 2, 2, 2 };

 int n = sizeof(a) / sizeof(a[0]);

 cout << MinimizeleftOverSum(a, n);

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

class GFG

{

// Function to find the minimized sum

static int MinimizeleftOverSum(int a[], int n)

{

 Vector<Integer> v1 = new Vector<Integer>(),

 v2 = new Vector<Integer>();

 for (int i = 0; i < n; i++)

 {

 if (a[i] % 2 == 1)

 v1.add(a[i]);

 else

 v2.add(a[i]);

 }

 // If more odd elements

 if (v1.size() > v2.size())

 {

 // Sort the elements

 Collections.sort(v1);

 Collections.sort(v2);

 // Left-over elements

 int x = v1.size() - v2.size() - 1;

 int sum = 0;

 int i = 0;

 // Find the sum of leftover elements

 while (i < x)

 {

 sum += v1.get(i++);

 }

 // Return the sum

 return sum;

 }

 // If more even elements

 else if (v2.size() > v1.size())

 {

 // Sort the elements

 Collections.sort(v1);

 Collections.sort(v2);

 // Left-over elements

 int x = v2.size() - v1.size() - 1;

 int sum = 0;

 int i = 0;

 // Find the sum of leftover elements

 while (i < x)

 {

 sum += v2.get(i++);

 }

 // Return the sum

 return sum;

 }

 // If same elements

 else

 return 0;

}

// Driver code

public static void main(String[] args)

{

 int a[] = { 2, 2, 2, 2 };

 int n = a.length;

 System.out.println(MinimizeleftOverSum(a, n));

}

}

// This code is contributed by Princi Singh  
  
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

# Function to find the minimized sum

def MinimizeleftOverSum(a, n) :

 

 v1, v2 = [], [];

 for i in range(n) :

 

 if (a[i] % 2) :

 v1.append(a[i]);

 else :

 v2.append(a[i]);

 

 # If more odd elements

 if (len(v1) > len(v2)) :

 # Sort the elements

 v1.sort();

 v2.sort();

 # Left-over elements

 x = len(v1) - len(v2) - 1;

 sum = 0;

 i = 0;

 # Find the sum of leftover elements

 while (i < x) :

 sum += v1[i];

 i += 1

 # Return the sum

 return sum;

 

 # If more even elements

 elif (len(v2) > len(v1)) :

 # Sort the elements

 v1.sort();

 v2.sort();

 # Left-over elements

 x = len(v2) - len(v1) - 1;

 sum = 0;

 i = 0;

 # Find the sum of leftover elements

 while (i < x) :

 sum += v2[i];

 i += 1

 

 # Return the sum

 return sum;

 

 # If same elements

 else :

 return 0;

# Driver code

if __name__ == "__main__" :

 a = [ 2, 2, 2, 2 ];

 n = len(a);

 

 print(MinimizeleftOverSum(a, n));

# This code is contributed by Ryuga  
  
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

using System.Collections.Generic;

class GFG

{

// Function to find the minimized sum

static int MinimizeleftOverSum(int []a,

 int n)

{

 List<int> v1 = new List<int>(),

 v2 = new List<int>();

 for (int i = 0; i < n; i++)

 {

 if (a[i] % 2 == 1)

 v1.Add(a[i]);

 else

 v2.Add(a[i]);

 }

 // If more odd elements

 if (v1.Count > v2.Count)

 {

 // Sort the elements

 v1.Sort();

 v2.Sort();

 // Left-over elements

 int x = v1.Count - v2.Count - 1;

 int sum = 0;

 int i = 0;

 // Find the sum of leftover elements

 while (i < x)

 {

 sum += v1[i++];

 }

 // Return the sum

 return sum;

 }

 // If more even elements

 else if (v2.Count > v1.Count)

 {

 // Sort the elements

 v1.Sort();

 v2.Sort();

 // Left-over elements

 int x = v2.Count - v1.Count - 1;

 int sum = 0;

 int i = 0;

 // Find the sum of leftover elements

 while (i < x)

 {

 sum += v2[i++];

 }

 // Return the sum

 return sum;

 }

 // If same elements

 else

 return 0;

}

// Driver code

public static void Main(String[] args)

{

 int []a = { 2, 2, 2, 2 };

 int n = a.Length;

 Console.WriteLine(MinimizeleftOverSum(a, n));

}

}

// This code is contributed by PrinciRaj1992  
  
---  
  
 __

 __

 **Output:**

    
    
    6
    
    
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


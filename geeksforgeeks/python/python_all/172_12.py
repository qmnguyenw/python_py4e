Check if elements of an array can be arranged satisfying the given condition



Given an array **arr** of **N** (even) integer elements. The task is to check
if it is possible to reorder the elements of the array such that:

    
    
    **arr[2*i + 1] = 2 * A[2 * i]** 
    
    for **i = 0 ... N-1**. 
    

Print **True** if it is possible, otherwise print **False**.

 **Examples:**

>  **Input:** arr[] = {4, -2, 2, -4}  
>  **Output:** True  
> {-2, -4, 2, 4} is a valid arrangement, -2 * 2 = -4 and 2 * 2 = 4
>
>  **Input:** arr[] = {1, 2, 4, 16, 8, 4}  
>  **Output:** False
>
>  
>
>
>  
>

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** The idea is that, if **k** is current minimum element in the
array then it must pair with **2 * k** as there does not exist any other
element **k / 2** to pair it with.  
We check elements in ascending order. When we check an element **k** and it
isn’t used, it must pair with **2 * k**. We will attempt to arrange **k**
followed by **2 * k** however if we can’t, then the answer is **False**. In
the end, if all the operations are successful, then print **True**.  
We will store a count of each element to keep track of what we have not yet
considered.

Below is the implementation of above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation of the approach

#include<bits/stdc++.h>

using namespace std;

 

// Function to return true if the elements 

// can be arranged in the desired order

string canReorder(int A[],int n)

{

 map<int,int> m;

 

 for(int i=0;i<n;i++)

 m[A[i]]++;

 

 sort(A,A+n);

 int count = 0;

 

 for(int i=0;i<n;i++)

 {

 if (m[A[i]] == 0)

 continue;

 

 // If 2 * x is not found to pair

 if (m[2 * A[i]]){

 

 count+=2;

 

 // Remove an occurrence of x 

 // and an occurrence of 2 * x

 m[A[i]] -= 1;

 m[2 * A[i]] -= 1;

 }

 }

 if(count ==n)

 return "true";

 else

 return "false";

}

 

 

// Driver Code

int main()

{

int A[] = {4, -2, 2, -4};

int n= sizeof(A)/sizeof(int);

 

// Function call to print required answer

cout<<(canReorder(A,n));

 

return 0;

}

//contributed by Arnab Kundu  
  
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

import java.util.HashMap;

import java.util.Map;

import java.util.Arrays;

 

class GfG

{

 

 // Function to return true if the elements 

 // can be arranged in the desired order 

 static String canReorder(int A[],int n) 

 { 

 HashMap<Integer,Integer> m = new HashMap<>(); 

 

 for(int i = 0; i < n; i++)

 { 

 

 if (m.containsKey(A[i]))

 m.put(A[i], m.get(A[i]) + 1);

 else

 m.put(A[i], 1);

 }

 

 Arrays.sort(A); 

 int count = 0; 

 

 for(int i = 0; i < n; i++) 

 { 

 if (m.get(A[i]) == 0) 

 continue; 

 

 // If 2 * x is not found to pair 

 if (m.containsKey(2 * A[i]))

 { 

 

 count += 2; 

 

 // Remove an occurrence of x 

 // and an occurrence of 2 * x 

 m.put(A[i], m.get(A[i]) - 1); 

 m.put(2 * A[i], m.get(2 * A[i]) - 1); 

 } 

 } 

 

 if(count == n) 

 return "true"; 

 else

 return "false"; 

 } 

 

 // Driver code

 public static void main(String []args)

 {

 

 int A[] = {4, -2, 2, -4}; 

 int n = A.length; 

 

 // Function call to print required answer 

 System.out.println(canReorder(A,n));

 }

}

 

// This code is contributed by Rituraj Jain  
  
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

# Python implementation of the approach

import collections

 

# Function to return true if the elements 

# can be arranged in the desired order

def canReorder(A):

 

 count = collections.Counter(A)

 

 for x in sorted(A, key = abs):

 if count[x] == 0:

 continue

 

 # If 2 * x is not found to pair

 if count[2 * x] == 0:

 return False

 

 # Remove an occurrence of x 

 # and an occurrence of 2 * x

 count[x] -= 1

 count[2 * x] -= 1

 

 return True

 

 

# Driver Code

A = [4, -2, 2, -4]

 

# Function call to print required answer

print(canReorder(A))  
  
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

 

// Function to return true if the elements 

// can be arranged in the desired order 

static String canReorder(int []A,int n) 

{ 

 Dictionary<int, 

 int> m = new Dictionary<int, 

 int>();

 

 for(int i = 0; i < n; i++)

 { 

 if (m.ContainsKey(A[i]))

 m[A[i]]= m[A[i]] + 1;

 else

 m.Add(A[i], 1);

 }

 

 Array.Sort(A); 

 int count = 0; 

 

 for(int i = 0; i < n; i++) 

 { 

 if (m[A[i]] == 0) 

 continue; 

 

 // If 2 * x is not found to pair 

 if (m.ContainsKey(2 * A[i]))

 { 

 count += 2; 

 

 // Remove an occurrence of x 

 // and an occurrence of 2 * x 

 m[A[i]]= m[A[i]] - 1;

 if (m.ContainsKey(2 * A[i]))

 m[2 * A[i]]= m[2 * A[i]] - 1;

 else

 m.Add(2 * A[i], m[2 * A[i]] - 1); 

 } 

 } 

 if(count == n) 

 return "True"; 

 else

 return "False"; 

} 

 

// Driver code

public static void Main(String []args)

{

 int []A = {4, -2, 2, -4}; 

 int n = A.Length; 

 

 // Function call to print required answer 

 Console.WriteLine(canReorder(A,n));

}

}

 

// This code is contributed by Rajput-Ji  
  
---  
  
 __

 __

 **Output:**

    
    
    True
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save


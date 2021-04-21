Count all the permutation of an array



Given an array of integer A[] with no duplicate elements, write a function
that returns the count of all the permutations of an array having no subarray
of [i, i+1] for every i in A[].

 **Examples:**

    
    
    **Input  :** 1 3 9 
    **Output :** 3
    All the permutation of 1 3 9 are : 
    [1, 3, 9], [1, 9, 3], [3, 9, 1], [3, 1, 9], [9, 1, 3], [9, 3, 1]
    Here [1, 3, 9], [9, 1, 3] are removed as they contain subarray 
    [1, 3] from original list and [3, 9, 1] removed as it contains 
    subarray [3, 9] from original list so, 
    Following are the 3 arrays that satisfy the condition : 
    [1, 9, 3], [3, 1, 9], [9, 3, 1]
    
    **Input  :** 1 3 9 12
    **Output :** 11
    

**Naive Solution :** Iterate through list of all permutations and remove those
arrays which contains any subarray **[i, i+1]** from **A[ ]**.

 **Code: Python code for finding out the permutation in the array**

 __

 __  
 __

 __

 __  
 __  
 __

# Python implementation of the approach

from itertools import permutations

 

# Function that returns the count of all the permutation

# having no subarray of [i,i+1]

 

def count(arr):

 z=[]

 perm = permutations(arr)

 

 for i in list(perm):

 z.append(list(i))

 q=[]

 

 for i in range(len(arr)-1):

 x,y=arr[i],arr[i+1]

 

 for j in range(len(z)):

 if z[j].index(x)!=len(z[j])-1:

 if z[j][z[j].index(x)+1]==y:

 q.append(z[j])

 

 for i in range(len(q)):

 if q[i] in z:

 z.remove(q[i])

 return len(z)

 

# Driver Code

A = [1,3, 8, 9]

print(count(A))  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    11

 **Efficient Solution :** Following is a recursive solution based on fact that
length of the array decides the number of all permutations having no subarray
**[i, i+1]** for every i in **A[ ]**

Suppose the length of A[ ] is n, then

    
    
    n        = n-1
    count(0) = 1
    count(1) = 1
    count(n) = n * count(n-1) + (n-1) * count(n-2)

 **Code : Below is the code for implementing the recursive function that
return count of permutations**  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation of the approach

// Recursive function that return count of 

// permutation based on the length of array.

#include <bits/stdc++.h>

using namespace std;

 

int count(int n)

{

 if(n == 0)

 return 1;

 if(n == 1)

 return 1;

 else

 return (n * count(n - 1)) + 

 ((n - 1) * count(n - 2));

}

 

// Driver code

int main()

{

 int A[] = {1, 2, 3, 9};

 

 int len = sizeof(A) / sizeof(A[0]);

 cout << count(len - 1);

}

 

// This code is contributed by 29AjayKumar  
  
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

// Recursive function that return count of 

// permutation based on the length of array.

import java.util.*;

 

class GFG

{

 

static int count(int n)

{

 if(n == 0)

 return 1;

 if(n == 1)

 return 1;

 else

 return (n * count(n - 1)) + 

 ((n - 1) * count(n - 2));

}

 

// Driver Code

static public void main(String[] arg) 

{

 int []A = {1, 2, 3, 9};

 

 System.out.print(count(A.length - 1));

}

}

 

// This code is contributed by PrinciRaj1992  
  
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

# Python implementation of the approach

# Recursive function that return count of 

# permutation based on the length of array.

 

def count(n):

 if n == 0:

 return 1

 if n == 1:

 return 1

 else:

 return (n * count(n-1)) + ((n-1) *
count(n-2))

 

# Driver Code

A = [1, 2, 3, 9]

print(count(len(A)-1))  
  
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

// Recursive function that return count of 

// permutation based on the length of array.

using System;

 

class GFG

{

 

static int count(int n)

{

 if(n == 0)

 return 1;

 if(n == 1)

 return 1;

 else

 return (n * count(n - 1)) + 

 ((n - 1) * count(n - 2));

}

 

// Driver Code

static public void Main(String[] arg) 

{

 int []A = {1, 2, 3, 9};

 

 Console.Write(count(A.Length - 1));

}

}

 

// This code is contributed by Princi Singh  
  
---  
  
 __

 __

 **Output :**

    
    
    11

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


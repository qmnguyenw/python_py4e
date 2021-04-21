Maximum XOR of Two Numbers in an Array



Given an array **Arr** of non-negative integers of size **N**. The task is to
find the maximum possible xor between two numbers present in the array.

 **Example** :

>  **Input:** Arr = {25, 10, 2, 8, 5, 3}  
>  **Output:** 28  
> The maximum result is 5 ^ 25 = 28
>
>  **Input:** Arr = {1, 2, 3, 4, 5, 6, 7}  
>  **Output:** 7  
> The maximum result is 1 ^ 6 = 7

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Naive Approach:** A Simple Solution is to generate all pairs of the given
array and compute XOR of the pairs. Finally, return maximum XOR value. This
solution takes ![O\(N^{2}\)](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-f465572c52dbd36f7bf27071f090f7f6_l3.png) time.

  

  

Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation

#include <bits/stdc++.h>

using namespace std;

 

// Function to return the

// maximum xor

int max_xor(int arr[], int n)

{

 

 int maxXor = 0;

 

 // Calculating xor of each pair

 for (int i = 0; i < n; i++) {

 for (int j = i + 1; j < n; j++) {

 maxXor = max(maxXor,

 arr[i] ^ arr[j]);

 }

 }

 return maxXor;

}

 

// Driver Code

int main()

{

 

 int arr[] = { 25, 10, 2, 8, 5, 3 };

 int n = sizeof(arr) / sizeof(arr[0]);

 

 cout << max_xor(arr, n) << endl;

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

class GFG 

{

 

 // Function to return the

 // maximum xor

 static int max_xor(int arr[], int n) 

 {

 int maxXor = 0;

 

 // Calculating xor of each pair

 for (int i = 0; i < n; i++)

 {

 for (int j = i + 1; j < n; j++) 

 {

 maxXor = Math.max(maxXor,

 arr[i] ^ arr[j]);

 }

 }

 return maxXor;

 }

 

 // Driver Code

 public static void main(String[] args) 

 {

 int arr[] = {25, 10, 2, 8, 5, 3};

 int n = arr.length;

 

 System.out.println(max_xor(arr, n));

 }

} 

 

// This code is contributed by Rajput-Ji  
  
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

# Python3 implementation

 

# Function to return the

# maximum xor

def max_xor(arr, n):

 

 maxXor = 0;

 

 # Calculating xor of each pair

 for i in range(n):

 for j in range(i + 1, n):

 maxXor = max(maxXor,\

 arr[i] ^ arr[j]);

 

 return maxXor;

 

# Driver Code

if __name__ == '__main__':

 

 arr = [ 25, 10, 2, 8, 5, 3 ];

 n = len(arr);

 

 print(max_xor(arr, n));

 

# This code is contributed by 29AjayKumar  
  
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

 

class GFG 

{

 

// Function to return the

// maximum xor

static int max_xor(int []arr, int n) 

{

 int maxXor = 0;

 

 // Calculating xor of each pair

 for (int i = 0; i < n; i++)

 {

 for (int j = i + 1; j < n; j++) 

 {

 maxXor = Math.Max(maxXor,

 arr[i] ^ arr[j]);

 }

 }

 return maxXor;

}

 

// Driver Code

public static void Main() 

{

 int []arr = {25, 10, 2, 8, 5, 3};

 int n = arr.Length;

 

 Console.WriteLine(max_xor(arr, n));

}

}

 

// This code is contributed by AnkitRai01  
  
---  
  
 __

 __

 **Output:**

    
    
    28
    

**Time Complexity:** ![O\(N^{2}\)](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-f465572c52dbd36f7bf27071f090f7f6_l3.png),
where **N** is the size of the array

 **Efficient Approach:** The approach is similar to this article where the
task is to find **maximum AND value pair**.  
So the idea is to change the problem statement from finding maximum xor of two
numbers in an array to -> find two numbers in an array, such that xor of which
equals to a number **X**. In this case, **X** will be the maximum number we
want to achieve till i-th bit.

To find the largest value of an XOR operation, the value of xor should have
every bit to be a set bit i.e 1. In a 32 bit number, the goal is to get the
most 1 set starting left to right.

To evaluate each bit, there is a **mask** needed for that bit. A **mask**
defines which bit should present in the answer and which bit is not. Here we
will use **mask** to keep the prefix for every number ( means by taking the
**ans** with the mask how many bits are remaining from the number ) in the
input till the i-th bit then with the list of possible numbers in our set,
after inserting the number we will evaluate if we can update the max for that
bit position to be 1.  

Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation of the above approach

 

#include <bits/stdc++.h>

using namespace std;

 

// Function to return the

// maximum xor

int max_xor(int arr[], int n)

{

 int maxx = 0, mask = 0;

 

 set<int> se;

 

 for (int i = 30; i >= 0; i--) {

 

 // set the i'th bit in mask

 // like 100000, 110000, 111000..

 mask |= (1 << i);

 

 for (int i = 0; i < n; ++i) {

 

 // Just keep the prefix till

 // i'th bit neglecting all

 // the bit's after i'th bit

 se.insert(arr[i] & mask);

 }

 

 int newMaxx = maxx | (1 << i);

 

 for (int prefix : se) {

 

 // find two pair in set

 // such that a^b = newMaxx

 // which is the highest

 // possible bit can be obtained

 if (se.count(newMaxx ^ prefix)) {

 maxx = newMaxx;

 break;

 }

 }

 

 // clear the set for next

 // iteration

 se.clear();

 }

 

 return maxx;

}

 

// Driver Code

int main()

{

 

 int arr[] = { 25, 10, 2, 8, 5, 3 };

 int n = sizeof(arr) / sizeof(arr[0]);

 

 cout << max_xor(arr, n) << endl;

 

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

// Java implementation of the above approach

import java.util.*;

class GFG

{

 

// Function to return the

// maximum xor

static int max_xor(int arr[], int n)

{

 int maxx = 0, mask = 0;

 

 HashSet<Integer> se = new HashSet<Integer>();

 

 for (int i = 30; i >= 0; i--) 

 {

 

 // set the i'th bit in mask

 // like 100000, 110000, 111000..

 mask |= (1 << i);

 

 for (int j = 0; j < n; ++j) 

 {

 

 // Just keep the prefix till

 // i'th bit neglecting all

 // the bit's after i'th bit

 se.add(arr[j] & mask);

 }

 

 int newMaxx = maxx | (1 << i);

 

 for (int prefix : se)

 {

 

 // find two pair in set

 // such that a^b = newMaxx

 // which is the highest

 // possible bit can be obtained

 if (se.contains(newMaxx ^ prefix))

 {

 maxx = newMaxx;

 break;

 }

 }

 

 // clear the set for next

 // iteration

 se.clear();

 }

 return maxx;

}

 

// Driver Code

public static void main(String[] args)

{

 int arr[] = { 25, 10, 2, 8, 5, 3 };

 int n = arr.length;

 

 System.out.println(max_xor(arr, n));

}

} 

 

// This code is contributed by Rajput-Ji  
  
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

# Python3 implementation of the above approach

 

# Function to return the 

# maximum xor 

def max_xor( arr , n):

 

 maxx = 0

 mask = 0; 

 

 se = set()

 

 for i in range(30, -1, -1):

 

 # set the i'th bit in mask 

 # like 100000, 110000, 111000..

 mask |= (1 << i)

 newMaxx = maxx | (1 << i)

 

 for i in range(n):

 

 # Just keep the prefix till 

 # i'th bit neglecting all 

 # the bit's after i'th bit 

 se.add(arr[i] & mask)

 

 for prefix in se:

 

 # find two pair in set 

 # such that a^b = newMaxx 

 # which is the highest 

 # possible bit can be obtained

 if (newMaxx ^ prefix) in se:

 maxx = newMaxx

 break

 

 # clear the set for next 

 # iteration 

 se.clear()

 return maxx

 

# Driver Code 

arr = [ 25, 10, 2, 8, 5, 3 ]

n = len(arr)

print(max_xor(arr, n)) 

 

# This code is contributed by ANKITKUMAR34  
  
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

// C# implementation of the above approach

using System;

using System.Collections.Generic;

 

class GFG

{

 

// Function to return the

// maximum xor

static int max_xor(int []arr, int n)

{

 int maxx = 0, mask = 0;

 

 HashSet<int> se = new HashSet<int>();

 

 for (int i = 30; i >= 0; i--) 

 {

 

 // set the i'th bit in mask

 // like 100000, 110000, 111000..

 mask |= (1 << i);

 

 for (int j = 0; j < n; ++j) 

 {

 

 // Just keep the prefix till

 // i'th bit neglecting all

 // the bit's after i'th bit

 se.Add(arr[j] & mask);

 }

 

 int newMaxx = maxx | (1 << i);

 

 foreach (int prefix in se)

 {

 

 // find two pair in set

 // such that a^b = newMaxx

 // which is the highest

 // possible bit can be obtained

 if (se.Contains(newMaxx ^ prefix))

 {

 maxx = newMaxx;

 break;

 }

 }

 

 // clear the set for next

 // iteration

 se.Clear();

 }

 return maxx;

}

 

// Driver Code

public static void Main(String[] args)

{

 int []arr = { 25, 10, 2, 8, 5, 3 };

 int n = arr.Length;

 

 Console.WriteLine(max_xor(arr, n));

}

}

 

// This code is contributed by Princi Singh  
  
---  
  
 __

 __

 **Output:**

    
    
    28
    

**Time Complexity:** ![O\(Nlog\(M\)\)](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-bbc32b8c7bff9beab9a48436366203ae_l3.png),
where **N** is the size of the array and **M** is the maximum number present
in the array.

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


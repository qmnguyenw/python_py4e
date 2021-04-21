Minimum number of coins that can generate all the values in the given range



Given an integer **N** , the task is to find the minimum number of coins
required to create all the values in the range **[1, N]**.

 **Examples:**

    
    
    **Input:** N = 5
    **Output:** 3
    The coins {1, 2, 4} can be used to generate 
    all the values in the range [1, 5].
    1 = 1
    2 = 2
    3 = 1 + 2
    4 = 4
    5 = 1 + 4
    
    **Input:** N = 10
    **Output:** 4

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:** The problem is a variation of coin change problem, it can be
solved with the help of binary numbers. In the above example, it can be seen
that to create all the values between **1** to **10** , denominator **{1, 2,
4, 8}** are required which can be rewritten as **{2 0, 21, 22, 23}**. The
minimum number of coins to create all the values for a value **N** can be
computed using the below algorithm.

    
    
    // A list which contains the sum of all previous 
    // bit values including that bit value
    list = [ 1, 3, 7, 15, 31, 63, 127, 255, 511, 1023]
        // range = N
        for value in  list:
            if(value >= N):
                print(list.index(value) + 1)
                break

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

int index(vector<int> vec, int value)

{

 vector<int>::iterator it;

 it = find(vec.begin(), vec.end(), value);

 return (it - vec.begin());

}

// Function to return the count

// of minimum coins required

int findCount(int N)

{

 // To store the required sequence

 vector<int> list;

 int sum = 0;

 int i;

 // Creating list of the sum of all

 // previous bit values including

 // that bit value

 for (i = 0; i < 20; i++) {

 sum += pow(2, i);

 list.push_back(sum);

 }

 for (i = 0; i < 20; i++) {

 if (list[i] >= N) {

 return (index(list, list[i]) + 1);

 }

 }

}

// Driver Code

int main()

{

 int N = 10;

 cout << findCount(N) << endl;

 return 0;

}

// This code is contributed by kanugargng  
  
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

class GFG {

 // Function to return the count

 // of minimum coins required

 static int findCount(int N)

 {

 Vector list = new Vector();

 int sum = 0;

 int i;

 // Creating list of the sum of all

 // previous bit values including

 // that bit value

 for (i = 0; i < 20; i++) {

 sum += Math.pow(2, i);

 list.add(sum);

 }

 for (i = 0; i < 20; i++) {

 if ((int)list.get(i) >= N)

 return (list.indexOf(list.get(i)) + 1);

 }

 return 0;

 }

 // Driver Code

 public static void main(String[] args)

 {

 int N = 10;

 // Function Call to find count

 System.out.println(findCount(N));

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

# Python3 implementation of the approach

# Function to return the count

# of minimum coins required

def findCount(N):

 # To store the required sequence

 list = []

 sum = 0

 # Creating list of the sum of all

 # previous bit values including

 # that bit value

 for i in range(0, 20):

 sum += 2**i

 list.append(sum)

 for value in list:

 if(value >= N):

 return (list.index(value) + 1)

# Driver code

N = 10

print(findCount(N))  
  
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

class GFG {

 // Function to return the count

 // of minimum coins required

 static int findCount(int N)

 {

 List<int> list = new List<int>();

 int sum = 0;

 int i;

 // Creating list of the sum of all

 // previous bit values including

 // that bit value

 for (i = 0; i < 20; i++) {

 sum += (int)Math.Pow(2, i);

 list.Add(sum);

 }

 for (i = 0; i < 20; i++) {

 if ((int)list[i] >= N)

 return (i + 1);

 }

 return 0;

 }

 // Driver Code

 public static void Main(String[] args)

 {

 int N = 10;

 Console.WriteLine(findCount(N));

 }

}

// This code is contributed by PrinciRaj1992  
  
---  
  
 __

 __

 **Output**

  

  

    
    
    4


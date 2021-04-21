Minimum cost to merge numbers from 1 to N



Given an integer **N** , the task is to find the **minimum cost** to merge all
the numbers from **1** to **N** where the cost of merging two set of numbers A
and B is equal to the product of the product of the numbers in the respective
sets.

 **Examples:**

> **Input:** N = 4  
> **Output:** 32  
> Merging {1} and {2} costs 1 * 2 = 2  
> Merging {1, 2} and {3} costs 2 * 3 = 6  
> Merge{1, 2, 3} and {4} costs 6 * 4 = 24  
> Hence, the minimal cost is 2 + 6 + 24 = 32
>
>  **Input:** N = 2  
> **Output:** 2

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:**

  

  

  * The first approach that comes in our mind is sorting. We take first two **smallest** elements and add them, then continue adding to the rest of the elements in the sorted array. But it **fails** when the current running sum exceeds the next smallest value in the array coming next.

    
    
    Take N = 5,
    If we take the sorting approach, then-
    Merge {1} and {2} - 1 * 2 = 2
    Merge {1, 2} and {3} - 2 * 3 = 6
    Merge{1, 2, 3} and {4} - 6 * 4 = 24
    Merge{1, 2, 3, 4} and {5} - 24 * 5 = 120
    Total sum = **152**
    
    
    But optimal way is,
    Merge {1} and {2} - 1 * 2 = 2
    Merge {1, 2} and {3} - 2 * 3 = 6
    Merge {4} and {5} - 4 * 5 = 20
    Merge {1, 2, 3} and {4, 5} - 6 * 20 = 120
    Total sum = **148**
    This is the minimal answer.

  * So, the **correct approach** to solve this problem is the Min-heap based approach. Initially, we push all the numbers from **1** to **N** into the Min-Heap. 
  * At every iteration, we extract the **minimum** and the **second minimum** element from the Min-Heap and insert their product back into it. This ensures that the addition cost generated will be **minimum**. 
  * We keep on repeating the above step until there is only one element remaining in the Min-Heap. The calculated sum till that instant gives us the required answer. 

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to find the Minimum

// cost to merge numbers

// from 1 to N.

#include <bits/stdc++.h>

using namespace std;

// Function returns the

// minimum cost

int GetMinCost(int N)

{

 // Min Heap representation

 priority_queue<int, vector<int>,

 greater<int> > pq;

 // Add all elements to heap

 for (int i = 1; i <= N; i++) {

 pq.push(i);

 }

 

 int cost = 0;

 

 while (pq.size() > 1)

 {

 // First minimum

 int mini = pq.top();

 pq.pop();

 // Second minimum

 int secondmini = pq.top();

 pq.pop();

 // Multiply them

 int current = mini * secondmini;

 // Add to the cost

 cost += current;

 // Push the product into the

 // heap again

 pq.push(current);

 }

 // Return the optimal cost

 return cost;

}

// Driver code

int main()

{

 int N = 5;

 cout << GetMinCost(N);

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

// Java program for the above approach

import java.util.*;

class GFG {

// Function returns the

// minimum cost

static int GetMinCost(int N)

{

 // Min Heap representation

 PriorityQueue<Integer> pq;

 pq = new PriorityQueue<>();

 // Add all elements to heap

 for(int i = 1; i <= N; i++)

 {

 pq.add(i);

 }

 int cost = 0;

 while (pq.size() > 1)

 {

 

 // First minimum

 int mini = pq.remove();

 

 // Second minimum

 int secondmini = pq.remove();

 

 // Multiply them

 int current = mini * secondmini;

 

 // Add to the cost

 cost += current;

 

 // Push the product into the

 // heap again

 pq.add(current);

 }

 

 // Return the optimal cost

 return cost;

}

// Driver Code

public static void main(String args[])

{

 int N = 5;

 // Function call

 System.out.println(GetMinCost(N));

}

}

// This code is contributed by rutvik_56  
  
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

# python3 program to find the Minimum

# cost to merge numbers

# from 1 to N.

# Function returns the

# minimum cost

def GetMinCost(N):

 

 # Min Heap representation

 pq = []

 # Add all elements to heap

 for i in range(1, N+1, 1):

 pq.append(i)

 pq.sort(reverse = False)

 

 cost = 0

 

 while (len(pq) > 1):

 

 # First minimum

 mini = pq[0]

 pq.remove(pq[0])

 # Second minimum

 secondmini = pq[0]

 pq.remove(pq[0])

 # Multiply them

 current = mini * secondmini

 # Add to the cost

 cost += current

 # Push the product into the

 # heap again

 pq.append(current)

 pq.sort(reverse = False)

 # Return the optimal cost

 return cost

# Driver code

if __name__ == '__main__':

 

 N = 5

 print(GetMinCost(N))

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

// C# program to find the Minimum

// cost to merge numbers 

// from 1 to N.

using System;

using System.Collections.Generic;

class GFG{

// Function returns the 

// minimum cost

static int GetMinCost(int N)

{

 

 // Min Heap representation

 List<int> pq = new List<int>();

 

 // Add all elements to heap

 for(int i = 1; i <= N; i++)

 {

 pq.Add(i);

 }

 

 int cost = 0;

 pq.Sort();

 

 while (pq.Count > 1)

 {

 

 // First minimum

 int mini = pq[0];

 pq.RemoveAt(0);

 

 // Second minimum

 int secondmini = pq[0];

 pq.RemoveAt(0);

 

 // Multiply them

 int current = mini * secondmini;

 

 // Add to the cost

 cost += current;

 

 // Push the product into the

 // heap again

 pq.Add(current);

 pq.Sort();

 }

 

 // Return the optimal cost

 return cost;

}

// Driver code

static void Main()

{

 int N = 5;

 

 Console.WriteLine(GetMinCost(N));

}

}

// This code is contributed by divyeshrabadiya07  
  
---  
  
 __

 __

 **Output:**

    
    
    148

**Time Complexity:** _O(NlogN)_  
**Auxiliary Space:** _O(N)_  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


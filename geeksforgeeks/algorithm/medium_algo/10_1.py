Check if it is possible to reach a number by making jumps of two given length



Given a starting position ‘k’ and two jump sizes ‘d1’ and ‘d2’, our task is to
find the minimum number of jumps needed to reach ‘x’ if it is possible.

At any position P, we are allowed to jump to positions :

  *  **P + d1** and **P – d1**
  *  **P + d2** and **P – d2**

 **Examples:**

    
    
    **Input** : k = 10, d1 = 4, d2 = 6 and x = 8 
    **Output** : 2
    1st step 10 + d1 = 14
    2nd step 14 - d2 = 8
    
    **Input** : k = 10, d1 = 4, d2 = 6 and x = 9
    **Output** : -1
    -1 indicates it is not possible to reach x.
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

In the previous article we discussed a strategy to check whether a list of
numbers is reachable by K by making jump of two given lengths.

Here, instead of a list of numbers, we are given a single integer **x** and if
it is reachable from **k** then the task is to find the minimum number of
steps or jumps needed.

  

  

We will solve this using **Breadth first Search** :  
 **Approach** :

  * Check if ‘x’ is reachable from **k**. The number **x** is reachable from k if it satisfies **(x – k) % gcd(d1, d2) = 0**.
  * If x is reachable :
    1. Maintain a hash table to store the already visited positions.
    2. Apply bfs algorithm starting from the position k.
    3. If you reach position P in ‘stp’ steps, you can reach p+d1 position in ‘stp+1’ steps.
    4. If position P is the required position ‘x’ then steps taken to reach P is the answer

The image below depicts how the algorithm finds out number of steps needed to
reach x = 8 with k = 10, d1 = 4 and d2 = 6.  
![Algo Example](https://docs.google.com/drawings/d/e/2PACX-1vQNc-
ChldajMUiKj_gyuUb4IrdhU7cCl-CLDSnA_slb_nU47DBOWqvE-
ME35jMpaU6-vF4Jj1abOrrH/pub?w=1440&h=1080)

Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

#include<bits/stdc++.h>

using namespace std;

 

// Function to perform BFS traversal to

// find minimum number of step needed

// to reach x from K

int minStepsNeeded(int k, int d1, int d2, int x)

{

 // Calculate GCD of d1 and d2

 int gcd = __gcd(d1, d2);

 

 // If position is not reachable

 // return -1

 if ((k - x) % gcd != 0)

 return -1;

 

 // Queue for BFS

 queue<pair<int, int> > q;

 

 // Hash Table for marking

 // visited positions

 unordered_set<int> visited;

 

 // we need 0 steps to reach K

 q.push({ k, 0 });

 

 // Mark starting position

 // as visited

 visited.insert(k);

 

 while (!q.empty()) {

 

 int s = q.front().first;

 

 // stp is the number of steps

 // to reach position s

 int stp = q.front().second;

 

 if (s == x)

 return stp;

 

 q.pop();

 

 if (visited.find(s + d1) == visited.end()) {

 

 // if position not visited

 // add to queue and mark visited

 q.push({ s + d1, stp + 1 });

 

 visited.insert(s + d1);

 }

 

 if (visited.find(s + d2) == visited.end()) {

 q.push({ s + d2, stp + 1 });

 visited.insert(s + d2);

 }

 

 if (visited.find(s - d1) == visited.end()) {

 q.push({ s - d1, stp + 1 });

 visited.insert(s - d1);

 }

 if (visited.find(s - d2) == visited.end()) {

 q.push({ s - d2, stp + 1 });

 visited.insert(s - d2);

 }

 }

}

 

// Driver Code

int main()

{

 int k = 10, d1 = 4, d2 = 6, x = 8;

 

 cout << minStepsNeeded(k, d1, d2, x);

 

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

static class pair

{ 

 int first, second; 

 public pair(int first, int second) 

 { 

 this.first = first; 

 this.second = second; 

 } 

} 

static int __gcd(int a, int b) 

{ 

 if (b == 0) 

 return a; 

 return __gcd(b, a % b); 

 

}

// Function to perform BFS traversal to

// find minimum number of step needed

// to reach x from K

static int minStepsNeeded(int k, int d1, 

 int d2, int x)

{

 // Calculate GCD of d1 and d2

 int gcd = __gcd(d1, d2);

 

 // If position is not reachable

 // return -1

 if ((k - x) % gcd != 0)

 return -1;

 

 // Queue for BFS

 Queue<pair> q = new LinkedList<>();

 

 // Hash Table for marking

 // visited positions

 HashSet<Integer> visited = new HashSet<>();

 

 // we need 0 steps to reach K

 q.add(new pair(k, 0 ));

 

 // Mark starting position

 // as visited

 visited.add(k);

 

 while (!q.isEmpty()) 

 {

 int s = q.peek().first;

 

 // stp is the number of steps

 // to reach position s

 int stp = q.peek().second;

 

 if (s == x)

 return stp;

 

 q.remove();

 

 if (!visited.contains(s + d1)) 

 {

 

 // if position not visited

 // add to queue and mark visited

 q.add(new pair(s + d1, stp + 1));

 

 visited.add(s + d1);

 }

 

 if (visited.contains(s + d2)) 

 {

 q.add(new pair(s + d2, stp + 1));

 visited.add(s + d2);

 }

 

 if (!visited.contains(s - d1))

 {

 q.add(new pair(s - d1, stp + 1));

 visited.add(s - d1);

 }

 if (!visited.contains(s - d2)) 

 {

 q.add(new pair(s - d2, stp + 1));

 visited.add(s - d2);

 }

 }

 return Integer.MIN_VALUE;

}

 

// Driver Code

public static void main(String[] args)

{

 int k = 10, d1 = 4, d2 = 6, x = 8;

 

 System.out.println(minStepsNeeded(k, d1, d2, x));

}

}

 

// This code is contributed by 29AjayKumar  
  
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

from math import gcd as __gcd

from collections import deque as queue

 

# Function to perform BFS traversal to

# find minimum number of step needed

# to reach x from K

def minStepsNeeded(k, d1, d2, x):

 

 # Calculate GCD of d1 and d2

 gcd = __gcd(d1, d2)

 

 # If position is not reachable

 # return -1

 if ((k - x) % gcd != 0):

 return -1

 

 # Queue for BFS

 q = queue()

 

 # Hash Table for marking

 # visited positions

 visited = dict()

 

 # we need 0 steps to reach K

 q.appendleft([k, 0])

 

 # Mark starting position

 # as visited

 visited[k] = 1

 

 while (len(q) > 0):

 

 sr = q.pop()

 s, stp = sr[0], sr[1]

 

 # stp is the number of steps

 # to reach position s

 if (s == x):

 return stp

 

 if (s + d1 not in visited):

 

 # if position not visited

 # add to queue and mark visited

 q.appendleft([(s + d1), stp + 1])

 

 visited[(s + d1)] = 1

 

 if (s + d2 not in visited):

 q.appendleft([(s + d2), stp + 1])

 visited[(s + d2)] = 1

 

 if (s - d1 not in visited):

 q.appendleft([(s - d1), stp + 1])

 visited[(s - d1)] = 1

 

 if (s - d2 not in visited):

 q.appendleft([(s - d2), stp + 1])

 visited[(s - d2)] = 1

 

# Driver Code

k = 10

d1 = 4

d2 = 6

x = 8

 

print(minStepsNeeded(k, d1, d2, x))

 

# This code is contributed by Mohit Kumar  
  
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

public class pair

{ 

 public int first, second; 

 public pair(int first, int second) 

 { 

 this.first = first; 

 this.second = second; 

 } 

} 

 

static int __gcd(int a, int b) 

{ 

 if (b == 0) 

 return a; 

 return __gcd(b, a % b); 

 

}

 

// Function to perform BFS traversal to

// find minimum number of step needed

// to reach x from K

static int minStepsNeeded(int k, int d1, 

 int d2, int x)

{

 // Calculate GCD of d1 and d2

 int gcd = __gcd(d1, d2);

 

 // If position is not reachable

 // return -1

 if ((k - x) % gcd != 0)

 return -1;

 

 // Queue for BFS

 Queue<pair> q = new Queue<pair>();

 

 // Hash Table for marking

 // visited positions

 HashSet<int> visited = new HashSet<int>();

 

 // we need 0 steps to reach K

 q.Enqueue(new pair(k, 0));

 

 // Mark starting position

 // as visited

 visited.Add(k);

 

 while (q.Count != 0) 

 {

 int s = q.Peek().first;

 

 // stp is the number of steps

 // to reach position s

 int stp = q.Peek().second;

 

 if (s == x)

 return stp;

 

 q.Dequeue();

 

 if (!visited.Contains(s + d1)) 

 {

 

 // if position not visited

 // add to queue and mark visited

 q.Enqueue(new pair(s + d1, stp + 1));

 

 visited.Add(s + d1);

 }

 

 if (!visited.Contains(s + d2)) 

 {

 q.Enqueue(new pair(s + d2, stp + 1));

 visited.Add(s + d2);

 }

 

 if (!visited.Contains(s - d1))

 {

 q.Enqueue(new pair(s - d1, stp + 1));

 visited.Add(s - d1);

 }

 if (!visited.Contains(s - d2)) 

 {

 q.Enqueue(new pair(s - d2, stp + 1));

 visited.Add(s - d2);

 }

 }

 return int.MinValue;

}

 

// Driver Code

public static void Main(String[] args)

{

 int k = 10, d1 = 4, d2 = 6, x = 8;

 

 Console.WriteLine(minStepsNeeded(k, d1, d2, x));

}

}

 

// This code is contributed by PrinciRaj1992  
  
---  
  
 __

 __

 **Output:**

    
    
    2
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


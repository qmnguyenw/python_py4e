Count of all prime weight nodes between given nodes in the given Tree



Given a **weighted tree** containing **N** nodes, and two nodes **u** and
**v** , the task is to find the count of nodes having **prime weight** on the
simple path between **u and v (both inclusive)**.

 **Examples:**

>  **Input:**  
>
>
> ![](https://media.geeksforgeeks.org/wp-
> content/uploads/20190420095306/Untitled85.png)
>
> u = 3, v = 5  
> **Output:** 2  
> **Explanation:**  
> Prime weight on path 3 to 5 is [11, 5]. Hence the answer is 2.  
>
>
>  
>
>
>  
>

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:** To solve the problem mentioned above, the idea is to use the
basic concept when we find the LCA of two nodes.

  * Precompute all the prime numbers till MAX using the Sieve method to check if a number is prime or not in O(1)
  * Given two nodes u and v, we will make both nodes at the same level, by moving the greater level node move upwards. As we move up we will also check if the weight is prime or not.
  * If **v == u** then we will simply check the weight of the current node and return the count.
  * If **v is not equal to u** then we will move **both u and v upward by 1** till they are not the same.
  * Now we will finally check the weight of the first ancestor of u or v and return the count.

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program Count prime weight

// nodes between two nodes in the given tree

#include <bits/stdc++.h>

using namespace std;

#define MAX 1000

int weight[MAX];

int level[MAX];

int par[MAX];

bool prime[MAX + 1];

vector<int> graph[MAX];

// Function to perform

// Sieve Of Eratosthenes for prime number

void SieveOfEratosthenes()

{

 // Initialize all entries of prime it as true

 // A value in prime[i] will finally be false

 // if i is Not a prime, else true.

 memset(prime, true, sizeof(prime));

 for (int p = 2; p * p <= MAX; p++) {

 // Check if prime[p] is not changed,

 // then it is a prime

 if (prime[p] == true) {

 // Update all multiples

 // of p greater than or

 // equal to the square of it

 // numbers which are multiple

 // of p and are less than p^2

 // are already been marked.

 for (int i = p * p; i <= MAX; i += p)

 prime[i] = false;

 }

 }

}

// Function to perform dfs

void dfs(int node, int parent, int h)

{

 // Stores parent of each node

 par[node] = parent;

 // Stores level of each node from root

 level[node] = h;

 for (int child : graph[node]) {

 if (child == parent)

 continue;

 dfs(child, node, h + 1);

 }

}

// Function to perform prime

// number between the path

int findPrimeOnPath(int u, int v)

{

 int count = 0;

 // The node which is present farthest

 // from the root node is taken as v

 // If u is farther from root node

 // then swap the two

 if (level[u] > level[v])

 swap(u, v);

 int d = level[v] - level[u];

 // Find the ancestor of v

 // which is at same level as u

 while (d--) {

 // If Weight is prime

 // increment count

 if (prime[weight[v]])

 count++;

 v = par[v];

 }

 // If u is the ancestor of v

 // then u is the LCA of u and v

 // Now check if weigh[v]

 // is prime or not

 if (v == u) {

 if (prime[weight[v]])

 count++;

 return count;

 }

 // When v and u are on the same level but

 // are in different subtree. Now move both

 // u and v up by 1 till they are not same

 while (v != u) {

 if (prime[weight[v]])

 count++;

 if (prime[weight[u]])

 count++;

 u = par[u];

 v = par[v];

 }

 // If weight of first ancestor

 // is prime

 if (prime[weight[v]])

 count++;

 return count;

}

// Driver code

int main()

{

 // Precompute all the prime

 // numbers till MAX

 SieveOfEratosthenes();

 // Weights of the node

 weight[1] = 5;

 weight[2] = 10;

 weight[3] = 11;

 weight[4] = 8;

 weight[5] = 6;

 // Edges of the tree

 graph[1].push_back(2);

 graph[2].push_back(3);

 graph[2].push_back(4);

 graph[1].push_back(5);

 dfs(1, -1, 0);

 int u = 3, v = 5;

 cout << findPrimeOnPath(u, v)

 << endl;

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

// Java program to count

// prime weight nodes

// between two nodes

// in the given tree

import java.util.*;

class GFG{

 

static final int MAX = 1000;

static int []weight =

 new int[MAX];

static int []level =

 new int[MAX];

static int []par =

 new int[MAX];

static boolean []prime =

 new boolean[MAX + 1];

static Vector<Integer>[] graph =

 new Vector[MAX]; 

// Function to perform

// Sieve Of Eratosthenes

// for prime number

static void SieveOfEratosthenes()

{

 // Initialize all entries of

 // prime it as true a value in

 // prime[i] will finally be false

 // if i is Not a prime, else true.

 for (int i = 0;

 i < prime.length; i++)

 prime[i] = true;

 for (int p = 2;

 p * p <= MAX; p++)

 {

 // Check if prime[p]

 // is not changed,

 // then it is a prime

 if (prime[p] == true)

 {

 // Update all multiples

 // of p greater than or

 // equal to the square of it

 // numbers which are multiple

 // of p and are less than p^2

 // are already been marked.

 for (int i = p * p;

 i <= MAX; i += p)

 prime[i] = false;

 }

 }

}

// Function to perform dfs

static void dfs(int node,

 int parent, int h)

{

 // Stores parent of each node

 par[node] = parent;

 // Stores level of each

 // node from root

 level[node] = h;

 for (int child : graph[node])

 {

 if (child == parent)

 continue;

 dfs(child, node, h + 1);

 }

}

// Function to perform prime

// number between the path

static int findPrimeOnPath(int u,

 int v)

{

 int count = 0;

 // The node which is present

 // farthest from the root

 // node is taken as v

 // If u is farther from

 // root node then swap the two

 if (level[u] > level[v])

 {

 int temp = v;

 v = u;

 u = temp;

 }

 int d = level[v] - level[u];

 // Find the ancestor of v

 // which is at same level as u

 while (d-- > 0)

 {

 // If Weight is prime

 // increment count

 if (prime[weight[v]])

 count++;

 v = par[v];

 }

 // If u is the ancestor of v

 // then u is the LCA of u and v

 // Now check if weigh[v]

 // is prime or not

 if (v == u)

 {

 if (prime[weight[v]])

 count++; 

 return count;

 }

 // When v and u are on the

 // same level but are in

 // different subtree. Now

 // move both u and v up by

 // 1 till they are not same

 while (v != u)

 {

 if (prime[weight[v]])

 count++;

 if (prime[weight[u]])

 count++;

 u = par[u];

 v = par[v];

 }

 

 // If weight of first

 // ancestor is prime

 if (prime[weight[v]])

 count++;

 return count;

}

// Driver code

public static void main(String[] args)

{

 for (int i = 0; i < graph.length; i++)

 graph[i] = new Vector<Integer>();

 

 // Precompute all the prime

 // numbers till MAX

 SieveOfEratosthenes();

 // Weights of the node

 weight[1] = 5;

 weight[2] = 10;

 weight[3] = 11;

 weight[4] = 8;

 weight[5] = 6;

 // Edges of the tree

 graph[1].add(2);

 graph[2].add(3);

 graph[2].add(4);

 graph[1].add(5);

 dfs(1, -1, 0);

 int u = 3, v = 5;

 System.out.print(findPrimeOnPath(u, v));

}

}

// This code is contributed by shikhasingrajput  
  
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

# Python3 program count prime weight

# nodes between two nodes in the given tree

MAX = 1000

weight = [0 for i in range(MAX)]

level = [0 for i in range(MAX)]

par = [0 for i in range(MAX)]

prime = [True for i in range(MAX + 1)]

graph = [[] for i in range(MAX)]

# Function to perform

# Sieve Of Eratosthenes

# for prime number

def SieveOfEratosthenes():

 

 # Initialize all entries of prime it

 # as true. A value in prime[i] will

 # finally be false if i is Not a prime,

 # else true. memset(prime, true,

 # sizeof(prime))

 for p in range(2, MAX + 1):

 if p * p > MAX + 1:

 break

 # Check if prime[p] is not changed,

 # then it is a prime

 if (prime[p] == True):

 

 # Update all multiples

 # of p greater than or

 # equal to the square of it

 # numbers which are multiple

 # of p and are less than p^2

 # are already been marked.

 for i in range(p * p, MAX + 1, p):

 prime[i] = False

# Function to perform dfs

def dfs(node, parent, h):

 

 # Stores parent of each node

 par[node] = parent

 # Stores level of each node from root

 level[node] = h

 for child in graph[node]:

 if (child == parent):

 continue

 

 dfs(child, node, h + 1)

# Function to perform prime

# number between the path

def findPrimeOnPath(u, v):

 

 count = 0

 # The node which is present farthest

 # from the root node is taken as v

 # If u is farther from root node

 # then swap the two

 if (level[u] > level[v]):

 u, v = v, u

 d = level[v] - level[u]

 # Find the ancestor of v

 # which is at same level as u

 while (d):

 

 # If Weight is prime

 # increment count

 if (prime[weight[v]]):

 count += 1

 v = par[v]

 d -= 1

 # If u is the ancestor of v

 # then u is the LCA of u and v

 # Now check if weigh[v]

 # is prime or not

 if (v == u):

 if (prime[weight[v]]):

 count += 1

 

 return count

 # When v and u are on the same level but

 # are in different subtree. Now move both

 # u and v up by 1 till they are not same

 while (v != u):

 if (prime[weight[v]]):

 count += 1

 if (prime[weight[u]]):

 count += 1

 u = par[u]

 v = par[v]

 

 # If weight of first ancestor

 # is prime

 if (prime[weight[v]]):

 count += 1

 return count

# Driver code

if __name__ == '__main__':

 

 # Precompute all the prime

 # numbers till MAX

 SieveOfEratosthenes()

 # Weights of the node

 weight[1] = 5

 weight[2] = 10

 weight[3] = 11

 weight[4] = 8

 weight[5] = 6

 # Edges of the tree

 graph[1].append(2)

 graph[2].append(3)

 graph[2].append(4)

 graph[1].append(5)

 dfs(1, -1, 0)

 u = 3

 v = 5

 

 print(findPrimeOnPath(u, v))

 

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

// C# program to count prime weight

// nodes between two nodes in the

// given tree

using System;

using System.Collections.Generic;

class GFG{

 

static readonly int MAX = 1000;

static int []weight = new int[MAX];

static int []level = new int[MAX];

static int []par = new int[MAX];

static bool []prime = new bool[MAX + 1];

static List<int>[] graph = new List<int>[MAX]; 

// Function to perform

// Sieve Of Eratosthenes

// for prime number

static void SieveOfEratosthenes()

{

 

 // Initialize all entries of

 // prime it as true a value in

 // prime[i] will finally be false

 // if i is Not a prime, else true.

 for(int i = 0;

 i < prime.Length; i++)

 prime[i] = true;

 for(int p = 2;

 p * p <= MAX; p++)

 {

 

 // Check if prime[p]

 // is not changed,

 // then it is a prime

 if (prime[p] == true)

 {

 

 // Update all multiples

 // of p greater than or

 // equal to the square of it

 // numbers which are multiple

 // of p and are less than p^2

 // are already been marked.

 for(int i = p * p;

 i <= MAX; i += p)

 prime[i] = false;

 }

 }

}

// Function to perform dfs

static void dfs(int node, int parent,

 int h)

{

 

 // Stores parent of each node

 par[node] = parent;

 // Stores level of each

 // node from root

 level[node] = h;

 foreach(int child in graph[node])

 {

 if (child == parent)

 continue;

 

 dfs(child, node, h + 1);

 }

}

// Function to perform prime

// number between the path

static int findPrimeOnPath(int u,

 int v)

{

 int count = 0;

 // The node which is present

 // farthest from the root

 // node is taken as v

 // If u is farther from

 // root node then swap the two

 if (level[u] > level[v])

 {

 int temp = v;

 v = u;

 u = temp;

 }

 int d = level[v] - level[u];

 // Find the ancestor of v

 // which is at same level as u

 while (d-- > 0)

 {

 

 // If Weight is prime

 // increment count

 if (prime[weight[v]])

 count++;

 

 v = par[v];

 }

 // If u is the ancestor of v

 // then u is the LCA of u and v

 // Now check if weigh[v]

 // is prime or not

 if (v == u)

 {

 if (prime[weight[v]])

 count++; 

 

 return count;

 }

 // When v and u are on the

 // same level but are in

 // different subtree. Now

 // move both u and v up by

 // 1 till they are not same

 while (v != u)

 {

 if (prime[weight[v]])

 count++;

 if (prime[weight[u]])

 count++;

 u = par[u];

 v = par[v];

 }

 

 // If weight of first

 // ancestor is prime

 if (prime[weight[v]])

 count++;

 

 return count;

}

// Driver code

public static void Main(String[] args)

{

 for(int i = 0; i < graph.Length; i++)

 graph[i] = new List<int>();

 

 // Precompute all the prime

 // numbers till MAX

 SieveOfEratosthenes();

 // Weights of the node

 weight[1] = 5;

 weight[2] = 10;

 weight[3] = 11;

 weight[4] = 8;

 weight[5] = 6;

 // Edges of the tree

 graph[1].Add(2);

 graph[2].Add(3);

 graph[2].Add(4);

 graph[1].Add(5);

 dfs(1, -1, 0);

 int u = 3, v = 5;

 

 Console.Write(findPrimeOnPath(u, v));

}

}

// This code is contributed by Amit Katiyar  
  
---  
  
 __

 __

 **Output:**

    
    
    2
    
    
    
    
    
    
    
    
    
    
    
    

**_Complexity Analysis:_**

  * **Time Complexity:** O(N).   
In dfs, every node of the tree is processed once, and hence the complexity due
to the dfs is O(N) if there are total N nodes in the tree. Also, for
processing each node the SieveOfEratosthenes() function is used which has a
complexity of O(sqrt(N)) too but since this function is executed only once, it
does not affect the overall time complexity. Therefore, the time complexity is
O(N).

  *  **Auxiliary Space:** O(N).   
Extra space is used for the prime array, so the space complexity is O(N).

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


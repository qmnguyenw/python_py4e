Count the nodes of the tree which make a pangram when concatenated with the
sub-tree nodes



Given a tree, and the weights (in the form of strings) of all the nodes, the
task is to count the nodes whose weighted string when concatenated with the
strings of the sub-tree nodes becomes a pangram.  
**Pangram:** A pangram is a sentence containing every letter of the English
Alphabet.

 **Examples:**  

> **Input:**  
>
>
> ![](https://media.geeksforgeeks.org/wp-
> content/uploads/20190521144717/anagrams.png)
>
> **Output:** 1  
> Only the weighted string of sub-tree of node 1 makes the pangram.
>
>  
>
>
>  
>

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:** Perform dfs on the tree and update the weight of every node
such that it stores its weight concatenated with the weights of the sub-tree
nodes. Then, count the nodes whose updated weighted string forms a pangram.

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

vector<int> graph[100];

vector<string> weight(100);

// Function that returns if the

// string x is a pangram

bool Pangram(string x)

{

 map<char, int> mp;

 int n = x.size();

 for (int i = 0; i < n; i++)

 mp[x[i]]++;

 if (mp.size() == 26)

 return true;

 else

 return false;

}

// Function to return the count of nodes

// which make pangram with the

// sub-tree nodes

int countTotalPangram(int n)

{

 int cnt = 0;

 for (int i = 1; i <= n; i++)

 if (Pangram(weight[i]))

 cnt++;

 return cnt;

}

// Function to perform dfs and update the nodes

// such that weight[i] will store the weight[i]

// concatenated with the weights of

// all the nodes in the sub-tree

void dfs(int node, int parent)

{

 for (int to : graph[node]) {

 if (to == parent)

 continue;

 dfs(to, node);

 weight[node] += weight[to];

 }

}

// Driver code

int main()

{

 int n = 6;

 // Weights of the nodes

 weight[1] = "abcde";

 weight[2] = "fghijkl";

 weight[3] = "abcdefg";

 weight[4] = "mnopqr";

 weight[5] = "stuvwxy";

 weight[6] = "zabcdef";

 // Edges of the tree

 graph[1].push_back(2);

 graph[2].push_back(3);

 graph[2].push_back(4);

 graph[1].push_back(5);

 graph[5].push_back(6);

 dfs(1, 1);

 cout << countTotalPangram(n);

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

class GFG{

 

@SuppressWarnings("unchecked")

static Vector<Integer> []graph = new Vector[100];

static String []weight = new String[100];

// Function that returns if the

// String x is a pangram

static boolean Pangram(String x)

{

 HashMap<Character, Integer> mp = new HashMap<>();

 int n = x.length();

 for(int i = 0 ; i < n; i++)

 {

 if (mp.containsKey(x.charAt(i)))

 {

 mp.put(x.charAt(i),

 mp.get(x.charAt(i)) + 1);

 }

 else

 {

 mp.put(x.charAt(i), 1);

 }

 }

 if (mp.size() == 26)

 return true;

 else

 return false;

}

// Function to return the count of nodes

// which make pangram with the

// sub-tree nodes

static int countTotalPangram(int n)

{

 int cnt = 0;

 for(int i = 1; i <= n; i++)

 if (Pangram(weight[i]))

 cnt++;

 

 return cnt;

}

// Function to perform dfs and update the nodes

// such that weight[i] will store the weight[i]

// concatenated with the weights of

// all the nodes in the sub-tree

static void dfs(int node, int parent)

{

 for(int to : graph[node])

 {

 if (to == parent)

 continue;

 

 dfs(to, node);

 weight[node] += weight[to];

 }

}

// Driver code

public static void main(String[] args)

{

 int n = 6;

 // Weights of the nodes

 weight[1] = "abcde";

 weight[2] = "fghijkl";

 weight[3] = "abcdefg";

 weight[4] = "mnopqr";

 weight[5] = "stuvwxy";

 weight[6] = "zabcdef";

 for(int i = 0; i < graph.length; i++)

 graph[i] = new Vector<Integer>();

 

 // Edges of the tree

 graph[1].add(2);

 graph[2].add(3);

 graph[2].add(4);

 graph[1].add(5);

 graph[5].add(6);

 dfs(1, 1);

 System.out.print(countTotalPangram(n));

}

}

// This code is contributed by Amit Katiyar  
  
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

graph = [[] for i in range(100)]

weight = [0] * 100

# Function that returns if the

# string x is a pangram

def Pangram(x):

 mp = {}

 n = len(x)

 for i in range(n):

 if x[i] not in mp:

 mp[x[i]] = 0

 mp[x[i]] += 1

 if (len(mp)== 26):

 return True

 else:

 return False

# Function to return the count of nodes

# which make pangram with the

# sub-tree nodes

def countTotalPangram(n):

 cnt = 0

 for i in range(1, n + 1):

 if (Pangram(weight[i])):

 cnt += 1

 return cnt

# Function to perform dfs and update the nodes

# such that weight[i] will store the weight[i]

# concatenated with the weights of

# all the nodes in the sub-tree

def dfs(node, parent):

 for to in graph[node]:

 if (to == parent):

 continue

 dfs(to, node)

 weight[node] += weight[to]

# Driver code

n = 6

# Weights of the nodes

weight[1] = "abcde"

weight[2] = "fghijkl"

weight[3] = "abcdefg"

weight[4] = "mnopqr"

weight[5] = "stuvwxy"

weight[6] = "zabcdef"

# Edges of the tree

graph[1].append(2)

graph[2].append(3)

graph[2].append(4)

graph[1].append(5)

graph[5].append(6)

dfs(1, 1)

print(countTotalPangram(n))

# This code is contributed by SHUBHAMSINGH10  
  
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

// C# implementation of

// the above approach

using System;

using System.Collections.Generic;

class GFG{ 

static List<int> []graph =

 new List<int>[100];

static String []weight =

 new String[100];

// Function that returns if the

// String x is a pangram

static bool Pangram(String x)

{

 Dictionary<char,

 int> mp = new Dictionary<char,

 int>();

 int n = x.Length;

 for(int i = 0 ; i < n; i++)

 {

 if (mp.ContainsKey(x[i]))

 {

 mp[x[i]] = mp[x[i]] + 1;

 }

 else

 {

 mp.Add(x[i], 1);

 }

 }

 if (mp.Count == 26)

 return true;

 else

 return false;

}

// Function to return the

// count of nodes which

// make pangram with the

// sub-tree nodes

static int countTotalPangram(int n)

{

 int cnt = 0;

 for(int i = 1; i <= n; i++)

 if (Pangram(weight[i]))

 cnt++;

 return cnt;

}

// Function to perform dfs and

// update the nodes such that

// weight[i] will store the weight[i]

// concatenated with the weights of

// all the nodes in the sub-tree

static void dfs(int node, int parent)

{

 foreach(int to in graph[node])

 {

 if (to == parent)

 continue;

 dfs(to, node);

 weight[node] += weight[to];

 }

}

// Driver code

public static void Main(String[] args)

{

 int n = 6;

 // Weights of the nodes

 weight[1] = "abcde";

 weight[2] = "fghijkl";

 weight[3] = "abcdefg";

 weight[4] = "mnopqr";

 weight[5] = "stuvwxy";

 weight[6] = "zabcdef";

 for(int i = 0;

 i < graph.Length; i++)

 graph[i] = new List<int>();

 // Edges of the tree

 graph[1].Add(2);

 graph[2].Add(3);

 graph[2].Add(4);

 graph[1].Add(5);

 graph[5].Add(6);

 dfs(1, 1);

 Console.Write(countTotalPangram(n));

}

}

// This code is contributed by shikhasingrajput  
  
---  
  
 __

 __

 **Output:**

    
    
    1
    
    
    
    
    
    

**_Complexity Analysis:_**

  * **Time Complexity:** O(N*S).   
In dfs, every node of the tree is processed once, and hence the complexity due
to the dfs is O(N) if there are total N nodes in the tree. Also, for
processing each node the Pangram() function is used for every node which has a
complexity of O(S) where S is the sum of the length of all weight strings in a
subtree and since this is done for every node, the overall time complexity for
this part becomes O(N*S). Therefore, the final time complexity is O(N*S).

  *  **Auxiliary Space:** O(1).   
Any extra space is not required, so the space complexity is constant.

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


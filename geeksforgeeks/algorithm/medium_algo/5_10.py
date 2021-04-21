Minimum cost to traverse from one index to another in the String



Given a string **S** of length **N** consisting of lower case character, the
task is to find the minimum cost to reach from index **i** to index **j**.  
At any index **k** , the cost to jump to the index **k+1** and **k-1**
(without going out of bounds) is 1.  
Additionally, the cost to jump to any index **m** such that **S[m] = S[k]** is
0.

 **Examples:**

>  **Input :** S = “abcde”, i = 0, j = 4  
>  **Output :** 4  
>  **Explanation:**  
>  The shortest path will be:  
> 0->1->2->3->4  
> Thus, the answer will be 4.
>
>  **Input :** S = “abcdefb”, i = 0, j = 5  
>  **Output :** 2  
>  **Explanation:**  
>  0->1->6->5  
> 0->1 edge weight is 1, 1->6 edge weight is 0, and 6->5 edge weight is 1.  
> Thus, the answer will be 2

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:**

  

  

  1. One approach to solve this problem is 0-1 BFS.
  2. The setup can be visualized as a graph with **N** nodes.
  3. All the nodes will be connected to adjacent nodes with an edge of weight of ‘1’ and nodes with the same characters with an edge with weight ‘0’.
  4. In this setup, 0-1 BFS can be run to find the shortest path from index ‘i’ to index ‘j’.

 **Time complexity:** O(N^2) – As number of vertices would be of O(N^2)

 **Efficient Approach:**

  1. For each character **X** , all the characters are found for which it is adjacent to.
  2. A graph is created with number of nodes as number of distinct characters in the string, each representing a character.
  3. Each node **X** , will have an edge of weight 1 with all the nodes representing characters adjacent to character **X**.
  4. Then BFS can be run from nodes representing S[i] to nodes representing S[j] in this new graph

 **Time complexity:** O(N)

Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation of the above approach.

#include <bits/stdc++.h>

using namespace std;

 

// function to find the minimum cost

int findMinCost(string s, int i, int j)

{

 // graph

 vector<vector<int> > gr(26);

 

 // adjacency matrix

 bool edge[26][26];

 

 // initialising adjacency matrix

 for (int k = 0; k < 26; k++)

 for (int l = 0; l < 26; l++)

 edge[k][l] = 0;

 

 // creating adjacency list

 for (int k = 0; k < s.size(); k++) {

 // pushing left adjacent elelemt for index 'k'

 if (k - 1 >= 0

 and !edge[s[k] - 97][s[k - 1] - 97])

 gr[s[k] - 97].push_back(s[k - 1] - 97),

 edge[s[k] - 97][s[k - 1] - 97] = 1;

 // pushing right adjacent element for index 'k'

 if (k + 1 <= s.size() - 1

 and !edge[s[k] - 97][s[k + 1] - 97])

 gr[s[k] - 97].push_back(s[k + 1] - 97),

 edge[s[k] - 97][s[k + 1] - 97] = 1;

 }

 

 // queue to perform BFS

 queue<int> q;

 q.push(s[i] - 97);

 

 // visited array

 bool v[26] = { 0 };

 

 // variable to store depth of BFS

 int d = 0;

 

 // BFS

 while (q.size()) {

 

 // number of elements in the current level

 int cnt = q.size();

 

 // inner loop

 while (cnt--) {

 

 // current element

 int curr = q.front();

 

 // popping queue

 q.pop();

 

 // base case

 if (v[curr])

 continue;

 v[curr] = 1;

 

 // checking if the current node is required node

 if (curr == s[j] - 97)

 return d;

 

 // iterating through the current node

 for (auto it : gr[curr])

 q.push(it);

 }

 

 // updating depth

 d++;

 }

 

 return -1;

}

 

// Driver Code

int main()

{

 // input variables

 string s = "abcde";

 int i = 0;

 int j = 4;

 

 // function to find the minimum cost

 cout << findMinCost(s, i, j);

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

// Java implementation of the above approach.

import java.util.*;

 

class GFG 

{

 

 // function to find the minimum cost

 static int findMinCost(char[] s, int i, int j) 

 {

 // graph

 Vector<Integer>[] gr = new Vector[26];

 for (int iN = 0; iN < 26; iN++)

 gr[iN] = new Vector<Integer>();

 

 // adjacency matrix

 boolean[][] edge = new boolean[26][26];

 

 // initialising adjacency matrix

 for (int k = 0; k < 26; k++)

 for (int l = 0; l < 26; l++)

 edge[k][l] = false;

 

 // creating adjacency list

 for (int k = 0; k < s.length; k++) 

 {

 // pushing left adjacent elelemt for index 'k'

 if (k - 1 >= 0 && !edge[s[k] - 97][s[k - 1] - 97]) 

 {

 gr[s[k] - 97].add(s[k - 1] - 97);

 edge[s[k] - 97][s[k - 1] - 97] = true;

 }

 // pushing right adjacent element for index 'k'

 if (k + 1 <= s.length - 1 && !edge[s[k] - 97][s[k + 1] -
97]) 

 {

 gr[s[k] - 97].add(s[k + 1] - 97);

 edge[s[k] - 97][s[k + 1] - 97] = true;

 }

 }

 

 // queue to perform BFS

 Queue<Integer> q = new LinkedList<Integer>();

 q.add(s[i] - 97);

 

 // visited array

 boolean[] v = new boolean[26];

 

 // variable to store depth of BFS

 int d = 0;

 

 // BFS

 while (q.size() > 0) 

 {

 

 // number of elements in the current level

 int cnt = q.size();

 

 // inner loop

 while (cnt-- > 0) 

 {

 

 // current element

 int curr = q.peek();

 

 // popping queue

 q.remove();

 

 // base case

 if (v[curr])

 continue;

 v[curr] = true;

 

 // checking if the current node is required node

 if (curr == s[j] - 97)

 return d;

 

 // iterating through the current node

 for (Integer it : gr[curr])

 q.add(it);

 }

 

 // updating depth

 d++;

 }

 

 return -1;

 }

 

 // Driver Code

 public static void main(String[] args)

 {

 // input variables

 String s = "abcde";

 int i = 0;

 int j = 4;

 

 // function to find the minimum cost

 System.out.print(findMinCost(s.toCharArray(), i, j));

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

# Python3 implementation of the above approach.

from collections import deque as a queue

 

# function to find minimum cost

def findMinCost(s, i, j):

 

 # graph

 gr = [[] for i in range(26)]

 

 # adjacency matrix

 edge = [[ 0 for i in range(26)] for i in
range(26)]

 

 # initialising adjacency matrix

 for k in range(26):

 for l in range(26):

 edge[k][l] = 0

 

 # creating adjacency list

 for k in range(len(s)):

 

 # pushing left adjacent elelemt for index 'k'

 if (k - 1 >= 0 and edge[ord(s[k]) -
97][ord(s[k - 1]) - 97] == 0):

 gr[ord(s[k]) - 97].append(ord(s[k - 1]) - 97)

 edge[ord(s[k]) - 97][ord(s[k - 1]) - 97] =
1

 

 # pushing right adjacent element for index 'k'

 if (k + 1 <= len(s) - 1 and edge[ord(s[k]) -
97][ord(s[k + 1]) - 97] == 0):

 gr[ord(s[k]) - 97].append(ord(s[k + 1]) - 97)

 edge[ord(s[k]) - 97][ord(s[k + 1]) - 97] =
1

 

 # queue to perform BFS

 q = queue()

 q.append(ord(s[i]) - 97)

 

 # visited array

 v = [0] * (26)

 

 # variable to store depth of BFS

 d = 0

 

 # BFS

 while (len(q)):

 

 # number of elements in the current level

 cnt = len(q)

 

 # inner loop

 while (cnt > 0):

 

 # current element

 curr = q.popleft()

 

 

 # base case

 if (v[curr] == 1):

 continue

 v[curr] = 1

 

 # checking if the current node is required node

 if (curr == ord(s[j]) - 97):

 return curr

 

 # iterating through the current node

 for it in gr[curr]:

 q.append(it)

 print()

 cnt -= 1

 

 # updating depth

 d = d + 1

 

 return -1

 

# Driver Code

 

# input variables

s = "abcde"

i = 0

j = 4

 

# function to find the minimum cost

print(findMinCost(s, i, j))

 

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

// C# implementation of the above approach.

using System;

using System.Collections.Generic;

 

class GFG 

{

 

 // function to find the minimum cost

 static int findMinCost(char[] s, int i, int j) 

 {

 // graph

 List<int>[] gr = new List<int>[26];

 for (int iN = 0; iN < 26; iN++)

 gr[iN] = new List<int>();

 

 // adjacency matrix

 bool[,] edge = new bool[26, 26];

 

 // initialising adjacency matrix

 for (int k = 0; k < 26; k++)

 for (int l = 0; l < 26; l++)

 edge[k, l] = false;

 

 // creating adjacency list

 for (int k = 0; k < s.Length; k++) 

 {

 // pushing left adjacent elelemt for index 'k'

 if (k - 1 >= 0 && !edge[s[k] - 97, s[k - 1] - 97]) 

 {

 gr[s[k] - 97].Add(s[k - 1] - 97);

 edge[s[k] - 97, s[k - 1] - 97] = true;

 }

 

 // pushing right adjacent element for index 'k'

 if (k + 1 <= s.Length - 1 && 

 !edge[s[k] - 97, s[k + 1] - 97]) 

 {

 gr[s[k] - 97].Add(s[k + 1] - 97);

 edge[s[k] - 97, s[k + 1] - 97] = true;

 }

 }

 

 // queue to perform BFS

 Queue<int> q = new Queue<int>();

 q.Enqueue(s[i] - 97);

 

 // visited array

 bool[] v = new bool[26];

 

 // variable to store depth of BFS

 int d = 0;

 

 // BFS

 while (q.Count > 0) 

 {

 

 // number of elements in the current level

 int cnt = q.Count;

 

 // inner loop

 while (cnt-- > 0) 

 {

 

 // current element

 int curr = q.Peek();

 

 // popping queue

 q.Dequeue();

 

 // base case

 if (v[curr])

 continue;

 v[curr] = true;

 

 // checking if the current node is required node

 if (curr == s[j] - 97)

 return d;

 

 // iterating through the current node

 foreach (int it in gr[curr])

 q.Enqueue(it);

 }

 

 // updating depth

 d++;

 }

 

 return -1;

 }

 

 // Driver Code

 public static void Main(String[] args)

 {

 // input variables

 String s = "abcde";

 int i = 0;

 int j = 4;

 

 // function to find the minimum cost

 Console.Write(findMinCost(s.ToCharArray(), i, j));

 }

}

 

// This code is contributed by 29AjayKumar  
  
---  
  
 __

 __

 **Output:**

    
    
    4
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


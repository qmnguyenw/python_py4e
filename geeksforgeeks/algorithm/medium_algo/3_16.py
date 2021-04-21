Check if the given array can be constructed uniquely from the given set of
subsequences



Given an array **arr** of distinct elements and a list of subsequences
**seqs** of the array, the task is to check whether the given array can be
uniquely constructed from the given set of subsequences.  
 **Examples:**  

> **Input :** arr[] = {1, 2, 3, 4}, seqs[][] = {{1, 2}, {2, 3}, {3, 4}}  
> **Output:** Yes  
> **Explanations:** The sequences [1, 2], [2, 3], and [3, 4] can uniquely
> reconstruct  
> the original array {1, 2, 3, 4}.  
> **Input:** arr[] = {1, 2, 3, 4}, seqs[][] = {{1, 2}, {2, 3}, {2, 4}}  
> **Output:** No  
> **Explanations :** The sequences [1, 2], [2, 3], and [2, 4] cannot uniquely
> reconstruct  
> {1, 2, 3, 4}. There are two possible sequences that can be constructed from
> the given sequences:  
> 1) {1, 2, 3, 4}  
> 2) {1, 2, 4, 3}  
>

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:**  
In order to solve this problem we need to find the Topological Ordering of all
the array elements and check if only one topological ordering of the elements
exists or not, which can be confirmed by the presence of only single source at
every instant while finding the topological ordering of elements.  
Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to Check if

// the given array can be constructed

// uniquely from the given set of subsequences

#include <bits/stdc++.h>

using namespace std;

bool canConstruct(vector<int> originalSeq,

 vector<vector<int> > sequences)

{

 vector<int> sortedOrder;

 if (originalSeq.size() <= 0) {

 return false;

 }

 // Count of incoming edges for every vertex

 unordered_map<int, int> inDegree;

 // Adjacency list graph

 unordered_map<int, vector<int> > graph;

 for (auto seq : sequences) {

 for (int i = 0; i < seq.size(); i++) {

 inDegree[seq[i]] = 0;

 graph[seq[i]] = vector<int>();

 }

 }

 // Build the graph

 for (auto seq : sequences) {

 for (int i = 1; i < seq.size(); i++) {

 int parent = seq[i - 1], child = seq[i];

 graph[parent].push_back(child);

 inDegree[child]++;

 }

 }

 // if ordering rules for all the numbers

 // are not present

 if (inDegree.size() != originalSeq.size()) {

 return false;

 }

 // Find all sources i.e., all vertices

 // with 0 in-degrees

 queue<int> sources;

 for (auto entry : inDegree) {

 if (entry.second == 0) {

 sources.push(entry.first);

 }

 }

 // For each source, add it to the sortedOrder

 // and subtract one from all of in-degrees

 // if a child's in-degree becomes zero

 // add it to the sources queue

 while (!sources.empty()) {

 // If there are more than one source

 if (sources.size() > 1) {

 // Multiple sequences exist

 return false;

 }

 // If the next source is different from the origin

 if (originalSeq[sortedOrder.size()] !=

 sources.front()) {

 return false;

 }

 int vertex = sources.front();

 sources.pop();

 sortedOrder.push_back(vertex);

 vector<int> children = graph[vertex];

 for (auto child : children) {

 // Decrement the node's in-degree

 inDegree[child]--;

 if (inDegree[child] == 0) {

 sources.push(child);

 }

 }

 }

 // Compare the sizes of sortedOrder

 // and the original sequence

 return sortedOrder.size() == originalSeq.size();

}

int main(int argc, char* argv[])

{

 vector<int> arr = { 1, 2, 6, 7, 3, 5, 4 };

 vector<vector<int> > seqs = { { 1, 2, 3 },

 { 7, 3, 5 },

 { 1, 6, 3, 4 },

 { 2, 6, 5, 4 } };

 bool result = canConstruct(arr, seqs);

 if (result)

 cout << "Yes" << endl;

 else

 cout << "No" << endl;

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

// Java program to Check if

// the given array can be constructed

// uniquely from the given set of subsequences

import java.io.*;

import java.util.*;

class GFG {

 static boolean canConstruct(int[] originalSeq,

 int[][] sequences)

 {

 List<Integer> sortedOrder

 = new ArrayList<Integer>();

 if (originalSeq.length <= 0) {

 return false;

 }

 // Count of incoming edges for every vertex

 Map<Integer, Integer> inDegree

 = new HashMap<Integer, Integer>();

 // Adjacency list graph

 Map<Integer, ArrayList<Integer> > graph

 = new HashMap<Integer, ArrayList<Integer> >();

 for (int[] seq : sequences)

 {

 for (int i = 0; i < seq.length; i++)

 {

 inDegree.put(seq[i], 0);

 graph.put(seq[i], new ArrayList<Integer>());

 }

 }

 // Build the graph

 for (int[] seq : sequences)

 {

 for (int i = 1; i < seq.length; i++)

 {

 int parent = seq[i - 1], child = seq[i];

 graph.get(parent).add(child);

 inDegree.put(child,

 inDegree.get(child) + 1);

 }

 }

 // if ordering rules for all the numbers

 // are not present

 if (inDegree.size() != originalSeq.length)

 {

 return false;

 }

 // Find all sources i.e., all vertices

 // with 0 in-degrees

 List<Integer> sources = new ArrayList<Integer>();

 for (Map.Entry<Integer, Integer> entry :

 inDegree.entrySet())

 {

 if (entry.getValue() == 0)

 {

 sources.add(entry.getKey());

 }

 }

 // For each source, add it to the sortedOrder

 // and subtract one from all of in-degrees

 // if a child's in-degree becomes zero

 // add it to the sources queue

 while (!sources.isEmpty())

 {

 // If there are more than one source

 if (sources.size() > 1)

 {

 // Multiple sequences exist

 return false;

 }

 // If the next source is different from the

 // origin

 if (originalSeq[sortedOrder.size()]

 != sources.get(0))

 {

 return false;

 }

 int vertex = sources.get(0);

 sources.remove(0);

 sortedOrder.add(vertex);

 List<Integer> children = graph.get(vertex);

 for (int child : children)

 {

 // Decrement the node's in-degree

 inDegree.put(child,

 inDegree.get(child) - 1);

 if (inDegree.get(child) == 0)

 {

 sources.add(child);

 }

 }

 }

 // Compare the sizes of sortedOrder

 // and the original sequence

 return sortedOrder.size() == originalSeq.length;

 }

 

 // Driver code

 public static void main(String[] args)

 {

 int[] arr = { 1, 2, 6, 7, 3, 5, 4 };

 int[][] seqs = { { 1, 2, 3 },

 { 7, 3, 5 },

 { 1, 6, 3, 4 },

 { 2, 6, 5, 4 } };

 boolean result = canConstruct(arr, seqs);

 if (result)

 System.out.println("Yes");

 else

 System.out.println("No");

 }

}

// This code is contributed by jitin  
  
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

# Python 3 program to Check if

# the given array can be constructed

# uniquely from the given set of subsequences

def canConstruct(originalSeq, sequences):

 sortedOrder = []

 if (len(originalSeq) <= 0):

 return False

 # Count of incoming edges for every vertex

 inDegree = {i : 0 for i in range(100)}

 

 # Adjacency list graph

 graph = {i : [] for i in range(100)}

 for seq in sequences:

 for i in range(len(seq)):

 inDegree[seq[i]] = 0

 graph[seq[i]] = []

 # Build the graph

 for seq in sequences:

 for i in range(1, len(seq)):

 parent = seq[i - 1]

 child = seq[i]

 graph[parent].append(child)

 inDegree[child] += 1

 

 # If ordering rules for all the numbers

 # are not present

 if (len(inDegree) != len(originalSeq)):

 return False

 # Find all sources i.e., all vertices

 # with 0 in-degrees

 sources = []

 for entry in inDegree:

 if (entry[1] == 0):

 sources.append(entry[0])

 

 # For each source, add it to the sortedOrder

 # and subtract one from all of in-degrees

 # if a child's in-degree becomes zero

 # add it to the sources queue

 while (len(sources) > 0):

 

 # If there are more than one source

 if (len(sources) > 1):

 

 # Multiple sequences exist

 return False

 

 # If the next source is different from the origin

 if (originalSeq[len(sortedOrder)] != sources[0]):

 return False

 vertex = sources[0]

 sources.remove(sources[0])

 sortedOrder.append(vertex)

 children = graph[vertex]

 for child in children:

 

 # Decrement the node's in-degree

 inDegree[child] -= 1

 if (inDegree[child] == 0):

 sources.append(child)

 # Compare the sizes of sortedOrder

 # and the original sequence

 return len(sortedOrder) == len(originalSeq)

if __name__ == '__main__':

 arr = [ 1, 2, 6, 7, 3, 5, 4 ]

 seqs = [[ 1, 2, 3 ],

 [ 7, 3, 5 ],

 [ 1, 6, 3, 4 ],

 [ 2, 6, 5, 4 ]]

 result = canConstruct(arr, seqs)

 if (result):

 print("Yes")

 else:

 print("No")

# This code is contributed by Bhupendra_Singh  
  
---  
  
 __

 __

 **Output:**

    
    
    No

**Time complexity :**  
The time complexity of the above algorithm will be O(N+E), where ‘N’ is the
number of elements and ‘E’ is the total number of the rules. Since, at most,
each pair of numbers can give us one rule, we can conclude that the upper
bound for the rules is O(M) where ‘M’ is the count of numbers in all
sequences. So, we can say that the time complexity of our algorithm is O(N +
M).  
 **Auxiliary Space :** O(N+ M), since we are storing all possible rules for
each element.  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save


Least Common Ancestor of any number of nodes in Binary Tree



Given a binary tree (not a binary search tree) and any number of Key Nodes,
the task is to find the least common ancestor of all the key Nodes.

**Following is the definition of LCA from** **Wikipedia** **:**  
Let T be a rooted tree. The lowest common ancestor between two nodes n1 and n2
is defined as the lowest node in T that has both n1 and n2 as descendants
(where we allow a node to be a descendant of itself).

The LCA of any number of nodes in T is the shared common ancestor of the nodes
that is located farthest from the root.  

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200206115435/lca2-1.jpg)

**Example:** In the figure above:

  

  

    
    
    LCA of nodes 12, 14, 15 is node 3
    LCA of nodes 3, 14, 15 is node 3
    LCA of nodes 6, 7, 15 is node 3
    LCA of nodes 5, 13, 14, 15 is node 1
    LCA of nodes 6, 12 is node 6

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:**  
Following is the simple approach for Least Common Ancestor for any number of
nodes.

  * For every node calculate the matching number of nodes at that node and its sub-tree. 
    * If root is also a matching node.

> matchingNodes = matchingNodes in left sub-tree + matchingNodes in right sub-
> tree + 1  
>

  * If root is not a matching node.

> matchingNodes = matchingNodes in left sub-tree + matchingNodes in right-
> subtree  
>

  * If matching Nodes count at any node is equal to number of keys then add that node into the Ancestors list.
  * The First node in the Ancestors List is the Least Common Ancestor of all the given keys.

Below is the implementation of above approach.

## C++14

 __

 __  
 __

 __

 __  
 __  
 __

// C++ imlementation to find

// Ancestors of any number of nodes

#include <bits/stdc++.h>

using namespace std;

// Tree Class

class TreeNode

{

 public:

 int data;

 TreeNode *left, *right;

 

 TreeNode(int value)

 {

 this->data = value;

 this->left = NULL;

 this->right = NULL;

 }

};

int getKeysCount(TreeNode *root, vector<int> &keyNodes;,

 int matchingNodes,

 vector<TreeNode *> &ancestors;)

{

 

 // Base Case. When root is Null

 if (root == NULL)

 {

 return 0;

 }

 

 // Search for left and right subtree

 // for matching child Key Node.

 matchingNodes += getKeysCount(root->left, keyNodes,

 matchingNodes, ancestors) +

 getKeysCount(root->right, keyNodes,

 matchingNodes, ancestors);

 

 // Condition to check if Root Node

 // is also in Key Node

 if (find(keyNodes.begin(),

 keyNodes.end(), root->data) != keyNodes.end())

 {

 matchingNodes++;

 }

 

 // Condition when matching Nodes is

 // equal to the Key Nodes found

 if (matchingNodes == keyNodes.size())

 {

 ancestors.push_back(root);

 }

 

 return matchingNodes;

}

// Function to find Least Common

// Ancestors of N number of nodes

TreeNode *lcaOfNodes(TreeNode *root,

 vector<int> &keyNodes;)

{

 

 // Create a new list for

 // capturing all the ancestors

 // of the given nodes

 vector<TreeNode *> ancestors;

 

 // Intially there is No Matching Nodes

 int matchingNodes = 0;

 getKeysCount(root, keyNodes,

 matchingNodes, ancestors);

 

 // First Node in the Ancestors list

 // is the Least Common Ancestor of

 // Given keyNodes

 return ancestors[0];

}

// Driver Code

int main()

{

 

 // Creation of Tree

 TreeNode *root = new TreeNode(1);

 

 root->left = new TreeNode(2);

 root->right = new TreeNode(3);

 root->left->left = new TreeNode(4);

 root->left->right = new TreeNode(5);

 root->right->left = new TreeNode(6);

 root->right->right = new TreeNode(7);

 root->left->left->left = new TreeNode(8);

 root->left->left->right = new TreeNode(9);

 root->left->right->left = new TreeNode(10);

 root->left->right->right = new TreeNode(11);

 root->right->left->left = new TreeNode(12);

 root->right->left->right = new TreeNode(13);

 root->right->right->left = new TreeNode(14);

 root->right->right->right = new TreeNode(15);

 

 // Key Nodes for LCA

 vector<int> keyNodes;

 keyNodes.push_back(12);

 keyNodes.push_back(14);

 keyNodes.push_back(15);

 

 cout << lcaOfNodes(root, keyNodes)->data

 << endl;

 

 return 0;

}

// This code is contributed by sanjeev2552  
  
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

// Java imlementation to find

// Ancestors of any number of nodes

import java.util.ArrayList;

// Tree Class

class TreeNode {

 int data;

 TreeNode left;

 TreeNode right;

 public TreeNode(int value)

 {

 this.data = value;

 left = right = null;

 }

}

public class LCAofAnyNumberOfNodes {

 

 // Function to find Least Common

 // Ancestors of N number of nodes

 public static TreeNode lcaOfNodes(

 TreeNode root,

 ArrayList<Integer> keyNodes)

 {

 // Create a new list for

 // capturing all the ancestors

 // of the given nodes

 ArrayList<TreeNode> ancestors =

 new ArrayList<TreeNode>();

 

 // Intially there is No Matching Nodes

 int matchingNodes = 0;

 getKeysCount(root, keyNodes,

 matchingNodes, ancestors);

 // First Node in the Ancestors list

 // is the Least Common Ancestor of

 // Given keyNodes

 return ancestors.get(0);

 }

 private static int getKeysCount(

 TreeNode root, ArrayList<Integer> keyNodes,

 int matchingNodes,

 ArrayList<TreeNode> ancestors)

 {

 // Base Case. When root is Null

 if (root == null)

 return 0;

 // Search for left and right subtree

 // for matching child Key Node.

 matchingNodes += getKeysCount(root.left,

 keyNodes, matchingNodes, ancestors)

 + getKeysCount(root.right,

 keyNodes, matchingNodes, ancestors);

 

 // Condition to check if Root Node 

 // is also in Key Node

 if (keyNodes.contains(root.data)){

 matchingNodes++;

 }

 // Condition when matching Nodes is

 // equal to the Key Nodes found

 if (matchingNodes == keyNodes.size())

 ancestors.add(root);

 return matchingNodes;

 }

 

 // Driver Code

 public static void main(String[] args)

 {

 

 // Creation of Tree

 TreeNode root = new TreeNode(1);

 root.left = new TreeNode(2);

 root.right = new TreeNode(3);

 root.left.left = new TreeNode(4);

 root.left.right =

 new TreeNode(5);

 root.right.left =

 new TreeNode(6);

 root.right.right =

 new TreeNode(7);

 root.left.left.left =

 new TreeNode(8);

 root.left.left.right =

 new TreeNode(9);

 root.left.right.left =

 new TreeNode(10);

 root.left.right.right =

 new TreeNode(11);

 root.right.left.left =

 new TreeNode(12);

 root.right.left.right =

 new TreeNode(13);

 root.right.right.left =

 new TreeNode(14);

 root.right.right.right =

 new TreeNode(15);

 

 // Key Nodes for LCA

 ArrayList<Integer> keyNodes =

 new ArrayList<Integer>();

 keyNodes.add(12);

 keyNodes.add(14);

 keyNodes.add(15);

 System.out.println(

 lcaOfNodes(root, keyNodes).data

 );

 }

}  
  
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

// C# imlementation to find

// Ancestors of any number of nodes

using System;

using System.Collections.Generic;

// Tree Class

class TreeNode {

 public int data;

 public TreeNode left;

 public TreeNode right;

 

 public TreeNode(int value)

 {

 this.data = value;

 left = right = null;

 }

}

 

public class LCAofAnyNumberOfNodes {

 

 // Function to find Least Common

 // Ancestors of N number of nodes

 static TreeNode lcaOfNodes(

 TreeNode root,

 List<int> keyNodes)

 {

 // Create a new list for

 // capturing all the ancestors

 // of the given nodes

 List<TreeNode> ancestors =

 new List<TreeNode>();

 

 // Intially there is No Matching Nodes

 int matchingNodes = 0;

 getKeysCount(root, keyNodes,

 matchingNodes, ancestors);

 

 // First Node in the Ancestors list

 // is the Least Common Ancestor of

 // Given keyNodes

 return ancestors[0];

 }

 

 private static int getKeysCount(

 TreeNode root, List<int> keyNodes,

 int matchingNodes,

 List<TreeNode> ancestors)

 {

 // Base Case. When root is Null

 if (root == null)

 return 0;

 

 // Search for left and right subtree

 // for matching child Key Node.

 matchingNodes += getKeysCount(root.left,

 keyNodes, matchingNodes, ancestors)

 + getKeysCount(root.right,

 keyNodes, matchingNodes, ancestors);

 

 // Condition to check if Root Node 

 // is also in Key Node

 if (keyNodes.Contains(root.data)){

 matchingNodes++;

 }

 

 // Condition when matching Nodes is

 // equal to the Key Nodes found

 if (matchingNodes == keyNodes.Count)

 ancestors.Add(root);

 return matchingNodes;

 }

 

 // Driver Code

 public static void Main(String[] args)

 {

 

 // Creation of Tree

 TreeNode root = new TreeNode(1);

 

 root.left = new TreeNode(2);

 root.right = new TreeNode(3);

 root.left.left = new TreeNode(4);

 root.left.right =

 new TreeNode(5);

 root.right.left =

 new TreeNode(6);

 root.right.right =

 new TreeNode(7);

 root.left.left.left =

 new TreeNode(8);

 root.left.left.right =

 new TreeNode(9);

 root.left.right.left =

 new TreeNode(10);

 root.left.right.right =

 new TreeNode(11);

 root.right.left.left =

 new TreeNode(12);

 root.right.left.right =

 new TreeNode(13);

 root.right.right.left =

 new TreeNode(14);

 root.right.right.right =

 new TreeNode(15);

 

 // Key Nodes for LCA

 List<int> keyNodes = new List<int>();

 keyNodes.Add(12);

 keyNodes.Add(14);

 keyNodes.Add(15);

 Console.WriteLine(

 lcaOfNodes(root, keyNodes).data

 );

 }

}

// This code is contributed by PrinciRaj1992  
  
---  
  
 __

 __

 **Output:**

    
    
    3

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


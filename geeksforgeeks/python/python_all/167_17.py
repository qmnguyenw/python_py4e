Iterative Boundary Traversal of Complete Binary tree



Given a complete binary tree, traverse it such that all the boundary nodes are
visited in Anti-Clockwise order starting from the root.  
 **Example:**  

    
    
    **Input:**
                   18
               /       \  
             15         30  
            /  \        /  \
          40    50    100   20
    **Output:** 18 15 40 50 100 20 30

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.  

**Approach:**  

  * Traverse left-most nodes of the tree from top to down. (Left boundary)
  * Traverse bottom-most level of the tree from left to right. (Leaf nodes)
  * Traverse right-most nodes of the tree from bottom to up. (Right boundary)

We can traverse the left boundary quite easily with the help of a while loop
that checks when the node doesn’t have any left child. Similarly, we can
traverse the right boundary quite easily with the help of a while loop that
checks when the node doesn’t have any right child.  
The main challenge here is to traverse the last level of the tree in left to
right order. To traverse level-wise there is BFS and order of left to right
can be taken care of by pushing left nodes in the queue first. So the only
thing left now is to make sure it is the last level. Just check whether the
node has any child and only include them.  
We will have to take special care of the corner case that same nodes are not
traversed again. In the example above 40 is a part of the left boundary as
well as leaf nodes. Similarly, 20 is a part of the right boundary as well as
leaf nodes.  
So we will have to traverse only till the second last node of both the
boundaries in that case. Also keep in mind we should not traverse the root
again.  
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

/* A binary tree node has data, pointer

 to left child and a pointer to right

 child */

struct Node {

 int data;

 struct Node *left, *right;

};

/* Helper function that allocates a new

 node with the given data and NULL left

 and right pointers. */

struct Node* newNode(int data)

{

 Node* temp = new Node;

 temp->data = data;

 temp->left = temp->right = NULL;

 return temp;

}

// Function to print the nodes of a complete

// binary tree in boundary traversal order

void boundaryTraversal(Node* root)

{

 if (root) {

 // If there is only 1 node print it

 // and return

 if (!(root->left) && !(root->right)) {

 cout << root->data << endl;

 return;

 }

 // List to store order of traversed

 // nodes

 vector<Node*> list;

 list.push_back(root);

 // Traverse left boundary without root

 // and last node

 Node* L = root->left;

 while (L->left) {

 list.push_back(L);

 L = L->left;

 }

 // BFS designed to only include leaf nodes

 queue<Node*> q;

 q.push(root);

 while (!q.empty()) {

 Node* temp = q.front();

 q.pop();

 if (!(temp->left) && !(temp->right)) {

 list.push_back(temp);

 }

 if (temp->left) {

 q.push(temp->left);

 }

 if (temp->right) {

 q.push(temp->right);

 }

 }

 // Traverse right boundary without root

 // and last node

 vector<Node*> list_r;

 Node* R = root->right;

 while (R->right) {

 list_r.push_back(R);

 R = R->right;

 }

 // Reversing the order

 reverse(list_r.begin(), list_r.end());

 // Concatenating the two lists

 list.insert(list.end(), list_r.begin(),

 list_r.end());

 // Printing the node's data from the list

 for (auto i : list) {

 cout << i->data << " ";

 }

 cout << endl;

 return;

 }

}

// Driver code

int main()

{

 // Root node of the tree

 Node* root = newNode(20);

 root->left = newNode(8);

 root->right = newNode(22);

 root->left->left = newNode(4);

 root->left->right = newNode(12);

 root->right->left = newNode(10);

 root->right->right = newNode(25);

 boundaryTraversal(root);

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

/* A binary tree node has data, pointer

 to left child and a pointer to right

 child */

static class Node {

 int data;

 Node left, right;

};

/* Helper function that allocates a new

 node with the given data and null left

 and right pointers. */

static Node newNode(int data)

{

 Node temp = new Node();

 temp.data = data;

 temp.left = temp.right = null;

 return temp;

}

// Function to print the nodes of a complete

// binary tree in boundary traversal order

static void boundaryTraversal(Node root)

{

 if (root != null) {

 // If there is only 1 node print it

 // and return

 if ((root.left == null) && (root.right == null)) {

 System.out.print(root.data +"\n");

 return;

 }

 // List to store order of traversed

 // nodes

 Vector<Node> list = new Vector<Node>();

 list.add(root);

 // Traverse left boundary without root

 // and last node

 Node L = root.left;

 while (L.left != null) {

 list.add(L);

 L = L.left;

 }

 // BFS designed to only include leaf nodes

 Queue<Node> q = new LinkedList<>();

 q.add(root);

 while (!q.isEmpty()) {

 Node temp = q.peek();

 q.remove();

 if ((temp.left == null) && (temp.right == null)) {

 list.add(temp);

 }

 if (temp.left != null) {

 q.add(temp.left);

 }

 if (temp.right != null) {

 q.add(temp.right);

 }

 }

 // Traverse right boundary without root

 // and last node

 Vector<Node> list_r = new Vector<Node>();

 Node R = root.right;

 while (R.right != null) {

 list_r.add(R);

 R = R.right;

 }

 // Reversing the order

 Collections.reverse(list_r);

 // Concatenating the two lists

 list.addAll(list_r);

 // Printing the node's data from the list

 for (Node i : list) {

 System.out.print(i.data + " ");

 }

 System.out.println();

 return;

 }

}

// Driver code

public static void main(String[] args)

{

 // Root node of the tree

 Node root = newNode(20);

 root.left = newNode(8);

 root.right = newNode(22);

 root.left.left = newNode(4);

 root.left.right = newNode(12);

 root.right.left = newNode(10);

 root.right.right = newNode(25);

 boundaryTraversal(root);

}

}

// This code is contributed by Princi Singh  
  
---  
  
 __

 __

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python implementation of the approach

from collections import deque

 

# A binary tree node

class Node:

 

 # A constructor for making a new node

 def __init__(self, key):

 self.data = key

 self.left = None

 self.right = None

 

# Function to print the nodes of a complete

# binary tree in boundary traversal order

def boundaryTraversal(root):

 # If there is only 1 node print it and return

 if root:

 if not root.left and not root.right:

 print (root.data)

 return

 

 # List to store order of traversed nodes

 list = []

 list.append(root)

 

 # Traverse left boundary without root

 # and last node

 temp = root.left

 while temp.left:

 list.append(temp)

 temp = temp.left

 

 # BFS designed to only include leaf nodes

 q = deque()

 q.append(root)

 while len(q) != 0:

 x = q.pop()

 if not x.left and not x.right:

 list.append(x)

 if x.right:

 q.append(x.right)

 if x.left:

 q.append(x.left)

 

 # Traverse right boundary without root

 # and last node

 list_r = []

 temp = root.right

 while temp.right:

 list.append(temp)

 temp = temp.right

 

 # Reversing the order

 list_r = list_r[::-1]

 

 # Concatenating the two lists

 list += list_r

 

 # Printing the node's data from the list

 print (" ".join([str(i.data) for i in list]))

 return

 

# Root node of the tree

 

root = Node(20)

 

root.left = Node(8)

root.right = Node(22)

 

root.left.left = Node(4)

root.left.right = Node(12)

root.right.left = Node(10)

root.right.right = Node(25)

 

boundaryTraversal(root)  
  
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

/* A binary tree node has data, pointer

 to left child and a pointer to right

 child */

class Node

{

 public int data;

 public Node left, right;

};

/* Helper function that allocates a new

 node with the given data and null left

 and right pointers. */

static Node newNode(int data)

{

 Node temp = new Node();

 temp.data = data;

 temp.left = temp.right = null;

 return temp;

}

// Function to print the nodes of a complete

// binary tree in boundary traversal order

static void boundaryTraversal(Node root)

{

 if (root != null)

 {

 // If there is only 1 node print it

 // and return

 if ((root.left == null) &&

 (root.right == null))

 {

 Console.Write(root.data + "\n");

 return;

 }

 // List to store order of traversed

 // nodes

 List<Node> list = new List<Node>();

 list.Add(root);

 // Traverse left boundary without root

 // and last node

 Node L = root.left;

 while (L.left != null)

 {

 list.Add(L);

 L = L.left;

 }

 // BFS designed to only include leaf nodes

 Queue<Node> q = new Queue<Node>();

 q.Enqueue(root);

 while (q.Count != 0)

 {

 Node temp = q.Peek();

 q.Dequeue();

 if ((temp.left == null) &&

 (temp.right == null))

 {

 list.Add(temp);

 }

 if (temp.left != null)

 {

 q.Enqueue(temp.left);

 }

 if (temp.right != null)

 {

 q.Enqueue(temp.right);

 }

 }

 // Traverse right boundary without root

 // and last node

 List<Node> list_r = new List<Node>();

 Node R = root.right;

 while (R.right != null)

 {

 list_r.Add(R);

 R = R.right;

 }

 // Reversing the order

 list_r.Reverse();

 // Concatenating the two lists

 list.InsertRange(list.Count-1, list_r);

 // Printing the node's data from the list

 foreach (Node i in list)

 {

 Console.Write(i.data + " ");

 }

 Console.WriteLine();

 return;

 }

}

// Driver code

public static void Main(String[] args)

{

 // Root node of the tree

 Node root = newNode(20);

 root.left = newNode(8);

 root.right = newNode(22);

 root.left.left = newNode(4);

 root.left.right = newNode(12);

 root.right.left = newNode(10);

 root.right.right = newNode(25);

 boundaryTraversal(root);

}

}

// This code is contributed by 29AjayKumar  
  
---  
  
 __

 __

 **Output:**

    
    
    20 8 4 12 10 25 22

Want to learn from the best curated videos and practice problems, check out
the **C++ Foundation Course **for Basic to Advanced C++ and **C++ STL Course**
for foundation plus STL.

  
  

  

My Personal Notes _arrow_drop_up_

Save


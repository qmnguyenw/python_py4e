Flatten Binary Tree in order of Level Order Traversal



Given a Binary Tree, the task is to flatten it in order of Level order
traversal of the tree. In the flattened binary tree, the left node of all the
nodes must be NULL.

 **Examples:**

    
    
    **Input:** 
              1 
            /   \ 
           5     2 
          / \   / \ 
         6   4 9   3 
    **Output:** 1 5 2 6 4 9 3
    
    **Input:**
          1
           \
            2
             \
              3
               \
                4
                 \
                  5
    **Output:** 1 2 3 4 5
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** We will solve this problem by simulating the Level order
traversal of Binary Tree as follows:

  1. Create a queue to store the nodes of Binary tree.
  2. Create a variable “prev” and initialise it by parent node.
  3. Push left and right children of parent in the queue.
  4. Apply level order traversal. Lets say “curr” is front most element in queue. Then,
    * If ‘curr’ is NULL, continue.
    * Else push curr->left and curr->right in the queue
    * Set prev = curr

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

 

// Node of the Binary tree

struct node {

 int data;

 node* left;

 node* right;

 node(int data)

 {

 this->data = data;

 left = NULL;

 right = NULL;

 }

};

 

// Function to flatten Binary tree using

// level order traversal

void flatten(node* parent)

{

 // Queue to store nodes

 // for BFS

 queue<node*> q;

 q.push(parent->left);

 q.push(parent->right);

 node* prev = parent;

 

 // Code for BFS

 while (q.size()) {

 

 // Size of queue

 int s = q.size();

 while (s--) {

 

 // Front most node in

 // the queue

 node* curr = q.front();

 q.pop();

 

 // Base case

 if (curr == NULL)

 continue;

 prev->right = curr;

 prev->left = NULL;

 prev = curr;

 

 // Pushing new elements

 // in queue

 q.push(curr->left);

 q.push(curr->right);

 }

 }

 

 prev->left = NULL;

 prev->right = NULL;

}

 

// Function to print flattened

// Binary Tree

void print(node* parent)

{

 node* curr = parent;

 while (curr != NULL)

 cout << curr->data << " ", curr = curr->right;

}

 

// Driver code

int main()

{

 node* root = new node(1);

 root->left = new node(5);

 root->right = new node(2);

 root->left->left = new node(6);

 root->left->right = new node(4);

 root->right->left = new node(9);

 root->right->right = new node(3);

 

 // Calling required functions

 flatten(root);

 print(root);

 

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

 

// Node of the Binary tree

static class node 

{

 int data;

 node left;

 node right;

 node(int data)

 {

 this.data = data;

 left = null;

 right = null;

 }

};

 

// Function to flatten Binary tree using

// level order traversal

static void flatten(node parent)

{

 // Queue to store nodes

 // for BFS

 Queue<node> q = new LinkedList<>();

 q.add(parent.left);

 q.add(parent.right);

 node prev = parent;

 

 // Code for BFS

 while (q.size() > 0) 

 {

 

 // Size of queue

 int s = q.size();

 while (s-- > 0) 

 {

 

 // Front most node in

 // the queue

 node curr = q.peek();

 q.remove();

 

 // Base case

 if (curr == null)

 continue;

 prev.right = curr;

 prev.left = null;

 prev = curr;

 

 // Pushing new elements

 // in queue

 q.add(curr.left);

 q.add(curr.right);

 }

 }

 prev.left = null;

 prev.right = null;

}

 

// Function to print flattened

// Binary Tree

static void print(node parent)

{

 node curr = parent;

 while (curr != null)

 {

 System.out.print(curr.data + " ");

 curr = curr.right;

 }

}

 

// Driver code

public static void main(String[] args) 

{

 node root = new node(1);

 root.left = new node(5);

 root.right = new node(2);

 root.left.left = new node(6);

 root.left.right = new node(4);

 root.right.left = new node(9);

 root.right.right = new node(3);

 

 // Calling required functions

 flatten(root);

 print(root);

}

}

 

// This code is contributed by Rajput-Ji  
  
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

# Python implementation of above algorithm

 

# Utility class to create a node 

class node: 

 def __init__(self, key): 

 self.data = key 

 self.left = self.right = None

 

# Function to flatten Binary tree using

# level order traversal

def flatten( parent):

 

 # Queue to store nodes

 # for BFS

 q = []

 q.append(parent.left)

 q.append(parent.right)

 prev = parent

 

 # Code for BFS

 while (len(q) > 0) :

 

 # Size of queue

 s = len(q)

 while (s > 0) :

 s = s - 1

 

 # Front most node in

 # the queue

 curr = q[0]

 q.pop(0)

 

 # Base case

 if (curr == None):

 continue

 prev.right = curr

 prev.left = None

 prev = curr

 

 # appending elements

 # in queue

 q.append(curr.left)

 q.append(curr.right)

 

 prev.left = None

 prev.right = None

 

# Function to print flattened

# Binary Tree

def print_(parent):

 

 curr = parent

 while (curr != None):

 print( curr.data , end=" ")

 curr = curr.right

 

# Driver code

root = node(1)

root.left = node(5)

root.right = node(2)

root.left.left = node(6)

root.left.right = node(4)

root.right.left = node(9)

root.right.right = node(3)

 

# Calling required functions

flatten(root)

print_(root)

 

# This code is contributed by Arnab Kundu  
  
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

 

// Node of the Binary tree

public class node 

{

 public int data;

 public node left;

 public node right;

 public node(int data)

 {

 this.data = data;

 left = null;

 right = null;

 }

};

 

// Function to flatten Binary tree using

// level order traversal

static void flatten(node parent)

{

 // Queue to store nodes

 // for BFS

 Queue<node> q = new Queue<node>();

 q.Enqueue(parent.left);

 q.Enqueue(parent.right);

 node prev = parent;

 

 // Code for BFS

 while (q.Count > 0) 

 {

 

 // Size of queue

 int s = q.Count;

 while (s-- > 0) 

 {

 

 // Front most node in

 // the queue

 node curr = q.Peek();

 q.Dequeue();

 

 // Base case

 if (curr == null)

 continue;

 prev.right = curr;

 prev.left = null;

 prev = curr;

 

 // Pushing new elements

 // in queue

 q.Enqueue(curr.left);

 q.Enqueue(curr.right);

 }

 }

 prev.left = null;

 prev.right = null;

}

 

// Function to print flattened

// Binary Tree

static void print(node parent)

{

 node curr = parent;

 while (curr != null)

 {

 Console.Write(curr.data + " ");

 curr = curr.right;

 }

}

 

// Driver code

public static void Main(String[] args) 

{

 node root = new node(1);

 root.left = new node(5);

 root.right = new node(2);

 root.left.left = new node(6);

 root.left.right = new node(4);

 root.right.left = new node(9);

 root.right.right = new node(3);

 

 // Calling required functions

 flatten(root);

 print(root);

}

}

 

// This code is contributed by Rajput-Ji  
  
---  
  
 __

 __

  
 **Output :**

    
    
    1 5 2 6 4 9 3 

**Time Complexity:** O(N)  
 **Space Complexity:** O(N) where N is the size of Binary Tree.

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save


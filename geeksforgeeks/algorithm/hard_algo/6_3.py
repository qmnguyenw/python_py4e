Merge two BSTs with constant extra space



Given two Binary Search Trees(BST), print the elements of both BSTs in sorted
form.  
**Note** : Both the BSTs will not have any common element.

 **Examples:**

    
    
    **Input**
    _First BST_ : 
           3
        /     \
       1       5
    _Second BST_ :
        4
      /   \
    2       6
    **Output** : 1 2 3 4 5 6
    
    **Input** :
    _First BST_ : 
              8
             / \
            2   10
           /
          1
    _Second BST_ : 
              5
             / 
            3  
           /
          0
    **Output** : 0 1 2 3 5 8 10

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

The idea is to use the fact the leftmost element (first in inorder traversal)
of the tree is the least element in a BST. So we compute this value for both
the trees and print the smaller one, now we delete this printed element from
the respective tree and update it. Then we recursively call our function with
the updated tree. We do this until one of the trees is exhausted. Now we
simply print the inorder traversal of the other tree.

Below is the implementation of above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation of above approach

#include <bits/stdc++.h>

using namespace std;

// Structure of a BST Node

class Node {

public:

 int data;

 Node* left;

 Node* right;

 Node(int x)

 {

 data = x;

 left = right = NULL;

 }

};

// A utility function to print

// Inorder traversal of a Binary Tree

void inorder(Node* root)

{

 if (root != NULL) {

 inorder(root->left);

 cout << root->data << " ";

 inorder(root->right);

 }

}

// The function to print data

// of two BSTs in sorted order

void merge(Node* root1, Node* root2)

{

 // Base cases

 if (!root1 && !root2)

 return;

 // If the first tree is exhausted

 // simply print the inorder

 // traversal of the second tree

 if (!root1) {

 inorder(root2);

 return;

 }

 // If second tree is exhausted

 // simply print the inoreder

 // traversal of the first tree

 if (!root2) {

 inorder(root1);

 return;

 }

 // A temporary pointer currently

 // pointing to root of first tree

 Node* temp1 = root1;

 // previous pointer to store the

 // parent of temporary pointer

 Node* prev1 = NULL;

 // Traverse through the first tree until you reach

 // the leftmost element, which is the first element

 // of the tree in the inorder traversal.

 // This is the least element of the tree

 while (temp1->left) {

 prev1 = temp1;

 temp1 = temp1->left;

 }

 // Another temporary pointer currently

 // pointing to root of second tree

 Node* temp2 = root2;

 // Previous pointer to store the

 // parent of second temporary pointer

 Node* prev2 = NULL;

 // Traverse through the second tree until you reach

 // the leftmost element, which is the first element of

 // the tree in inorder traversal.

 // This is the least element of the tree.

 while (temp2->left) {

 prev2 = temp2;

 temp2 = temp2->left;

 }

 // Compare the least current least

 // elements of both the tree

 if (temp1->data <= temp2->data) {

 // If first tree's element is smaller print it

 cout << temp1->data << " ";

 // If the node has no parent, that

 // means this node is the root

 if (prev1 == NULL) {

 // Simply make the right

 // child of the root as new root

 merge(root1->right, root2);

 }

 // If node has a parent

 else {

 // As this node is the leftmost node,

 // it is certain that it will not have

 // a let child so we simply assign this

 // node's right pointer, which can be

 // either null or not, to its parent's left

 // pointer. This statement is

 // just doing the task of deleting the node

 prev1->left = temp1->right;

 // recursively call the merge

 // function with updated tree

 merge(root1, root2);

 }

 }

 else {

 cout << temp2->data << " ";

 // If the node has no parent, that

 // means this node is the root

 if (prev2 == NULL) {

 // Simply make the right child

 // of root as new root

 merge(root1, root2->right);

 }

 // If node has a parent

 else {

 prev2->left = temp2->right;

 // Recursively call the merge

 // function with updated tree

 merge(root1, root2);

 }

 }

}

// Driver Code

int main()

{

 Node *root1 = NULL, *root2 = NULL;

 root1 = new Node(3);

 root1->left = new Node(1);

 root1->right = new Node(5);

 root2 = new Node(4);

 root2->left = new Node(2);

 root2->right = new Node(6);

 // Print sorted nodes of both trees

 merge(root1, root2);

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

// Java implementation of above approach

import java.util.*;

class GFG{

 

// Structure of a BST Node

static class Node

{

 int data;

 Node left;

 Node right;

};

static Node newNode(int num)

{

 Node temp = new Node();

 temp.data = num;

 temp.left = temp.right = null;

 return temp;

}

// A utility function to print

// Inorder traversal of a Binary Tree

static void inorder(Node root)

{

 if (root != null)

 {

 inorder(root.left);

 System.out.print(root.data + " ");

 inorder(root.right);

 }

}

// The function to print data

// of two BSTs in sorted order

static void merge(Node root1, Node root2)

{

 

 // Base cases

 if (root1 == null && root2 == null)

 return;

 // If the first tree is exhausted

 // simply print the inorder

 // traversal of the second tree

 if (root1 == null)

 {

 inorder(root2);

 return;

 }

 // If second tree is exhausted

 // simply print the inoreder

 // traversal of the first tree

 if (root2 == null)

 {

 inorder(root1);

 return;

 }

 // A temporary pointer currently

 // pointing to root of first tree

 Node temp1 = root1;

 // previous pointer to store the

 // parent of temporary pointer

 Node prev1 = null;

 // Traverse through the first tree

 // until you reach the leftmost element,

 // which is the first element of the tree

 // in the inorder traversal.

 // This is the least element of the tree

 while (temp1.left != null)

 {

 prev1 = temp1;

 temp1 = temp1.left;

 }

 // Another temporary pointer currently

 // pointing to root of second tree

 Node temp2 = root2;

 // Previous pointer to store the

 // parent of second temporary pointer

 Node prev2 = null;

 // Traverse through the second tree

 // until you reach the leftmost element,

 // which is the first element of

 // the tree in inorder traversal.

 // This is the least element of the tree.

 while (temp2.left != null)

 {

 prev2 = temp2;

 temp2 = temp2.left;

 }

 // Compare the least current least

 // elements of both the tree

 if (temp1.data <= temp2.data)

 {

 

 // If first tree's element is

 // smaller print it

 System.out.print(temp1.data + " ");

 // If the node has no parent, that

 // means this node is the root

 if (prev1 == null)

 {

 

 // Simply make the right

 // child of the root as new root

 merge(root1.right, root2);

 }

 // If node has a parent

 else

 {

 

 // As this node is the leftmost node,

 // it is certain that it will not have

 // a let child so we simply assign this

 // node's right pointer, which can be

 // either null or not, to its parent's left

 // pointer. This statement is

 // just doing the task of deleting the node

 prev1.left = temp1.right;

 // recursively call the merge

 // function with updated tree

 merge(root1, root2);

 }

 }

 else

 {

 System.out.print(temp2.data + " ");

 // If the node has no parent, that

 // means this node is the root

 if (prev2 == null)

 {

 

 // Simply make the right child

 // of root as new root

 merge(root1, root2.right);

 }

 // If node has a parent

 else

 {

 prev2.left = temp2.right;

 // Recursively call the merge

 // function with updated tree

 merge(root1, root2);

 }

 }

}

// Driver Code

public static void main(String args[])

{

 Node root1 = null, root2 = null;

 

 root1 = newNode(3);

 root1.left = newNode(1);

 root1.right = newNode(5);

 

 root2 = newNode(4);

 root2.left = newNode(2);

 root2.right = newNode(6);

 // Print sorted nodes of both trees

 merge(root1, root2);

}

}

// This code is contributed by ipg2016107  
  
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

# Python3 implementation of above approach

# Node of the binary tree

class node:

 

 def __init__ (self, key):

 

 self.data = key

 self.left = None

 self.right = None

# A utility function to print

# Inorder traversal of a Binary Tree

def inorder(root):

 

 if (root != None):

 inorder(root.left)

 print(root.data, end = " ")

 inorder(root.right)

# The function to print data

# of two BSTs in sorted order

def merge(root1, root2):

 

 # Base cases

 if (not root1 and not root2):

 return

 # If the first tree is exhausted

 # simply print the inorder

 # traversal of the second tree

 if (not root1):

 inorder(root2)

 return

 # If second tree is exhausted

 # simply print the inoreder

 # traversal of the first tree

 if (not root2):

 inorder(root1)

 return

 # A temporary pointer currently

 # pointing to root of first tree

 temp1 = root1

 # previous pointer to store the

 # parent of temporary pointer

 prev1 = None

 # Traverse through the first tree

 # until you reach the leftmost

 # element, which is the first element

 # of the tree in the inorder traversal.

 # This is the least element of the tree

 while (temp1.left):

 prev1 = temp1

 temp1 = temp1.left

 # Another temporary pointer currently

 # pointing to root of second tree

 temp2 = root2

 # Previous pointer to store the

 # parent of second temporary pointer

 prev2 = None

 # Traverse through the second tree

 # until you reach the leftmost element,

 # which is the first element of the

 # tree in inorder traversal. This is

 # the least element of the tree.

 while (temp2.left):

 prev2 = temp2

 temp2 = temp2.left

 # Compare the least current least

 # elements of both the tree

 if (temp1.data <= temp2.data):

 # If first tree's element is

 # smaller print it

 print(temp1.data, end = " ")

 # If the node has no parent, that

 # means this node is the root

 if (prev1 == None):

 # Simply make the right

 # child of the root as new root

 merge(root1.right, root2)

 # If node has a parent

 else:

 # As this node is the leftmost node,

 # it is certain that it will not have

 # a let child so we simply assign this

 # node's right pointer, which can be

 # either null or not, to its parent's left

 # pointer. This statement is

 # just doing the task of deleting the node

 prev1.left = temp1.right

 # recursively call the merge

 # function with updated tree

 merge(root1, root2)

 else:

 print(temp2.data, end = " ")

 # If the node has no parent, that

 # means this node is the root

 if (prev2 == None):

 # Simply make the right child

 # of root as new root

 merge(root1, root2.right)

 # If node has a parent

 else:

 prev2.left = temp2.right

 # Recursively call the merge

 # function with updated tree

 merge(root1, root2)

# Driver Code

if __name__ == '__main__':

 root1 = None

 root2 = None

 root1 = node(3)

 root1.left = node(1)

 root1.right = node(5)

 root2 = node(4)

 root2.left = node(2)

 root2.right = node(6)

 # Print sorted nodes of both trees

 merge(root1, root2)

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

// C# implementation of above approach

using System;

// Structure of a BST Node

public class Node

{

 public int data;

 public Node left, right;

 

 public Node(int item)

 {

 data = item;

 left = right = null;

 }

}

class GFG{

 

static Node root1;

static Node root2;

// A utility function to print

// Inorder traversal of a Binary Tree

static void inorder(Node root)

{

 if (root != null)

 {

 inorder(root.left);

 Console.WriteLine(root.data + " ");

 inorder(root.right);

 }

}

// The function to print data

// of two BSTs in sorted order

static void merge(Node root1, Node root2)

{

 

 // Base cases

 if (root1 == null && root2 == null)

 {

 return;

 }

 

 // If the first tree is exhausted

 // simply print the inorder traversal

 // of the second tree

 if (root1 == null)

 { 

 inorder(root2);

 return;

 }

 

 // If second tree is exhausted

 // simply print the inoreder

 // traversal of the first tree

 if (root2 == null)

 {

 inorder(root1);

 return;

 }

 

 // A temporary pointer currently

 // pointing to root of first tree

 Node temp1 = root1;

 

 // previous pointer to store the

 // parent of temporary pointer

 Node prev1 = null;

 

 // Traverse through the first tree

 // until you reach the leftmost element,

 // which is the first element of the tree

 // in the inorder traversal.

 // This is the least element of the tree

 while (temp1.left != null)

 {

 prev1 = temp1;

 temp1 = temp1.left;

 }

 

 // Another temporary pointer currently

 // pointing to root of second tree

 Node temp2 = root2;

 

 // Previous pointer to store the

 // parent of second temporary pointer

 Node prev2 = null;

 

 // Traverse through the second tree until

 // you reach the leftmost element, which

 // is the first element of the tree in

 // inorder traversal. This is the least

 // element of the tree.

 while (temp2.left != null)

 {

 prev2 = temp2;

 temp2 = temp2.left;

 }

 

 // Compare the least current least

 // elements of both the tree

 if (temp1.data <= temp2.data)

 {

 

 // If first tree's element is

 // smaller print it

 Console.Write(temp1.data + " ");

 

 // If the node has no parent, that

 // means this node is the root

 if (prev1 == null)

 {

 

 // Simply make the right

 // child of the root as new root

 merge(root1.right, root2);

 }

 

 // If node has a parent

 else

 {

 

 // As this node is the leftmost node,

 // it is certain that it will not have

 // a let child so we simply assign this

 // node's right pointer, which can be

 // either null or not, to its parent's

 // left pointer. This statement is just

 // doing the task of deleting the node

 prev1.left = temp1.right;

 

 // Recursively call the merge

 // function with updated tree

 merge(root1, root2);

 }

 }

 else

 {

 Console.Write(temp2.data + " ");

 

 // If the node has no parent, that

 // means this node is the root

 if (prev2 == null)

 {

 

 // Simply make the right child

 // of root as new root

 merge(root1, root2.right);

 }

 

 // If node has a parent

 else

 {

 prev2.left = temp2.right;

 

 // Recursively call the merge

 // function with updated tree

 merge(root1, root2);

 }

 }

}

// Driver Code

static public void Main()

{

 GFG.root1 = new Node(3);

 GFG.root1.left = new Node(1);

 GFG.root1.right = new Node(5);

 

 GFG.root2 = new Node(4);

 GFG.root2.left = new Node(2);

 GFG.root2.right = new Node(6);

 

 // Print sorted nodes of both trees

 merge(root1, root2);

}

}

// This code is contributed by avanitrachhadiya2155  
  
---  
  
 __

 __

 **Output:**

    
    
    1 2 3 4 5 6

**Time Complexity:** O((M+N)(h1+h2)), where M and N are the number of nodes of
the two trees and, h1 and h2 are the heights of tree respectively.  
**Auxiliary Space:** O(1)  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save


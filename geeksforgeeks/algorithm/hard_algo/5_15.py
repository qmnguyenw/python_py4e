Reverse tree path using Queue



Given a tree and a node, the task is to reverse the path till the given Node
and print the in-order traversal of the modified tree.  
 **Examples:**  

    
    
    **Input:**  
                 7
               /   \
              6     5
             / \   / \
            4   3 2   1    
    Node = 4 
    **Output:** 7 6 3 4 2 5 1
    The path from root to node 4 is 7 -> 6 -> 4
    Reversing this path, the modified tree will be:
                 4
               /   \
              6     5
             / \   / \
            7   3 2   1 
    whose in-order traversal is 7 6 3 4 2 5 1
    
    **Input:**
                7
             /    \
            6       5
           / \     / \
          4  3     2  1   
    Node = 2 
    **Output:** 4 6 3 2 7 5 1
    
    

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:**

  * First store all the nodes on the given path in a queue.
  * If the key is found then replace this node data with the front of queue data and pop the front.
  * Keep on performing this operation in a recursive way up to the root and the path will be reversed in the original tree.
  * Now, print the in-order traversal of the modified tree.

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

// A Binary Tree Node

struct Node {

 int data;

 struct Node *left, *right;

};

// Function to reverse the tree path

queue<int> reverseTreePathUtil(Node* root, int data,

 queue<int> q1)

{

 queue<int> emptyQueue;

 // If root is null then return

 // an empty queue

 if (root == NULL)

 return emptyQueue;

 // If the node is found

 if (root->data == data) {

 // Replace it with the queue's front

 q1.push(root->data);

 root->data = q1.front();

 q1.pop();

 return q1;

 }

 // Push data into the queue for

 // storing data from start to end

 q1.push(root->data);

 // If the returned queue is empty then

 // it means that the left sub-tree doesn't

 // contain the required node

 queue<int> left = reverseTreePathUtil(root->left,

 data, q1);

 // If the returned queue is empty then

 // it means that the right sub-tree doesn't

 // contain the required node

 queue<int> right = reverseTreePathUtil(root->right,

 data, q1);

 // If the required node is found

 // in the right sub-tree

 if (!right.empty()) {

 // Replace with the queue's front

 root->data = right.front();

 right.pop();

 return right;

 }

 // If the required node is found

 // in the right sub-tree

 if (!left.empty()) {

 // Replace with the queue's front

 root->data = left.front();

 left.pop();

 return left;

 }

 // Return emptyQueue if path

 // is not found

 return emptyQueue;

}

// Function to call reverseTreePathUtil

// to reverse the tree path

void reverseTreePath(Node* root, int data)

{

 queue<int> q1;

 // reverse tree path

 reverseTreePathUtil(root, data, q1);

}

// Function to print the in-order

// traversal of the tree

void inorder(Node* root)

{

 if (root != NULL) {

 inorder(root->left);

 cout << root->data << " ";

 inorder(root->right);

 }

}

// Utility function to create a new tree node

Node* newNode(int data)

{

 Node* temp = new Node;

 temp->data = data;

 temp->left = temp->right = NULL;

 return temp;

}

// Driver code

int main()

{

 Node* root = newNode(7);

 root->left = newNode(6);

 root->right = newNode(5);

 root->left->left = newNode(4);

 root->left->right = newNode(3);

 root->right->left = newNode(2);

 root->right->right = newNode(1);

 int data = 4;

 // Function call to reverse the path

 reverseTreePath(root, data);

 // Print the in-order traversal

 // of the modified tree

 inorder(root);

 return 0;

}  
  
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

# Python3 implementation of the

# above approach

 

# A Binary Tree Node

class Node:

 

 def __init__(self, data):

 

 self.data = data

 self.left = None

 self.right = None

 

# Function to reverse the

# tree path

def reverseTreePathUtil(root,

 data, q1):

 emptyQueue = []

 

 # If root is null then

 # return an empty queue

 if (root == None):

 return emptyQueue;

 

 # If the node is found

 if (root.data == data):

 

 # Replace it with the

 # queue's front

 q1.append(root.data);

 root.data = q1[0]

 q1.pop(0);

 return q1; 

 

 # Push data into the

 # queue for storing

 # data from start to end

 q1.append(root.data);

 

 # If the returned queue

 # is empty then it means

 # that the left sub-tree

 # doesn't contain the

 # required node

 left = reverseTreePathUtil(root.left,

 data, q1);

 

 # If the returned queue is empty

 # then it means that the right

 # sub-tree doesn't contain the

 # required node

 right = reverseTreePathUtil(root.right,

 data, q1);

 

 # If the required node is found

 # in the right sub-tree

 if len(right) != 0:

 

 # Replace with the queue's

 # front

 root.data = right[0]

 right.pop(0);

 return right;

 

 # If the required node

 # is found in the right

 # sub-tree

 if len(left) != 0:

 

 # Replace with the

 # queue's front

 root.data = left[0]

 left.pop(0);

 return left;

 

 # Return emptyQueue

 # if path is not found

 return emptyQueue;

 

# Function to call reverseTreePathUtil

# to reverse the tree path

def reverseTreePath(root, data):

 q1 = []

 

 # reverse tree path

 reverseTreePathUtil(root,

 data, q1);

 

# Function to print the in-order

# traversal of the tree

def inorder(root):

 if (root != None):

 inorder(root.left);

 print(root.data,

 end = ' ')

 inorder(root.right);

 

# Utility function to create

# a new tree node

def newNode(data):

 temp = Node(data)

 return temp;

# Driver code

if __name__ == "__main__":

 

 root = newNode(7);

 root.left = newNode(6);

 root.right = newNode(5);

 root.left.left = newNode(4);

 root.left.right = newNode(3);

 root.right.left = newNode(2);

 root.right.right = newNode(1);

 

 data = 4;

 

 # Function call to reverse

 # the path

 reverseTreePath(root, data);

 

 # Print the in-order traversal

 # of the modified tree

 inorder(root);

 

# This code is contributed by Rutvik_56  
  
---  
  
 __

 __

 **Output:**

    
    
    7 6 3 4 2 5 1
    
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save


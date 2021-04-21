Distribute candies in a Binary Tree



Given a binary tree with N nodes, in which each node value represents number
of candies present at that node, and there are N candies in total. In one
move, one may choose two adjacent nodes and move one candy from one node to
another (the move may be from parent to child, or from child to parent.)  
The task is to find the number of moves required such that every node have
**exactly one** candy.  
 **Examples:**  

    
    
    **Input** :      3
               /   \
              0     0 
    **Output :** 2
    **Explanation** : From the root of the tree, we move one 
    candy to its left child, and one candy to
    its right child.
    
    **Input** :      0
               /   \
              3     0  
    **Output :** 3
    **Explanation** : From the left child of the root, we move 
    two candies to the root [taking two moves]. Then, we move 
    one candy from the root of the tree to the right child.

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Recursive Solution:**  
The idea is to traverse the tree from leaf to root and consecutively balance
all of the nodes. To balance a node, the number of candy at that node must be
1.  
There can be two cases:  

  1. If a node needs candies, if the node of the tree has 0 candies (an excess of -1 from what it needs), then we should push a candy from its parent onto the node.
  2. If the node has more than 1 candy. If it has say, 4 candies (an excess of 3), then we should push 3 candies off the node to its parent.

So, the total number of moves from that leaf to or from its parent is excess =
**abs(num_candies – 1)**.  
Once a node is balanced, we never have to consider this node again in the rest
of our calculation.  
Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to distribute candies

// in a Binary Tree

#include <bits/stdc++.h>

using namespace std;

// Binary Tree Node

struct Node {

 int key;

 struct Node *left, *right;

};

// Utility function to create a new node

Node* newNode(int key)

{

 Node* temp = new Node;

 temp->key = key;

 temp->left = temp->right = NULL;

 return (temp);

}

// Utility function to find the number of

// moves to distribute all of the candies

int distributeCandyUtil(Node* root, int& ans)

{

 // Base Case

 if (root == NULL)

 return 0;

 // Traverse left subtree

 int l = distributeCandyUtil(root->left, ans);

 // Traverse right subtree

 int r = distributeCandyUtil(root->right, ans);

 // Update number of moves

 ans += abs(l) + abs(r);

 // Return number of moves to balance

 // current node

 return root->key + l + r - 1;

}

// Function to find the number of moves to

// distribute all of the candies

int distributeCandy(Node* root)

{

 int ans = 0;

 distributeCandyUtil(root, ans);

 return ans;

}

// Driver program

int main()

{

 /* 3

 / \

 0 0

 

 Let us create Binary Tree

 shown in above example */

 Node* root = newNode(3);

 root->left = newNode(0);

 root->right = newNode(0);

 cout << distributeCandy(root);

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

// Java program to distribute candies

// in a Binary Tree

class GfG {

 // Binary Tree Node

 static class Node {

 int key;

 Node left, right;

 }

 static int ans = 0;

 // Utility function to create a new node

 static Node newNode(int key)

 {

 Node temp = new Node();

 temp.key = key;

 temp.left = null;

 temp.right = null;

 return (temp);

 }

 // Utility function to find the number of

 // moves to distribute all of the candies

 static int distributeCandyUtil(Node root)

 {

 // Base Case

 if (root == null)

 return 0;

 // Traverse left subtree

 int l = distributeCandyUtil(root.left);

 // Traverse right subtree

 int r = distributeCandyUtil(root.right);

 // Update number of moves

 ans += Math.abs(l) + Math.abs(r);

 // Return number of moves to balance

 // current node

 return root.key + l + r - 1;

 }

 // Function to find the number of moves to

 // distribute all of the candies

 static int distributeCandy(Node root)

 {

 distributeCandyUtil(root);

 return ans;

 }

 // Driver program

 public static void main(String[] args)

 {

 /* 3

 / \

 0 0

 

 Let us create Binary Tree

 shown in above example */

 Node root = newNode(3);

 root.left = newNode(0);

 root.right = newNode(0);

 System.out.println(distributeCandy(root));

 }

}

// This code is contributed by Prerna Saini.  
  
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

# Python3 program to distribute candies

# in a Binary Tree

 

# Binary Tree Node

class Node:

 

 def __init__(self, key):

 

 self.key = key

 self.left = None

 self.right = None

 

# Utility function to create a new node

def newNode(key):

 temp = Node(key)

 return temp

 

# Utility function to find the number of

# moves to distribute all of the candies

def distributeCandyUtil( root, ans):

 # Base Case

 if (root == None):

 return 0, ans;

 

 # Traverse left subtree

 l,ans = distributeCandyUtil(root.left, ans);

 

 # Traverse right subtree

 r,ans = distributeCandyUtil(root.right, ans);

 

 # Update number of moves

 ans += abs(l) + abs(r);

 

 # Return number of moves to balance

 # current node

 return root.key + l + r - 1, ans;

 

# Function to find the number of moves to

# distribute all of the candies

def distributeCandy(root):

 ans = 0;

 

 tmp, ans = distributeCandyUtil(root, ans);

 

 return ans;

 

# Driver program

if __name__=='__main__':

 

 ''' 3

 / \

 0 0

 

 Let us create Binary Tree

 shown in above example '''

 

 root = newNode(3);

 root.left = newNode(0);

 root.right = newNode(0);

 

 print(distributeCandy(root))

 

# This code is contributed by pratham76  
  
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

// C# program to distribute candies

// in a Binary Tree

using System;

class GFG {

 // Binary Tree Node

 public class Node {

 public int key;

 public Node left, right;

 }

 static int ans = 0;

 // Utility function to create a new node

 static Node newNode(int key)

 {

 Node temp = new Node();

 temp.key = key;

 temp.left = null;

 temp.right = null;

 return (temp);

 }

 // Utility function to find the number of

 // moves to distribute all of the candies

 static int distributeCandyUtil(Node root)

 {

 // Base Case

 if (root == null)

 return 0;

 // Traverse left subtree

 int l = distributeCandyUtil(root.left);

 // Traverse right subtree

 int r = distributeCandyUtil(root.right);

 // Update number of moves

 ans += Math.Abs(l) + Math.Abs(r);

 // Return number of moves to balance

 // current node

 return root.key + l + r - 1;

 }

 // Function to find the number of moves to

 // distribute all of the candies

 static int distributeCandy(Node root)

 {

 distributeCandyUtil(root);

 return ans;

 }

 // Driver Code

 public static void Main(String[] args)

 {

 /* 3

 / \

 0 0

 

 Let us create Binary Tree

 shown in above example */

 Node root = newNode(3);

 root.left = newNode(0);

 root.right = newNode(0);

 Console.WriteLine(distributeCandy(root));

 }

}

// This code is contributed by 29AjayKumar  
  
---  
  
 __

 __

 **Output** :  

  

  

    
    
    2

**Iterative Solution :**  

**Approach :** At each node, some candies will come from the left and goes to
the right or comes from the right and goes to left. At each case, moves will
increase. So, for each node we will count number of required candies in the
right child and in left child **i.e (total number of node – total candies)**
for each child. It is possible that it might be **less than 0** but in that
case too it will counted as move because extra candies also has to travel
through the root node.  

Below is the implementation of the iterative approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to distribute

// candies in a Binary Tree

#include <bits/stdc++.h>

using namespace std;

// Binary Tree Node

struct Node {

 int key;

 struct Node *left, *right;

};

// Utility function to create a new node

Node* newNode(int key)

{

 Node* temp = new Node;

 temp->key = key;

 temp->left = temp->right = NULL;

 return (temp);

}

int countinchild(Node* root)

{

 // as node exists.

 if (root == NULL)

 return 0;

 int numberofnodes = 0; // to count total nodes.

 int sum = 0; // to count total candies present.

 queue<Node*> q;

 q.push(root);

 while (q.size() != 0) {

 Node* f = q.front();

 q.pop();

 numberofnodes++;

 sum += f->key;

 if (f->left)

 q.push(f->left);

 if (f->right)

 q.push(f->right);

 }

 // as either less than 0 or greater, it will be counted as

 // move as explained in the approach.

 return abs(numberofnodes - sum);

}

int distributeCandy(Node* root)

{

 // moves will count for total no. of moves.

 int moves = 0;

 // as 0 node and 0 value.

 if (root == NULL)

 return 0;

 // as leaf node don't have to pass any candies.

 if (!root->left && !root->right)

 return 0;

 // queue to iterate on tree .

 queue<Node*> q;

 q.push(root);

 while (q.size() != 0) {

 Node* f = q.front();

 q.pop();

 // total pass from left child

 moves += countinchild(f->left);

 // total pass from right child

 moves += countinchild(f->right);

 if (f->left)

 q.push(f->left);

 if (f->right)

 q.push(f->right);

 }

 return moves;

}

// Driver program

int main()

{

 /* 1

 / \

 0 2

 

 Let us create Binary Tree 

 shown in above example */

 Node* root = newNode(1);

 root->left = newNode(0);

 root->right = newNode(2);

 cout << distributeCandy(root);

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

# Python3 program to distribute

# candies in a Binary Tree

 

# Binary Tree Node

class Node:

 

 def __init__(self, key):

 

 self.key = key

 self.left = None

 self.right = None

 

# Utility function to create a new node

def newNode(key):

 temp = Node(key)

 return temp 

 

def countinchild(root):

 # as node exists.

 if (root == None):

 return 0;

 numberofnodes = 0; # to count total nodes.

 sum = 0; # to count total candies present.

 

 q = []

 q.append(root);

 

 while (len(q) != 0): 

 f = q[0];

 q.pop(0);

 

 numberofnodes += 1

 sum += f.key;

 

 if (f.left):

 q.append(f.left);

 if (f.right):

 q.append(f.right);

 

 # as either less than 0 or greater, it will be counted as

 # move as explained in the approach.

 return abs(numberofnodes - sum);

def distributeCandy(root):

 # moves will count for total no. of moves.

 moves = 0;

 

 # as 0 node and 0 value.

 if (root == None):

 return 0;

 

 # as leaf node don't have to pass any candies.

 if (not root.left and not root.right):

 return 0;

 

 # queue to iterate on tree .

 q = []

 q.append(root);

 

 while (len(q) != 0): 

 f = q[0];

 q.pop(0);

 

 # total pass from left child

 moves += countinchild(f.left);

 

 # total pass from right child

 moves += countinchild(f.right);

 

 if (f.left):

 q.append(f.left);

 if (f.right):

 q.append(f.right);

 

 return moves;

# Driver program

if __name__=='__main__':

 

 '''

 / 1

 / \

 0 2

 

 Let us create Binary Tree 

 shown in above example '''

 

 root = newNode(1);

 root.left = newNode(0);

 root.right = newNode(2);

 print(distributeCandy(root))

 

# This code is contributed by rutvik_56  
  
---  
  
 __

 __

  

**Output**

    
    
    2

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


Sum of all the child nodes with even grandparents in a Binary Tree



Given a **Binary Tree**, calculate the sum of nodes with even valued
Grandparents.  
 **Examples:**

    
    
    **Input:** 
          22
        /    \
       3      8
      / \    / \
     4   8  1   9
                 \
                  2
    **Output:** 24
    **Explanation** 
    The nodes 4, 8, 2, 1, 9
    has even value grandparents. 
    Hence sum = 4 + 8 + 1 + 9 + 2 = 24.
    
    **Input:**
            1
          /   \
         2     3
        / \   / \
       4   5 6   7
      /
     8
    **Output:** 8
    **Explanation** 
    Only 8 has 2 as a grandparent.
    
    
    
    

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:** To solve the problem mentioned above, for each node that is not
null, check if they have a grandparent and if their grandparent is even valued
add the node’s data to the sum.  
Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation to find sum

// of all the child nodes with

// even grandparents in a Binary Tree

#include <bits/stdc++.h>

using namespace std;

/* A binary tree node has data and

pointers to the right and left children*/

struct TreeNode {

 int data;

 TreeNode *left, *right;

 TreeNode(int x)

 {

 data = x;

 left = right = NULL;

 }

};

// Function to calculate the sum

void getSum(

 TreeNode* curr, TreeNode* p,

 TreeNode* gp, int& sum)

{

 // Base condition

 if (curr == NULL)

 return;

 // Check if node has a grandparent

 // if it does check

 // if they are even valued

 if (gp != NULL && gp->data % 2 == 0)

 sum += curr->data;

 // Recurse for left child

 getSum(curr->left, curr, p, sum);

 // Recurse for right child

 getSum(curr->right, curr, p, sum);

}

// Driver Program

int main()

{

 TreeNode* root = new TreeNode(22);

 root->left = new TreeNode(3);

 root->right = new TreeNode(8);

 root->left->left = new TreeNode(4);

 root->left->right = new TreeNode(8);

 root->right->left = new TreeNode(1);

 root->right->right = new TreeNode(9);

 root->right->right->right = new TreeNode(2);

 int sum = 0;

 getSum(root, NULL, NULL, sum);

 cout << sum << '\n';

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

// Java implementation to find sum

// of all the child nodes with

// even grandparents in a Binary Tree

import java.util.*;

class GFG{

/* A binary tree node has data and

pointers to the right and left children*/

static class TreeNode

{

 int data;

 TreeNode left, right;

 TreeNode(int x)

 {

 data = x;

 left = right = null;

 }

}

 

static int sum = 0;

 

// Function to calculate the sum

static void getSum(TreeNode curr,

 TreeNode p,

 TreeNode gp)

{

 // Base condition

 if (curr == null)

 return;

 // Check if node has

 // a grandparent

 // if it does check

 // if they are even valued

 if (gp != null && gp.data % 2 == 0)

 sum += curr.data;

 // Recurse for left child

 getSum(curr.left, curr, p);

 // Recurse for right child

 getSum(curr.right, curr, p);

}

// Driver Program

public static void main(String[] args)

{

 TreeNode root = new TreeNode(22);

 root.left = new TreeNode(3);

 root.right = new TreeNode(8);

 root.left.left = new TreeNode(4);

 root.left.right = new TreeNode(8);

 root.right.left = new TreeNode(1);

 root.right.right = new TreeNode(9);

 root.right.right.right = new TreeNode(2);

 getSum(root, null, null);

 System.out.println(sum);

}

}

// This code is contributed by Rajput-Ji  
  
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

# Python3 implementation to find sum

# of all the child nodes with

# even grandparents in a Binary Tree

# A binary tree node has data and

# pointers to the right and left children

class TreeNode():

 

 def __init__(self, data):

 

 self.data = data

 self.left = None

 self.right = None

sum = 0

# Function to calculate the sum

def getSum(curr, p, gp):

 

 global sum

 

 # Base condition

 if (curr == None):

 return

 

 # Check if node has a grandparent

 # if it does check

 # if they are even valued

 if (gp != None and gp.data % 2 == 0):

 sum += curr.data

 

 # Recurse for left child

 getSum(curr.left, curr, p)

 

 # Recurse for right child

 getSum(curr.right, curr, p)

 

# Driver code

if __name__=="__main__":

 

 root = TreeNode(22)

 

 root.left = TreeNode(3)

 root.right = TreeNode(8)

 

 root.left.left = TreeNode(4)

 root.left.right = TreeNode(8)

 

 root.right.left = TreeNode(1)

 root.right.right = TreeNode(9)

 root.right.right.right = TreeNode(2)

 

 getSum(root, None, None)

 

 print(sum)

# This code is contributed by rutvik_56  
  
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

// C# implementation to find sum

// of all the child nodes with

// even grandparents in a Binary Tree

using System;

class GFG{

/* A binary tree node

has data and pointers to

the right and left children*/

class TreeNode

{

 public int data;

 public TreeNode left, right;

 public TreeNode(int x)

 {

 data = x;

 left = right = null;

 }

}

 

static int sum = 0;

 

// Function to calculate the sum

static void getSum(TreeNode curr,

 TreeNode p,

 TreeNode gp)

{

 // Base condition

 if (curr == null)

 return;

 // Check if node has

 // a grandparent

 // if it does check

 // if they are even valued

 if (gp != null && gp.data % 2 == 0)

 sum += curr.data;

 // Recurse for left child

 getSum(curr.left, curr, p);

 // Recurse for right child

 getSum(curr.right, curr, p);

}

// Driver Program

public static void Main(String[] args)

{

 TreeNode root = new TreeNode(22);

 root.left = new TreeNode(3);

 root.right = new TreeNode(8);

 root.left.left = new TreeNode(4);

 root.left.right = new TreeNode(8);

 root.right.left = new TreeNode(1);

 root.right.right = new TreeNode(9);

 root.right.right.right = new TreeNode(2);

 getSum(root, null, null);

 Console.WriteLine(sum);

}

}

// This code is contributed by Princi Singh  
  
---  
  
 __

 __

 **Output:**

    
    
    24
    
    
    
    
    
    
    
    
    

_**Time Complexity:** O(N)_  
 _ **Space Complexity:** O(H)_, Used by recursion stack where H = height of
the tree.

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save


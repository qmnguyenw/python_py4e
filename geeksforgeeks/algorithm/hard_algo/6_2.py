Cartesian tree from inorder traversal | Segment Tree



Given an in-order traversal of a cartesian tree, the task is to build the
entire tree from it.

 **Examples:**

    
    
    **Input:** arr[] = {1, 5, 3}
    **Output:** 1 5 3
      5
     / \
    1   3
    
    **Input:** arr[] = {3, 7, 4, 8}
    **Output:** 3 7 4 8
         8
        /
       7
      / \
     3   4
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** We have already seen an algorithm here that takes O(NlogN) time
on an average but can get to O(N2) in the worst case.

In this article, we will see how to build the cartesian in worst case running
time of **O(Nlog(N))**. For this, we will use segment-tree to answer range-max
queries.

Below will be our recursive algorithm on range {L, R}:

  

  

  1. Find the maximum in this range {L, R} using range-max query on the segment-tree. Let’s say ‘M’ is index the maximum in the range.
  2. Pick up ‘arr[M]’ as the value for current node and create a node with this value.
  3. Solve for range {L, M-1} and {M+1, R}.
  4. Set the node returned by {L, M-1} as the left child of current node and {M+1, R} as the right child.

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

 

#define maxLen 30

 

// Node of the BST

struct node {

 int data;

 node* left;

 node* right;

 node(int data)

 {

 left = NULL;

 right = NULL;

 this->data = data;

 }

};

 

// Array to store segment tree

int segtree[maxLen * 3];

 

// Function to create segment-tree to answer

// range-max query

int buildTree(int l, int r, int i, int* arr)

{

 // Base case

 if (l == r) {

 segtree[i] = l;

 return l;

 }

 

 // Maximum index in left range

 int l1 = buildTree(l, (l + r) / 2,

 2 * i + 1, arr);

 

 // Maximum index in right range

 int r1 = buildTree((l + r) / 2 + 1,

 r, 2 * i + 2, arr);

 

 // If value at l1 > r1

 if (arr[l1] > arr[r1])

 segtree[i] = l1;

 

 // Else

 else

 segtree[i] = r1;

 

 // Returning the maximum in range

 return segtree[i];

}

 

// Function to answer range max query

int rangeMax(int l, int r, int rl,

 int rr, int i, int* arr)

{

 

 // Base cases

 if (r < rl || l > rr)

 return -1;

 if (l >= rl and r <= rr)

 return segtree[i];

 

 // Maximum in left range

 int l1 = rangeMax(l, (l + r) / 2, rl,

 rr, 2 * i + 1, arr);

 

 // Maximum in right range

 int r1 = rangeMax((l + r) / 2 + 1, r,

 rl, rr, 2 * i + 2, arr);

 

 // l1 = -1 means left range

 // was out-side required range

 if (l1 == -1)

 return r1;

 if (r1 == -1)

 return l1;

 

 // Returning the maximum

 // among two ranges

 if (arr[l1] > arr[r1])

 return l1;

 else

 return r1;

}

 

// Function to print the inorder

// traversal of the binary tree

void inorder(node* curr)

{

 

 // Base case

 if (curr == NULL)

 return;

 

 // Traversing the left sub-tree

 inorder(curr->left);

 

 // Printing current node

 cout << curr->data << " ";

 

 // Traversing the right sub-tree

 inorder(curr->right);

}

 

// Function to build cartesian tree

node* createCartesianTree(int l, int r, int* arr, int n)

{

 // Base case

 if (r < l)

 return NULL;

 

 // Maximum in the range

 int m = rangeMax(0, n - 1, l, r, 0, arr);

 

 // Creating current node

 node* curr = new node(arr[m]);

 

 // Creating left sub-tree

 curr->left = createCartesianTree(l, m - 1, arr, n);

 

 // Creating right sub-tree

 curr->right = createCartesianTree(m + 1, r, arr, n);

 

 // Returning current node

 return curr;

}

 

// Driver code

int main()

{

 // In-order traversal of cartesian tree

 int arr[] = { 8, 11, 21, 100, 5, 70, 55 };

 

 // Size of the array

 int n = sizeof(arr) / sizeof(int);

 

 // Building the segment tree

 buildTree(0, n - 1, 0, arr);

 

 // Building and printing cartesian tree

 inorder(createCartesianTree(0, n - 1, arr, n));

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

static int maxLen = 30;

 

// Node of the BST

static class node

{

 int data;

 node left;

 node right;

 node(int data)

 {

 left = null;

 right = null;

 this.data = data;

 }

};

 

// Array to store segment tree

static int segtree[] = new int[maxLen * 3];

 

// Function to create segment-tree to answer

// range-max query

static int buildTree(int l, int r, 

 int i, int[] arr)

{

 // Base case

 if (l == r) 

 {

 segtree[i] = l;

 return l;

 }

 

 // Maximum index in left range

 int l1 = buildTree(l, (l + r) / 2,

 2 * i + 1, arr);

 

 // Maximum index in right range

 int r1 = buildTree((l + r) / 2 + 1,

 r, 2 * i + 2, arr);

 

 // If value at l1 > r1

 if (arr[l1] > arr[r1])

 segtree[i] = l1;

 

 // Else

 else

 segtree[i] = r1;

 

 // Returning the maximum in range

 return segtree[i];

}

 

// Function to answer range max query

static int rangeMax(int l, int r, int rl,

 int rr, int i, int[] arr)

{

 

 // Base cases

 if (r < rl || l > rr)

 return -1;

 if (l >= rl && r <= rr)

 return segtree[i];

 

 // Maximum in left range

 int l1 = rangeMax(l, (l + r) / 2, rl,

 rr, 2 * i + 1, arr);

 

 // Maximum in right range

 int r1 = rangeMax((l + r) / 2 + 1, r,

 rl, rr, 2 * i + 2, arr);

 

 // l1 = -1 means left range

 // was out-side required range

 if (l1 == -1)

 return r1;

 if (r1 == -1)

 return l1;

 

 // Returning the maximum

 // among two ranges

 if (arr[l1] > arr[r1])

 return l1;

 else

 return r1;

}

 

// Function to print the inorder

// traversal of the binary tree

static void inorder(node curr)

{

 

 // Base case

 if (curr == null)

 return;

 

 // Traversing the left sub-tree

 inorder(curr.left);

 

 // Printing current node

 System.out.print(curr.data + " ");

 

 // Traversing the right sub-tree

 inorder(curr.right);

}

 

// Function to build cartesian tree

static node createCartesianTree(int l, int r,

 int[] arr, int n)

{

 // Base case

 if (r < l)

 return null;

 

 // Maximum in the range

 int m = rangeMax(0, n - 1, l, r, 0, arr);

 

 // Creating current node

 node curr = new node(arr[m]);

 

 // Creating left sub-tree

 curr.left = createCartesianTree(l, m - 1, arr, n);

 

 // Creating right sub-tree

 curr.right = createCartesianTree(m + 1, r, arr, n);

 

 // Returning current node

 return curr;

}

 

// Driver code

public static void main(String args[])

{

 // In-order traversal of cartesian tree

 int arr[] = { 8, 11, 21, 100, 5, 70, 55 };

 

 // Size of the array

 int n = arr.length;

 

 // Building the segment tree

 buildTree(0, n - 1, 0, arr);

 

 // Building && printing cartesian tree

 inorder(createCartesianTree(0, n - 1, arr, n));

}

}

 

// This code is contributed by Arnab Kundu  
  
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

 

# Node of a linked list 

class Node: 

 def __init__(self, data = None, left = None,

 right = None ): 

 self.data = data

 self.right = right

 self.left = left

 

maxLen = 30

 

# Array to store segment tree

segtree = [0]*(maxLen * 3)

 

# Function to create segment-tree to answer

# range-max query

def buildTree(l , r ,i , arr):

 

 global segtree

 global maxLen

 

 # Base case

 if (l == r) :

 

 segtree[i] = l

 return l

 

 # Maximum index in left range

 l1 = buildTree(l, int((l + r) / 2),

 2 * i + 1, arr)

 

 # Maximum index in right range

 r1 = buildTree(int((l + r) / 2) + 1,r,

 2 * i + 2, arr)

 

 # If value at l1 > r1

 if (arr[l1] > arr[r1]):

 segtree[i] = l1

 

 # Else

 else:

 segtree[i] = r1

 

 # Returning the maximum in range

 return segtree[i]

 

# Function to answer range max query

def rangeMax(l, r, rl, rr, i, arr):

 

 global segtree

 global maxLen

 

 # Base cases

 if (r < rl or l > rr):

 return -1

 if (l >= rl and r <= rr):

 return segtree[i]

 

 # Maximum in left range

 l1 = rangeMax(l, int((l + r) / 2), rl, 

 rr, 2 * i + 1, arr)

 

 # Maximum in right range

 r1 = rangeMax(int((l + r) / 2) + 1, r, rl, 

 rr, 2 * i + 2, arr)

 

 # l1 = -1 means left range

 # was out-side required range

 if (l1 == -1):

 return r1

 if (r1 == -1):

 return l1

 

 # Returning the maximum

 # among two ranges

 if (arr[l1] > arr[r1]):

 return l1

 else:

 return r1

 

# Function to print the inorder

# traversal of the binary tree

def inorder(curr):

 

 # Base case

 if (curr == None):

 return

 

 # Traversing the left sub-tree

 inorder(curr.left)

 

 # Printing current node

 print(curr.data, end= " ")

 

 # Traversing the right sub-tree

 inorder(curr.right)

 

# Function to build cartesian tree

def createCartesianTree(l , r , arr, n):

 

 # Base case

 if (r < l):

 return None

 

 # Maximum in the range

 m = rangeMax(0, n - 1, l, r, 0, arr)

 

 # Creating current node

 curr = Node(arr[m])

 

 # Creating left sub-tree

 curr.left = createCartesianTree(l, m - 1, arr, n)

 

 # Creating right sub-tree

 curr.right = createCartesianTree(m + 1, r, arr, n)

 

 # Returning current node

 return curr

 

# Driver code

 

# In-order traversal of cartesian tree

arr = [ 8, 11, 21, 100, 5, 70, 55 ]

 

# Size of the array

n = len(arr)

 

# Building the segment tree

buildTree(0, n - 1, 0, arr)

 

# Building && printing cartesian tree

inorder(createCartesianTree(0, n - 1, arr, n))

 

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

 

class GFG 

{ 

 static int maxLen = 30; 

 

 // Node of the BST 

 public class node 

 { 

 public int data; 

 public node left; 

 public node right; 

 public node(int data) 

 { 

 left = null; 

 right = null; 

 this.data = data; 

 } 

 }; 

 

 // Array to store segment tree 

 static int []segtree = new int[maxLen * 3]; 

 

 // Function to create segment-tree to answer 

 // range-max query 

 static int buildTree(int l, int r, 

 int i, int[] arr) 

 { 

 // Base case 

 if (l == r) 

 { 

 segtree[i] = l; 

 return l; 

 } 

 

 // Maximum index in left range 

 int l1 = buildTree(l, (l + r) / 2, 

 2 * i + 1, arr); 

 

 // Maximum index in right range 

 int r1 = buildTree((l + r) / 2 + 1, 

 r, 2 * i + 2, arr); 

 

 // If value at l1 > r1 

 if (arr[l1] > arr[r1]) 

 segtree[i] = l1; 

 

 // Else 

 else

 segtree[i] = r1; 

 

 // Returning the maximum in range 

 return segtree[i]; 

 } 

 

 // Function to answer range max query 

 static int rangeMax(int l, int r, int rl, 

 int rr, int i, int[] arr) 

 { 

 

 // Base cases 

 if (r < rl || l > rr) 

 return -1; 

 if (l >= rl && r <= rr) 

 return segtree[i]; 

 

 // Maximum in left range 

 int l1 = rangeMax(l, (l + r) / 2, rl, 

 rr, 2 * i + 1, arr); 

 

 // Maximum in right range 

 int r1 = rangeMax((l + r) / 2 + 1, r, 

 rl, rr, 2 * i + 2, arr); 

 

 // l1 = -1 means left range 

 // was out-side required range 

 if (l1 == -1) 

 return r1; 

 if (r1 == -1) 

 return l1; 

 

 // Returning the maximum 

 // among two ranges 

 if (arr[l1] > arr[r1]) 

 return l1; 

 else

 return r1; 

 } 

 

 // Function to print the inorder 

 // traversal of the binary tree 

 static void inorder(node curr) 

 { 

 

 // Base case 

 if (curr == null) 

 return; 

 

 // Traversing the left sub-tree 

 inorder(curr.left); 

 

 // Printing current node 

 Console.Write(curr.data + " "); 

 

 // Traversing the right sub-tree 

 inorder(curr.right); 

 } 

 

 // Function to build cartesian tree 

 static node createCartesianTree(int l, int r, 

 int[] arr, int n) 

 { 

 // Base case 

 if (r < l) 

 return null; 

 

 // Maximum in the range 

 int m = rangeMax(0, n - 1, l, r, 0, arr); 

 

 // Creating current node 

 node curr = new node(arr[m]); 

 

 // Creating left sub-tree 

 curr.left = createCartesianTree(l, m - 1,

 arr, n); 

 

 // Creating right sub-tree 

 curr.right = createCartesianTree(m + 1, r, 

 arr, n); 

 

 // Returning current node 

 return curr; 

 } 

 

 // Driver code 

 public static void Main() 

 { 

 // In-order traversal of cartesian tree 

 int []arr = { 8, 11, 21, 100, 5, 70, 55 }; 

 

 // Size of the array 

 int n = arr.Length; 

 

 // Building the segment tree 

 buildTree(0, n - 1, 0, arr); 

 

 // Building && printing cartesian tree 

 inorder(createCartesianTree(0, n - 1, arr, n)); 

 } 

}

 

// This code is contributed by AnkitRai01   
  
---  
  
__

__

**Output:**

    
    
    8 11 21 100 5 70 55
    

**Time complexity:** O(NlogN)

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save


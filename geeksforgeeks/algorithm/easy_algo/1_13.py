Count of root to leaf paths whose permutation is palindrome in a Binary Tree



Given a binary tree where node contains characters, the task is to count the
number of paths from root vertex to leaf such that at least one permutation of
the node values in the path is a palindrome.  
 **Examples:**

    
    
    **Input:** 
                       2
                     /   \
                    3     1
                  /   \     \
                 3     4     2
               /   \       /   \
              2     1     2     1
    
    **Output:** 2
    **Explanation:**
    Paths whose one of the
    permuation are palindrome are -
    2 => 3 => 3 => 2 and 
    2 => 1 => 2 => 1
    
    **Input:**
                    2
                  /   \
                 a     3
               /   \
              2     a
    **Output:** 2
    **Explanation:**
    Palindromic paths are 
    2 => a => 2 and 
    2 => a => a 
    
    
    
    
    
    

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:** The idea is to use pre-order traversal to traverse the binary
tree and keep track of the path. Whenever a leaf node is reached then check
that if any permutation of nodes values in the current path is a palindromic
path or not.  
To check the permutation of the values of the nodes is palindromic or not
maintain the frequency of each character using a map. The path will be
palindromic if the number of elements with odd frequency is at most 1.  
Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation to count of

// the path whose permutation is

// a palindromic path

#include <bits/stdc++.h>

using namespace std;

#define ll long long

// Map to store the frequency

map<char, int> freq;

int ans = 0;

// Structure of the node

struct Node {

 char val;

 struct Node *left, *right;

};

// Function to add new node

Node* newNode(char key)

{

 Node* temp = new Node;

 temp->val = key;

 temp->left = temp->right = NULL;

 return (temp);

}

// Function to check that the path

// is a palindrome or not

int checkPalin()

{

 int oddCount = 0;

 for (auto x : freq) {

 if (x.second % 2 == 1)

 oddCount++;

 }

 return oddCount <= 1;

}

// Function to count the root to

// leaf path whose permutation is

// a palindromic path

void cntpalin(Node* root)

{

 if (root == NULL)

 return;

 freq[root->val]++;

 if (root->left == NULL

 && root->right == NULL) {

 if (checkPalin() == true)

 ans++;

 }

 cntpalin(root->left);

 cntpalin(root->right);

 freq[root->val]--;

}

// Driver Code

int main()

{

 Node* root = newNode('2');

 root->left = newNode('a');

 root->left->right = newNode('a');

 root->left->left = newNode('2');

 root->left->right->right = newNode('2');

 root->right = newNode('3');

 // Function Call

 cntpalin(root);

 cout << ans << endl;

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

// Java implementation to count of

// the path whose permutation is

// a palindromic path

import java.util.*;

class GFG{

// Map to store the frequency

static HashMap<Character,

 Integer> freq =

 new HashMap<>();

static int ans = 0;

// Structure of the node

static class Node

{

 char val;

 Node left, right;

};

// Function to add new node

static Node newNode(char key)

{

 Node temp = new Node();

 temp.val = key;

 temp.left = temp.right = null;

 return (temp);

}

// Function to check that the path

// is a palindrome or not

static boolean checkPalin()

{

 int oddCount = 0;

 for (Map.Entry<Character,

 Integer> x : freq.entrySet())

 {

 if (x.getValue() % 2 == 1)

 oddCount++;

 }

 return oddCount <= 1 ? true : false;

}

// Function to count the root to

// leaf path whose permutation is

// a palindromic path

static void cntpalin(Node root)

{

 if (root == null)

 return;

 if(freq.containsKey(root.val))

 {

 freq.put(root.val,

 freq.get(root.val) + 1);

 }

 else

 {

 freq.put(root.val, 1);

 }

 if (root.left == null &&

 root.right == null)

 {

 if (checkPalin() == true)

 ans++;

 }

 

 cntpalin(root.left);

 cntpalin(root.right);

 

 if(freq.containsKey(root.val))

 {

 freq.put(root.val,

 freq.get(root.val) - 1);

 }

}

// Driver Code

public static void main(String[] args)

{

 Node root = newNode('2');

 root.left = newNode('a');

 root.left.right = newNode('a');

 root.left.left = newNode('2');

 root.left.right.right = newNode('2');

 root.right = newNode('3');

 // Function Call

 cntpalin(root);

 System.out.print(ans + "\n");

}

}

// This code is contributed by Princi Singh  
  
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

# Python3 program for the

# above approach

from collections import deque

# A Tree node

class Node:

 

 def __init__(self, x):

 

 self.data = x

 self.left = None

 self.right = None

 

freq = {}

ans = 0

# Function to check that the path

# is a palindrome or not

def checkPalin():

 

 oddCount = 0

 

 for x in freq:

 if (freq[x] % 2 == 1):

 oddCount+=1

 return oddCount <= 1

# Function to count the root to

# leaf path whose permutation is

# a palindromic path

def cntpalin(root):

 

 global freq, ans

 

 if (root == None):

 return

 

 freq[root.data] = freq.get(root.data,

 0) + 1

 if (root.left == None

 and root.right == None):

 if (checkPalin() == True):

 ans += 1

 

 cntpalin(root.left)

 cntpalin(root.right)

 freq[root.data] -= 1

# Driver Code

if __name__ == '__main__':

 

 root = Node('2')

 root.left = Node('a')

 root.left.right = Node('a')

 root.left.left = Node('2')

 root.left.right.right = Node('2')

 root.right = Node('3')

 # Function Call

 cntpalin(root)

 print(ans)

# This code is contributed by Rutvik_56  
  
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

// C# implementation to count of

// the path whose permutation is

// a palindromic path

using System;

using System.Collections.Generic;

class GFG{

// Map to store the frequency

static Dictionary<char,

 int> freq = new Dictionary<char,

 int>();

static int ans = 0;

// Structure of the node

public class Node

{

 public char val;

 public Node left,

 right;

};

// Function to add new node

static Node newNode(char key)

{

 Node temp = new Node();

 temp.val = key;

 temp.left = temp.right = null;

 return (temp);

}

// Function to check that

// the path is a palindrome

// or not

static bool checkPalin()

{

 int oddCount = 0;

 foreach (KeyValuePair<char,

 int> x in freq)

 {

 if (x.Value % 2 == 1)

 oddCount++;

 }

 return oddCount <= 1 ? true : false;

}

// Function to count the root to

// leaf path whose permutation is

// a palindromic path

static void cntpalin(Node root)

{

 if (root == null)

 return;

 if(freq.ContainsKey(root.val))

 {

 freq[root.val] = freq[root.val] + 1;

 }

 else

 {

 freq.Add(root.val, 1);

 }

 if (root.left == null &&

 root.right == null)

 {

 if (checkPalin() == true)

 ans++;

 }

 

 cntpalin(root.left);

 cntpalin(root.right);

 

 if(freq.ContainsKey(root.val))

 {

 freq[root.val] = freq[root.val] - 1;

 }

}

// Driver Code

public static void Main(String[] args)

{

 Node root = newNode('2');

 root.left = newNode('a');

 root.left.right = newNode('a');

 root.left.left = newNode('2');

 root.left.right.right = newNode('2');

 root.right = newNode('3');

 // Function Call

 cntpalin(root);

 Console.Write(ans + "\n");

}

}

// This code is contributed by Amit Katiyar  
  
---  
  
 __

 __

 **Output:**

    
    
    2
    
    
    
    
    
    
    
    
    
    
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save


Sum of all Palindrome Numbers present in a Linked list



Given a linked list with integer node values, the task is to find the sum of
all **Palindrome Numbers** present as Node values.

 **Examples:**

>  **Input:** 13 -> 212 -> 22 -> 44 -> 4 -> 3  
>  **Output:** 285  
>  **Explanation:** The sum of palindrome numbers {22, 212, 44, 4, 3} is 285
>
>  **Input:** 19 -> 22 -> 141  
>  **Output:** 163

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** In order to solve this problem we are using an approach similar
to calculate the Sum of all Palindromes in an Array. Iterate through all the
nodes of the linked list and check if the current node value is a palindrome
or not. If so, add the value and store the sum. The final sum of all such
values gives the desired answer.

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to calculate

// the sum of all palindromic

// numbers in a linked list

 

#include <bits/stdc++.h>

using namespace std;

 

// Node of the singly

// linked list

struct Node {

 int data;

 Node* next;

};

 

// Function to insert a node at

// the beginning of the singly

// Linked List

void push(Node** head_ref, int new_data)

{

 // allocate node

 Node* new_node = (Node*)malloc(

 sizeof(struct Node));

 

 // Insert the data

 new_node->data = new_data;

 

 // Point the new Node

 // to the current head

 new_node->next = (*head_ref);

 

 // Make the new Node as

 // the new head

 (*head_ref) = new_node;

}

 

// Function to check

// if a number n is

// palindrome or not

bool isPalin(int n)

{

 int d = 0, s = 0;

 int temp = n;

 while (n > 0) {

 d = n % 10;

 s = s * 10 + d;

 n = n / 10;

 }

 

 // If n is equal to

 // the its reverse

 // it is a palindrome

 return temp == s;

}

 

// Function to calculate

// the sum of all nodes

// which are palindrome

int sumOfpal(Node* head_1)

{

 int s = 0;

 Node* ptr = head_1;

 while (ptr != NULL) {

 

 // If the value of the

 // current node is

 // a palindrome

 if (isPalin(ptr->data)) {

 

 // Add the value

 // to the sum

 s += ptr->data;

 }

 ptr = ptr->next;

 }

 return s;

}

 

// Driver Code

int main()

{

 // Create the head

 // of the linked list

 Node* head1 = NULL;

 

 // Insert nodes into

 // the linked list

 push(&head1;, 13);

 push(&head1;, 212);

 push(&head1;, 22);

 push(&head1;, 44);

 push(&head1;, 4);

 push(&head1;, 3);

 

 // Print the sum of all

 // palindromes

 cout << sumOfpal(head1)

 << endl;

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

// Java program to calculate

// the sum of all palindromes

// in a linked list

 

import java.util.*;

 

class GFG {

 

 // Node of the singly

 // linked list

 static class Node {

 int data;

 Node next;

 };

 

 // Function to insert a node

 // at the beginning of the

 // singly Linked List

 static Node push(Node head_ref,

 int new_data)

 {

 // Allocate node

 Node new_node = new Node();

 

 // Insert the data

 new_node.data = new_data;

 

 // Point the current Node

 // to the current head

 new_node.next = (head_ref);

 

 // Make the current node

 // as the new head

 (head_ref) = new_node;

 

 return head_ref;

 }

 

 // Function to check if

 // a number is palindrome

 static boolean isPalin(int n)

 {

 int d = 0, s = 0;

 int temp = n;

 while (n > 0) {

 d = n % 10;

 s = s * 10 + d;

 n = n / 10;

 }

 // If n is equal to its

 // reverse, it is a

 // palindrome

 return temp == s;

 }

 

 // Function to calculate sum

 // of all nodes with value

 // which is a palindrome

 static int sumOfpal(Node head_1)

 {

 int s = 0;

 Node ptr = head_1;

 while (ptr != null) {

 // If the value of the

 // current node

 // is a palindrome

 if (isPalin(ptr.data)) {

 

 // Add that value to

 // the sum

 s += ptr.data;

 }

 ptr = ptr.next;

 }

 

 // Return the sum

 return s;

 }

 

 // Driver Code

 public static void main(String args[])

 {

 // Create the head

 Node head1 = null;

 

 // Insert nodes to the

 // Linked List

 head1 = push(head1, 13);

 head1 = push(head1, 212);

 head1 = push(head1, 22);

 head1 = push(head1, 44);

 head1 = push(head1, 4);

 head1 = push(head1, 3);

 

 System.out.println(

 sumOfpal(head1));

 }

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

# Python3 program to

# calculate the sum of all 

# palindromes present in 

# a Linked List

 

class Node: 

 

 def __init__(self, data): 

 self.data = data 

 self.next = next

 

# Function to insert a 

# node at the beginning 

# of the singly Linked List 

def push( head_ref, new_data) : 

 

 # Alocate node 

 new_node = Node(0) 

 

 # Insert data 

 new_node.data = new_data 

 

 # Pont to the head 

 new_node.next = (head_ref) 

 

 # Make the new Node

 # the new head

 (head_ref) = new_node 

 

 return head_ref

 

 

# Function to check if 

# a number is palindrome 

def isPalin(n) : 

 

 d = 0; s = 0; 

 temp = n;

 while (n > 0) : 

 

 d = n % 10; 

 s = s * 10 + d; 

 n = n // 10; 

 

 # If n is equal to its reverse, 

 # it is a palindrome 

 return s == temp; 

 

 

# Function to calculate sum of 

# all elements in a Linked List 

# which are palindrome 

def sumOfpal(head_ref1) : 

 

 s = 0; 

 ptr1 = head_ref1

 

 while (ptr1 != None) :

 # If the value of the 

 # current node 

 # is a palindrome

 if (isPalin(ptr1.data)) :

 

 # Add that value

 s = s + ptr1.data

 

 # Move to the next node

 ptr1 = ptr1.next

 

 # Return the final sum

 return s; 

 

# Driver code 

 

# Create the Head

head1 = None

 

# Insert nodes 

head1 = push(head1, 13) 

head1 = push(head1, 212) 

head1 = push(head1, 22) 

head1 = push(head1, 44) 

head1 = push(head1, 4)

head1 = push(head1, 3)

 

print(sumOfpal(head1))  
  
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

// C# program to calculate

// the sum of all palindromes

// in a linked list

using System;

 

class GFG {

 

// Node of the singly

// linked list

class Node

{

 public int data;

 public Node next;

};

 

// Function to insert a node

// at the beginning of the

// singly Linked List

static Node push(Node head_ref,

 int new_data)

{

 

 // Allocate node

 Node new_node = new Node();

 

 // Insert the data

 new_node.data = new_data;

 

 // Point the current Node

 // to the current head

 new_node.next = (head_ref);

 

 // Make the current node

 // as the new head

 (head_ref) = new_node;

 

 return head_ref;

}

 

// Function to check if

// a number is palindrome

static bool isPalin(int n)

{

 int d = 0, s = 0;

 int temp = n;

 

 while (n > 0)

 {

 d = n % 10;

 s = s * 10 + d;

 n = n / 10;

 }

 

 // If n is equal to its

 // reverse, it is a

 // palindrome

 return temp == s;

}

 

// Function to calculate sum

// of all nodes with value

// which is a palindrome

static int sumOfpal(Node head_1)

{

 int s = 0;

 Node ptr = head_1;

 

 while (ptr != null)

 {

 

 // If the value of the

 // current node

 // is a palindrome

 if (isPalin(ptr.data))

 {

 

 // Add that value to

 // the sum

 s += ptr.data;

 }

 ptr = ptr.next;

 }

 

 // Return the sum

 return s;

}

 

// Driver Code

public static void Main(String []args)

{

 

 // Create the head

 Node head1 = null;

 

 // Insert nodes to the

 // Linked List

 head1 = push(head1, 13);

 head1 = push(head1, 212);

 head1 = push(head1, 22);

 head1 = push(head1, 44);

 head1 = push(head1, 4);

 head1 = push(head1, 3);

 

 Console.WriteLine(sumOfpal(head1));

}

}

 

// This code is contributed by sapnasingh4991  
  
---  
  
 __

 __

 **Output:**

    
    
    285
    

Want to learn from the best curated videos and practice problems, check out
the **C++ Foundation Course **for Basic to Advanced C++ and **C++ STL Course**
for foundation plus STL. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save


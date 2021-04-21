Reverse a singly Linked List in groups of given size | Set 3



Given a singly linked list and an integer **K** , the task is to reverse every
**K** nodes of the given linked list.  
 **Examples:**

> **Input:** 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> NULL, K = 3  
> **Output:** 3 2 1 6 5 4 8 7
>
>  **Input:** 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> NULL, K = 5  
> **Output:** 5 4 3 2 1 8 7 6

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:** Two different approaches to solve this problem have been
discussed in Set 1 and Set 2 of this article. In this article, an approach
based on deque will be discussed.

  1. Create a deque.
  2. Store the address of the first k nodes in the deque.
  3. Pop first and the last value from the deque and swap the data values at those addresses.
  4. Repeat step 3 till the deque is not empty.
  5. Repeat step 2 for the next k nodes and till the end of the linked list is not reached.

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

 

// Link list node

struct node {

 int data;

 struct node* next;

};

 

// Function to insert a node at

// the head of the linked list

void push(node** head_ref, int new_data)

{

 /* Allocate node */

 node* new_node = new node();

 

 /* Put in the data */

 new_node->data = new_data;

 

 /* Link the old list off the new node */

 new_node->next = (*head_ref);

 

 /* Move the head to point to the new node */

 (*head_ref) = new_node;

}

 

// Function to print the linked list

void printList(node* head)

{

 while (head != NULL) {

 cout << head->data << " ";

 head = head->next;

 }

}

 

/* Function to reverse the linked list in groups of 

size k and return the pointer to the new head node. */

struct node* reverse(struct node* head, int k)

{

 

 if (head == NULL)

 return head;

 

 // Create deque to store the address

 // of the nodes of the linked list

 deque<node*> q;

 

 // Store head pointer in current to

 // traverse the linked list

 node* current = head;

 int i;

 

 // Iterate through the entire linked

 // list by moving the current

 while (current != NULL) {

 i = 1;

 

 // Store addresses of the k

 // nodes in the deque

 while (i <= k) {

 if (current == NULL)

 break;

 q.push_back(current);

 current = current->next;

 i++;

 }

 

 /* pop first and the last value from 

 the deque and swap the data values at 

 those addresses

 Do this till there exist an address in 

 the deque or deque is not empty*/

 while (!q.empty()) {

 node* front = q.front();

 node* last = q.back();

 swap(front->data, last->data);

 

 // pop from the front if

 // the deque is not empty

 if (!q.empty())

 q.pop_front();

 

 // pop from the back if

 // the deque is not empty

 if (!q.empty())

 q.pop_back();

 }

 }

 return head;

}

 

// Driver code

int main()

{

 

 // Start with the empty list

 node* head = NULL;

 

 // Created Linked list is

 // 1->2->3->4->5->6->7->8->9->10

 push(&head;, 10);

 push(&head;, 9);

 push(&head;, 8);

 push(&head;, 7);

 push(&head;, 6);

 push(&head;, 5);

 push(&head;, 4);

 push(&head;, 3);

 push(&head;, 2);

 push(&head;, 1);

 

 int k = 2;

 

 // Get the new head after reversing the

 // linked list in groups of size k

 head = reverse(head, k);

 

 printList(head);

 

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

// Java implementation of the above approach

import java.util.*;

 

class LinkedList{ 

 

static Node head; 

 

// Creating node class

static class Node

{ 

 int data; 

 Node next; 

 

 Node(int d) 

 { 

 data = d; 

 next = null; 

 } 

}

 

// Inserts a new Node at front of the list. 

public void push(int new_data) 

{ 

 

 // Allocate the Node & 

 // Put in the data

 Node new_node = new Node(new_data); 

 

 // Make next of new Node as head 

 new_node.next = head; 

 

 // Move the head to point to new Node 

 head = new_node; 

}

 

// Prints content of linked list 

void printList(Node node) 

{ 

 while (node != null)

 { 

 System.out.print(node.data + " "); 

 node = node.next; 

 } 

} 

 

// Function to reverse the linked list 

// in groups of size k and return the 

// pointer to the new head node.

Node reverse(Node head, int k)

{

 if (head == null)

 return head;

 

 // Create deque to store the address

 // of the nodes of the linked list

 Deque<Node> q = new ArrayDeque<Node>();

 

 // Store head pointer in current to

 // traverse the linked list

 Node current = head;

 int i;

 

 // Iterate through the entire linked

 // list by moving the current

 while (current != null)

 {

 i = 1;

 

 // Store addresses of the k

 // nodes in the deque

 while (i <= k)

 {

 if (current == null)

 break;

 

 q.addLast(current);

 current = current.next;

 i++;

 }

 

 // pop first and the last value from 

 // the deque and swap the data values at 

 // those addresses

 // Do this till there exist an address in 

 // the deque or deque is not empty

 while (!q.isEmpty())

 {

 Node front = q.peekFirst();

 Node last = q.peekLast();

 

 // Swapping front and

 // last nodes

 int temp = front.data;

 front.data = last.data;

 last.data = temp;

 

 // pop from the front if

 // the deque is not empty

 if (!q.isEmpty())

 q.removeFirst();

 

 // pop from the back if

 // the deque is not empty

 if (!q.isEmpty())

 q.removeLast();

 }

 }

 return head;

}

 

// Driver code

public static void main(String[] args) 

{ 

 LinkedList list = new LinkedList(); 

 

 // Created Linked list is

 // 1->2->3->4->5->6->7->8->9->10

 list.push(10); 

 list.push(9); 

 list.push(8); 

 list.push(7);

 list.push(6); 

 list.push(5); 

 list.push(4); 

 list.push(3);

 list.push(2); 

 list.push(1); 

 

 int k = 2;

 

 // Get the new head after reversing the

 // linked list in groups of size k

 head = list.reverse(head, k); 

 list.printList(head); 

} 

} 

 

// This code is contributed by Bindu Madhav   
  
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

 

# Link list node

class Node:

 def __init__(self):

 self.data = 0

 self.next = None

 

# Function to insert a node at

# the head of the linked list

def push(head_ref, new_data):

 

 # Allocate node 

 new_node = Node()

 

 # Put in the data 

 new_node.data = new_data

 

 # Link the old list off the new node 

 new_node.next = (head_ref)

 

 # Move the head to point to the new node 

 (head_ref) = new_node

 return head_ref

 

# Function to print the linked list

def printList( head):

 

 while (head != None) :

 print( head.data, end = " ")

 head = head.next

 

# Function to reverse the linked list in groups of 

# size k and return the pointer to the new head node. 

def reverse( head, k):

 

 if (head == None):

 return head

 

 # Create deque to store the address

 # of the nodes of the linked list

 q = []

 

 # Store head pointer in current to

 # traverse the linked list

 current = head

 i = 0

 

 # Iterate through the entire linked

 # list by moving the current

 while (current != None) :

 i = 1

 

 # Store addresses of the k

 # nodes in the deque

 while (i <= k) :

 if (current == None):

 break

 q.append(current)

 current = current.next

 i = i + 1

 

 # pop first and the last value from 

 # the deque and swap the data values at 

 # those addresses

 # Do this till there exist an address in 

 # the deque or deque is not empty

 while (len(q) > 0): 

 front = q[-1]

 last = q[0]

 

 temp = front.data

 front.data = last.data

 last.data = temp

 

 # pop from the front if

 # the deque is not empty

 if (len(q) > 0):

 q.pop()

 

 # pop from the back if

 # the deque is not empty

 if (len(q)):

 q.pop(0)

 

 return head

 

# Driver code

 

# Start with the empty list

head = None

 

# Created Linked list is

# 1.2.3.4.5.6.7.8.9.10

head = push(head, 10)

head = push(head, 9)

head = push(head, 8)

head = push(head, 7)

head = push(head, 6)

head = push(head, 5)

head = push(head, 4)

head = push(head, 3)

head = push(head, 2)

head = push(head, 1)

 

k = 2

 

# Get the new head after reversing the

# linked list in groups of size k

head = reverse(head, k)

printList(head)

 

# This code is contributed by Arnab Kundu  
  
---  
  
 __

 __

 **Output:**

    
    
    2 1 4 3 6 5 8 7 10 9 
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save


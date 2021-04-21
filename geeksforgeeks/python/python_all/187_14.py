Python Program to Reverse a linked list



Given pointer to the head node of a linked list, the task is to reverse the
linked list. We need to reverse the list by changing links between nodes.  
Examples:

    
    
    Input : Head of following linked list  
           1->2->3->4->NULL
    Output : Linked list should be changed to,
           4->3->2->1->NULL
    
    Input : Head of following linked list  
           1->2->3->4->5->NULL
    Output : Linked list should be changed to,
           5->4->3->2->1->NULL
    
    Input : NULL
    Output : NULL
    
    Input  : 1->NULL
    Output : 1->NULL

 **Iterative Method**

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to reverse a linked list

# Time Complexity : O(n)

# Space Complexity : O(n) as 'next'

#variable is getting created in each loop.

# Node class

class Node:

 # Constructor to initialize the node object

 def __init__(self, data):

 self.data = data

 self.next = None

class LinkedList:

 # Function to initialize head

 def __init__(self):

 self.head = None

 # Function to reverse the linked list

 def reverse(self):

 prev = None

 current = self.head

 while(current is not None):

 next = current.next

 current.next = prev

 prev = current

 current = next

 self.head = prev

 # Function to insert a new node at the beginning

 def push(self, new_data):

 new_node = Node(new_data)

 new_node.next = self.head

 self.head = new_node

 # Utility function to print the linked LinkedList

 def printList(self):

 temp = self.head

 while(temp):

 print temp.data,

 temp = temp.next

# Driver program to test above functions

llist = LinkedList()

llist.push(20)

llist.push(4)

llist.push(15)

llist.push(85)

print "Given Linked List"

llist.printList()

llist.reverse()

print "\nReversed Linked List"

llist.printList()

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)  
  
---  
  
 __

 __

 **Output:**

    
    
    Given Linked List
    85 15 4 20 
    Reversed Linked List
    20 4 15 85

 **A Simpler and Tail Recursive Method**

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Simple and tail recursive Python program to

# reverse a linked list

# Node class

class Node:

 # Constructor to initialize the node object

 def __init__(self, data):

 self.data = data

 self.next = None

class LinkedList:

 # Function to initialize head

 def __init__(self):

 self.head = None

 def reverseUtil(self, curr, prev):

 # If last node mark it head

 if curr.next is None:

 self.head = curr

 # Update next to prev node

 curr.next = prev

 return

 # Save curr.next node for recursive call

 next = curr.next

 # And update next

 curr.next = prev

 self.reverseUtil(next, curr)

 # This function mainly calls reverseUtil()

 # with previous as None

 def reverse(self):

 if self.head is None:

 return

 self.reverseUtil(self.head, None)

 # Function to insert a new node at the beginning

 def push(self, new_data):

 new_node = Node(new_data)

 new_node.next = self.head

 self.head = new_node

 # Utility function to print the linked LinkedList

 def printList(self):

 temp = self.head

 while(temp):

 print temp.data,

 temp = temp.next

# Driver program

llist = LinkedList()

llist.push(8)

llist.push(7)

llist.push(6)

llist.push(5)

llist.push(4)

llist.push(3)

llist.push(2)

llist.push(1)

print "Given linked list"

llist.printList()

llist.reverse()

print "\nReverse linked list"

llist.printList()

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)  
  
---  
  
 __

 __

Please refer complete article onReverse a linked list for more details!  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

  
  

  

My Personal Notes _arrow_drop_up_

Save


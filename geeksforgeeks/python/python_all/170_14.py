Python program to find middle of a linked list using one traversal



Given a singly linked list, find middle of the linked list. Given a singly
linked list, find middle of the linked list. For example, if given linked list
is 1->2->3->4->5 then output should be 3.

 **Method 1:**  
Traverse the whole linked list and count the no. of nodes. Now traverse the
list again till count/2 and return the node at count/2.

 **Method 2:**  
Traverse linked list using two pointers. Move one pointer by one and other
pointer by two. When the fast pointer reaches end slow pointer will reach
middle of the linked list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 program to find the middle of a

# given linked list 

 

# Node class 

class Node: 

 

 # Function to initialise the node object 

 def __init__(self, data): 

 self.data = data 

 self.next = None

 

class LinkedList:

 

 def __init__(self):

 self.head = None

 

 def push(self, new_data):

 new_node = Node(new_data)

 new_node.next = self.head

 self.head = new_node

 

 # Function to get the middle of 

 # the linked list

 def printMiddle(self):

 slow_ptr = self.head

 fast_ptr = self.head

 

 if self.head is not None:

 while (fast_ptr is not None and fast_ptr.next is not
None):

 fast_ptr = fast_ptr.next.next

 slow_ptr = slow_ptr.next

 print("The middle element is: ", slow_ptr.data)

 

# Driver code

list1 = LinkedList()

list1.push(5)

list1.push(4)

list1.push(2)

list1.push(3)

list1.push(1)

list1.printMiddle()  
  
---  
  
 __

 __

 **Output:**

    
    
    The middle element is:  2
    

**Method 3:**  
Initialized the temp variable as head  
Initialized count to Zero  
Take loop till head will become Null(i.e end of the list) and increment the
temp node when count is odd only, in this way temp will traverse till mid
element and head will traverse all linked list. Print the data of temp.

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 program to find the middle of a

# given linked list 

 

class Node:

 def __init__(self, value):

 self.data = value

 self.next = None

 

class LinkedList:

 

 def __init__(self):

 self.head = None

 

 # create Node and and make linked list

 def push(self, new_data):

 new_node = Node(new_data)

 new_node.next = self.head

 self.head = new_node

 

 def printMiddle(self):

 temp = self.head 

 count = 0

 

 while self.head:

 

 # only update when count is odd

 if (count & 1): 

 temp = temp.next

 self.head = self.head.next

 

 # increment count in each iteration 

 count += 1

 

 print(temp.data) 

 

# Driver code

llist = LinkedList() 

llist.push(1)

llist.push(20) 

llist.push(100) 

llist.push(15) 

llist.push(35)

llist.printMiddle()

# code has been contributed by - Yogesh Joshi  
  
---  
  
 __

 __

 **Output:**

    
    
    100
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

  
  

  

My Personal Notes _arrow_drop_up_

Save


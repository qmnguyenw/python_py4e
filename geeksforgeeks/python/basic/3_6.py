Linked list using dstructure library in Python



Dstructure is a Python library for creating data structures like linked list,
stack, queue, hashmap, tree, etc. A linked list is a linear data structure, in
which the elements are not stored at contiguous memory locations. The elements
in a linked list are linked using pointers as shown in the below image:

![](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/gq/2013/03/Linkedlist.png)

    
    
    pip install dstructure
    

Let’s see how to create different types of linked lists using this library.

 **1\. Singly Linked List**

Singly-linked lists contain nodes that have a data field as well as ‘next’
field, which points to the next node in a line of nodes. Operations that can
be performed on singly linked lists include insertion, deletion, and
traversal.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

from dstructure.ll.SLL import SLL

 

obj = SLL()

obj.insert(10) # insert 10 in linked list

obj.insert(20) # insert 20 in linked list

obj.insert(30) # insert 30 in linked list

obj.insert(40) # insert 40 in linked list

obj.insert(50) # insert 50 in linked list

obj.insert(60) # insert 60 in linked list

obj.delete_f() # delete first node in linked list

obj.delete_l() # delete last node in linked list

obj.delete(20) # delete the node which we pass and return True
otherwise False

obj.getnodes() # return all the node in linked list in list.

obj.print() # print all the in this format 10 -> 30 -> 40  
  
---  
  
 __

 __

 **Output:**

    
    
    [30,40,50]
    30 -> 40 -> 50
    

**2.Doubly Linked List.**

Doubly linked list is a type of linked list in which each node apart from
storing its data has two links. The first link points to the previous node in
the list and the second link points to the next node in the list.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

from dstructure.ll.DLL import DLL

 

obj = DLL()

obj.insert(10) # insert 10 in linked list

obj.insert(20) # insert 20 in linked list

obj.insert(30) # insert 30 in linked list

obj.insert(40) # insert 40 in linked list

obj.delete_f() # delete first node in linked list

obj.delete_l() # delete last node in linked list

obj.delete(20) # delete the node which we pass and return True
otherwise False

obj.getnodes() # return all the node in linked list in list.

obj.print() # print all the in this format 10 <-> 30 <-> 40  
  
---  
  
 __

 __

 **Output:**

    
    
    10 <-> 30 <-> 40
    

**3.Singly Circular Linked List.**

In a singly linked list, for accessing any node of the linked list, we start
traversing from the first node. If we are at any node in the middle of the
list, then it is not possible to access nodes that precede the given node.
This problem can be solved by slightly altering the structure of the singly
linked list. In a singly linked list, the next part (pointer to next node) is
NULL, if we utilize this link to point to the first node then we can reach
preceding nodes.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

from dstructure.ll.SCLL import SCLL

 

obj = SCLL()

obj.insert(10) # insert 10 in linked list

obj.insert(20) # insert 20 in linked list

obj.insert(30) # insert 30 in linked list

obj.insert(40) # insert 40 in linked list

obj.delete_f() # delete first node in linked list

obj.delete_l() # delete last node in linked list

obj.delete(20) # delete the node which we pass and return True
otherwise False

obj.getnodes() # return all the node in linked list in list.

obj.print() # print all the in this format 10 -> 30 -> 40  
  
---  
  
 __

 __

 **Output:**

    
    
    10 -> 30 -> 40
    

**4.Doubly Circular Linked List.**

Circular Doubly Linked List has properties of both doubly linked list and
circular linked list in which two consecutive elements are linked or connected
by previous and next pointer and the last node points to first node by next
pointer and also the first node points to last node by the previous pointer.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

from dstructure.ll.DCLL import DCLL

 

obj = DCLL()

obj.insert(10) # insert 10 in linked list

obj.insert(20) # insert 20 in linked list

obj.insert(30) # insert 30 in linked list

obj.insert(40) # insert 40 in linked list

obj.delete_f() # delete first node in linked list

obj.delete_l() # delete last node in linked list

obj.delete(20) # delete the node which we pass and return True
otherwise False

obj.getnodes() # return all the node in linked list in list.

obj.print() # print all the in this format 10 <-> 30 <-> 40  
  
---  
  
 __

 __

 **Output:**

    
    
    10 <-> 30 <-> 40
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


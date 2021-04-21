Implementation of XOR Linked List in Python



 **Prerequisite:**XOR Linked List

An ordinary Doubly Linked List requires space for two address fields to store
the addresses of previous and next nodes. A memory-efficient version of Doubly
Linked List can be created using only one space for the address field with
every node. This memory efficient Doubly Linked List is called XOR Linked List
or Memory Efficient as the list uses bitwise XOR operation to save space for
one address. In the XOR linked list, instead of storing actual memory
addresses, every node stores the XOR of addresses of previous and next nodes.

The XOR Linked List implementation in Python is not of much use because the
Python garbage collector doesn’t allow to save the node whose address is being
XORed.

#### The functions that are implemented in the below program are:

  *  **InsertAtStart():** Method to insert a node at the beginning.
  *  **InsertAtEnd():** Method to insert a node at the end.
  *  **DeleteAtStart():** Method to delete a node at the beginning.
  *  **DeleteAtEnd():** Method to delete a node at the end.
  *  **Print():** Method to traverse through the linked list from beginning to end.
  *  **ReversePrint():** Method to traverse through the linked list from end to the beginning.
  *  **Length():** Method to return the size of the linked list.
  *  **PrintByIndex():** Method to return the data value of the node of the linked list specified by a particular index.
  *  **isEmpty():** Method to check if the linked list is empty or not.
  *  **__type_cast():** Method to return a new instance of _type_ which points to the same memory block.

 **Below is the complete Python program to implement XOR Linked List with the
above methods:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import required module

import ctypes

 

 

 

# create node class

class Node:

 def __init__(self, value):

 self.value = value

 self.npx = 0

 

 

 

# create linked list class

class XorLinkedList:

 

 # constructor

 def __init__(self):

 self.head = None

 self.tail = None

 self.__nodes = []

 

 # method to insert node at beginning

 def InsertAtStart(self, value):

 node = Node(value)

 if self.head is None: # If list is empty

 self.head = node

 self.tail = node

 else:

 self.head.npx = id(node) ^ self.head.npx

 node.npx = id(self.head)

 self.head = node

 self.__nodes.append(node)

 

 # method to insert node at end

 def InsertAtEnd(self, value):

 node = Node(value)

 if self.head is None: # If list is empty

 self.head = node

 self.tail = node

 else:

 self.tail.npx = id(node) ^ self.tail.npx

 node.npx = id(self.tail)

 self.tail = node

 self.__nodes.append(node)

 

 # method to remove node at beginning

 def DeleteAtStart(self):

 if self.isEmpty(): # If list is empty

 return "List is empty !"

 elif self.head == self.tail: # If list has 1 node

 self.head = self.tail = None

 elif (0 ^ self.head.npx) == id(self.tail): # If
list has 2 nodes

 self.head = self.tail

 self.head.npx = self.tail.npx = 0

 else: # If list has more than 2 nodes

 res = self.head.value

 x = self.__type_cast(0 ^ self.head.npx) # Address of next
node

 y = (id(self.head) ^ x.npx) # Address of next of next node

 self.head = x

 self.head.npx = 0 ^ y

 return res

 

 # method to remove node at end

 def DeleteAtEnd(self):

 if self.isEmpty(): # If list is empty

 return "List is empty !"

 elif self.head == self.tail: # If list has 1 node

 self.head = self.tail = None

 elif self.__type_cast(0 ^ self.head.npx) ==
(self.tail): # If list has 2 nodes

 self.tail = self.head

 self.head.npx = self.tail.npx = 0

 else: # If list has more than 2 nodes

 prev_id = 0

 node = self.head

 next_id = 1

 while next_id:

 next_id = prev_id ^ node.npx

 if next_id:

 prev_id = id(node)

 node = self.__type_cast(next_id)

 res = node.value

 x = self.__type_cast(prev_id).npx ^ id(node)

 y = self.__type_cast(prev_id)

 y.npx = x ^ 0

 self.tail = y

 return res

 

 # method to traverse linked list

 def Print(self):

 """We are printing values rather than returning it bacause

 for returning we have to append all values in a list

 and it takes extra memory to save all values in a list."""

 

 if self.head != None:

 prev_id = 0

 node = self.head

 next_id = 1

 print(node.value, end=' ')

 while next_id:

 next_id = prev_id ^ node.npx

 if next_id:

 prev_id = id(node)

 node = self.__type_cast(next_id)

 print(node.value, end=' ')

 else:

 return

 else:

 print("List is empty !")

 

 # method to traverse linked list in reverse order

 def ReversePrint(self):

 

 # Print Values is reverse order.

 """We are printing values rather than returning it bacause

 for returning we have to append all values in a list

 and it takes extra memory to save all values in a list."""

 

 if self.head != None:

 prev_id = 0

 node = self.tail

 next_id = 1

 print(node.value, end=' ')

 while next_id:

 next_id = prev_id ^ node.npx

 if next_id:

 prev_id = id(node)

 node = self.__type_cast(next_id)

 print(node.value, end=' ')

 else:

 return

 else:

 print("List is empty !")

 

 # method to get length of linked list

 def Length(self):

 if not self.isEmpty():

 prev_id = 0

 node = self.head

 next_id = 1

 count = 1

 while next_id:

 next_id = prev_id ^ node.npx

 if next_id:

 prev_id = id(node)

 node = self.__type_cast(next_id)

 count += 1

 else:

 return count

 else:

 return 0

 

 # method to get node data value by index

 def PrintByIndex(self, index):

 prev_id = 0

 node = self.head

 for i in range(index):

 next_id = prev_id ^ node.npx

 

 if next_id:

 prev_id = id(node)

 node = self.__type_cast(next_id)

 else:

 return "Value dosn't found index out of range."

 return node.value

 

 # method to check if the liked list is empty or not

 def isEmpty(self):

 if self.head is None:

 return True

 return False

 

 # method to return a new instance of type

 def __type_cast(self, id):

 return ctypes.cast(id, ctypes.py_object).value

 

 

 

# Driver Code

 

# create object

obj = XorLinkedList()

 

# insert nodes

obj.InsertAtEnd(2)

obj.InsertAtEnd(3)

obj.InsertAtEnd(4)

obj.InsertAtStart(0)

obj.InsertAtStart(6)

obj.InsertAtEnd(55)

 

# display length

print("\nLength:", obj.Length())

 

# traverse

print("\nTraverse linked list:")

obj.Print()

 

print("\nTraverse in reverse order:")

obj.ReversePrint()

 

# display data values by index

print('\nNodes:')

for i in range(obj.Length()):

 print("Data value at index", i, 'is', obj.PrintByIndex(i))

 

# removing nodes

print("\nDelete Last Node: ", obj.DeleteAtEnd())

print("\nDelete First Node: ", obj.DeleteAtStart())

 

# new length

print("\nUpdated length:", obj.Length())

 

# display data values by index

print('\nNodes:')

for i in range(obj.Length()):

 print("Data value at index", i, 'is', obj.PrintByIndex(i))

 

# traverse

print("\nTraverse linked list:")

obj.Print()

 

print("\nTraverse in reverse order:")

obj.ReversePrint()  
  
---  
  
 __

 __

 **Output:**

    
    
    Length: 6
    
    Traverse linked list:
    6 0 2 3 4 55 
    Traverse in reverse order:
    55 4 3 2 0 6 
    Nodes:
    Data value at index 0 is 6
    Data value at index 1 is 0
    Data value at index 2 is 2
    Data value at index 3 is 3
    Data value at index 4 is 4
    Data value at index 5 is 55
    
    Delete Last Node:  55
    
    Delete First Node:  6
    
    Updated length: 4
    
    Nodes:
    Data value at index 0 is 0
    Data value at index 1 is 2
    Data value at index 2 is 3
    Data value at index 3 is 4
    
    Traverse linked list:
    0 2 3 4 
    Traverse in reverse order:
    4 3 2 0
    

In Python garbage collector collect nodes and decrease the reference count of
the object of a node when the object of the node is XORed, Python thinks there
is no way to access the node so we used the __in which we store objects of
node just for preventing it to become garbage.

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save


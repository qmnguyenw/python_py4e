Pygorithm module in Python



Pygorithm module is a Python module written purely in Python and for
educational purposes only. One can get the code, time complexities and much
more by just importing the required algorithm. It is a good way to start
learning Python programming and understanding concepts. Pygorithm module can
also help to learn the implementation of all major algorithms in Python
language.

To install Pygorithm module:

    
    
    pip3 install pygorithm

Example:

 __

 __  
 __

 __

 __  
 __  
 __

# import the required data structure

from pygorithm.data_structures import stack

 

 

# create a stack with default stack size 10

myStack = stack.Stack()

 

# push elements into the stack

myStack.push(2)

myStack.push(5)

myStack.push(9)

myStack.push(10)

 

# print the contents of stack

print(myStack)

 

# pop elements from stack

myStack.pop()

print(myStack)

 

# peek element in stack

print(myStack.peek())

 

# size of stack

print(myStack.size())  
  
---  
  
 __

 __

 **Output:**

    
    
    2 5 9 10
    2 5 9
    9
    3
    

  
To see all the available functions in a module, just type **help()** with
the module name as argument.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Help on package pygorithm.data_structures

help(data_structures)  
  
---  
  
 __

 __

 **Output:**

    
    
    NAME
        pygorithm.data_structures - Collection of data structure examples
    
    PACKAGE CONTENTS
        graph
        heap
        linked_list
        quadtree
        queue
        stack
        tree
        trie
    
    DATA
        __all__ = ['graph', 'heap', 'linked_list', 'queue', 'stack', 'tree', '...
    

To get code for any of these data_structures using get_code().

 __

 __  
 __

 __

 __  
 __  
 __

# to get code for BinarySearchTree

BStree = tree.BinarySearchTree.get_code()

 

print(BStree)  
  
---  
  
 __

 __

 **Output:**

    
    
    class BinarySearchTree(object):
       
        def __init__(self):
            self.root = None
    
        def insert(self, data):
            """
            inserts a node in the tree
            """
            if self.root:
                return self.root.insert(data)
            else:
                self.root = BSTNode(data)
                return True
    
        def delete(self, data):
            """
            deletes the node with the specified data from the tree
            """
            if self.root is not None:
                return self.root.delete(data)
    
        def find(self, data):
            if self.root:
                return self.root.find(data)
            else:
                return False
    
        def preorder(self):
            """
            finding the preorder of the tree
            """
            if self.root is not None:
                return self.root.preorder(self.root)
    
        def inorder(self):
            """
            finding the inorder of the tree
            """
            if self.root is not None:
                return self.root.inorder(self.root)
    
        def postorder(self):
            """
            finding the postorder of the tree
            """
            if self.root is not None:
                return self.root.postorder(self.root)
        
        @staticmethod
        def get_code():
            """
            returns the code of the current class
            """
            return inspect.getsource(BinarySearchTree)

  
To get complexities for the following scripts:

 __

 __  
 __

 __

 __  
 __  
 __

# create a stack with default stack size 10

Bsort = sorting.bubble_sort.time_complexities()  
  
---  
  
 __

 __

 **Output:**

    
    
    Best Case: O(n), Average Case: O(n ^ 2), Worst Case: O(n ^ 2).
    
    For Improved Bubble Sort:
    Best Case: O(n); Average Case: O(n * (n - 1) / 4); Worst Case: O(n ^ 2)
    

Quick Link to source code of Pygorithm

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


Pretty print Linked List in Python



Creating custom data types can be tricky, especially when you want to use it
like any other data type. Linked List can be thought of as an example of a
custom data type. In other languages, if you want to print the linked list,
you would define a separate print function, something like **pprint** but it
looks kind of odd, right? Like it would be great to have the default **print**
function do the same, right? Well, that’s where Python comes in. Python has
some amazing methods called **Dunder methods**.

## Dunder methods

Dunder stands for **double under** methods. Basically, any methods that start
and end with double underscores are called **Dunder** methods or **Magic**
methods. One such example of under method is **__init__**. One similar method
is **__str__** , which we are going to use in this article. This method can be
used for pretty-printing in Python. **Pretty print** is nothing but applying
various kinds of styles and formatting the content to be printed. Learn more
about dunder methods here.

 **__str__** methods specify what should be returned from a class when that
class is printed using the standard **print** function. Using this concept, we
can have a lot of better representation of custom datatype. Here, bellow is an
example of such custom representation. Note that the focus is on the Linked
List implementation but more on the pythonic way of representing it.

**Example:** Pretty print a singly linked list **10- >15->20** as **[10, 15,
20]**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

class Node:

 def __init__(self, val=None):

 self.val = val

 self.next = None

 

 

class LinkedList:

 def __init__(self, head=None):

 self.head = head

 

 def __str__(self):

 

 # defining a blank res variable

 res = ""

 

 # initializing ptr to head

 ptr = self.head

 

 # traversing and adding it to res

 while ptr:

 res += str(ptr.val) + ", "

 ptr = ptr.next

 

 # removing trailing commas

 res = res.strip(", ")

 

 # chen checking if 

 # anything is present in res or not

 if len(res):

 return "[" + res + "]"

 else:

 return "[]"

 

 

if __name__ == "__main__":

 

 # defining linked list

 ll = LinkedList()

 

 # defining nodes

 node1 = Node(10)

 node2 = Node(15)

 node3 = Node(20)

 

 # connecting the nodes

 ll.head = node1

 node1.next = node2

 node2.next = node3

 

 # when print is called, by default 

 #it calls the __str__ method

 print(ll)  
  
---  
  
 __

 __

 **Output**

  

  

    
    
    [10, 15, 20]
    


Python program to reverse a stack



The **stack** is a linear data structure which works on the LIFO concept. LIFO
stands for last in first out. In the stack, the insertion and deletion are
possible at one end the end is called the top of the stack.

In this article, we will see how to reverse a stack using Python.

 **Algorithm:**

  * Define some basic function of the stack like push(), pop(), show(), empty(), for basic operation like respectively append an item in stack, remove an item in stack, display the stack, check the given stack is empty or not.
  * Define two recursive functions BottomInsertion() and Reverse()..

 **BottomInsertion()** : this method append element at the bottom of the stack
and BottomInsertion accept two values as an argument first is stack and the
second is elements, this is a recursive method.

    
    
    # insert element at the bottom of the stack
    def BottomInsert(s, value):
        # if stack is empty then call push() method.
        if s.empty():  
            s.push(value)
            
        # if stack is not empty then execute else
        # block
        else:
        
            # remove the element and store it to
            # popped  
            popped = s.pop()
            
            # invoke it self and pass stack and value 
            # as an argument.
            BottomInsert(s, value)
            
            # append popped item in the bottom of the stack 
            s.push(popped)

 **Reverse()** : the method is reverse elements of the stack, this method
accept stack as an argument Reverse() is also a Recursive() function.
Reverse() is invoked BottomInsertion() method for completing the reverse
operation on the stack.

  

  

    
    
    # Reverse()
    def Reverse(s): 
    
        # check the stack is empty of not  
        if s.empty():
        
            # if empty then do nothing
            pass
            
        # if stack is not empty then 
        else:
        
            # pop element and stare it to popped
            popped = s.pop()
            
            # call it self ans pass stack as an argument
            Reverse(s)
            
            # call BottomInsert() method and pass stack
            # and popped element as an argument
            BottomInsert(s, popped)

Below is the implementation.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# create class for stack

class Stack:

 

 # create empty list

 def __init__(self):

 self.Elements = []

 

 # push() for insert an element

 def push(self, value):

 self.Elements.append(value)

 

 # pop() for remove an element

 def pop(self):

 return self.Elements.pop()

 

 # empty() check the stack is empty of not

 def empty(self):

 return self.Elements == []

 

 # show() display stack

 def show(self):

 for value in reversed(self.Elements):

 print(value)

 

# Insert_Bottom() insert value at bottom

def BottomInsert(s, value):

 

 # check the stack is empty or not

 if s.empty(): 

 

 # if stack is empty then call

 # push() method.

 s.push(value)

 

 # if stack is not empty then execute

 # else block

 else:

 popped = s.pop()

 BottomInsert(s, value)

 s.push(popped)

 

# Reverse() reverse the stack

def Reverse(s):

 if s.empty():

 pass

 else:

 popped = s.pop()

 Reverse(s)

 BottomInsert(s, popped)

 

 

# create object of stack class

stk = Stack()

 

stk.push(1)

stk.push(2)

stk.push(3)

stk.push(4)

stk.push(5)

 

print("Orginal Stack")

stk.show()

 

print("\nStack after Reversing")

Reverse(stk)

stk.show()  
  
---  
  
 __

 __

 **Output:**

    
    
    Orginal Stack
    5
    4
    3
    2
    1
    
    Stack after Reversing
    1
    2
    3
    4
    5
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


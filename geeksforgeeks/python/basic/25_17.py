Stack and Queues in Python



Prerequisites : list and Deque in Python.

Unlike C++ STL and Java Collections, Python does have specific
classes/interfaces for Stack and Queue. Following are different ways to
implement in Python

 **1) Using list**  
 **Stack** works on the principle of “Last-in, first-out”. Also, the inbuilt
functions in Python make the code short and simple. To add an item to the top
of the list, i.e., to push an item, we use **append()** function and to pop
out an element we use **pop()** function. These functions work quiet
efficiently and fast in end operations.

Let’s look at an example and try to understand the working of push() and pop()
function:  
Example:

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate Implementing

# stack using list

stack = ["Amar", "Akbar", "Anthony"]

stack.append("Ram")

stack.append("Iqbal")

print(stack)

 

# Removes the last item

print(stack.pop())

 

print(stack)

 

# Removes the last item

print(stack.pop())

 

print(stack)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    ['Amar', 'Akbar', 'Anthony', 'Ram', 'Iqbal']
    Iqbal
    ['Amar', 'Akbar', 'Anthony', 'Ram']
    Ram
    ['Amar', 'Akbar', 'Anthony']
    


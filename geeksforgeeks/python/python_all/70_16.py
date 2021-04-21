Python Program to Reverse the Content of a File using Stack



  
Given a file, the task is to print as well as store the lines of that file in
reverse order using Stack.

 **Examples:**

    
    
    **Input :**
    I am
    new to this
    world of
    Python.
    
    **Output :**
    Python.
    world of
    new to this
    I am
    
    
    **Input :**
    1
    2
    3
    4
    5
    **Output :**
    5
    4
    3
    2
    1
    

**Approach:**

  * Create an empty stack.
  * One by one push every line of the file to the stack.
  * One by one pop each line from the stack and put them back to the file.

Below is the implementation.

 **Input File:**

  

  

![reverse-file-python](https://media.geeksforgeeks.org/wp-
content/uploads/20200504140337/reverse-file-python.png)

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to reverse the lines

# of a file using Stack.

 

 

# Creating Stack class (LIFO rule)

class Stack:

 

 def __init__(self):

 

 # Creating an empty stack

 self._arr = []

 

 # Creating push() method.

 def push(self, val):

 self._arr.append(val)

 

 def is_empty(self):

 

 # Returns True if empty

 return len(self._arr) == 0

 

 # Creating Pop method.

 def pop(self):

 

 if self.is_empty():

 print("Stack is empty")

 return

 

 return self._arr.pop()

 

# Creating a function which will reverse

# the lines of a file and Overwrites the 

# given file with its contents line-by-line

# reversed

def reverse_file(filename):

 

 S = Stack()

 original = open(filename)

 

 for line in original:

 S.push(line.rstrip("\n"))

 

 original.close()

 

 

 output = open(filename, 'w')

 

 while not S.is_empty():

 output.write(S.pop()+"\n")

 

 output.close()

 

 

# Driver Code

filename = "GFG.txt"

 

# Calling the reverse_file function

reverse_file(filename)

 

# Now reading the content of the file

with open(filename) as file:

 for f in file.readlines():

 print(f, end ="")  
  
---  
  
 __

 __

 **Output:**

    
    
    Ths is a World of Geeks.
    Welcome to GeeksforGeeks.

![python-reverse-file-using-stack](https://media.geeksforgeeks.org/wp-
content/uploads/20200504140504/python-reverse-file-using-stack.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


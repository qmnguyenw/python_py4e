Multimethods in Python



 **Multimethod** basically means a function that has multiple versions,
distinguished by the type of the arguments. For better understanding consider
the below example.

    
    
    @multimethod
    def sum(x: int, y: int):
        return x + y
    
    @multimethod
    def sum(x: str, y: str):
        return x+" "+y
    
    **The above example is similar to**
    
    def sum(x, y):
        
        if isinstance(x, int) and isinstance(y, int):
            return x + y
        
        elif isinstance(x, str) and isinstance(y, str):
            return x + ' ' + y
    

### Installation

At syntactical level, Python does not support multiple dispatch but it is
possible to add multiple dispatch using a library extension multimethod. To
install this library type the below command in the terminal.

    
    
    pip install multimethod

 **Example 1:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# multimethods

 

 

from multimethod import multimethod

 

 

# Function that will be called

# for integer addition

@multimethod

def sum(x: int, y: int):

 return x + y

 

# Function that will be called

# for string addition

@multimethod

def sum(x: str, y: str):

 return x+" "+y

 

# Driver's code

print(sum(2, 3))

print(sum("Hello", "World"))  
  
---  
  
 __

 __

 **Output:**

    
    
    5
    Hello World

 **Example 2:**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# multimethods

 

 

from multimethod import multimethod

 

 

class GFG(object):

 

 @multimethod

 def double(self, x: int):

 print(2 * x)

 

 @multimethod

 def double(self, x: complex):

 print("sorry, I don't like complex numbers")

 

# Driver Code

obj = GFG()

obj.double(3)

obj.double(6j)  
  
---  
  
 __

 __

 **Output:**

    
    
    6
    sorry, I don't like complex numbers

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


Python – Call function from another function



 **Prerequisite:** Functions in Python

In Python, any written function can be called by another function. Note that
this could be the most elegant way of breaking a problem into chunks of small
problems. In this article, we will learn how can we call a defined function
from another function with help of multiple examples.

 _ **Calling and Called Function ?**_  
The Function which calls another Function is called **Calling Function** and
function which is called by another Function is call **Called Function**.

 **How Function execution works ?**  
A stack data structure is used during the execution of the function calls.
Whenever a function is invoked then the calling function is pushed into the
stack and called function is executed. When the called function completes its
execution and returns then the calling function is popped from the stack and
executed. Calling Function execution will be completed only when called
Function is execution completes.

In the below figure. The function call is made from the Main function to
_Function1_ , Now the state of the Main function is stored in Stack and
execution of the Main function is continued when the _Function 1_ returns. The
_Fucntion1_ Calls _Function2_ now the State of the _Function1_ is stored stack
and execution of _Function 1_ will be continued when _Function 2_ returns.  
![](https://media.geeksforgeeks.org/wp-content/uploads/20191205143745/nested-
function-calling.png)

  

  

Consider the below Example of the function call. The Function SumOfSquares
function calls the Function Square which returns the square of the number.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate calling the

# function from another function

 

def Square(X):

 # computes the Square of the given number 

 # and return to the caller function

 return (X * X)

 

def SumofSquares(Array, n):

 

 # Initialize variable Sum to 0. It stores the 

 # Total sum of squares of the array of elements

 Sum = 0

 for i in range(n):

 

 # Square of Array[i] element is stored in SquaredValue

 SquaredValue = Square(Array[i])

 

 # Cummulative sum is stored in Sum variable

 Sum += SquaredValue

 return Sum

 

# Driver Function

Array = [1, 2, 3, 4, 5, 6, 7, 8, 9,
10]

n = len(Array)

 

# Return value from the function 

# Sum of Squares is stored in Total

Total = SumofSquares(Array, n)

print("Sum of the Square of List of Numbers:", Total)  
  
---  
  
 __

 __

 **Output :**

    
    
    Sum of the Square of List of Numbers: 385 
    

  
**Calling Function From another Function within Same class –**

In the below example, the class method Function1 calls method Function2
from the class.

 __

 __  
 __

 __

 __  
 __  
 __

'''

Call a function from within another function

in the same class in Python 

'''

 

class Main:

 

 # constructor of Main class

 def __init__(self):

 # Initialization of the Strings

 self.String1 ="Hello"

 self.String2 ="World"

 

 def Function1(self):

 # calling Function2 Method

 self.Function2()

 print("Function1 : ", self.String2)

 return

 

 def Function2(self):

 print("Function2 : ", self.String1)

 return

 

# Instance of Class Main

Object = Main()

 

# Calling Function1

Object.Function1()  
  
---  
  
 __

 __

 **Output :**

    
    
    Function2 :  Hello
    Function1 :  World
    

**Calling _parent class_ Function from _Child class_ Function –**

Consider the below example the child class method invokes the parent class
method. The child class inherits the attributes from the parent class.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate calling parent class

# method from the child class method

 

class Parent:

 

 # constructor of Parent class

 def __init__(self):

 # Initialization of the Strings

 self.String1 ="Hello"

 self.String2 ="World"

 

 def Function2(self):

 print("Function2 : ", self.String1)

 return

 

# Child class is inheriting from Parent class

class Child(Parent):

 

 def Function1(self):

 # calling Function2 Method in parent class 

 self.Function2()

 print("Function1 : ", self.String2)

 return

 

### Instance of Parent class

Object1 = Parent()

 

### Instance of Child class

Object2 = Child()

 

# Calling Function1 using Child class instance

Object2.Function1()  
  
---  
  
 __

 __

 **Output :**

    
    
    Function2 :  Hello
    Function1 :  World
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


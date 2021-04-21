Python Variables



Python is not “statically typed”. We do not need to declare variables before
using them or declare their type. A variable is created the moment we first
assign a value to it. A variable is a name given to a memory location. It is
the basic unit of storage in a program.

  * The value stored in a variable can be changed during program execution.
  * A variable is only a name given to a memory location, all the operations done on the variable effects that memory location.

###  **Rules for creating variables in Python:**

  * A variable name must start with a letter or the underscore character.
  * A variable name cannot start with a number.
  * A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ ).
  * Variable names are case-sensitive (name, Name and NAME are three different variables).
  * The reserved words(keywords) cannot be used naming the variable.

 **Let’s see the simple variable creation:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

#!/usr / bin / python

 

# An integer assignment

age = 45

 

# A floating point

salary = 1456.8

 

# A string

name = "John"

 

print(age)

print(salary)

print(name)  
  
---  
  
 __

 __

 **Output:**

    
    
    45
    1456.8
    John
    

### **Declare the Variable:**

Let’s see how to declare the variable and print the variable.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# declaring the var

Number = 100

 

# display

print( Number)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    100
    

### **Re-declare the Variable:**

We can re-declare the python variable once we have declared the variable
already.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# declaring the var

Number = 100

 

# display

print("Before declare: ", Number)

 

# re-declare the var

Number = 120.3

 

print("After re-declare:", Number)  
  
---  
  
 __

 __

 **Output:**

    
    
    Before declare:  100
    After re-declare: 120.3
    

### **Assigning a single value to multiple variables:**

Also, Python allows assigning a single value to several variables
simultaneously with “=” operators.  
For example:

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

#!/usr / bin / python

 

a = b = c = 10

 

print(a)

print(b)

print(c)  
  
---  
  
 __

 __

 **Output:**

    
    
    10
    10
    10

###  **Assigning different values to multiple variables:**

Python allows adding different values in a single line with “,”operators.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

#!/usr / bin / python

 

a, b, c = 1, 20.2, "GeeksforGeeks"

 

print(a)

print(b)

print(c)  
  
---  
  
 __

 __

 **Output:**

    
    
    1
    20.2
    GeeksforGeeks

###  **Can we use** the **same name for different types?**

If we use the same name, the variable starts referring to a new value and
type.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

#!/usr / bin / python

 

a = 10

a = "GeeksforGeeks"

 

print(a)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    GeeksforGeeks

###  **How does + operator work with variables?**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

#!/usr / bin / python

 

a = 10

b = 20

print(a+b)

 

a = "Geeksfor"

b = "Geeks"

print(a+b)  
  
---  
  
 __

 __

 **Output**

    
    
    30
    GeeksforGeeks
    

### **Can we use + for different types also?**

No using for different types would produce error.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

#!/usr / bin / python

 

a = 10

b = "Geeks"

print(a+b)  
  
---  
  
 __

 __

 **Output :**

    
    
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    

### Global and Local Variables in Python:

 **Local** ******variables** **** are the ones that are defined and declared
inside a function. We can not call this variable outside the function.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# This function uses global variable s

def f():

 s = "Welcome geeks"

 print(s)

 

 

f()  
  
---  
  
 __

 __

 **Output:**

    
    
    Welcome geeks
    

**Global variables** are the ones that are defined and declared outside a
function, and we need to use them inside a function.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# This function has a variable with

# name same as s.

def f():

 print(s)

 

 

# Global scope

s = "I love Geeksforgeeks"

f()  
  
---  
  
 __

 __

 **Output:**

    
    
    I love Geeksforgeeks
    

### Global keyword in Python:

Global keyword is a keyword that allows a user to modify a variable outside of
the current scope. It is used to create global variables from a non-global
scope i.e inside a function. Global keyword is used inside a function only
when we want to do assignments or when we want to change a variable. Global is
not needed for printing and accessing.

 **Rules of global keyword:**

  * If a variable is assigned a value anywhere within the function’s body, it’s assumed to be a local unless explicitly declared as global.
  * Variables that are only referenced inside a function are implicitly global.
  * We Use global keyword to use a global variable inside a function.
  * There is no need to use global keyword outside a function.

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to modify a global

# value inside a function

 

x = 15

 

 

def change():

 

 # using a global keyword

 global x

 

 # increment value of a by 5

 x = x + 5

 print("Value of x inside a function :", x)

 

 

change()

print("Value of x outside a function :", x)  
  
---  
  
 __

 __

 **Output:**

    
    
    Value of x inside a function : 20
    Value of x outside a function : 20
    

### Variable type in Python:

Data types are the classification or categorization of data items. It
represents the kind of value that tells what operations can be performed on a
particular data. Since everything is an object in Python programming, data
types are actually classes and variables are instance (object) of these
classes.

Following are the standard or built-in data type of Python:

  * Numeric
  * Sequence Type
  * Boolean
  * Set
  * Dictionary

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# numberic

var = 123

print("Numbric data : ", var)

 

# Sequence Type

String1 = 'Welcome to the Geeks World'

print("String with the use of Single Quotes: ")

print(String1)

 

# Boolean

print(type(True))

print(type(False))

 

# Creating a Set with

# the use of a String

set1 = set("GeeksForGeeks")

print("\nSet with the use of String: ")

print(set1)

 

# Creating a Dictionary

# with Integer Keys

Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}

print("\nDictionary with the use of Integer Keys: ")

print(Dict)  
  
---  
  
 __

 __

 **Output:**

    
    
    Numbric data :  123
    String with the use of Single Quotes: 
    Welcome to the Geeks World
    <class 'bool'>
    <class 'bool'>
    
    Set with the use of String: 
    {'r', 'G', 'e', 'k', 'o', 's', 'F'}
    
    Dictionary with the use of Integer Keys: 
    {1: 'Geeks', 2: 'For', 3: 'Geeks'}
    

### **Object References:**

Let, we assign a variable x to value 5, and another variable y to the variable
x.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

x= 5

y = x  
  
---  
  
 __

 __

When Python looks at the first statement, what it does is that, first, it
creates an object to represent the value 5. Then, it creates the variable x if
it doesn’t exist and made it a reference to this new object 5. The second line
causes Python to create the variable y, and it is not assigned with x, rather
it is made to reference that object that x does. The net effect is that the
variables x and y wind up referencing the same object. This situation, with
multiple names referencing the same object, is called a **Shared Reference**
in Python.  
Now, if we write:

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

x= 'Geeks'  
  
---  
  
 __

 __

This statement makes a new object to represent ‘Geeks’ and makes x to
reference this new object.

###  **Creating objects (or variables of a class type):**

Please refer Class, Object and Members for more details.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to show that the variables with a value

# assigned in class declaration, are class variables and

# variables inside methods and constructors are instance

# variables.

 

# Class for Computer Science Student

class CSStudent:

 

 # Class Variable

 stream = 'cse'

 

 # The init method or constructor

 def __init__(self, roll):

 

 # Instance Variable 

 self.roll = roll 

 

# Objects of CSStudent class

a = CSStudent(101)

b = CSStudent(102)

 

print(a.stream) # prints "cse"

print(b.stream) # prints "cse"

print(a.roll) # prints 101

 

# Class variables can be accessed using class

# name also

print(CSStudent.stream) # prints "cse"   
  
---  
  
__

__

**Output**

    
    
    cse
    cse
    101
    cse
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


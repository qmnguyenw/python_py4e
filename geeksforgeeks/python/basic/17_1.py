Constructors in Python



 **Prerequisites :** Object Oriented Programming in Python, Object Oriented
Programming in Python | Set 2  
Constructors are generally used for instantiating an object.The task of
constructors is to initialize(assign values) to the data members of the class
when an object of class is created.In Python the __init__() method is called
the constructor and is always called when an object is created.

 **Syntax of constructor declaration :**

    
    
    def __init__(self):
        # body of the constructor

 **Types of constructors :**

  *  **default constructor :** The default constructor is simple constructor which doesn’t accept any arguments.It’s definition has only one argument which is a reference to the instance being constructed.
  *  **parameterized constructor :** constructor with parameters is known as parameterized constructor.The parameterized constructor take its first argument as a reference to the instance being constructed known as self and the rest of the arguments are provided by the programmer.

 **Example of default constructor :**

 __

 __  
 __

 __

 __  
 __  
 __

class GeekforGeeks:

 

 # default constructor

 def __init__(self):

 self.geek = "GeekforGeeks"

 

 # a method for printing data members

 def print_Geek(self):

 print(self.geek)

 

 

# creating object of the class

obj = GeekforGeeks()

 

# calling the instance method using the object obj

obj.print_Geek()  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    GeekforGeeks

 **Example of parameterized constructor :**

 __

 __  
 __

 __

 __  
 __  
 __

class Addition:

 first = 0

 second = 0

 answer = 0

 

 # parameterized constructor

 def __init__(self, f, s):

 self.first = f

 self.second = s

 

 def display(self):

 print("First number = " + str(self.first))

 print("Second number = " + str(self.second))

 print("Addition of two numbers = " + str(self.answer))

 

 def calculate(self):

 self.answer = self.first + self.second

 

# creating object of the class

# this will invoke parameterized constructor

obj = Addition(1000, 2000)

 

# perform Addition

obj.calculate()

 

# display result

obj.display()  
  
---  
  
 __

 __

 **Output :**

    
    
    First number = 1000
    Second number = 2000
    Addition of two numbers = 3000

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

